# Docker Containers and Port Mapping: A Comprehensive Guide

## Table of Contents

1. [Introduction to Docker Containers](#introduction-to-docker-containers)
2. [Basic Container Operations](#basic-container-operations)
3. [Docker Networking Fundamentals](#docker-networking-fundamentals)
4. [Understanding Port Mapping](#understanding-port-mapping)
5. [Port Mapping Techniques](#port-mapping-techniques)
6. [Advanced Port Mapping Topics](#advanced-port-mapping-topics)
7. [Port Mapping in Docker Compose](#port-mapping-in-docker-compose)
8. [Common Use Cases and Examples](#common-use-cases-and-examples)
9. [Troubleshooting Port Mapping Issues](#troubleshooting-port-mapping-issues)
10. [Best Practices](#best-practices)

## Introduction to Docker Containers

Docker containers are lightweight, standalone, executable packages that include everything needed to run an application: code, runtime, system tools, libraries, and settings. Containers isolate software from its surroundings, ensuring it works uniformly across different environments.

### Container vs. Image

Before diving into running containers, it's important to understand the relationship between Docker images and containers:

- **Docker Image**: A read-only template with instructions for creating a Docker container
- **Docker Container**: A runnable instance of an image

Think of an image as a class and a container as an object instantiated from that class.

## Basic Container Operations

### Running Your First Container

The `docker run` command is the primary way to start a new container:

```bash
docker run hello-world
```

This command:
1. Looks for the "hello-world" image locally
2. If not found, pulls it from Docker Hub
3. Creates a new container
4. Runs the container, which prints a message
5. Exits when the process completes

### Container Lifecycle Commands

```bash
# Start a new container
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Stop a running container gracefully
docker stop CONTAINER_ID_OR_NAME

# Force stop a container (like unplugging a computer)
docker kill CONTAINER_ID_OR_NAME

# Start a stopped container
docker start CONTAINER_ID_OR_NAME

# Restart a container
docker restart CONTAINER_ID_OR_NAME

# Remove a stopped container
docker rm CONTAINER_ID_OR_NAME

# Remove a running container forcibly
docker rm -f CONTAINER_ID_OR_NAME
```

### Important `docker run` Options

```bash
# Run container in background (detached mode)
docker run -d nginx

# Give the container a name
docker run --name my-nginx nginx

# Remove container automatically when it exits
docker run --rm nginx

# Allocate a pseudo-TTY and keep STDIN open
docker run -it ubuntu bash
```

## Docker Networking Fundamentals

Before diving into port mapping, it's essential to understand Docker's networking model.

### Default Network Types

Docker creates several networks automatically:

```bash
# List all networks
docker network ls
```

The default networks include:

- **bridge**: The default network. Containers on this network can communicate but are isolated from the host network.
- **host**: Containers use the host's networking directly (no isolation).
- **none**: Containers have no external network connectivity.

### Network Inspection

```bash
# Inspect bridge network
docker network inspect bridge
```

This command reveals details about the network, including:
- Subnet and gateway configuration
- Connected containers
- Network driver information

## Understanding Port Mapping

### Container Isolation

By default, containers are isolated from the host network. While they can connect to external networks, external clients can't connect directly to a container.

### The Need for Port Mapping

Port mapping (also called port publishing or port forwarding) creates a connection between:
- A port on the host system
- A port on the container

This mapping allows external systems to communicate with applications running inside containers.

### Container and Host Ports

In Docker port mapping:
- **Host Port**: The port on your computer/server
- **Container Port**: The port inside the Docker container

These don't have to be the same number, which allows multiple containers to use the same internal port (e.g., 80) while mapping to different host ports.

### Port Mapping Diagram

```
               Host                   │                Container
                                      │
┌───────────────────────────────────┐ │ ┌───────────────────────────────────┐
│                                   │ │ │                                   │
│  External Client                  │ │ │  Container Application            │
│  connects to host's IP            │ │ │  listens on container port        │
│  on published port                │ │ │                                   │
│                                   │ │ │                                   │
└───────────────┬───────────────────┘ │ └───────────────┬───────────────────┘
                │                     │                 │
                │                     │                 │
                ▼                     │                 ▼
┌───────────────────────────────────┐ │ ┌───────────────────────────────────┐
│                                   │ │ │                                   │
│  Host Port (e.g., 8080)           │ │ │  Container Port (e.g., 80)        │
│                                   │ │ │                                   │
└───────────────┬───────────────────┘ │ └───────────────┬───────────────────┘
                │                     │                 │
                └─────────────────────┼─────────────────┘
                                      │
                    Port Mapping      │
                                      │
```

## Port Mapping Techniques

### Basic Port Mapping

The `-p` or `--publish` flag maps container ports to host ports:

```bash
# Map container port 80 to host port 8080
docker run -p 8080:80 nginx
```

Breaking down the format: `-p [HOST_PORT]:[CONTAINER_PORT]`

In this example:
- The Nginx container listens on port 80 (default)
- The host machine maps port 8080 to the container's port 80
- You can access the Nginx server at http://localhost:8080

### Multiple Port Mappings

You can map multiple ports for a single container:

```bash
# Map container ports 80 and 443 to host ports 8080 and 8443
docker run -p 8080:80 -p 8443:443 nginx
```

### Random Host Port Assignment

If you only need access but don't care about the specific host port:

```bash
# Map container port 80 to a random available host port
docker run -p 80 nginx

# Check which port was assigned
docker ps
```

The output of `docker ps` will show something like `0.0.0.0:49153->80/tcp`, meaning port 80 in the container is mapped to port 49153 on the host.

### Specific Interface Binding

By default, ports are bound to all network interfaces (0.0.0.0). You can specify a particular interface:

```bash
# Bind only to localhost (127.0.0.1)
docker run -p 127.0.0.1:8080:80 nginx

# Bind to a specific IP on a multi-homed host
docker run -p 192.168.1.100:8080:80 nginx
```

### UDP Port Mapping

By default, Docker maps TCP ports. For UDP ports, specify the protocol:

```bash
# Map UDP port 53
docker run -p 53:53/udp dns-server

# Map both TCP and UDP for the same port
docker run -p 53:53/tcp -p 53:53/udp dns-server
```

### Publish All Ports

To automatically map all exposed ports (defined in the Dockerfile with `EXPOSE`):

```bash
docker run -P nginx
```

This assigns random host ports for each exposed container port.

## Advanced Port Mapping Topics

### Range of Ports

You can map a range of ports at once:

```bash
# Map container ports 8000-8005 to same host ports
docker run -p 8000-8005:8000-8005 multi-service-app
```

### Host Mode Networking

Skip port mapping entirely by using host network mode:

```bash
docker run --network=host nginx
```

In host mode:
- The container shares the host's network namespace
- Container services are available directly on the host's ports
- No port mapping required
- **Note**: This reduces isolation and container portability

### Container-to-Container Communication

Containers on the same network can communicate directly using container names:

```bash
# Create a network
docker network create mynetwork

# Run container in the network
docker run --name db --network mynetwork -d postgres

# Run another container that can reach the db by name
docker run --name web --network mynetwork -d -p 8080:80 mywebapp
```

Now the `web` container can connect to the `db` container using the hostname `db`.

### MacVLAN Networks

For direct network connection to physical network:

```bash
# Create a macvlan network
docker network create -d macvlan \
  --subnet=192.168.1.0/24 \
  --gateway=192.168.1.1 \
  -o parent=eth0 macnet

# Run container with its own IP on the physical network
docker run --network macnet -d nginx
```

## Port Mapping in Docker Compose

Docker Compose makes it easy to define port mappings in a declarative way:

```yaml
# docker-compose.yml
version: '3'
services:
  web:
    image: nginx
    ports:
      # Simple port mapping
      - "8080:80"
      # With specific interface
      - "127.0.0.1:8443:443"
      # UDP port
      - "53:53/udp"
      # Container port only (random host port)
      - "3000"
```

## Common Use Cases and Examples

### Web Server Example

```bash
# Run Nginx web server
docker run -d -p 8080:80 --name webserver nginx

# Verify by accessing http://localhost:8080 in browser
# or using curl
curl http://localhost:8080
```

### Database Server Example

```bash
# Run MySQL with port mapping
docker run -d \
  --name mysql \
  -e MYSQL_ROOT_PASSWORD=my-secret-pw \
  -p 3306:3306 \
  mysql:8.0

# Connect from host
mysql -h 127.0.0.1 -P 3306 -u root -p
```

### Full Web Application Stack

```bash
# PostgreSQL database
docker run -d \
  --name postgres \
  -e POSTGRES_PASSWORD=password \
  -p 5432:5432 \
  postgres:13

# Backend API
docker run -d \
  --name backend \
  -p 8000:8000 \
  --link postgres:db \
  my-backend-app

# Frontend web server
docker run -d \
  --name frontend \
  -p 80:80 \
  --link backend:api \
  my-frontend-app
```

### Running Multiple Instances of the Same Service

```bash
# First instance on host port 8081
docker run -d -p 8081:80 --name web1 nginx

# Second instance on host port 8082
docker run -d -p 8082:80 --name web2 nginx

# Third instance on host port 8083
docker run -d -p 8083:80 --name web3 nginx
```

## Troubleshooting Port Mapping Issues

### Common Problems and Solutions

1. **Port already in use**

   ```
   Error: Bind for 0.0.0.0:8080 failed: port is already allocated
   ```

   Solutions:
   - Choose a different host port
   - Stop the service using the port:
     ```bash
     # Find what's using port 8080
     sudo lsof -i :8080
     # or
     netstat -tuln | grep 8080
     ```

2. **Container not listening on expected port**

   Check if the application inside the container is correctly configured to listen on the specified port:

   ```bash
   # Inspect the container
   docker inspect CONTAINER_ID
   
   # Check logs
   docker logs CONTAINER_ID
   
   # Access shell and verify listening ports
   docker exec -it CONTAINER_ID sh
   netstat -tuln  # May need to install with: apt-get update && apt-get install -y net-tools
   ```

3. **Firewall blocking connections**

   Ensure your firewall allows connections to the mapped ports:

   ```bash
   # Linux (UFW)
   sudo ufw allow 8080/tcp
   
   # Linux (iptables)
   sudo iptables -A INPUT -p tcp --dport 8080 -j ACCEPT
   ```

4. **Binding to wrong network interface**

   Ensure you're binding to the correct interface or to all interfaces:

   ```bash
   # Bind to all interfaces
   docker run -p 0.0.0.0:8080:80 nginx
   ```

### Debugging Tools

1. **Check container status**

   ```bash
   docker ps
   ```

2. **Inspect port mappings**

   ```bash
   docker port CONTAINER_ID
   ```

3. **Check container logs**

   ```bash
   docker logs CONTAINER_ID
   ```

4. **Network inspection**

   ```bash
   docker inspect CONTAINER_ID | grep IPAddress
   ```

5. **Test connectivity from inside the container**

   ```bash
   docker exec -it CONTAINER_ID sh
   wget -O- http://localhost:80  # Test internal connectivity
   ```

## Best Practices

### Security Considerations

1. **Don't expose unnecessary ports**

   Only map ports that need to be accessible from outside.

2. **Use specific IP bindings when possible**

   ```bash
   # Only accept connections from localhost
   docker run -p 127.0.0.1:8080:80 nginx
   ```

3. **Consider using a reverse proxy**

   Use Nginx or Traefik as a secure entry point to your containers.

4. **Run containers with non-root users**

   ```bash
   docker run -p 8080:80 --user 1000:1000 nginx
   ```

### Performance Optimization

1. **Avoid host mode when not needed**

   Host mode bypasses Docker's network isolation but can impact portability.

2. **Use custom networks for container-to-container communication**

   Direct container communication doesn't need port mapping.

3. **For high-throughput applications, consider host networking**

   ```bash
   docker run --network host high-performance-app
   ```

4. **Be mindful of ephemeral port range**

   When mapping many ports, be aware of the host's ephemeral port range limits.

### Organization and Maintenance

1. **Use consistent port mappings**

   Establish conventions for your team:
   ```bash
   # Frontend on 80xx
   docker run -p 8080:80 frontend
   
   # API on 90xx
   docker run -p 9000:8000 api
   
   # Database on 54xx
   docker run -p 5432:5432 postgres
   ```

2. **Document port mappings**

   Maintain documentation of which services use which ports.

3. **Use Docker Compose for complex setups**

   Docker Compose files serve as both configuration and documentation.

4. **Label containers with port information**

   ```bash
   docker run -p 8080:80 --label "ports=host:8080->container:80" nginx
   ```

## Practical Hands-on Exercises

### Exercise 1: Basic Port Mapping

Run an Nginx web server and access it from your host:

```bash
# Step 1: Pull the Nginx image
docker pull nginx

# Step 2: Run Nginx with port mapping
docker run -d -p 8080:80 --name my-nginx nginx

# Step 3: Verify the container is running
docker ps

# Step 4: Access the web server
curl http://localhost:8080
# Or open http://localhost:8080 in your browser

# Step 5: Stop and remove the container
docker stop my-nginx
docker rm my-nginx
```

### Exercise 2: Multiple Port Mappings

Run a container with multiple mapped ports:

```bash
# Step 1: Pull the image (httpd with SSH)
docker pull httpd

# Step 2: Run with multiple port mappings
docker run -d \
  -p 8080:80 \
  -p 2222:22 \
  --name multiport-container httpd

# Step 3: Verify port mappings
docker port multiport-container

# Step 4: Access the web server
curl http://localhost:8080

# Step 5: Clean up
docker rm -f multiport-container
```

### Exercise 3: Different Interface Bindings

Run containers bound to different network interfaces:

```bash
# Step 1: Run container bound to localhost only
docker run -d -p 127.0.0.1:8080:80 --name localhost-only nginx

# Step 2: Try accessing from localhost
curl http://localhost:8080  # Should work

# Step 3: Run container bound to all interfaces
docker run -d -p 0.0.0.0:8081:80 --name all-interfaces nginx

# Step 4: Clean up
docker rm -f localhost-only all-interfaces
```

### Exercise 4: Container-to-Container Communication

Create a multi-container setup with communication:

```bash
# Step 1: Create a custom network
docker network create myapp-network

# Step 2: Run a backend container
docker run -d \
  --network myapp-network \
  --name backend \
  -e POSTGRES_PASSWORD=password \
  postgres:13

# Step 3: Run a frontend container that can access the backend
docker run -d \
  --network myapp-network \
  --name frontend \
  -p 8080:80 \
  nginx

# Step 4: Test communication between containers
docker exec -it frontend sh -c "apt-get update && apt-get install -y curl && curl backend:5432"
# This might fail with connection refused (which is expected since postgres doesn't respond to HTTP),
# but it shows that name resolution works

# Step 5: Clean up
docker rm -f frontend backend
docker network rm myapp-network
```

## Real-World Examples

### Running a WordPress Site

```bash
# Create a network for the WordPress setup
docker network create wordpress-network

# Run MySQL database
docker run -d \
  --name wordpress-db \
  --network wordpress-network \
  -e MYSQL_ROOT_PASSWORD=rootpassword \
  -e MYSQL_DATABASE=wordpress \
  -e MYSQL_USER=wordpress \
  -e MYSQL_PASSWORD=wordpress \
  -v mysql-data:/var/lib/mysql \
  mysql:5.7

# Run WordPress connected to the database
docker run -d \
  --name wordpress \
  --network wordpress-network \
  -e WORDPRESS_DB_HOST=wordpress-db \
  -e WORDPRESS_DB_USER=wordpress \
  -e WORDPRESS_DB_PASSWORD=wordpress \
  -e WORDPRESS_DB_NAME=wordpress \
  -p 8080:80 \
  -v wordpress-data:/var/www/html \
  wordpress:latest

# Access WordPress at http://localhost:8080
```

### Setting Up a Web Application with Redis Cache

```bash
# Create network
docker network create webapp-network

# Run Redis cache
docker run -d \
  --name redis \
  --network webapp-network \
  redis:alpine

# Run web application
docker run -d \
  --name webapp \
  --network webapp-network \
  -e REDIS_HOST=redis \
  -p 3000:3000 \
  mywebapp:latest

# Access webapp at http://localhost:3000
```

### Running a Reverse Proxy with Multiple Services

```bash
# Create network
docker network create proxy-network

# Run first service
docker run -d \
  --name service1 \
  --network proxy-network \
  httpd:alpine

# Run second service
docker run -d \
  --name service2 \
  --network proxy-network \
  nginx:alpine

# Run reverse proxy
docker run -d \
  --name proxy \
  --network proxy-network \
  -p 80:80 \
  -v $(pwd)/nginx.conf:/etc/nginx/conf.d/default.conf \
  nginx:alpine

# Where nginx.conf contains:
# server {
#     listen 80;
#     location /service1/ {
#         proxy_pass http://service1/;
#     }
#     location /service2/ {
#         proxy_pass http://service2/;
#     }
# }
```

## Monitoring Port Usage

### Viewing Container Port Mappings

```bash
# View all containers with their port mappings
docker ps -a --format "table {{.Names}}\t{{.Image}}\t{{.Ports}}"

# View port mappings for a specific container
docker port CONTAINER_ID_OR_NAME
```

### Monitoring Network Traffic on Container Ports

```bash
# Install necessary tools
apt-get update && apt-get install -y iptraf-ng tcpdump

# Monitor traffic on a specific port
sudo tcpdump -i docker0 port 80

# Monitor all docker network interfaces
sudo iptraf-ng
```
