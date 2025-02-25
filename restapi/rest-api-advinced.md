# DevOps API Best Practices

## API Security Best Practices

Securing APIs is critical for protecting sensitive data and preventing unauthorized access. Here are key security practices every DevOps engineer should implement:

### Authentication and Authorization

- **Implement Strong Authentication**:
  - Use OAuth 2.0 or OpenID Connect for robust identity management
  - Support multi-factor authentication for sensitive operations
  - Never use Basic Auth without HTTPS
  - Implement JWT (JSON Web Tokens) with proper signing

```bash
# Example: Securing an API endpoint with JWT in Node.js (Express)
const jwt = require('express-jwt');
const jwksRsa = require('jwks-rsa');

const checkJwt = jwt({
  secret: jwksRsa.expressJwtSecret({
    cache: true,
    rateLimit: true,
    jwksRequestsPerMinute: 5,
    jwksUri: 'https://your-tenant.auth0.com/.well-known/jwks.json'
  }),
  audience: 'https://api.yourservice.com',
  issuer: 'https://your-tenant.auth0.com/',
  algorithms: ['RS256']
});

// Protect API routes
app.get('/api/protected-resource', checkJwt, (req, res) => {
  // Handle the request
});
```

- **Implement Proper Authorization**:
  - Use role-based access control (RBAC)
  - Apply the principle of least privilege
  - Create granular API permissions
  - Validate user permissions for each request
  - Implement resource-based access controls

### Transport Security

- **Enforce HTTPS Everywhere**:
  - Redirect HTTP to HTTPS
  - Use HTTP Strict Transport Security (HSTS)
  - Keep TLS/SSL implementations up-to-date
  - Use modern cipher suites and protocols (TLS 1.2+)

```nginx
# Nginx Configuration Example: Enforcing HTTPS and HSTS
server {
    listen 80;
    server_name api.example.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name api.example.com;

    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    ssl_ciphers 'ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305';

    # Enable HSTS
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;

    # ...rest of your configuration
}
```

### Input Validation and Output Sanitization

- **Validate All Input**:
  - Check data types, ranges, formats, and sizes
  - Validate request parameters, headers, and body content
  - Use schema validation with libraries like JSON Schema

```python
# Python Example: Request Validation with Flask and Marshmallow
from flask import Flask, request, jsonify
from marshmallow import Schema, fields, validate, ValidationError

app = Flask(__name__)

class UserSchema(Schema):
    username = fields.String(required=True, validate=validate.Length(min=3, max=50))
    email = fields.Email(required=True)
    age = fields.Integer(validate=validate.Range(min=18, max=120))

@app.route('/api/users', methods=['POST'])
def create_user():
    schema = UserSchema()
    try:
        # Validate incoming data
        data = schema.load(request.json)
        # Process the validated data
        return jsonify({"status": "success", "message": "User created"}), 201
    except ValidationError as err:
        return jsonify({"status": "error", "errors": err.messages}), 400
```

- **Sanitize Output**:
  - Escape HTML/JavaScript when rendering user-provided content
  - Set proper Content-Type headers
  - Implement JSON escaping

### API-Specific Security Controls

- **Implement Rate Limiting**:
  - Protect against brute force and DoS attacks
  - Set limits based on IP, API key, or user
  - Return 429 (Too Many Requests) when limits are exceeded

```nginx
# Rate Limiting in Nginx
http {
    limit_req_zone $binary_remote_addr zone=api_limit:10m rate=5r/s;

    server {
        location /api/ {
            limit_req zone=api_limit burst=10 nodelay;

            # Rest of your configuration
        }
    }
}
```

- **Set Reasonable Timeouts**:

  - Configure reasonable connection, read, and write timeouts
  - Prevent long-running requests from consuming resources

- **Implement API Gateways**:
  - Use an API gateway to centralize authentication, rate limiting, and monitoring
  - Products like Kong, Amazon API Gateway, or Azure API Management

