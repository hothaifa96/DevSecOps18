# AWS Infrastructure Monitoring


boto3: https://medium.com/featurepreneur/boto3-aws-sdk-for-python-e7391b9901c5 

## Project Overview

A  Flask-based monitoring solution that provides real-time insights into AWS infrastructure components. This application enables DevOps teams to monitor critical AWS services through an intuitive dashboard and detailed API endpoints.

## Key Features

- **Real-time Monitoring**: Get up-to-date status of AWS resources
- **Multi-service Support**: Monitor ECS, S3, EBS, and network configurations in one place
- **Secure Authentication**: AWS credentials management with session-based access

## Supported AWS Services

### Amazon ECS
- Cluster health and status
- Service deployment status
- Task counts and distribution
- Container instance monitoring

### Amazon S3
- Bucket inventory and properties
- Storage utilization and classification
- Lifecycle rule management
- Encryption status and security posture

### Amazon EBS
- Volume status and utilization
- Performance metrics (IOPS, throughput)
- Attachment status
- Encryption compliance

### Network Configuration
- VPC status and configuration
- Security group rule analysis
- Potential security vulnerabilities
- Network topology insights

## API Reference

### Authentication

```
POST /api/v1/auth/login
```

**Request Body:**
```json
{
  "aws_access_key_id": "",
  "aws_secret_access_key": "",
  "aws_region": "us-west-2"
}
```

**Response:**
```json
{
  "expires_at": "2025-03-06T14:30:00Z"
}
```

### ECS Monitoring

#### List Clusters

```
GET /api/v1/ecs/clusters
```

**Response:**
```json
{
  "clusters": [
    {
      "cluster_name": "production-api",
      "cluster_arn": "arn:aws:ecs:us-west-2:123456789012:cluster/production-api",
      "status": "ACTIVE",
      "registered_container_instances_count": 10,
      "running_tasks_count": 45,
      "pending_tasks_count": 2
    }
  ]
}
```

#### List Services

```
GET /api/v1/ecs/clusters/{cluster_name}/services
```

**Response:**
```json
{
  "services": [
    {
      "service_name": "web-frontend",
      "service_arn": "arn:aws:ecs:us-west-2:123456789012:service/production-api/web-frontend",
      "status": "ACTIVE",
      "desired_count": 5,
      "running_count": 5,
      "pending_count": 0,
      "deployment_status": "PRIMARY"
    }
  ]
}
```

### S3 Monitoring

#### List Buckets

```
GET /api/v1/s3/buckets
```

**Response:**
```json
{
  "buckets": [
    {
      "name": "company-assets",
      "creation_date": "2023-01-15T10:30:00Z",
      "region": "us-west-2",
      "object_count": 15420,
      "total_size_bytes": 1073741824,
      "versioning_enabled": true,
      "public_access_blocked": true
    }
  ]
}
```

#### Get Bucket Details

```
GET /api/v1/s3/buckets/{bucket_name}/details
```

**Response:**
```json
{
  "name": "company-assets",
  "creation_date": "2023-01-15T10:30:00Z",
  "region": "us-west-2",
  "storage_class_summary": {
    "STANDARD": 1073741824,
    "STANDARD_IA": 536870912,
    "GLACIER": 268435456
  },
  "lifecycle_rules": [
    {
      "id": "archive-old-logs",
      "status": "Enabled",
      "transitions": [
        {
          "days": 30,
          "storage_class": "STANDARD_IA"
        },
        {
          "days": 90,
          "storage_class": "GLACIER"
        }
      ]
    }
  ],
  "encryption": {
    "enabled": true,
    "type": "AES256"
  }
}
```

### EBS Monitoring

#### List Volumes

```
GET /api/v1/ebs/volumes
```

**Response:**
```json
{
  "volumes": [
    {
      "volume_id": "vol-0a1b2c3d4e5f6g7h8",
      "size": 100,
      "volume_type": "gp3",
      "state": "in-use",
      "iops": 3000,
      "throughput": 125,
      "attached_instance": "i-0a1b2c3d4e5f6g7h8",
      "device": "/dev/sda1",
      "availability_zone": "us-west-2a",
      "encrypted": true
    }
  ]
}
```

#### Get Volume Metrics

```
GET /api/v1/ebs/volumes/{volume_id}/metrics
```

