# Flask Blog API Lab (Easy)

This lab will guide you through creating a simple Flask-based RESTful API for managing blog posts. You'll implement basic CRUD (Create, Read, Update, Delete) operations and learn how to structure API endpoints in Flask.

- Set up a basic Flask application
- Implement RESTful API endpoints
- Work with JSON data in Flask
- Implement proper HTTP status codes and responses

- Configure the application to run on port 5000
- Set up a simple in-memory list to store blog posts

### 2. Data Model
Each blog post should contain the following fields:
- `id`: A unique identifier (integer)
- `title`: The title of the blog post (string)
- `content`: The main content of the blog post (string)
- `author`: The name of the author (string)
- `date_posted`: The date when the post was created (string in ISO format)

### 3. API Endpoints

Implement the following API endpoints:

#### GET /posts
- Returns a JSON array of all blog posts
- Response format:
  ```json
  {
    "success": true,
    "posts": [
      {
        "id": 1,
        "title": "First Post",
        "content": "This is my first post",
        "author": "John Doe",
        "date_posted": "2025-02-28T10:00:00"
      },
      ...
    ]
  }
  ```

#### GET /posts/<id>
- Returns a specific blog post by ID
- If found, returns the post as JSON with a 200 status code
- If not found, returns a 404 error with an appropriate message
- Response format for successful request:
  ```json
  {
    "success": true,
    "post": {
      "id": 1,
      "title": "First Post",
      "content": "This is my first post",
      "author": "John Doe",
      "date_posted": "2025-02-28T10:00:00"
    }
  }
  ```

#### POST /posts
- Creates a new blog post
- Accepts JSON data in the request body
- Required fields: title, content, author
- Automatically assigns an ID and date_posted
- Returns the created post with a 201 status code
- Response format:
  ```json
  {
    "success": true,
    "message": "Post created successfully",
    "post": {
      "id": 1,
      "title": "First Post",
      "content": "This is my first post",
      "author": "John Doe",
      "date_posted": "2025-02-28T10:00:00"
    }
  }
  ```

#### PUT /posts/<id>
- Updates an existing blog post
- Accepts JSON data in the request body
- Fields that can be updated: title, content, author
- Returns the updated post with a 200 status code
- If post not found, returns a 404 error
- Response format for successful update:
  ```json
  {
    "success": true,
    "message": "Post updated successfully",
    "post": {
      "id": 1,
      "title": "Updated Title",
      "content": "Updated content",
      "author": "John Doe",
      "date_posted": "2025-02-28T10:00:00"
    }
  }
  ```

#### DELETE /posts/<id>
- Deletes a blog post by ID
- Returns a success message with a 200 status code
- If post not found, returns a 404 error
- Response format for successful deletion:
  ```json
  {
    "success": true,
    "message": "Post deleted successfully"
  }
  ```

### 4. Validation Requirements
- Validate that required fields (title, content, author) are present in POST requests
- If validation fails, return a 400 status code with appropriate error messages
- Ensure proper error handling for all endpoints

## Testing Instructions

### Manual Testing
Test each endpoint using a tool like Postman, curl, or any API testing tool of your choice.

#### Example Test Cases:

1. **GET /posts** - Should return all posts
2. **GET /posts/1** - Should return the post with ID 1 if it exists
3. **GET /posts/999** - Should return a 404 error if post doesn't exist
4. **POST /posts** with valid data - Should create a new post
5. **POST /posts** with missing fields - Should return a 400 error
6. **PUT /posts/1** with valid data - Should update the post
7. **PUT /posts/999** - Should return a 404 error if post doesn't exist
8. **DELETE /posts/1** - Should delete the post
9. **DELETE /posts/999** - Should return a 404 error if post doesn't exist

### Expected Responses
Document the expected HTTP status codes and response bodies for each test case.

## Bonus Challenges

### 1. Search Functionality
Create a new file with requests try to test the application while flask is running

### 2. Basic Authentication
- Implement basic authentication for POST, PUT, and DELETE operations
- Only authenticated users should be able to create, update, or delete posts

### 3. Pagination
Add pagination to limit the number of posts returned:
- `GET /posts?page=1&per_page=10` - Returns the first 10 posts
- Include metadata about pagination in the response