```yaml
# Kong API Gateway Configuration Example
services:
  - name: user-service
    url: http://user-service:8000
    routes:
      - name: user-api
        paths:
          - /api/users
    plugins:
      - name: rate-limiting
        config:
          minute: 60
          hour: 1000
          policy: local
      - name: jwt
        config:
          secret_is_base64: false
          key_claim_name: kid
```

### Security Headers and Configuration

- **Implement Security Headers**:
  - Content-Security-Policy (CSP)
  - X-Content-Type-Options: nosniff
  - X-Frame-Options: DENY
  - X-XSS-Protection: 1; mode=block

```python
# Adding Security Headers in a Flask Application
@app.after_request
def add_security_headers(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self'"
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response
```

- **Disable CORS When Not Needed**:
  - Only enable CORS for trusted domains
  - Implement proper CORS configuration when needed

```javascript
// Express.js CORS Configuration
const cors = require("cors");

// Restrictive CORS - only allow specific origin
const corsOptions = {
  origin: "https://trusted-app.example.com",
  methods: ["GET", "POST", "PUT", "DELETE"],
  allowedHeaders: ["Content-Type", "Authorization"],
  maxAge: 86400, // 24 hours
};

app.use(cors(corsOptions));
```

### Security Testing and Auditing

- **Perform Regular Security Audits**:

  - Automated security scanning
  - Manual penetration testing
  - Code reviews focused on security

- **Implement Vulnerability Disclosure Program**:

  - Make it easy for security researchers to report vulnerabilities
  - Respond promptly to reported issues

- **Use OWASP API Security Top 10 as a Guide**:
  - Review your API against known vulnerabilities
  - Stay updated on emerging threats

## Monitoring and Analytics

Effective monitoring is essential for maintaining reliable and secure API services.

### Monitoring Infrastructure

- **Set Up Comprehensive Monitoring**:
  - Use tools like Prometheus, Grafana, New Relic, or Datadog
  - Monitor both infrastructure and application metrics
  - Implement distributed tracing with Jaeger or Zipkin

```yaml
# Prometheus Configuration Example
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: "api-servers"
    metrics_path: "/metrics"
    static_configs:
      - targets: ["api-server-1:9090", "api-server-2:9090"]

  - job_name: "api-gateway"
    static_configs:
      - targets: ["api-gateway:9090"]
```

### Key Metrics to Monitor

- **Performance Metrics**:
  - Response time (average, percentiles: p95, p99)
  - Request rate
  - Error rate
  - CPU, memory, and disk usage
  - Network I/O

```bash
# Grafana Dashboard Query Example (PromQL)
# Average response time for the last 5 minutes
rate(http_request_duration_seconds_sum{service="api"}[5m]) /
rate(http_request_duration_seconds_count{service="api"}[5m])

# Error rate percentage
sum(rate(http_requests_total{service="api",status=~"5.."}[5m])) /
sum(rate(http_requests_total{service="api"}[5m])) * 100
```

- **Health Metrics**:
  - Service uptime
  - Database connectivity
  - Dependency status
  - Certificate expiration
  - Disk space

### Logging Best Practices

- **Implement Structured Logging**:
  - Use JSON format for machine-parseable logs
  - Include context: request IDs, user IDs, timestamps
  - Differentiate between access logs and application logs

```javascript
// Node.js Structured Logging with Winston
const winston = require("winston");

const logger = winston.createLogger({
  level: "info",
  format: winston.format.json(),
  defaultMeta: { service: "user-api" },
  transports: [
    new winston.transports.File({ filename: "error.log", level: "error" }),
    new winston.transports.File({ filename: "combined.log" }),
  ],
});

// Log API requests with context
app.use((req, res, next) => {
  const requestId = req.headers["x-request-id"] || uuid();
  req.requestId = requestId;

  // Log at completion of request
  const start = Date.now();
  res.on("finish", () => {
    logger.info({
      type: "request",
      requestId,
      method: req.method,
      path: req.path,
      statusCode: res.statusCode,
      responseTime: Date.now() - start,
      userAgent: req.headers["user-agent"],
      userId: req.user?.id,
    });
  });

  next();
});
```

