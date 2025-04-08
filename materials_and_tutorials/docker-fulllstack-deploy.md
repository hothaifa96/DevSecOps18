# Comprehensive Docker Full-Stack Application Tutorial


## Introduction

Containerizing a full-stack application with Docker offers numerous benefits:

- Consistent environments across development, testing, and production
- Isolated dependencies for each component
- Simplified deployment and scaling
- Easier onboarding for new developers
- Efficient resource utilization

This tutorial walks through creating Dockerfiles for frontend, backend, and database components, connecting them properly, and implementing best practices.

## Project Structure

A typical full-stack application structure might look like this:

```
my-fullstack-app/
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   ├── public/
│   └── src/
├── backend/
│   ├── Dockerfile
│   ├── package.json
│   └── src/
└── database/
    ├── init-scripts/
    └── data/
```

## Dockerizing Components

### Frontend Dockerfile

Let's create a Dockerfile for a React frontend application:

```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
```

### Backend Dockerfile

For a Node.js Express backend:

```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 4000

CMD ["npm", "run", "dev"]
```


### Database Setup

For most applications, we'll use an official database image rather than creating our own Dockerfile. Let's use PostgreSQL as an example:

```bash
docker volume create postgres_data

docker run -d \
  --name postgres \
  -v postgres_data:/var/lib/postgresql/data \
  -v ./database/init-scripts:/docker-entrypoint-initdb.d \
  -e POSTGRES_PASSWORD=$DB_PASSWORD \
  -e POSTGRES_USER=$DB_USER \
  -e POSTGRES_DB=$DB_NAME \
  -p 5432:5432 \
  postgres:15-alpine
```

## Connection Strings

### Frontend to Backend

In a React application, you would typically connect to the backend like this:

```javascript
const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:4000/api';

export const fetchData = async () => {
  try {
    const response = await fetch(`${API_URL}/data`);
    return await response.json();
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};
```

### Backend to Database

For Node.js with PostgreSQL (using node-postgres):



## Architecture Diagram

```
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│                 │      │                 │      │                 │
│    Frontend     │──────│    Backend      │──────│    Database     │
│    (React)      │      │    (Node.js)    │      │  (PostgreSQL)   │
│                 │      │                 │      │                 │
└─────────────────┘      └─────────────────┘      └─────────────────┘
     Port: 3000             Port: 4000              Port: 5432
     (80 in prod)          (internal in prod)      (internal in prod)
```

## Docker Network Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         Docker Network                          │
│                                                                 │
│  ┌─────────────┐       ┌─────────────┐       ┌─────────────┐    │
│  │             │       │             │       │             │    │
│  │  Frontend   │─HTTP─▶│  Backend    │─SQL──▶│  Database   │    │
│  │  Container  │◀─────│  Container   │◀─────│  Container  │    │
│  │             │       │             │       │             │    │
│  └─────────────┘       └─────────────┘       └─────────────┘    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Container Communication Flow

```
┌───────────────┐     ┌───────────────┐     ┌───────────────┐
│   Frontend    │     │    Backend    │     │   Database    │
│   Container   │     │   Container   │     │   Container   │
└───────┬───────┘     └───────┬───────┘     └───────┬───────┘
        │                     │                     │
        │  HTTP Request       │                     │
        │ ──────────────────▶ │                     │
        │                     │                     │
        │                     │   SQL Query         │
        │                     │ ──────────────────▶ │
        │                     │                     │
        │                     │   Query Results     │
        │                     │ ◀────────────────── │
        │                     │                     │
        │  HTTP Response      │                     │
        │ ◀────────────────── │                     │
        │                     │                     │
```

## Best Practices

### Dockerfile Best Practices

1. **Use specific image tags** instead of `latest` to ensure consistency
2. **Layer caching** - order Dockerfile instructions from least to most frequently changed
3. **Minimize the number of layers** by combining related commands
4. **Non-root users** for security
5. **Use .dockerignore** to exclude unnecessary files
6. **Scan images for vulnerabilities** with tools like Docker Scout

Example `.dockerignore` file:

```
node_modules
npm-debug.log
Dockerfile*
docker-compose*
.git
.gitignore
README.md
.env*
```


Example with health checks:

```yaml
services:
  backend:
    build:
      context: ./backend
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:4000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    restart: unless-stopped
```

### Security Best Practices

1. **Never store secrets in Dockerfiles** or images
2. **Use environment variables or secrets management**
3. **Scan images for vulnerabilities**
4. **Minimal base images** (alpine/slim variants)
5. **Run containers as non-root users**
6. **Use read-only file systems** where possible
7. **Limit container capabilities and resources**

## Deployment Considerations

### Container Orchestration

For production deployments, consider using:

- **Docker Swarm**: Simple, built into Docker
- **Kubernetes**: More complex but powerful orchestration
- **AWS ECS/EKS**: Managed container services

### CI/CD Pipeline

A typical CI/CD pipeline might look like this:

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│          │     │          │     │          │     │          │
│   Code   │────▶│   Build  │────▶│   Test   │────▶│  Deploy  │
│          │     │          │     │          │     │          │
└──────────┘     └──────────┘     └──────────┘     └──────────┘
```

Example GitHub Actions workflow (`.github/workflows/docker-build.yml`):

```yaml
name: Docker Build and Push

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2

      - name: Login to DockerHub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Build and push backend
        uses: docker/build-push-action@v4
        with:
          context: ./backend
          file: ./backend/Dockerfile.prod
          push: true
          tags: yourusername/backend:latest

      - name: Build and push frontend
        uses: docker/build-push-action@v4
        with:
          context: ./frontend
          file: ./frontend/Dockerfile.prod
          push: true
          tags: yourusername/frontend:latest
