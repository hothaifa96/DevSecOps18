# Introduction to Docker

Docker is a powerful platform that allows you to build, share, and run applications in containers. Containers are lightweight, isolated environments that package everything an application needs to run, including code, runtime, system tools, libraries, and settings.

## Why Docker is Important

Docker solves the "it works on my machine" problem by ensuring consistency across different environments. Here's why Docker has become essential in modern software development:

1. **Consistency**: Applications run the same way regardless of where Docker is installed
2. **Isolation**: Applications and their dependencies run in isolated containers
3. **Portability**: Containers can run on any system that has Docker installed
4. **Efficiency**: Containers share the host OS kernel, making them more lightweight than virtual machines
5. **Scalability**: Easy to scale applications horizontally by running multiple container instances

## Docker Architecture

Docker uses a client-server architecture:
- **Docker Client**: Command-line interface you use to interact with Docker
- **Docker Daemon (Server)**: Background service that manages Docker objects
- **Docker Registry**: Storage for Docker images (like Docker Hub)

![Docker Architecture](https://docs.docker.com/engine/images/architecture.svg)

## Key Docker Concepts

### Images
Docker images are read-only templates used to create containers. Think of them as blueprints or snapshots.

### Containers
Containers are runnable instances of images. They can be started, stopped, moved, and deleted.

### Dockerfile
A text file containing instructions to build a Docker image automatically.

## Basic Commands Recap

Here's a quick refresher of the basic commands you've already learned:

| Command | Description |
|---------|-------------|
| `docker pull <image>` | Download an image from a registry |
| `docker start <container>` | Start a stopped container |
| `docker run <image>` | Create and start a new container |
| `docker ps` | List running containers |
| `docker images` | List available images |

## Beyond Basic Commands

### Container Management
```bash
# Run a container in detached mode (background)
docker run -d <image>

# Stop a running container
docker stop <container>

# Remove a container
docker rm <container>

# Remove an image
docker rmi <image>

# View container logs
docker logs <container>

# Execute a command in a running container
docker exec -it <container> <command>
```

### Container Lifecycle
```
Created → Running → Paused → Stopped → Removed
```

### Data Management



## Docker Best Practices

1. **Use official images** as base whenever possible
2. **Keep images small** by removing unnecessary files
3. **Use multi-stage builds** to reduce final image size
4. **Don't run containers as root** for better security
5. **Use environment variables** for configuration
6. **Label your images** with metadata
7. **Use .dockerignore** files to exclude unnecessary files


## Resources for Further Learning

- [Docker Documentation](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/) - Repository of Docker images
- [Play with Docker](https://labs.play-with-docker.com/) - Free online Docker playground
- [Docker GitHub Repository](https://github.com/docker)
- [Docker Curriculum](https://docker-curriculum.com/) - Comprehensive tutorial

## Common Docker Commands Cheat Sheet

| Command | Description |
|---------|-------------|
| `docker pull <image>` | Download an image |
| `docker build -t <name> .` | Build an image from a Dockerfile |
| `docker run <image>` | Run a container |
| `docker run -d <image>` | Run a container in the background |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers |
| `docker images` | List images |
| `docker stop <container>` | Stop a container |
| `docker rm <container>` | Remove a container |
| `docker rmi <image>` | Remove an image |