- **Centralized Log Management**:
  - Aggregate logs with the ELK stack (Elasticsearch, Logstash, Kibana) or Graylog
  - Implement log rotation and retention policies
  - Set up alerts based on log patterns

### Alerting Strategy

- **Define Alert Thresholds**:
  - Set meaningful thresholds based on business impact
  - Implement tiered alerting (warning vs. critical)
  - Avoid alert fatigue with proper tuning

```yaml
# Alertmanager Configuration Example
route:
  receiver: "team-api"
  group_by: ["alertname", "cluster", "service"]
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h
  routes:
    - match:
        severity: critical
      receiver: "pager-duty-critical"
      repeat_interval: 1h
    - match:
        severity: warning
      receiver: "slack-warnings"

receivers:
  - name: "team-api"
    slack_configs:
      - channel: "#api-alerts"
        send_resolved: true

  - name: "pager-duty-critical"
    pagerduty_configs:
      - service_key: "<your-pagerduty-service-key>"

  - name: "slack-warnings"
    slack_configs:
      - channel: "#api-warnings"
        send_resolved: true
```

- **On-Call Rotation**:
  - Establish clear on-call schedules
  - Use tools like PagerDuty or OpsGenie
  - Document escalation procedures

### API Analytics

- **Track API Usage Patterns**:

  - Most used endpoints
  - User adoption metrics
  - Feature utilization
  - Client types (platforms, versions)

- **Performance Analytics**:

  - Endpoint performance comparison
  - Bottleneck identification
  - Regional performance variations

- **Business Impact Metrics**:
  - Conversion rates tied to API
  - Revenue-generating API operations
  - Customer engagement metrics

## Real-world DevOps Integration Examples

### CI/CD Pipeline for API Deployment

- **Automated Testing and Deployment**:
  - Unit tests
  - Integration tests
  - Contract tests
  - Security scans
  - Automated deployments with blue/green or canary strategies

```yaml
# GitLab CI/CD Pipeline Example for API
stages:
  - build
  - test
  - security
  - deploy-staging
  - integration-test
  - deploy-production

build:
  stage: build
  script:
    - docker build -t ${CI_REGISTRY_IMAGE}:${CI_COMMIT_SHA} .
    - docker push ${CI_REGISTRY_IMAGE}:${CI_COMMIT_SHA}

unit-tests:
  stage: test
  script:
    - npm install
    - npm run test:unit

integration-tests:
  stage: test
  script:
    - npm run test:integration

security-scan:
  stage: security
  script:
    - npm audit
    - docker run --rm -v $(pwd):/app owasp/zap2docker-stable zap-baseline.py -t https://staging-api.example.com

deploy-staging:
  stage: deploy-staging
  script:
    - kubectl set image deployment/api-staging api=${CI_REGISTRY_IMAGE}:${CI_COMMIT_SHA}
  environment:
    name: staging
    url: https://staging-api.example.com

contract-tests:
  stage: integration-test
  script:
    - npm run test:contract

deploy-production:
  stage: deploy-production
  script:
    - kubectl set image deployment/api-production api=${CI_REGISTRY_IMAGE}:${CI_COMMIT_SHA}
  environment:
    name: production
    url: https://api.example.com
  when: manual
```

### Kubernetes API Deployment Example

- **API Microservice Architecture**:
  - Containerization with Docker
  - Orchestration with Kubernetes
  - Service mesh integration

```yaml
# Kubernetes Deployment for API Service
apiVersion: apps/v1
kind: Deployment
metadata:
  name: user-api
  labels:
    app: user-api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: user-api
  template:
    metadata:
      labels:
        app: user-api
    spec:
      containers:
        - name: user-api
          image: example/user-api:v1.2.3
          ports:
            - containerPort: 8080
          readinessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 5
            periodSeconds: 10
          livenessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 15
            periodSeconds: 20
          resources:
            limits:
              cpu: "1"
              memory: "512Mi"
            requests:
              cpu: "0.5"
              memory: "256Mi"
          env:
            - name: DB_HOST
              valueFrom:
                configMapKeyRef:
                  name: api-config
                  key: db_host
            - name: DB_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: api-secrets
                  key: db_password
---
apiVersion: v1
kind: Service
metadata:
  name: user-api
spec:
  selector:
    app: user-api
  ports:
    - port: 80
      targetPort: 8080
  type: ClusterIP
```

