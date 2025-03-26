# Complete Dockerfile Tutorial

## Introduction to Dockerfiles

A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image. Using `docker build`, users can create an automated build that executes several command-line instructions in succession.

This tutorial covers everything from basic Dockerfile syntax to advanced multi-stage builds and optimization techniques.

## Table of Contents

1. [Dockerfile Basics](#dockerfile-basics)
2. [Core Dockerfile Instructions](#core-dockerfile-instructions)
3. [Building Images from Dockerfiles](#building-images-from-dockerfiles)
4. [Dockerfile Best Practices](#dockerfile-best-practices)
5. [Environment Variables and Arguments](#environment-variables-and-arguments)
6. [Working with Volumes](#working-with-volumes)
7. [Multi-Stage Builds](#multi-stage-builds)
8. [Optimizing Dockerfile for Caching](#optimizing-dockerfile-for-caching)
9. [Security Considerations](#security-considerations)
10. [Advanced Dockerfile Examples](#advanced-dockerfile-examples)
11. [Debugging Dockerfile Issues](#debugging-dockerfile-issues)
12. [Dockerfile Linting and Validation](#dockerfile-linting-and-validation)

## Dockerfile Basics

A Dockerfile must begin with a `FROM` instruction which sets the base image. A Dockerfile generally consists of:

```dockerfile
# Comment
INSTRUCTION arguments
```

Instructions are not case-sensitive but are conventionally written in UPPERCASE for clarity.

### Basic Structure Example

```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
```

## Core Dockerfile Instructions

### FROM

Specifies the base image to use as the starting point:

```dockerfile
FROM ubuntu:20.04
FROM python:3.9-alpine
FROM node:14 AS build-stage
```

You can use `FROM scratch` to start from an empty image for building minimal images.

### WORKDIR

Sets the working directory for any subsequent `RUN`, `CMD`, `ENTRYPOINT`, `COPY`, and `ADD` instructions:

```dockerfile
WORKDIR /app
```

Best practice is to use `WORKDIR` instead of complex `RUN cd /some/path` commands.

### COPY and ADD

Both copy files from the host into the image:

```dockerfile
# Copy a single file
COPY file.txt /app/

# Copy a directory
COPY src/ /app/src/

# Copy with wildcards
COPY *.txt /app/

# Copy and preserve file ownership and permissions
COPY --chown=user:group file.txt /app/
```

`ADD` has similar syntax but additional features:
- Can extract compressed files (tar, gzip, etc.)
- Can download files from URLs (not recommended; use `RUN curl` or `RUN wget` instead)

```dockerfile
# Extract a tar file into the destination
ADD app.tar.gz /app/

# Download from a URL (not recommended)
ADD http://example.com/file.txt /app/
```

### RUN

Executes commands in a new layer on top of the current image:

```dockerfile
# Shell form
RUN apt-get update && apt-get install -y curl

# Exec form (recommended)
RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "curl"]
```

Chain commands with `&&` to avoid creating unnecessary layers.

### CMD and ENTRYPOINT

`CMD` provides the default command for running the container:

```dockerfile
# Shell form
CMD echo "Hello world"

# Exec form (recommended)
CMD ["echo", "Hello world"]

# Common pattern for web servers
CMD ["npm", "start"]
```

`ENTRYPOINT` configures the container to run as an executable:

```dockerfile
ENTRYPOINT ["nginx", "-g", "daemon off;"]
```

The difference is that `CMD` can be overridden at runtime, while `ENTRYPOINT` is fixed but can receive additional arguments from `CMD` or the command line.

Common pattern combining both:

```dockerfile
ENTRYPOINT ["python", "app.py"]
CMD ["--help"]
```

Here, `--help` will be passed to `app.py` but can be overridden.

### EXPOSE

Informs Docker that the container listens on specified network ports at runtime:

```dockerfile
EXPOSE 80
EXPOSE 80/tcp
EXPOSE 80/udp
```

This doesn't actually publish the port—use `-p` or `-P` with `docker run` to publish ports.

### ENV

Sets environment variables in the image:

```dockerfile
ENV NODE_ENV=production
ENV PATH="/usr/local/bin:${PATH}"

# Multiple variables can be set at once
ENV APP_HOME=/app \
    APP_VERSION=1.0.0 \
    DEBUG=false
```

### ARG

Defines build-time variables that can be passed during the build:

```dockerfile
ARG VERSION=latest
ARG BUILD_DATE
ARG USER=www-data

FROM ubuntu:${VERSION}
```

Use `--build-arg` when building the image:

```bash
docker build --build-arg VERSION=18.04 -t myapp .
```

### LABEL

Adds metadata to an image:

```dockerfile
LABEL version="1.0"
LABEL description="This is my custom image"
LABEL maintainer="example@example.com"

# Multiple labels in one instruction
LABEL org.opencontainers.image.version="1.0.0" \
    org.opencontainers.image.authors="Example Team <team@example.com>" \
    org.opencontainers.image.url="https://example.com"
```

### USER

Sets the user name or UID to use when running the image:

```dockerfile
USER www-data
USER 1000
```

### VOLUME

Creates a mount point and marks it as holding externally mounted volumes:

```dockerfile
VOLUME /data
VOLUME ["/data", "/logs"]
```

### HEALTHCHECK

Tells Docker how to test if the container is still working:

```dockerfile
HEALTHCHECK --interval=5m --timeout=3s \
    CMD curl -f http://localhost/ || exit 1

HEALTHCHECK NONE  # Disable any healthcheck inherited from the base image
```

### SHELL

Changes the default shell used for the shell form of commands:

```dockerfile
SHELL ["/bin/bash", "-c"]
```

### STOPSIGNAL

Sets the system call signal that will be sent to the container to exit:

```dockerfile
STOPSIGNAL SIGTERM
```

### ONBUILD

Adds a trigger instruction to be executed when the image is used as the base for another build:

```dockerfile
ONBUILD ADD . /app/src
ONBUILD RUN /app/src/build.sh
```

## Building Images from Dockerfiles

Once you've created your Dockerfile, you can build an image using the `docker build` command:

```bash
# Basic build from current directory
docker build -t myimage:latest .

# Build with a specific Dockerfile
docker build -f Dockerfile.prod -t myimage:prod .

# Build with build arguments
docker build --build-arg VERSION=2.0 -t myimage .

# Build without using cache
docker build --no-cache -t myimage .

# Build with specific target stage in multi-stage build
docker build --target build-stage -t myimage:build .
```

## Dockerfile Best Practices

### Use Official Base Images

Start with official images when possible:

```dockerfile
FROM node:14-alpine  # Better than custom OS with Node installed
```

### Minimize Layers

Combine related commands to reduce the number of layers:

```dockerfile
# Bad: Creates 3 layers
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get clean

# Good: Creates 1 layer
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
```

### Use .dockerignore File

Create a `.dockerignore` file to exclude files and directories from the build context:

```
# Example .dockerignore
node_modules
npm-debug.log
Dockerfile*
.dockerignore
.git
.gitignore
README.md
LICENSE
*.swp
*.md
```

### Set Non-Root Users

Run containers as a non-root user when possible:

```dockerfile
# Create a user and group
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set permissions
RUN mkdir /app && chown -R appuser:appuser /app

# Switch to the user
USER appuser

WORKDIR /app
```

### Use Specific Tags

Avoid `latest` tag in production; use specific versions:

```dockerfile
FROM node:14.17.0-alpine3.13
```

### Clean Up in the Same Layer

Remove temporary files in the same `RUN` instruction:

```dockerfile
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
```

### Sort Multi-line Arguments

Keep multi-line arguments sorted for better readability and maintainability:

```dockerfile
RUN apt-get update && apt-get install -y \
    curl \
    git \
    nginx \
    python \
    unzip \
    && rm -rf /var/lib/apt/lists/*
```

## Environment Variables and Arguments

### Using Build Arguments

Build arguments are variables available only during the build process:

```dockerfile
ARG NODE_ENV=production
ARG VERSION

# Use arguments in other instructions
RUN if [ "$NODE_ENV" = "development" ]; then \
    npm install; \
    else \
    npm install --only=production; \
    fi

# Arguments available after FROM must be redeclared
FROM ubuntu:${VERSION}
ARG NODE_ENV
RUN echo $NODE_ENV
```

### Using Environment Variables

Environment variables persist in the built image:

```dockerfile
# Set default environment variables
ENV APP_HOME=/app \
    LOG_LEVEL=info \
    NODE_ENV=production

# Use variables in other instructions
RUN mkdir -p ${APP_HOME}
WORKDIR ${APP_HOME}

# Override variables at runtime
# docker run -e NODE_ENV=development myimage
```

### Using ARG and ENV Together

A common pattern is to set default ENV values from ARG:

```dockerfile
ARG VERSION=1.0
ENV APP_VERSION=${VERSION}
```

This allows the build argument to influence the environment variable, but the environment variable remains in the image.

## Working with Volumes

### Declaring Volumes

```dockerfile
# Specify one or more volumes
VOLUME /data
VOLUME ["/data", "/logs", "/tmp"]

# Typically used for:
# - Database storage
# - Configuration files
# - Shared files between containers
```

### Docker Compose and Volumes

While Dockerfile can declare volumes, Docker Compose provides more control:

```yaml
# docker-compose.yml example with volumes
version: '3'
services:
web:
build: .
volumes:
- ./data:/app/data
- db-data:/app/db

volumes:
db-data:
```

## Multi-Stage Builds

Multi-stage builds allow you to use multiple FROM statements in a Dockerfile. Each FROM instruction can use a different base image, and begins a new stage of the build:

```dockerfile
# Build stage
FROM node:14 AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Production stage
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

Benefits of multi-stage builds:
- Smaller final images
- Separation of build and runtime environments
- No need for separate build scripts

### More Complex Multi-Stage Example

```dockerfile
# Stage 1: Build the application
FROM maven:3.8-openjdk-11 AS builder
WORKDIR /app
COPY pom.xml .
# Download dependencies separately (for better caching)
RUN mvn dependency:go-offline
COPY src ./src
RUN mvn package -DskipTests

# Stage 2: Create a slim JRE image
FROM eclipse-temurin:11-jre-alpine
WORKDIR /app
# Copy only the built jar from the previous stage
COPY --from=builder /app/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

### Using Specific Stages

You can build up to a specific stage:

```bash
docker build --target builder -t myapp:build .
```

## Optimizing Dockerfile for Caching

Docker caches the result of each instruction to speed up subsequent builds. Understanding and optimizing for this caching mechanism is important:

### Order Instructions from Least to Most Frequently Changing

```dockerfile
# Less frequently changed instructions
FROM node:14
WORKDIR /app
RUN npm install -g some-global-tool

# More frequently changed instructions
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
```

### Cache Busting

Instructions invalidate the cache when their inputs change. For package managers, separate dependency installation from code copying:

```dockerfile
# Copy just package files first
COPY package.json package-lock.json ./
RUN npm install

# Then copy the rest of the code
COPY . .
```

### Using Build Arguments for Cache Busting

Sometimes you want to force a fresh build from a certain point:

```dockerfile
FROM ubuntu:20.04

ARG CACHEBUST=1
RUN echo "Build number: $CACHEBUST" && apt-get update
```

Build with:
```bash
docker build --build-arg CACHEBUST=$(date +%s) -t myapp .
```

## Security Considerations

### Avoid Storing Secrets in Images

```dockerfile
# Bad practice
ENV AWS_ACCESS_KEY=...
ENV AWS_SECRET_KEY=...

# Better: Use build arguments that don't persist in the final image
ARG AWS_ACCESS_KEY
ARG AWS_SECRET_KEY
RUN aws configure set aws_access_key_id $AWS_ACCESS_KEY && \
    aws configure set aws_secret_access_key $AWS_SECRET_KEY && \
    aws s3 cp s3://my-bucket/config.json /app/config.json

# Best: Use runtime secrets injection
# docker run --env-file=.env myimage
```

### Scan Images for Vulnerabilities

```bash
# Using Docker Scan (powered by Snyk)
docker scan myimage:latest

# Alternative tools include:
# - Clair
# - Trivy
# - Anchore
```

### Use Minimal Base Images

```dockerfile
# Full OS base image
FROM ubuntu:20.04  # ~70MB+

# Smaller alternative
FROM alpine:3.14  # ~5MB

# Even smaller, language-specific bases
FROM python:3.9-alpine  # Python + Alpine
FROM node:14-slim  # Node.js + Debian Slim
```

### Keep Images Updated

Regularly rebuild images to get the latest security patches:

```dockerfile
# Specify exact versions but rebuild regularly
FROM python:3.9.7-alpine3.14
```

## Advanced Dockerfile Examples

### Python Web Application

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN useradd -m appuser
USER appuser

# Configure environment
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/home/appuser/.local/bin:$PATH"

# Run application
EXPOSE 8000
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000", "--workers", "4"]
```

### Node.js Web Application

```dockerfile
FROM node:16-alpine AS builder

# Set working directory
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm ci

# Copy and build code
COPY . .
RUN npm run build

# Production image
FROM node:16-alpine

# Set working directory
WORKDIR /app

# Install production dependencies
COPY package*.json ./
RUN npm ci --only=production

# Copy built application from builder stage
COPY --from=builder /app/dist ./dist

# Create non-root user
RUN addgroup -g 1001 appuser && \
    adduser -S -u 1001 -G appuser appuser
USER appuser

# Run application
EXPOSE 3000
CMD ["npm", "start"]
```

### Java Spring Boot Application

```dockerfile
FROM maven:3.8-openjdk-17 AS builder

WORKDIR /app

# Copy pom.xml and download dependencies
COPY pom.xml .
RUN mvn dependency:go-offline -B

# Copy source and build
COPY src ./src
RUN mvn package -DskipTests

# Create slim runtime image
FROM eclipse-temurin:17-jre-alpine

WORKDIR /app

# Copy built jar from builder stage
COPY --from=builder /app/target/*.jar app.jar

# Run as non-root
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# Set Spring Boot profile
ENV SPRING_PROFILES_ACTIVE=production

# Run application
EXPOSE 8080
ENTRYPOINT ["java", "-Djava.security.egd=file:/dev/./urandom", "-jar", "app.jar"]
```

### Go Application

```dockerfile
FROM golang:1.17-alpine AS builder

WORKDIR /app

# Download dependencies
COPY go.mod go.sum ./
RUN go mod download

# Copy source and build
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .

# Create minimal runtime image
FROM alpine:3.14

WORKDIR /app

# Install certificates for HTTPS
RUN apk --no-cache add ca-certificates

# Copy binary from builder stage
COPY --from=builder /app/app .

# Create non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# Run application
EXPOSE 8080
CMD ["./app"]
```

## Debugging Dockerfile Issues

### Common Issues and Solutions

1. **Build fails with "context canceled"**
- Usually indicates a timeout issue or interrupted build
- Make sure `.dockerignore` excludes large files

2. **Build is slow**
- Optimize caching with proper ordering of instructions
- Use `.dockerignore` to reduce build context size
- Use smaller base images

3. **Image is too large**
- Use multi-stage builds
- Remove unnecessary files in the same layer they're created
- Use smaller base images like Alpine

4. **Container exits immediately**
- Check your `CMD` or `ENTRYPOINT`
- Use `docker run -it` to get an interactive shell
- Look at logs with `docker logs <container-id>`

5. **Can't access service in container**
- Make sure you've used `EXPOSE` and published the port with `-p`
- Check if the service is bound to localhost instead of 0.0.0.0

### Debugging Commands

```bash
# See the history of an image (layers)
docker history myimage:latest

# Inspect image configuration
docker inspect myimage:latest

# Run container with interactive shell
docker run -it --rm myimage:latest /bin/sh

# Show logs
docker logs <container-id>

# Check which files are included in the build context
docker build --no-cache -t test . -f - <<EOF
FROM alpine
WORKDIR /src
COPY . .
RUN find . -type f | sort
EOF
```

## Dockerfile Linting and Validation

### Using hadolint

Hadolint is a Dockerfile linter that helps you build best practice Docker images:

```bash
# Install hadolint
docker pull hadolint/hadolint

# Lint a Dockerfile
docker run --rm -i hadolint/hadolint < Dockerfile
```

Common issues it catches:
- Using `latest` tags
- Missing version in `apt-get install`
- Not cleaning up in the same layer
- Using `sudo`

### Automated Validation in CI/CD

Add Dockerfile validation to your CI/CD pipeline:

```yaml
# GitHub Actions example
name: Validate Dockerfile

on: [push, pull_request]

jobs:
lint:
runs-on: ubuntu-latest
steps:
- uses: actions/checkout@v2
- name: Lint Dockerfile
uses: brpaz/hadolint-action@master
with:
dockerfile: "Dockerfile"
```
