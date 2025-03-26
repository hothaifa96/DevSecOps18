# Docker Lab 4: Flask RESTful API Service

## Overview
In this lab, you'll containerize a Flask-based RESTful API service for a product catalog with multiple endpoints and JSON responses.

## Learning Objectives
- Create a Dockerfile for a Flask API service
- Configure a production-ready container for a Flask application
- Understand Docker networking for API services
- Implement Docker best practices for web services

## Requirements
- Docker installed on your system
- Basic knowledge of Python, Flask and RESTful APIs
- Text editor or IDE
- API testing tool (curl, Postman, or similar)

## Files Structure
```
flask_rest_api/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── products.py
│   │   └── categories.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Create the Flask API Application

Create the directory structure and add the following files:

**app/__init__.py**:
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app(config_class=None):
    app = Flask(__name__)
    
    # Load configuration
    if config_class is None:
        app.config.from_object('config')
    else:
        app.config.from_object(config_class)
    
    # Enable CORS
    CORS(app)
    
    # Initialize extensions
    db.init_app(app)
    
    # Register blueprints
    from app.routes.products import product_bp
    from app.routes.categories import category_bp
    
    app.register_blueprint(product_bp, url_prefix='/api/products')
    app.register_blueprint(category_bp, url_prefix='/api/categories')
    
    # Create a route to test the API
    @app.route('/api/health')
    def health_check():
        return {"status": "healthy", "version": "1.0.0"}
    
    return app
```

**app/models.py**:
```python
from app import db
from datetime import datetime
import uuid

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    products = db.relationship('Product', backref='category', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at.isoformat(),
            'product_count': len(self.products)
        }

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(20), unique=True, default=lambda: f"PRD-{uuid.uuid4().hex[:8].upper()}")
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'sku': self.sku,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'stock': self.stock,
            'category_id': self.category_id,
            'category_name': self.category.name if self.category else None,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
```

**app/routes/__init__.py**:
```python
# Package initialization
```

**app/routes/products.py**:
```python
from flask import Blueprint, request, jsonify
from app.models import Product, Category
from app import db
from app.utils.helpers import validate_product

product_bp = Blueprint('products', __name__)

@product_bp.route('/', methods=['GET'])
def get_products():
    """Get all products with optional filtering"""
    # Get query parameters
    category_id = request.args.get('category_id', type=int)
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    in_stock = request.args.get('in_stock', type=bool, default=None)
    
    # Start with base query
    query = Product.query
    
    # Apply filters if provided
    if category_id is not None:
        query = query.filter_by(category_id=category_id)
    
    if min_price is not None:
        query = query.filter(Product.price >= min_price)
    
    if max_price is not None:
        query = query.filter(Product.price <= max_price)
    
    if in_stock is not None:
        if in_stock:
            query = query.filter(Product.stock > 0)
        else:
            query = query.filter(Product.stock == 0)
    
    # Execute query and convert to dictionaries
    products = [product.to_dict() for product in query.all()]
    
    return jsonify({
        'count': len(products),
        'products': products
    })

@product_bp.route('/<int:id>', methods=['GET'])
def get_product(id):
    """Get a single product by ID"""
    product = Product.query.get_or_404(id)
    return jsonify(product.to_dict())

@product_bp.route('/', methods=['POST'])
def create_product():
    """Create a new product"""
    data = request.get_json()
    
    # Validate input data
    errors = validate_product(data)
    if errors:
        return jsonify({'errors': errors}), 400
    
    # Check if category exists if provided
    category_id = data.get('category_id')
    if category_id and not Category.query.get(category_id):
        return jsonify({'errors': ['Category not found']}), 404
    
    # Create new product
    product = Product(
        name=data['name'],
        description=data.get('description', ''),
        price=data['price'],
        stock=data.get('stock', 0),
        category_id=category_id
    )
    
    db.session.add(product)
    db.session.commit()
    
    return jsonify(product.to_dict()), 201

@product_bp.route('/<int:id>', methods=['PUT'])
def update_product(id):
    """Update an existing product"""
    product = Product.query.get_or_404(id)
    data = request.get_json()
    
    # Validate input data
    errors = validate_product(data, update=True)
    if errors:
        return jsonify({'errors': errors}), 400
    
    # Check if category exists if provided
    category_id = data.get('category_id')
    if category_id and not Category.query.get(category_id):
        return jsonify({'errors': ['Category not found']}), 404
    
    # Update product fields
    if 'name' in data:
        product.name = data['name']
    if 'description' in data:
        product.description = data.get('description', '')
    if 'price' in data:
        product.price = data['price']
    if 'stock' in data:
        product.stock = data['stock']
    if category_id:
        product.category_id = category_id
    
    db.session.commit()
    
    return jsonify(product.to_dict())

@product_bp.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    """Delete a product"""
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    
    return jsonify({'message': 'Product deleted successfully'}), 200
```

