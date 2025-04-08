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
use this command to install python packages ```bash pip install --no-cache-dir -r requirements.txt```
use this command to install python packages ```bash python3 <file-name>.py```
the app runs in port 5000

## Creating the Frontend Dockerfile

use this command to install python packages ```bash  npm i ```
use this command to install python packages ```bash npm start```
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