### Infrastructure as Code (IaC) for API Infrastructure

- **Terraform for Cloud Resources**:
  - Provision API Gateway
  - Set up load balancers
  - Configure network security

```hcl
# Terraform AWS API Gateway Example
provider "aws" {
  region = "us-west-2"
}

resource "aws_api_gateway_rest_api" "example_api" {
  name        = "example-api"
  description = "Example API Gateway"

  endpoint_configuration {
    types = ["REGIONAL"]
  }
}

resource "aws_api_gateway_resource" "users_resource" {
  rest_api_id = aws_api_gateway_rest_api.example_api.id
  parent_id   = aws_api_gateway_rest_api.example_api.root_resource_id
  path_part   = "users"
}

resource "aws_api_gateway_method" "users_get" {
  rest_api_id   = aws_api_gateway_rest_api.example_api.id
  resource_id   = aws_api_gateway_resource.users_resource.id
  http_method   = "GET"
  authorization_type = "COGNITO_USER_POOLS"
  authorizer_id = aws_api_gateway_authorizer.cognito.id
}

resource "aws_api_gateway_integration" "users_get_integration" {
  rest_api_id = aws_api_gateway_rest_api.example_api.id
  resource_id = aws_api_gateway_resource.users_resource.id
  http_method = aws_api_gateway_method.users_get.http_method

  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.users_lambda.invoke_arn
}

resource "aws_api_gateway_deployment" "example" {
  depends_on = [
    aws_api_gateway_integration.users_get_integration
  ]

  rest_api_id = aws_api_gateway_rest_api.example_api.id
  stage_name  = "v1"
}

resource "aws_lambda_permission" "apigw_lambda" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.users_lambda.function_name
  principal     = "apigateway.amazonaws.com"

  source_arn = "${aws_api_gateway_rest_api.example_api.execution_arn}/*/${aws_api_gateway_method.users_get.http_method}${aws_api_gateway_resource.users_resource.path}"
}
```

### API Gateway Implementation

- **Using API Gateway for Advanced Features**:
  - Authentication/authorization
  - Rate limiting
  - Request transformation
  - Response caching

```yaml
# AWS API Gateway with Swagger Definition
swagger: "2.0"
info:
  title: User API
  version: "1.0"
basePath: /v1
schemes:
  - https
paths:
  /users:
    get:
      summary: List all users
      produces:
        - application/json
      parameters:
        - name: limit
          in: query
          type: integer
          required: false
          default: 20
      responses:
        200:
          description: Successful response
      security:
        - CognitoAuth: []
      x-amazon-apigateway-integration:
        uri: arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:123456789012:function:GetUsers/invocations
        passthroughBehavior: when_no_match
        httpMethod: POST
        type: aws_proxy
    post:
      summary: Create a new user
      produces:
        - application/json
      consumes:
        - application/json
      parameters:
        - name: user
          in: body
          required: true
          schema:
            $ref: "#/definitions/User"
      responses:
        201:
          description: User created
      security:
        - CognitoAuth: []
      x-amazon-apigateway-integration:
        uri: arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:123456789012:function:CreateUser/invocations
        passthroughBehavior: when_no_match
        httpMethod: POST
        type: aws_proxy

securityDefinitions:
  CognitoAuth:
    type: apiKey
    name: Authorization
    in: header
    x-amazon-apigateway-authtype: cognito_user_pools
    x-amazon-apigateway-authorizer:
      providerARNs:
        - arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_XXXXXXXXX
      type: cognito_user_pools

definitions:
  User:
    type: object
    required:
      - username
      - email
    properties:
      username:
        type: string
      email:
        type: string
      firstName:
        type: string
      lastName:
        type: string
```

### Monitoring Integration Example

- **Connecting API Metrics to Monitoring System**:
  - Instrumenting code
  - Exposing metrics endpoints
  - Integration with monitoring platforms