```

## Development vs Production

### Development Features

- Volume mounts for hot reloading
- Exposed ports for direct access
- Debug tools and verbose logging
- Local environment variables

### Production Features

- Multi-stage builds for optimized images
- Minimal exposed ports
- Security optimizations
- Health checks and auto-restart policies
- Resource constraints

## Monitoring and Logging

### Logging Solutions

```yaml
services:
  backend:
    # ... other configurations
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

For centralized logging, consider:
- ELK Stack (Elasticsearch, Logstash, Kibana)
- Prometheus + Grafana
- DataDog
- New Relic

### Monitoring Integration

Example Prometheus configuration (`prometheus.yml`):

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'backend'
    static_configs:
      - targets: ['backend:4000']
  - job_name: 'frontend'
    static_configs:
      - targets: ['frontend:80']
  - job_name: 'database'
    static_configs:
      - targets: ['postgres-exporter:9187']
```

## Sample Application

Let's create a simple full-stack application with:
- React frontend
- Node.js (Express) backend
- PostgreSQL database

### Sample Frontend Code

```jsx
// frontend/src/App.js
import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [formData, setFormData] = useState({ name: '', email: '' });

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    try {
      const response = await fetch('/api/users');
      if (!response.ok) throw new Error('Network response was not ok');
      const data = await response.json();
      setUsers(data);
      setLoading(false);
    } catch (error) {
      setError('Error fetching users: ' + error.message);
      setLoading(false);
    }
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('/api/users', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      
      if (!response.ok) throw new Error('Network response was not ok');
      
      const newUser = await response.json();
      setUsers([...users, newUser]);
      setFormData({ name: '', email: '' });
    } catch (error) {
      setError('Error adding user: ' + error.message);
    }
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>{error}</div>;

  return (
    <div className="App">
      <h1>User Management</h1>
      
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          value={formData.name}
          onChange={handleChange}
          placeholder="Name"
          required
        />
        <input
          type="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
          placeholder="Email"
          required
        />
        <button type="submit">Add User</button>
      </form>
      
      <h2>Users</h2>
      <ul>
        {users.map(user => (
          <li key={user.id}>
            {user.name} ({user.email})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
```

### Sample Backend Code

```javascript
// backend/src/index.js
const express = require('express');
const cors = require('cors');
const db = require('./db');

const app = express();
const PORT = process.env.PORT || 4000;

app.use(cors());
app.use(express.json());

// Health check endpoint
app.get('/health', (req, res) => {
  res.status(200).send('OK');
});

// Get all users
app.get('/api/users', async (req, res) => {
  try {
    const result = await db.query('SELECT * FROM users ORDER BY id ASC');
    res.json(result.rows);
  } catch (error) {
    console.error('Error fetching users:', error);
    res.status(500).json({ error: 'Server error' });
  }
});

// Add a new user
app.post('/api/users', async (req, res) => {
  const { name, email } = req.body;
  
  if (!name || !email) {
    return res.status(400).json({ error: 'Name and email are required' });
  }
  
  try {
    const result = await db.query(
      'INSERT INTO users (name, email) VALUES ($1, $2) RETURNING *',
      [name, email]
    );
    res.status(201).json(result.rows[0]);
  } catch (error) {
    console.error('Error creating user:', error);
    res.status(500).json({ error: 'Server error' });
  }
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

### Database Initialization Script

```sql
-- database/init-scripts/init.sql
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Add some initial data
INSERT INTO users (name, email) VALUES
  ('John Doe', 'john@example.com'),
  ('Jane Smith', 'jane@example.com')
ON CONFLICT (email) DO NOTHING;
```

### Running the Application

1. Create an `.env` file:

```
DB_USER=postgres
DB_PASSWORD=mysecretpassword
DB_NAME=myapp
```

2. Start the application:

```bash
# Development
docker-compose up

# Production
docker-compose -f docker-compose.prod.yml up -d
```

3. Access the application:
   - Frontend: http://localhost:3000 (dev) or http://localhost (prod)
   - Backend API: http://localhost:4000/api/users (dev only)

## Scaling the Application

As your application grows, you might need to:

1. **Add load balancing**:

```yaml
services:
  backend:
    # ...other configs
    deploy:
      replicas: 3
```

2. **Implement database replication**

3. **Add a caching layer** (Redis)

```yaml
services:
  redis:
    image: redis:alpine
    networks:
      - app-network
```

4. **Set up a reverse proxy** (Nginx/Traefik)

```yaml
services:
  proxy:
    image: traefik:v2.5
    command:
      - "--providers.docker=true"
      - "--providers.docker.exposedbydefault=false"
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
    networks:
      - app-network
```

## Conclusion

This tutorial covered the essentials of containerizing a full-stack application with Docker. By following these patterns and best practices, you can create a containerized application that is:

- Easy to develop and maintain
- Secure and reliable
- Scalable and performant
- Consistent across environments

Remember that Docker is a tool, and like any tool, it should be used appropriately for your specific needs. Start simple and gradually adopt more advanced patterns as your application and team grow.