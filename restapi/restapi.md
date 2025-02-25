# Comprehensive REST API Tutorial for DevOps

## Table of Contents

1. [Introduction to REST APIs](#introduction-to-rest-apis)
2. [HTTP Methods](#http-methods)
3. [HTTP Status Codes](#http-status-codes)
4. [Request and Response Structure](#request-and-response-structure)
5. [Authentication and Authorization](#authentication-and-authorization)
6. [Tools for Working with REST APIs](#tools-for-working-with-rest-apis)
   - [Browser DevTools](#browser-devtools)
   - [Postman](#postman)
   - [Curl](#curl)
7. [Working with REST APIs in Different Languages](#working-with-rest-apis-in-different-languages)
   - [Python (requests)](#python-requests)
   - [JavaScript (Fetch API, Axios)](#javascript-fetch-api-axios)
   - [Java (RestTemplate, HttpClient)](#java-resttemplate-httpclient)
   - [Go (net/http)](#go-nethttp)
8. [Building REST APIs](#building-rest-apis)
   - [Node.js with Express](#nodejs-with-express)
   - [Python with Flask/FastAPI](#python-with-flaskfastapi)
9. [API Documentation](#api-documentation)
10. [Testing REST APIs](#testing-rest-apis)
11. [API Security Best Practices](#api-security-best-practices)
12. [Monitoring and Analytics](#monitoring-and-analytics)
13. [Real-world DevOps Integration Examples](#real-world-devops-integration-examples)
14. [Troubleshooting Common Issues](#troubleshooting-common-issues)

## Introduction to REST APIs

REST (Representational State Transfer) is an architectural style for designing networked applications. RESTful APIs are designed around resources, which are any kind of object, data, or service that can be accessed by the client.

### Key Principles of REST

1. **Stateless**: Each request from client to server must contain all the information needed to understand and process the request. The server cannot store any client context between requests.

2. **Client-Server Architecture**: The client and server are separate, allowing them to evolve independently.

3. **Cacheable**: Responses must define themselves as cacheable or non-cacheable to prevent clients from reusing stale or inappropriate data.

4. **Uniform Interface**: The API has a uniform and consistent interface, including:

   - Resource identification in requests
   - Resource manipulation through representations
   - Self-descriptive messages
   - Hypermedia as the engine of application state (HATEOAS)

5. **Layered System**: The API can be composed of multiple layers, but each layer can only see the layer it is interacting with.

### REST vs. SOAP

| Feature     | REST                                 | SOAP                                  |
| ----------- | ------------------------------------ | ------------------------------------- |
| Protocol    | HTTP/HTTPS                           | Multiple (HTTP, SMTP, TCP, etc.)      |
| Data Format | Usually JSON, can be XML, YAML, etc. | XML only                              |
| Bandwidth   | Requires less bandwidth              | More verbose, requires more bandwidth |
| Ease of Use | Simpler to use                       | More complex                          |
| Caching     | Supports caching                     | Limited caching support               |
| Security    | Uses HTTPS                           | Built-in WS-Security standards        |

## HTTP Methods

REST APIs use HTTP methods to perform operations on resources:

| Method  | Purpose                                               | Properties                  |
| ------- | ----------------------------------------------------- | --------------------------- |
| GET     | Retrieve data                                         | Safe, Idempotent, Cacheable |
| POST    | Create new resources                                  | Neither safe nor idempotent |
| PUT     | Update existing resources (complete replacement)      | Idempotent, not safe        |
| PATCH   | Partially update resources                            | Not necessarily idempotent  |
| DELETE  | Remove resources                                      | Idempotent, not safe        |
| HEAD    | Like GET but returns only headers (no body)           | Safe, Idempotent, Cacheable |
| OPTIONS | Get information about available communication options | Safe, Idempotent            |

### Method Properties Explained

- **Safe**: Operation does not change resources on the server
- **Idempotent**: Multiple identical requests have the same effect as a single request
- **Cacheable**: Response can be cached for future equivalent requests

## HTTP Status Codes

HTTP status codes indicate the result of the HTTP request:

### 1xx: Informational

- `100 Continue`: The server has received the request headers and the client should proceed to send the request body.
- `101 Switching Protocols`: The requester has asked the server to switch protocols and the server has agreed to do so.
- `102 Processing`: The server has received and is processing the request, but no response is available yet.

### 2xx: Success

- `200 OK`: Standard response for successful HTTP requests.
- `201 Created`: Request has been fulfilled, resulting in the creation of a new resource.
- `202 Accepted`: Request has been accepted for processing, but processing is not complete.
- `204 No Content`: Server successfully processed the request, but is not returning any content.
- `206 Partial Content`: Server is delivering only part of the resource due to a range header sent by the client.

### 3xx: Redirection

- `300 Multiple Choices`: Multiple options for the resource from which the client may choose.
- `301 Moved Permanently`: Resource has been permanently moved to a new URL.
- `302 Found`: Resource temporarily resides under a different URL.
- `303 See Other`: Response to the request can be found under a different URL.
- `304 Not Modified`: Resource has not been modified since last requested.
- `307 Temporary Redirect`: Resource temporarily resides under a different URL.
- `308 Permanent Redirect`: Resource has permanently moved to a new URL.

### 4xx: Client Errors

- `400 Bad Request`: Server cannot or will not process the request due to a client error.
- `401 Unauthorized`: Authentication is required and has failed or not been provided.
- `403 Forbidden`: Server understood the request but refuses to authorize it.
- `404 Not Found`: Resource could not be found.
- `405 Method Not Allowed`: Request method is not supported for the requested resource.
- `406 Not Acceptable`: Resource cannot generate content according to the Accept headers.
- `408 Request Timeout`: Server timed out waiting for the request.
- `409 Conflict`: Request could not be completed due to a conflict with the current state of the resource.
- `413 Payload Too Large`: Request entity is larger than limits defined by server.
- `414 URI Too Long`: URI requested by the client is too long.
- `415 Unsupported Media Type`: Media format of the requested data is not supported by the server.
- `429 Too Many Requests`: User has sent too many requests in a given amount of time.

### 5xx: Server Errors

- `500 Internal Server Error`: Generic error message when server encounters an unexpected condition.
- `501 Not Implemented`: Server does not recognize the request method or lacks the ability to fulfill it.
- `502 Bad Gateway`: Server, while acting as a gateway, received an invalid response from an upstream server.
- `503 Service Unavailable`: Server is currently unavailable (overloaded or down for maintenance).
- `504 Gateway Timeout`: Server, acting as a gateway, did not receive a timely response from an upstream server.
- `505 HTTP Version Not Supported`: Server does not support the HTTP protocol version used in the request.

## Request and Response Structure

### Request Structure

```
[METHOD] /resource/path HTTP/1.1
Host: example.com
Content-Type: application/json
Authorization: Bearer [token]
Accept: application/json
User-Agent: Mozilla/5.0 (...)

{
  "key": "value",
  "another_key": "another_value"
}
```

#### Components:

1. **Method and Path**: HTTP verb and resource URL
2. **Headers**: Metadata about the request
   - `Content-Type`: Format of the request body
   - `Authorization`: Credentials for protected resources
   - `Accept`: Expected response format
   - Other custom headers as needed
3. **Body**: Payload data (JSON, XML, form data, etc.) - not included in GET requests

### Response Structure

```
HTTP/1.1 200 OK
Content-Type: application/json
Cache-Control: max-age=3600
X-Rate-Limit-Remaining: 98

{
  "id": 123,
  "name": "Example Resource",
  "updated_at": "2023-02-12T15:19:21Z"
}
```

#### Components:

1. **Status Line**: HTTP version, status code, and reason phrase
2. **Headers**: Metadata about the response
   - `Content-Type`: Format of the response body
   - `Cache-Control`: Caching directives
   - Custom headers with additional information
3. **Body**: Response data (JSON, XML, HTML, etc.)

## Authentication and Authorization

### Common Authentication Methods

1. **Basic Authentication**
   - Credentials sent in the `Authorization` header, encoded as Base64
   - Format: `Authorization: Basic {base64(username:password)}`
   - Should only be used with HTTPS

```
Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
```

2. **API Keys**
   - Single token identifying the client
   - Can be sent in headers, query parameters, or request body
   - Format: `X-API-Key: your_api_key_here` or `?api_key=your_api_key_here`

```
X-API-Key: abcd1234efgh5678
```

3. **OAuth 2.0**
   - Token-based framework for authorization
   - Provides various "flows" for different types of applications
   - Format: `Authorization: Bearer {access_token}`

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

4. **JWT (JSON Web Tokens)**

   - Compact, self-contained tokens with encoded claims
   - Can be used for both authentication and information transfer
   - Format: `Authorization: Bearer {jwt_token}`

5. **API Keys + HMAC Signatures**
   - Combines API key with cryptographic signature of the request
   - Prevents tampering and replay attacks

### Authorization Methods

1. **Role-Based Access Control (RBAC)**

   - Permissions assigned to roles, users assigned to roles
   - Common in enterprise applications

2. **Attribute-Based Access Control (ABAC)**

   - Access decisions based on attributes of user, resource, action, and context
   - More flexible but complex

3. **Scopes (OAuth 2.0)**
   - Permissions are defined as scopes (e.g., `read:users`, `write:posts`)
   - Access tokens include permitted scopes

## Tools for Working with REST APIs

### Browser DevTools

Modern browsers come with developer tools that allow you to inspect network traffic:

#### Using Chrome DevTools

1. **Open DevTools**: Press F12 or Ctrl+Shift+I (Cmd+Option+I on Mac)
2. **Go to Network Tab**: Shows all HTTP requests
3. **Filter Requests**: Use filters (XHR/Fetch, JS, CSS, etc.)
4. **Inspect Request/Response**:
   - Headers: View request and response headers
   - Preview: Formatted view of response data
   - Response: Raw response data
   - Timing: Performance metrics

#### Key Features

- **Request Filtering**: Filter by type, domain, or custom text
- **Throttling**: Simulate slower network connections
- **Preserve Log**: Keep request history when navigating
- **Copy as cURL**: Right-click any request and select "Copy as cURL" for terminal use
- **Request Blocking**: Block specific URLs for testing
- **Clear Cache & Cookies**: For testing authentication scenarios

#### Example Workflow

1. Open the Network tab
2. Perform action on website that triggers API calls
3. Find the API call in the list
4. Examine request headers, parameters, and body
5. Check response status, headers, and body
6. Use the information to understand the API or debug issues

### Postman

Postman is a dedicated API client that simplifies testing and documentation:

#### Key Features

1. **Collections**: Organize requests into folders
2. **Environments**: Switch between development, testing, and production
3. **Variables**: Store and reuse values (tokens, URLs, IDs)
4. **Pre-request Scripts**: Run JavaScript before a request
5. **Tests**: Write assertions to verify responses
6. **Authentication Helper**: Simplified auth setup
7. **Request History**: View all sent requests
8. **Mock Servers**: Create mock responses
9. **Documentation**: Generate API docs

#### Example Request in Postman

1. **Create New Request**:

   - Select HTTP method (GET, POST, etc.)
   - Enter URL
   - Add headers (Content-Type, Authorization, etc.)
   - Add request body if needed

2. **Send Request and Analyze Response**:

   - Status code
   - Response time
   - Response headers
   - Response body
   - Cookies

3. **Save to Collection**:
   - Name the request
   - Choose or create a collection
   - Add description

### Curl

cURL is a command-line tool for transferring data with URLs:

#### Basic Syntax

```bash
curl [options] [URL]
```

#### Common Options

- `-X, --request`: Specify HTTP method
- `-H, --header`: Add HTTP header
- `-d, --data`: Add request body
- `-i, --include`: Include response headers
- `-v, --verbose`: Verbose output (shows complete request & response)
- `-u, --user`: Basic authentication credentials
- `-o, --output`: Write output to file

#### Examples

**GET Request**

```bash
curl https://api.example.com/users
```

**GET with Headers**

```bash
curl -H "Accept: application/json" https://api.example.com/users
```

**POST Request with JSON Body**

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"name": "John", "email": "john@example.com"}' \
  https://api.example.com/users
```

**PUT Request**

```bash
curl -X PUT \
  -H "Content-Type: application/json" \
  -d '{"name": "John Updated", "email": "john.updated@example.com"}' \
  https://api.example.com/users/123
```

**DELETE Request**

```bash
curl -X DELETE https://api.example.com/users/123
```

**Authentication**

```bash
# Basic Auth
curl -u username:password https://api.example.com/users

# Bearer Token
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  https://api.example.com/users
```

**File Upload**

```bash
curl -X POST \
  -F "file=@/path/to/file.jpg" \
  https://api.example.com/upload
```

**Download File**

```bash
curl -o output.jpg https://api.example.com/images/123
```

**Follow Redirects**

```bash
curl -L https://api.example.com/redirecting-endpoint
```

**View Details of the Request/Response**

```bash
curl -v https://api.example.com/users
```

## Working with REST APIs in Different Languages

### Python (requests)

Python's `requests` library is a powerful and user-friendly HTTP client:

#### Installation

```bash
pip install requests
```

#### Basic Usage

**GET Request**

```python
import requests

response = requests.get('https://api.example.com/users')
data = response.json()  # Parse JSON response

print(f"Status Code: {response.status_code}")
print(f"Response: {data}")
```

**GET with Parameters**

```python
params = {'limit': 10, 'offset': 20}
response = requests.get('https://api.example.com/users', params=params)
```

**GET with Headers**

```python
headers = {
    'Authorization': 'Bearer your-token-here',
    'Accept': 'application/json'
}
response = requests.get('https://api.example.com/users', headers=headers)
```

**POST Request**

```python
data = {
    'name': 'John Doe',
    'email': 'john@example.com'
}
response = requests.post('https://api.example.com/users', json=data)
```

**PUT Request**

```python
data = {
    'name': 'John Updated',
    'email': 'john.updated@example.com'
}
response = requests.put('https://api.example.com/users/123', json=data)
```

**DELETE Request**

```python
response = requests.delete('https://api.example.com/users/123')
```

**File Upload**

```python
files = {'file': open('document.pdf', 'rb')}
response = requests.post('https://api.example.com/upload', files=files)
```

**Handling Authentication**

```python
# Basic Auth
response = requests.get('https://api.example.com/users', auth=('username', 'password'))

# Custom Auth Header
headers = {'Authorization': 'Bearer your-token-here'}
response = requests.get('https://api.example.com/users', headers=headers)
```

**Session for Multiple Requests**

```python
session = requests.Session()
session.headers.update({'Authorization': 'Bearer your-token-here'})

# All requests will share the same session and headers
response1 = session.get('https://api.example.com/users')
response2 = session.get('https://api.example.com/posts')
```

**Error Handling**

```python
try:
    response = requests.get('https://api.example.com/users')
    response.raise_for_status()  # Raises exception for 4XX/5XX responses
    data = response.json()
except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: {err}")
except requests.exceptions.ConnectionError as err:
    print(f"Connection Error: {err}")
except requests.exceptions.Timeout as err:
    print(f"Timeout Error: {err}")
except requests.exceptions.RequestException as err:
    print(f"Error: {err}")
```

**Timeouts**

```python
# Timeout after 5 seconds
response = requests.get('https://api.example.com/users', timeout=5)
```