```javascript
// Node.js Prometheus Metrics Integration
const express = require("express");
const promClient = require("prom-client");
const app = express();

// Create a Registry to register the metrics
const register = new promClient.Registry();
promClient.collectDefaultMetrics({ register });

// Create custom metrics
const httpRequestDurationMicroseconds = new promClient.Histogram({
  name: "http_request_duration_seconds",
  help: "Duration of HTTP requests in seconds",
  labelNames: ["method", "route", "status_code"],
  buckets: [0.1, 0.3, 0.5, 0.7, 1, 3, 5, 7, 10],
});

const httpRequestsTotal = new promClient.Counter({
  name: "http_requests_total",
  help: "Total number of HTTP requests",
  labelNames: ["method", "route", "status_code"],
});

register.registerMetric(httpRequestDurationMicroseconds);
register.registerMetric(httpRequestsTotal);

// Middleware to measure request duration
app.use((req, res, next) => {
  const end = httpRequestDurationMicroseconds.startTimer();
  res.on("finish", () => {
    const route = req.route ? req.route.path : req.path;
    end({ method: req.method, route, status_code: res.statusCode });
    httpRequestsTotal.inc({
      method: req.method,
      route,
      status_code: res.statusCode,
    });
  });
  next();
});

// Expose metrics endpoint for Prometheus scraping
app.get("/metrics", async (req, res) => {
  res.set("Content-Type", register.contentType);
  res.end(await register.metrics());
});

// API routes
app.get("/api/users", (req, res) => {
  // Handle request
  res.json({ users: [] });
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});
```

## Troubleshooting Common Issues

### API Performance Issues

- **Latency Problems**:
  - **Symptoms**: Slow response times, timeouts
  - **Troubleshooting Steps**:
    1. Check system metrics (CPU, memory, disk I/O)
    2. Review database query performance
    3. Look for network bottlenecks
    4. Check for external service dependencies
    5. Analyze application code for inefficiencies
  - **Solutions**:
    - Optimize database queries
    - Implement caching
    - Scale horizontally or vertically
    - Reduce payload sizes

```bash
# Using curl with timing details to diagnose latency
curl -w "\nDNS Lookup: %{time_namelookup}s\nConnect: %{time_connect}s\nTLS Setup: %{time_appconnect}s\nPre-transfer: %{time_pretransfer}s\nStart Transfer: %{time_starttransfer}s\nTotal: %{time_total}s\n" -o /dev/null -s https://api.example.com/users
```

### Authentication and Authorization Issues

- **Authentication Failures**:
  - **Symptoms**: 401 Unauthorized responses, token validation errors
  - **Troubleshooting Steps**:
    1. Verify token format and expiration
    2. Check authentication server connectivity
    3. Review client credentials
    4. Examine token signature validation
  - **Solutions**:
    - Refresh access tokens
    - Update client credentials
    - Fix token validation logic

```bash
# Testing JWT token expiration
TOKEN="your.jwt.token"
EXPIRY=$(echo -n $TOKEN | cut -d"." -f2 | base64 -d 2>/dev/null | jq -r '.exp')
NOW=$(date +%s)

if [ $EXPIRY -lt $NOW ]; then
  echo "Token expired. Expiry: $(date -d @$EXPIRY)"
else
  echo "Token valid. Expires: $(date -d @$EXPIRY)"
fi
```

- **Authorization Problems**:
  - **Symptoms**: 403 Forbidden responses
  - **Troubleshooting Steps**:
    1. Verify user roles and permissions
    2. Check resource access controls
    3. Examine authorization logic
  - **Solutions**:
    - Update user permissions
    - Fix authorization rules
    - Ensure proper role assignments

### API Integration Issues

- **Contract Violations**:
  - **Symptoms**: Unexpected data formats, missing fields
  - **Troubleshooting Steps**:
    1. Compare request/response against API documentation
    2. Verify API versioning
    3. Check for schema changes
  - **Solutions**:
    - Update client code to match API contract
    - Implement versioning strategy
    - Use contract testing