**Query Parameters:**
- `period`: The granularity of the metrics in seconds (default: 3600)
- `start_time`: Start time for metrics (default: 24 hours ago)
- `end_time`: End time for metrics (default: now)

**Response:**
```json
{
  "volume_id": "vol-0a1b2c3d4e5f6g7h8",
  "metrics": {
    "read_ops": [
      {"timestamp": "2025-03-05T12:00:00Z", "value": 1245.6},
      {"timestamp": "2025-03-05T13:00:00Z", "value": 1356.2}
    ],
    "write_ops": [
      {"timestamp": "2025-03-05T12:00:00Z", "value": 2341.8},
      {"timestamp": "2025-03-05T13:00:00Z", "value": 2567.3}
    ],
    "read_bytes": [
      {"timestamp": "2025-03-05T12:00:00Z", "value": 45678912},
      {"timestamp": "2025-03-05T13:00:00Z", "value": 51234567}
    ],
    "write_bytes": [
      {"timestamp": "2025-03-05T12:00:00Z", "value": 78912345},
      {"timestamp": "2025-03-05T13:00:00Z", "value": 85678912}
    ],
    "queue_length": [
      {"timestamp": "2025-03-05T12:00:00Z", "value": 0.25},
      {"timestamp": "2025-03-05T13:00:00Z", "value": 0.31}
    ]
  }
}
```

### Network Monitoring

#### List VPCs

```
GET /api/v1/network/vpcs
```

**Response:**
```json
{
  "vpcs": [
    {
      "vpc_id": "vpc-0a1b2c3d4e5f6g7h8",
      "cidr_block": "10.0.0.0/16",
      "state": "available",
      "is_default": false,
      "dhcp_options_id": "dopt-0a1b2c3d4e5f6g7h8",
      "instance_tenancy": "default",
      "subnet_count": 6,
      "security_group_count": 12
    }
  ]
}
```

#### List Security Groups

```
GET /api/v1/network/vpcs/{vpc_id}/security-groups
```

**Response:**
```json
{
  "security_groups": [
    {
      "group_id": "sg-0a1b2c3d4e5f6g7h8",
      "group_name": "web-servers",
      "description": "Security group for web servers",
      "inbound_rules": [
        {
          "protocol": "tcp",
          "port_range": "80-80",
          "source": "0.0.0.0/0",
          "description": "HTTP from anywhere"
        },
        {
          "protocol": "tcp",
          "port_range": "443-443",
          "source": "0.0.0.0/0",
          "description": "HTTPS from anywhere"
        }
      ],
      "outbound_rules": [
        {
          "protocol": "-1",
          "port_range": "0-65535",
          "destination": "0.0.0.0/0",
          "description": "All traffic to anywhere"
        }
      ]
    }
  ]
}
```

### Dashboard

```
GET /api/v1/dashboard/summary
```

**Response:**
```json
{
  "summary": {
    "ecs": {
      "total_clusters": 3,
      "total_services": 12,
      "total_tasks": 45,
      "unhealthy_services": 1
    },
    "s3": {
      "total_buckets": 8,
      "total_storage_gb": 1250,
      "buckets_without_encryption": 1,
      "publicly_accessible_buckets": 0
    },
    "ebs": {
      "total_volumes": 25,
      "total_storage_gb": 4500,
      "unattached_volumes": 2,
      "unencrypted_volumes": 3
    },
    "network": {
      "total_vpcs": 4,
      "total_subnets": 24,
      "security_groups_with_open_ssh": 2,
      "route_tables": 12
    }
  }
}
```

## Technical Architecture

### Application Structure

```
/app
  /api
    /v1
      /auth
      /ecs
      /s3
      /ebs
      /network
      /dashboard
  /models
  /services
  /utils
  /config
/tests
```

### Technology Stack

- **Framework**: Flask, Flask-RESTful
- **AWS SDK**: Boto3
- **Authentication**: Session-based with token expiration
- **Testing**: Pytest for unit and integration tests

## Security Considerations

- AWS credentials are never stored on disk
- All API endpoints require authentication
- Token-based sessions with expiration
- HTTPS required for all communications
- Security insights help identify misconfigurations


# **Select 1 resource and implement the busniess logic**
## **upload the code to a git repo nammed AWS-infra-api**
### **Along with the repo send the full name of you to the mail :**
### **h.dso.biu@gmail.com**
