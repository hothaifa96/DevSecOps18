# Comprehensive Docker Networking Tutorial

## Table of Contents

1. [Introduction to Docker Networking](#introduction-to-docker-networking)
2. [Docker Network Drivers](#docker-network-drivers)
3. [Basic Networking Commands](#basic-networking-commands)
4. [Default Bridge Network](#default-bridge-network)
5. [User-defined Bridge Networks](#user-defined-bridge-networks)
6. [Host Network](#host-network)
7. [Overlay Networks](#overlay-networks)
8. [Macvlan Networks](#macvlan-networks)
9. [None Network](#none-network)
10. [Network Aliases and DNS](#network-aliases-and-dns)
11. [Exposing and Publishing Ports](#exposing-and-publishing-ports)
12. [Container Network Model (CNM)](#container-network-model)
13. [Network Troubleshooting](#network-troubleshooting)
15. [Advanced Networking Examples](#advanced-networking-examples)

## Introduction to Docker Networking

Docker networking enables communication between containers, the host system, and external networks. It allows containers to be connected to networks, providing isolation and facilitating communication between applications.

### Why Docker Networking?

- **Isolation**: Separate application environments
- **Communication**: Enable containers to talk to each other
- **Portability**: Consistent network behavior across environments
- **Security**: Network segmentation and access control
- **Scalability**: Support for distributed applications

## Docker Network Drivers

Docker provides various network drivers to accommodate different use cases:

| Driver | Description | Scope | Use Case |
|--------|-------------|-------|----------|
| bridge | Default network driver, creates a private network for containers | Local | Standalone containers on a single host |
| host | Removes network isolation, uses host's networking directly | Local | High performance on a single host, when network isolation isn't needed |
| overlay | Connect multiple Docker daemons across hosts | Swarm | Multi-host applications in Docker Swarm |
| macvlan | Assign a MAC address to a container, making it appear as a physical device | Local | Applications that expect to be directly connected to the physical network |
| none | Disables all networking | Local | Containers that don't need network access |
| network plugins | Custom network implementations | Varies | Specialized network requirements |

## Basic Networking Commands

### Listing Networks

```bash
# List all networks
docker network ls
```

### Creating Networks

```bash
# Create a bridge network
docker network create my-bridge-network

# Create a network with specific subnet and gateway
docker network create --subnet=172.18.0.0/16 --gateway=172.18.0.1 my-custom-network

# Create an overlay network for Swarm
docker network create --driver overlay my-overlay-network
```

### Inspecting Networks

```bash
# Get detailed information about a network
docker network inspect my-bridge-network
```

### Removing Networks

```bash
# Remove a network
docker network rm my-bridge-network

# Remove all unused networks
docker network prune
```

### Connecting/Disconnecting Containers

```bash
# Connect a running container to a network
docker network connect my-bridge-network my-container

# Disconnect a container from a network
docker network disconnect my-bridge-network my-container
```

## Default Bridge Network

All Docker installations come with a default bridge network named `bridge`. When you run a container without specifying a network, it automatically connects to this default bridge network.

### Demo: Exploring the Default Bridge Network

```bash
# Check existing networks
docker network ls

# Inspect the default bridge network
docker network inspect bridge

# Run a Busybox container on the default bridge
docker run -it --rm --name busybox1 busybox sh

# In the container, check the network configuration
ip addr show
ip route
cat /etc/resolv.conf
ping 8.8.8.8
exit

# Run another Busybox container
docker run -it --rm --name busybox2 busybox sh

# In the second container, try to ping the first one by name
ping busybox1  # This will fail because DNS resolution doesn't work in the default bridge network
# Try to ping by IP instead (get the IP from docker inspect)
ping [IP_OF_BUSYBOX1]  # This should work
exit
```

## User-defined Bridge Networks

User-defined bridge networks are superior to the default bridge network, as they provide:

- Automatic DNS resolution between containers
- Better isolation
- Containers can be connected/disconnected on the fly
- Each user-defined network creates a configurable bridge

### Demo: Creating and Using a User-defined Bridge Network

```bash
# Create a user-defined bridge network
docker network create my-network

# Run two containers on the new network
docker run -itd --name ubuntu1 --network my-network ubuntu bash
docker run -it --name busybox1 --network my-network busybox sh

# From busybox1, ping ubuntu1 by name
ping ubuntu1  # This should work, demonstrating automatic DNS resolution

# Exit the container
exit

# Connect an existing container to the network
docker run -itd --name ubuntu2 ubuntu bash
docker network connect my-network ubuntu2

# Now ubuntu2 is on both the default bridge and my-network
docker run -it --name busybox2 --network my-network busybox sh

# From busybox2, ping both ubuntu containers
ping ubuntu1
ping ubuntu2

# Exit the container
exit
```

## Host Network

When using the host network mode, a container shares the networking namespace with the host. The container doesn't get its own IP-address allocated.

### Demo: Using Host Network Mode

```bash
# Start a Nginx container using host networking
docker run -d --name nginx-host --network host nginx

# The container is now using the host's network stack
# Access nginx via localhost on the host system
curl localhost:80

# Check the listening ports on the host
netstat -tulpn | grep nginx

# Stop and remove the container
docker stop nginx-host
docker rm nginx-host
```

## Overlay Networks

Overlay networks enable communication between containers running on different Docker hosts, which is essential for Docker Swarm services.

### Demo: Creating and Using an Overlay Network

```bash
# On the manager node, create an overlay network
docker network create --driver overlay my-overlay-network

# Create a service using this network
docker service create --name my-nginx --network my-overlay-network --replicas 2 nginx

# Check the service
docker service ls
docker service ps my-nginx

# On any node, inspect the network
docker network inspect my-overlay-network
```

## Macvlan Networks

Macvlan networks allow you to assign a MAC address to a container, making it appear as a physical device on your network.

### Demo: Setting Up a Macvlan Network

```bash
# Identify the parent interface on your host
ip addr

# Create a macvlan network
docker network create -d macvlan \
  --subnet=192.168.1.0/24 \
  --gateway=192.168.1.1 \
  -o parent=eth0 my-macvlan-network

# Run a container on the macvlan network
docker run -itd --name macvlan-ubuntu --network my-macvlan-network ubuntu bash

# Inspect the container to see its IP
docker inspect macvlan-ubuntu | grep IPAddress
```

## None Network

The `none` network driver provides a container with its own network stack and namespace but does not configure interfaces inside it. It's useful for containers that don't need network access.

### Demo: Using None Network

```bash
# Run a container with no networking
docker run -it --network none busybox sh

# Check network interfaces
ip addr  # Should only show loopback interface

# Verify no default route exists
ip route

# Try to ping an external address
ping 8.8.8.8  # This will fail

# Exit the container
exit
```

## Network Aliases and DNS

Docker provides built-in DNS for container name resolution. Network aliases allow a container to be discoverable using additional names.

### Demo: Working with Network Aliases

```bash
# Create a network
docker network create app-network

# Run containers with network aliases
docker run -itd --name db --network app-network --network-alias database postgres
docker run -it --name client --network app-network busybox sh

# From the client container, ping both the container name and its alias
ping db
ping database

# Both should work due to Docker's embedded DNS server
exit
```

## Exposing and Publishing Ports

### Exposing Ports (Documentation Only)

The `EXPOSE` instruction in a Dockerfile informs Docker that the container listens on specific network ports at runtime.

```dockerfile
# Example Dockerfile fragment
EXPOSE 80/tcp
EXPOSE 80/udp
```

Exposing ports is only documentation and doesn't actually publish the port.

### Publishing Ports

Publishing ports maps a container's ports to the host.

```bash
# Publish a port
docker run -d --name web -p 8080:80 nginx  # Maps port 80 in the container to 8080 on the host

# Publish to a specific interface
docker run -d --name web-localhost -p 127.0.0.1:8081:80 nginx  # Only accessible from localhost

# Publish to a random port
docker run -d --name web-random -P nginx  # -P publishes all exposed ports to random host ports

# Check the port mappings
docker port web
docker port web-random
```

### Demo: Accessing Published Ports

```bash
# Run an nginx container with a published port
docker run -d --name nginx-demo -p 8080:80 nginx

# Access the web server from the host
curl localhost:8080

# Get information about published ports
docker port nginx-demo
```

## Container Network Model (CNM)

The Container Network Model (CNM) is Docker's approach to providing networking for containers with these key components:

- **Sandbox**: Contains the network configuration of a container (interfaces, routes, DNS, etc.)
- **Endpoint**: Connects a sandbox to a network (like a virtual NIC)
- **Network**: Collection of endpoints with connectivity between them

## Network Troubleshooting

### Common Issues and Diagnosis

```bash
# Check container's network settings
docker inspect --format='{{json .NetworkSettings.Networks}}' container_name | jq

# Check if the container can reach the internet
docker exec -it container_name ping 8.8.8.8

# Check DNS resolution
docker exec -it container_name nslookup google.com

# Check container's routing table
docker exec -it container_name route -n

# Check iptables rules (on host)
sudo iptables -t nat -L -n

# For overlay networks, check the overlay network driver
docker network inspect my-overlay-network
```

### Specific Troubleshooting Demo

```bash
# Create a test environment
docker network create troubleshoot-net
docker run -itd --name troubled-ubuntu --network troubleshoot-net ubuntu

# Install networking tools in the container
docker exec -it troubled-ubuntu apt-get update
docker exec -it troubled-ubuntu apt-get install -y iputils-ping net-tools dnsutils

# Check basic connectivity
docker exec -it troubled-ubuntu ping 8.8.8.8

# Check DNS resolution
docker exec -it troubled-ubuntu nslookup google.com

# Check routing table
docker exec -it troubled-ubuntu route -n

# Check open ports inside container
docker exec -it troubled-ubuntu netstat -tulpn
```

## Advanced Networking Examples

### Demo 1: Inter-container Communication with Busybox and Ubuntu

```bash
# Create a custom network
docker network create demo-net

# Start an Ubuntu container as a server
docker run -d --name ubuntu-server --network demo-net ubuntu sleep infinity

# Install and start a web server in the Ubuntu container
docker exec -it ubuntu-server bash -c "apt-get update && apt-get install -y nginx && service nginx start"

# Get the IP address of the Ubuntu container
UBUNTU_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' ubuntu-server)

# Start a Busybox container to communicate with the Ubuntu server
docker run -it --name busybox-client --network demo-net busybox sh

# Inside the Busybox container
wget -O- ubuntu-server
ping ubuntu-server
# Exit the container
exit

# Clean up
docker stop ubuntu-server busybox-client
docker rm ubuntu-server busybox-client
docker network rm demo-net
```

### Demo 2: Multi-network Setup with Isolated Containers

```bash
# Create two isolated networks
docker network create frontend-net
docker network create backend-net

# Start a web server in the frontend network
docker run -d --name web-server --network frontend-net -p 8080:80 nginx

# Start a database in the backend network
docker run -d --name db-server --network backend-net -e POSTGRES_PASSWORD=password postgres

# Start an application server connected to both networks
docker run -d --name app-server --network frontend-net ubuntu sleep infinity
docker network connect backend-net app-server

# Verify connectivity from the app server
docker exec -it app-server apt-get update
docker exec -it app-server apt-get install -y curl postgresql-client

# Test connectivity to web server
docker exec -it app-server curl web-server

# Test connectivity to database
docker exec -it app-server bash -c "PGPASSWORD=password psql -h db-server -U postgres -c 'SELECT 1'"

# Verify the web server cannot directly access the database
docker network connect frontend-net busybox-tester
docker exec -it busybox-tester ping db-server  # This should fail

# Clean up
docker stop web-server db-server app-server
docker rm web-server db-server app-server
docker network rm frontend-net backend-net
```

### Demo 3: Network Policies with Custom MTU and Subnet

```bash
# Create a custom network with specific settings
docker network create --driver bridge \
  --opt com.docker.network.driver.mtu=1400 \
  --subnet=172.20.0.0/16 \
  --gateway=172.20.0.1 \
  custom-config-net

# Inspect the network
docker network inspect custom-config-net

# Run containers on this network
docker run -it --name custom-busybox --network custom-config-net busybox sh

# Inside the container, check MTU and network config
ip addr
exit

# Clean up
docker rm custom-busybox
docker network rm custom-config-net
```

### Demo 4: Service Discovery and Load Balancing

This demo shows how Docker's embedded DNS can be used for simple service discovery.

```bash
# Create a network
docker network create service-net

# Run multiple instances of the same service
docker run -d --name service1 --network service-net --network-alias myservice busybox sleep infinity
docker run -d --name service2 --network service-net --network-alias myservice busybox sleep infinity
docker run -d --name service3 --network service-net --network-alias myservice busybox sleep infinity

# Run a client that resolves the service name multiple times
docker run -it --name client --network service-net busybox sh

# Inside the client, resolve the service name multiple times
for i in $(seq 1 10); do nslookup myservice; done
# You should see different IPs being returned, demonstrating round-robin DNS

# Exit the container
exit

# Clean up
docker stop service1 service2 service3 client
docker rm service1 service2 service3 client
docker network rm service-net
```

---

This tutorial covers both basic and advanced Docker networking concepts with practical examples using Busybox and Ubuntu containers. By following these demonstrations, you'll gain a solid understanding of how Docker networking works and how to configure it for various use cases.