```javascript
// Axios Interceptor for API Debugging
axios.interceptors.request.use(
  (request) => {
    console.log("Request:", {
      method: request.method,
      url: request.url,
      data: request.data,
      headers: request.headers,
    });
    return request;
  },
  (error) => {
    console.error("Request Error:", error);
    return Promise.reject(error);
  }
);

axios.interceptors.response.use(
  (response) => {
    console.log("Response:", {
      status: response.status,
      data: response.data,
      headers: response.headers,
    });
    return response;
  },
  (error) => {
    console.error(
      "Response Error:",
      error.response
        ? {
            status: error.response.status,
            data: error.response.data,
            headers: error.response.headers,
          }
        : error.message
    );
    return Promise.reject(error);
  }
);
```

- **CORS Issues**:
  - **Symptoms**: Browser console errors about CORS policy
  - **Troubleshooting Steps**:
    1. Check server CORS configuration
    2. Verify request Origin headers
    3. Examine preflight requests
  - **Solutions**:
    - Update CORS policy on server
    - Ensure all required headers are included

```bash
# Testing CORS with curl (preflight request)
curl -X OPTIONS https://api.example.com/users \
  -H "Origin: https://app.example.com" \
  -H "Access-Control-Request-Method: GET" \
  -H "Access-Control-Request-Headers: Content-Type, Authorization" \
  -v
```

### Rate Limiting and Throttling

- **Rate Limit Exceeded**:
  - **Symptoms**: 429 Too Many Requests responses
  - **Troubleshooting Steps**:
    1. Check rate limit headers in responses
    2. Review API usage patterns
    3. Examine request distribution
  - **Solutions**:
    - Implement client-side rate limiting
    - Add request queueing
    - Optimize API usage to reduce calls

```python
# Python Requests with Retry Logic for Rate Limiting
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

retry_strategy = Retry(
    total=3,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["HEAD", "GET", "OPTIONS", "POST", "PUT", "DELETE"],
    backoff_factor=1
)

adapter = HTTPAdapter(max_retries=retry_strategy)
session = requests.Session()
session.mount("https://", adapter)
session.mount("http://", adapter)

try:
    response = session.get("https://api.example.com/users")
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
    if e.response.status_code == 429:
        reset_time = e.response.headers.get('X-RateLimit-Reset')
        print(f"Rate limit exceeded. Try again after: {reset_time}")
```

### Server-side Issues

- **Server Errors (5xx)**:
  - **Symptoms**: 500, 502, 503, 504 responses
  - **Troubleshooting Steps**:
    1. Check server logs
    2. Monitor resource utilization
    3. Review recent deployments
    4. Examine load balancer status
  - **Solutions**:
    - Fix application bugs
    - Scale resources
    - Implement circuit breakers
    - Rollback problematic deployments

```bash
# Checking Kubernetes pod logs
kubectl logs deployment/api-service -n api-namespace

# Checking server metrics
kubectl top pods -n api-namespace

# Checking events
kubectl get events -n api-namespace
```

### Debugging Strategies

- **Request Tracing**:
  - Implement distributed tracing with Jaeger or Zipkin
  - Use correlation IDs across services

```python
# Python Flask with OpenTelemetry tracing
from flask import Flask, request
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.flask import FlaskInstrumentor

# Configure the tracer
resource = Resource(attributes={SERVICE_NAME: "user-api"})
tracer_provider = TracerProvider(resource=resource)
trace.set_tracer_provider(tracer_provider)

# Configure the Jaeger exporter
jaeger_exporter = JaegerExporter(
    agent_host_name="jaeger",
    agent_port=6831,
)

# Add the exporter to the tracer
tracer_provider.add_span_processor(BatchSpanProcessor(jaeger_exporter))

# Get a tracer
tracer = trace.get_tracer(__name__)

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)

@app.route('/api/users/<user_id>')
def get_user(user_id):
    with tracer.start_as_current_span("get_user_details") as span:
        span.set_attribute("user.id", user_id)
        # Fetch user from database
        span.add_event("Fetching user from database")

        # ... code to fetch user ...

        span.add_event("User successfully retrieved")
        return {"id": user_id, "name":
```
