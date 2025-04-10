# Network Bandwidth Logger (NetBL) Docker Exercise

In this exercise, you will build Docker containers for a full-stack network bandwidth monitoring application. The application consists of two main components:

1. A Flask backend API
2. A React frontend application

Both components will connect to a PostgreSQL database which we'll run as a separate container.

## Exercise Overview

You will:

1. Create Dockerfiles for the backend and frontend
2. Build the Docker images
3. Run containers individually with the correct configurations
4. Test the complete application

## Creating the Backend Dockerfile

use this command to install python packages `bash pip install --no-cache-dir -r requirements.txt`
use this command to install python packages `bash python3 <file-name>.py`
the app runs in port 5000

## Creating the Frontend Dockerfile

use this command to install python packages `bash  npm i `
use this command to install python packages `bash npm start`
the app runs in port 3000

## Building the Containers

## Create a Docker Network

First, create a network so the containers can communicate:

##Run the PostgreSQL Container

```bash
  postgres_data:/var/lib/postgresql/data
  POSTGRES_PASSWORD=netbl_password
  POSTGRES_USER=netbl_user
  POSTGRES_DB=netbl_db
  <image name for example : postgres:15-alpine>
```

### Step 3: Build and Run the Backend Container

```bash
# Run the container
use those env
  -e DB_HOST=postgres \
  -e DB_USER=netbl_user \
  -e DB_PASSWORD=netbl_password \
  -e DB_NAME=netbl_db \
```

for the frontend

```bash
  -e REACT_APP_API_URL=http://localhost:<port>/api
```

### solution

```bash
docker volume create postgres_data
```

```bash
docker network create nbl
```

```bash
docker run --name postgres -v postgres_data:/var/lib/postgresql/data -e POSTGRES_PASSWORD=123456 -e POSTGRES_USER=mama -e POSTGRES_DB=netbl_db -d --network nbl postgres:14.17-bookworm
```

```bash
docker run --name backend1 -P -e DB_PASSWORD=123456 -e DB_HOST=postgres -e DB_USER=mama -d  nbl-server
```

```bash
docker run --name nbl-frontend -d -p 3000:3000 -e REACT_APP_API_URL=http://localhost:32773/api nbl-frontend
```
