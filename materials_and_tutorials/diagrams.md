# Docker: Dockerfile, Images, and Containers Diagrams

## Overview of Docker Components

Docker consists of three primary components that work together:

1. **Dockerfile**: A text file with instructions to build an image
2. **Image**: A read-only template used to create containers
3. **Container**: A runnable instance of an image

Understanding how these components relate to each other is essential for mastering Docker.

## The Relationship Between Dockerfile, Image, and Container

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │     │                 │
│   Dockerfile    │────►│     Image       │────►│    Container    │
│                 │build│                 │run  │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                │                        ▲
                                │                        │
                                │        run             │
                                └────────────────────────┘
```

- **Dockerfile → Image**: Use `docker build` to create an image from a Dockerfile
- **Image → Container**: Use `docker run` to create and start a container from an image
- **Multiple containers** can be created from the same image

## Detailed Dockerfile Diagram

```
┌─────────────────────────────────────────────────┐
│ Dockerfile                                      │
│                                                 │
│ FROM nginx:latest                               │
│ ┌─────────────────────────────────────────────┐ │
│ │ Base Image Specification                    │ │
│ └─────────────────────────────────────────────┘ │
│                                                 │
│ WORKDIR /app                                    │
│ ┌─────────────────────────────────────────────┐ │
│ │ Set Working Directory                       │ │
│ └─────────────────────────────────────────────┘ │
│                                                 │
│ COPY . /app                                     │
│ ┌─────────────────────────────────────────────┐ │
│ │ Copy Files from Host to Image               │ │
│ └─────────────────────────────────────────────┘ │
│                                                 │
│ RUN npm install                                 │
│ ┌─────────────────────────────────────────────┐ │
│ │ Execute Commands in a New Layer             │ │
│ └─────────────────────────────────────────────┘ │
│                                                 │
│ EXPOSE 80                                       │
│ ┌─────────────────────────────────────────────┐ │
│ │ Declare Port the Container Will Listen On   │ │
│ └─────────────────────────────────────────────┘ │
│                                                 │
│ CMD ["nginx", "-g", "daemon off;"]              │
│ ┌─────────────────────────────────────────────┐ │
│ │ Default Command to Run When Container Starts│ │
│ └─────────────────────────────────────────────┘ │
│                                                 │
└─────────────────────────────────────────────────┘
```

## Docker Image Layers

Images in Docker are built in layers, with each instruction in a Dockerfile creating a new layer:

```
┌─────────────────────────────────────────────────┐
│ Docker Image                                    │
│                                                 │
│ ┌─────────────────────────────────────────────┐ │
│ │ Layer 5: CMD ["nginx", "-g", "daemon off;"] │ │
│ ├─────────────────────────────────────────────┤ │
│ │ Layer 4: EXPOSE 80                          │ │
│ ├─────────────────────────────────────────────┤ │
│ │ Layer 3: RUN npm install                    │ │
│ ├─────────────────────────────────────────────┤ │
│ │ Layer 2: COPY . /app                        │ │
│ ├─────────────────────────────────────────────┤ │
│ │ Layer 1: WORKDIR /app                       │ │
│ ├─────────────────────────────────────────────┤ │
│ │ Layer 0: FROM nginx:latest (Base Image)     │ │
│ └─────────────────────────────────────────────┘ │
│                                                 │
└─────────────────────────────────────────────────┘
```

Key points about image layers:
- Each layer is immutable (read-only)
- Layers are cached, which speeds up builds
- Only the changes between layers are stored
- Layers are shared between images that use the same instructions

## Container Structure

A running container adds a writable layer on top of the read-only image layers:

```
┌─────────────────────────────────────────────────┐
│ Container                                       │
│                                                 │
│ ┌─────────────────────────────────────────────┐ │
│ │ Thin Writable Layer (Container Layer)       │ │
│ │   - Files added/modified during runtime     │ │
│ │   - Changes isolated to this container      │ │
│ └─────────────────────────────────────────────┘ │
│                                                 │
│ ┌─────────────────────────────────────────────┐ │
│ │ Read-Only Image Layers                      │ │
│ │   - Layer 5: CMD instruction                │ │
│ │   - Layer 4: EXPOSE instruction             │ │
│ │   - Layer 3: RUN instruction                │ │
│ │   - Layer 2: COPY instruction               │ │
│ │   - Layer 1: WORKDIR instruction            │ │
│ │   - Layer 0: Base image                     │ │
│ └─────────────────────────────────────────────┘ │
│                                                 │
└─────────────────────────────────────────────────┘
```

## Multiple Containers from One Image

```
                  ┌─────────────────────┐
                  │                     │
                  │    Docker Image     │
                  │                     │
                  └──────────┬──────────┘
                             │
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│                 │ │                 │ │                 │
│  Container 1    │ │  Container 2    │ │  Container 3    │
│                 │ │                 │ │                 │
└─────────────────┘ └─────────────────┘ └─────────────────┘
```

- All containers share the same read-only image layers
- Each container has its own writable layer
- Changes in one container do not affect others
- Deleting a container does not affect the image

## Docker Build Process

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │     │                 │
│   Dockerfile    │     │  Docker Daemon  │     │  Docker Image   │
│                 │     │                 │     │                 │
└────────┬────────┘     └────────┬────────┘     └────────┬────────┘
         │                       │                       │
         │   docker build        │                       │
         ├──────────────────────►│                       │
         │                       │                       │
         │                       │  Process each         │
         │                       │  instruction          │
         │                       │  and create layers    │
         │                       ├──────────────────────►│
         │                       │                       │
         │                       │                       │
         │                       │  Cache layers         │
         │                       │  for reuse            │
         │                       │◄──────────────────────┤
         │                       │                       │
         │   Return image ID     │                       │
         │◄──────────────────────┤                       │
         │                       │                       │
         │                       │                       │
```