**app/routes/categories.py**:
```python
from flask import Blueprint, request, jsonify
from app.models import Category
from app import db
from app.utils.helpers import validate_category

category_bp = Blueprint('categories', __name__)

@category_bp.route('/', methods=['GET'])
def get_categories():
    """Get all categories"""
    categories = [category.to_dict() for category in Category.query.all()]
    
    return jsonify({
        'count': len(categories),
        'categories': categories
    })

@category_bp.route('/<int:id>', methods=['GET'])
def get_category(id):
    """Get a single category by ID"""
    category = Category.query.get_or_404(id)
    return jsonify(category.to_dict())

@category_bp.route('/', methods=['POST'])
def create_category():
    """Create a new category"""
    data = request.get_json()
    
    # Validate input data
    errors = validate_category(data)
    if errors:
        return jsonify({'errors': errors}), 400
    
    # Check if category name already exists
    if Category.query.filter_by(name=data['name']).first():
        return jsonify({'errors': ['Category with this name already exists']}), 400
    
    # Create new category
    category = Category(
        name=data['name'],
        description=data.get('description', '')
    )
    
    db.session.add(category)
    db.session.commit()
    
    return jsonify(category.to_dict()), 201

@category_bp.route('/<int:id>', methods=['PUT'])
def update_category(id):
    """Update an existing category"""
    category = Category.query.get_or_404(id)
    data = request.get_json()
    
    # Validate input data
    errors = validate_category(data, update=True)
    if errors:
        return jsonify({'errors': errors}), 400
    
    # Check for name conflict if name is being updated
    if 'name' in data and data['name'] != category.name:
        if Category.query.filter_by(name=data['name']).first():
            return jsonify({'errors': ['Category with this name already exists']}), 400
        category.name = data['name']
    
    # Update description if provided
    if 'description' in data:
        category.description = data.get('description', '')
    
    db.session.commit()
    
    return jsonify(category.to_dict())

@category_bp.route('/<int:id>', methods=['DELETE'])
def delete_category(id):
    """Delete a category"""
    category = Category.query.get_or_404(id)
    
    # Check if category has products
    if category.products:
        return jsonify({'errors': ['Cannot delete category with associated products']}), 400
    
    db.session.delete(category)
    db.session.commit()
    
    return jsonify({'message': 'Category deleted successfully'}), 200
```

**app/utils/__init__.py**:
```python
# Package initialization
```

**app/utils/helpers.py**:
```python
def validate_product(data, update=False):
    """Validate product data"""
    errors = []
    
    # For creation, name and price are required
    if not update:
        if 'name' not in data:
            errors.append('Product name is required')
        if 'price' not in data:
            errors.append('Product price is required')
    
    # For updates, validate fields if they are provided
    if 'name' in data and not data['name']:
        errors.append('Product name cannot be empty')
    
    if 'price' in data:
        try:
            price = float(data['price'])
            if price < 0:
                errors.append('Product price cannot be negative')
        except (ValueError, TypeError):
            errors.append('Product price must be a valid number')
    
    if 'stock' in data:
        try:
            stock = int(data['stock'])
            if stock < 0:
                errors.append('Product stock cannot be negative')
        except (ValueError, TypeError):
            errors.append('Product stock must be a valid integer')
    
    return errors

def validate_category(data, update=False):
    """Validate category data"""
    errors = []
    
    # For creation, name is required
    if not update and 'name' not in data:
        errors.append('Category name is required')
    
    # For updates, validate name if provided
    if 'name' in data and not data['name']:
        errors.append('Category name cannot be empty')
    
    return errors
```

**config.py**:
```python
import os

# Get the folder where this file is located
basedir = os.path.abspath(os.path.dirname(__file__))

# Database configuration
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'instance', 'catalog.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Application configuration
SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
DEBUG = os.environ.get('FLASK_DEBUG', '0') == '1'
JSON_SORT_KEYS = False  # Preserve JSON order for better readability
```

**run.py**:
```python
import os
from app import create_app, db
from app.models import Category, Product

app = create_app()

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()
    
    # Add some sample data if the database is empty
    if not Category.query.first():
        # Create categories
        electronics = Category(name="Electronics", description="Electronic devices and gadgets")
        clothing = Category(name="Clothing", description="Apparel and fashion items")
        books = Category(name="Books", description="Books and publications")
        
        db.session.add_all([electronics, clothing, books])
        db.session.commit()
        
        # Create products
        products = [
            Product(name="Smartphone", description="Latest smartphone with advanced features", 
                   price=699.99, stock=25, category_id=electronics.id),
            Product(name="Laptop", description="Powerful laptop for work and gaming", 
                   price=1299.99, stock=10, category_id=electronics.id),
            Product(name="T-shirt", description="Comfortable cotton t-shirt", 
                   price=19.99, stock=100, category_id=clothing.id),
            Product(name="Jeans", description="Classic blue jeans", 
                   price=49.99, stock=50, category_id=clothing.id),
            Product(name="Novel", description="Bestselling fiction novel", 
                   price=14.99, stock=30, category_id=books.id),
            Product(name="Textbook", description="Educational textbook", 
                   price=59.99, stock=15, category_id=books.id)
        ]
        
        db.session.add_all(products)
        db.session.commit()

if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    
    # Run the application
    app.run(host='0.0.0.0', port=port)
```

### 2. Create Requirements File

Create a file called `requirements.txt`:

```
Flask==2.0.1
Flask-SQLAlchemy==2.5.1
Flask-CORS==3.0.10
gunicorn==20.1.0
```

### 3. Create Dockerfile

Your task is to create a Dockerfile that:
- Uses an appropriate Python base image
- Installs the required dependencies
- Sets up the Flask application files
- Configures environment variables
- Exposes the correct port
- Sets up volume for persistent database storage
- Uses Gunicorn as the production WSGI server
- Runs the application with proper security considerations

## Lab Tasks

1. Create a Dockerfile that containerizes the Flask API service
2. Build and run the Docker container
3. Test the API endpoints using curl or Postman
4. Verify data persistence by stopping and restarting the container
5. Implement proper security for the production Docker container