## Docker Run Process

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │     │                 │
│   Docker Image  │     │  Docker Daemon  │     │    Container    │
│                 │     │                 │     │                 │
└────────┬────────┘     └────────┬────────┘     └────────┬────────┘
         │                       │                       │
         │   docker run          │                       │
         ├──────────────────────►│                       │
         │                       │                       │
         │                       │  Create container     │
         │                       │  from image           │
         │                       ├──────────────────────►│
         │                       │                       │
         │                       │  Allocate resources   │
         │                       │  (filesystem,         │
         │                       │   network, etc.)      │
         │                       │                       │
         │                       │  Start container      │
         │                       │  process              │
         │                       │                       │
         │                       │  Return container ID  │
         │                       │◄──────────────────────┤
         │                       │                       │
         │                       │                       │
```

## Image Sharing and Distribution

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │     │                 │
│   Local Image   │     │  Docker Registry│     │   Remote Host   │
│                 │     │  (Docker Hub)   │     │                 │
└────────┬────────┘     └────────┬────────┘     └────────┬────────┘
         │                       │                       │
         │   docker push         │                       │
         ├──────────────────────►│                       │
         │                       │                       │
         │                       │   docker pull         │
         │                       │◄──────────────────────┤
         │                       │                       │
         │                       │                       │
         │   docker pull         │                       │
         │◄──────────────────────┤                       │
         │                       │                       │
         │                       │                       │
```

## Container State Lifecycle

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│                        Docker Container Lifecycle                │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
          │
          │ docker create
          ▼
┌────────────────┐
│                │
│    Created     │
│                │
└───────┬────────┘
        │
        │ docker start
        ▼
┌────────────────┐          ┌────────────────┐
│                │          │                │
│    Running     │──────────►    Paused      │
│                │ docker   │                │
└───────┬────────┘  pause   └───────┬────────┘
        │                           │
        │                           │ docker unpause
        │                           │
        │                           ▼
        │                  ┌────────────────┐
        │                  │                │
        │                  │    Running     │
        │                  │                │
        │                  └───────┬────────┘
        │                          │
        │ docker stop               │
        ▼                          │
┌────────────────┐                 │
│                │                 │
│    Stopped     │                 │
│                │                 │
└───────┬────────┘                 │
        │                          │
        │ docker rm                │
        ▼                          ▼
┌────────────────┐          ┌────────────────┐
│                │          │                │
│    Deleted     │◄─────────┤    Deleted     │
│                │ docker rm│                │
└────────────────┘          └────────────────┘
```

## Volume and Bind Mounts

```
┌───────────────────────────────────────────┐
│                   Host                     │
│                                           │
│  ┌───────────────┐    ┌───────────────┐   │
│  │   Host Path   │    │ Named Volume  │   │
│  │  /path/to/dir │    │     vol-1     │   │
│  └───────┬───────┘    └───────┬───────┘   │
│          │                    │           │
│          │ Bind Mount         │ Volume    │
└──────────┼────────────────────┼───────────┘
           │                    │            
┌──────────┼────────────────────┼───────────┐
│          │                    │           │
│  ┌───────▼───────┐    ┌───────▼───────┐   │
│  │ /container/dir│    │ /var/lib/data │   │
│  └───────────────┘    └───────────────┘   │
│                                           │
│                 Container                 │
└───────────────────────────────────────────┘
```


## Multiple Containers from One Image

```
                  ┌─────────────────────┐
                  │                     │
                  │    Docker Image     │
                  │                     │
                  └──────────┬──────────┘
                             │
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│                 │ │                 │ │                 │
│  Container 1    │ │  Container 2    │ │  Container 3    │
│                 │ │                 │ │                 │
└─────────────────┘ └─────────────────┘ └─────────────────┘
```

- All containers share the same read-only image layers
- Each container has its own writable layer
- Changes in one container do not affect others
- Deleting a container does not affect the image
