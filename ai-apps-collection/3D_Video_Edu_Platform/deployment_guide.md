# 🚀 Deployment Guide - 3D Video Educational AI Platform

This guide will help you deploy your 3D Video Educational AI Platform to production.

## 📋 Prerequisites

### System Requirements
- **CPU**: 8+ cores recommended for Blender rendering
- **RAM**: 16GB+ recommended (32GB+ for 4K rendering)
- **GPU**: NVIDIA RTX 3060+ or equivalent for GPU rendering
- **Storage**: 100GB+ free space for video output
- **OS**: Linux (Ubuntu 20.04+), macOS, or Windows 10+

### Software Requirements
- Python 3.8+
- Blender 3.0+
- FFmpeg (for video processing)
- Docker (optional, for containerized deployment)

## 🐳 Docker Deployment (Recommended)

### 1. Create Dockerfile

```dockerfile
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    blender \
    ffmpeg \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create output directory
RUN mkdir -p /app/output

# Expose port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run the application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### 2. Create docker-compose.yml

```yaml
version: '3.8'

services:
  video-edu-platform:
    build: .
    ports:
      - "8501:8501"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - GOOGLE_API_KEY=${GOOGLE_API_KEY}
    volumes:
      - ./output:/app/output
      - ./logs:/app/logs
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8501/_stcore/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - video-edu-platform
    restart: unless-stopped
```

### 3. Deploy with Docker

```bash
# Build and start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

## ☁️ Cloud Deployment

### AWS Deployment

#### 1. EC2 Instance Setup

```bash
# Launch EC2 instance (t3.xlarge or larger)
# Install Docker
sudo yum update -y
sudo yum install -y docker
sudo systemctl start docker
sudo systemctl enable docker

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Clone and deploy
git clone <your-repo>
cd 3D_Video_Edu_Platform
docker-compose up -d
```

#### 2. ECS Deployment

```yaml
# task-definition.json
{
  "family": "video-edu-platform",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "2048",
  "memory": "4096",
  "executionRoleArn": "arn:aws:iam::account:role/ecsTaskExecutionRole",
  "containerDefinitions": [
    {
      "name": "video-edu-platform",
      "image": "your-account.dkr.ecr.region.amazonaws.com/video-edu-platform:latest",
      "portMappings": [
        {
          "containerPort": 8501,
          "protocol": "tcp"
        }
      ],
      "environment": [
        {
          "name": "OPENAI_API_KEY",
          "value": "your-openai-key"
        },
        {
          "name": "GOOGLE_API_KEY",
          "value": "your-google-key"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/video-edu-platform",
          "awslogs-region": "us-east-1",
          "awslogs-stream-prefix": "ecs"
        }
      }
    }
  ]
}
```

### Google Cloud Platform

#### 1. Cloud Run Deployment

```yaml
# cloudbuild.yaml
steps:
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/$PROJECT_ID/video-edu-platform', '.']
  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'gcr.io/$PROJECT_ID/video-edu-platform']
  - name: 'gcr.io/cloud-builders/gcloud'
    args: [
      'run', 'deploy', 'video-edu-platform',
      '--image', 'gcr.io/$PROJECT_ID/video-edu-platform',
      '--platform', 'managed',
      '--region', 'us-central1',
      '--allow-unauthenticated',
      '--memory', '4Gi',
      '--cpu', '2',
      '--timeout', '3600'
    ]
```

#### 2. Deploy to Cloud Run

```bash
# Build and deploy
gcloud builds submit --config cloudbuild.yaml

# Set environment variables
gcloud run services update video-edu-platform \
  --set-env-vars="OPENAI_API_KEY=your-key,GOOGLE_API_KEY=your-key"
```

### Azure Deployment

#### 1. Container Instances

```yaml
# azure-deploy.yaml
apiVersion: 2018-10-01
location: eastus
name: video-edu-platform
properties:
  containers:
  - name: video-edu-platform
    properties:
      image: your-registry.azurecr.io/video-edu-platform:latest
      resources:
        requests:
          cpu: 2
          memoryInGb: 4
      ports:
      - port: 8501
      environmentVariables:
      - name: OPENAI_API_KEY
        value: your-openai-key
      - name: GOOGLE_API_KEY
        value: your-google-key
  osType: Linux
  ipAddress:
    type: Public
    ports:
    - protocol: tcp
      port: 8501
  restartPolicy: Always
```

## 🔧 Production Configuration

### 1. Environment Variables

```bash
# .env.production
OPENAI_API_KEY=your-openai-api-key
GOOGLE_API_KEY=your-google-api-key
BLENDER_PATH=/usr/bin/blender
FFMPEG_PATH=/usr/bin/ffmpeg
OUTPUT_DIR=/app/output
LOG_LEVEL=INFO
MAX_CONCURRENT_VIDEOS=3
VIDEO_QUALITY=1080p
DEFAULT_LANGUAGE=en
```

### 2. Nginx Configuration

```nginx
# nginx.conf
events {
    worker_connections 1024;
}

http {
    upstream video_edu_platform {
        server video-edu-platform:8501;
    }

    server {
        listen 80;
        server_name your-domain.com;

        location / {
            proxy_pass http://video_edu_platform;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_read_timeout 86400;
        }

        # Handle large file uploads
        client_max_body_size 100M;
    }
}
```

### 3. SSL Configuration

```bash
# Install Certbot
sudo apt-get install certbot python3-certbot-nginx

# Get SSL certificate
sudo certbot --nginx -d your-domain.com

# Auto-renewal
sudo crontab -e
# Add: 0 12 * * * /usr/bin/certbot renew --quiet
```

## 📊 Monitoring and Logging

### 1. Application Monitoring

```python
# monitoring.py
import logging
from prometheus_client import Counter, Histogram, start_http_server
import time

# Metrics
VIDEO_GENERATION_COUNTER = Counter('video_generation_total', 'Total videos generated')
VIDEO_GENERATION_DURATION = Histogram('video_generation_duration_seconds', 'Video generation duration')

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler()
    ]
)

def monitor_video_generation(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            VIDEO_GENERATION_COUNTER.inc()
            return result
        finally:
            duration = time.time() - start_time
            VIDEO_GENERATION_DURATION.observe(duration)
    return wrapper
```

### 2. Health Checks

```python
# health_check.py
from flask import Flask, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/health')
def health_check():
    checks = {
        'blender': check_blender(),
        'ffmpeg': check_ffmpeg(),
        'disk_space': check_disk_space(),
        'api_keys': check_api_keys()
    }
    
    all_healthy = all(checks.values())
    status = 'healthy' if all_healthy else 'unhealthy'
    
    return jsonify({
        'status': status,
        'checks': checks
    }), 200 if all_healthy else 503

def check_blender():
    try:
        result = subprocess.run(['blender', '--version'], 
                              capture_output=True, text=True, timeout=10)
        return result.returncode == 0
    except:
        return False

def check_ffmpeg():
    try:
        result = subprocess.run(['ffmpeg', '-version'], 
                              capture_output=True, text=True, timeout=10)
        return result.returncode == 0
    except:
        return False

def check_disk_space():
    statvfs = os.statvfs('/app/output')
    free_space = statvfs.f_frsize * statvfs.f_bavail
    return free_space > 1024 * 1024 * 1024  # 1GB minimum

def check_api_keys():
    return bool(os.getenv('OPENAI_API_KEY') and os.getenv('GOOGLE_API_KEY'))
```

## 🔒 Security Configuration

### 1. API Rate Limiting

```python
# rate_limiting.py
from functools import wraps
import time
from collections import defaultdict

# Simple in-memory rate limiter
rate_limits = defaultdict(list)

def rate_limit(calls_per_minute=10):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            user_id = kwargs.get('user_id', 'anonymous')
            
            # Clean old calls
            rate_limits[user_id] = [
                call_time for call_time in rate_limits[user_id]
                if now - call_time < 60
            ]
            
            # Check rate limit
            if len(rate_limits[user_id]) >= calls_per_minute:
                raise Exception("Rate limit exceeded")
            
            # Record this call
            rate_limits[user_id].append(now)
            
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

### 2. Input Validation

```python
# validation.py
import re
from typing import Dict, Any

def validate_topic_input(data: Dict[str, Any]) -> Dict[str, Any]:
    """Validate and sanitize topic input"""
    
    # Topic validation
    if not data.get('topic') or len(data['topic']) > 500:
        raise ValueError("Invalid topic")
    
    # Subject validation
    valid_subjects = ['Physics', 'Chemistry', 'Biology', 'Mathematics', 'History']
    if data.get('subject') not in valid_subjects:
        raise ValueError("Invalid subject")
    
    # Level validation
    valid_levels = ['Elementary', 'Middle School', 'High School', 'College', 'Professional']
    if data.get('level') not in valid_levels:
        raise ValueError("Invalid level")
    
    # Sanitize topic
    data['topic'] = re.sub(r'[<>"\']', '', data['topic'])
    
    return data
```

## 📈 Scaling Considerations

### 1. Horizontal Scaling

```yaml
# kubernetes-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: video-edu-platform
spec:
  replicas: 3
  selector:
    matchLabels:
      app: video-edu-platform
  template:
    metadata:
      labels:
        app: video-edu-platform
    spec:
      containers:
      - name: video-edu-platform
        image: your-registry/video-edu-platform:latest
        ports:
        - containerPort: 8501
        resources:
          requests:
            memory: "2Gi"
            cpu: "1000m"
          limits:
            memory: "4Gi"
            cpu: "2000m"
        env:
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: api-secrets
              key: openai-key
---
apiVersion: v1
kind: Service
metadata:
  name: video-edu-platform-service
spec:
  selector:
    app: video-edu-platform
  ports:
  - port: 80
    targetPort: 8501
  type: LoadBalancer
```

### 2. Queue System for Video Processing

```python
# queue_system.py
import redis
from rq import Queue, Worker
import time

# Redis connection
redis_conn = redis.Redis(host='localhost', port=6379, db=0)
video_queue = Queue('video_generation', connection=redis_conn)

def process_video_async(topic, subject, level, user_id):
    """Add video generation job to queue"""
    job = video_queue.enqueue(
        'video_processor.generate_video',
        topic, subject, level, user_id,
        timeout='1h'
    )
    return job.id

def get_job_status(job_id):
    """Get job status"""
    job = video_queue.fetch_job(job_id)
    if job:
        return {
            'status': job.get_status(),
            'result': job.result,
            'progress': job.meta.get('progress', 0)
        }
    return None
```

## 🚀 Launch Checklist

- [ ] **Infrastructure**
  - [ ] Server/cloud instance provisioned
  - [ ] Domain name configured
  - [ ] SSL certificate installed
  - [ ] CDN configured (optional)

- [ ] **Application**
  - [ ] Docker image built and tested
  - [ ] Environment variables configured
  - [ ] Database initialized (if using)
  - [ ] Monitoring and logging set up

- [ ] **Security**
  - [ ] API keys secured
  - [ ] Rate limiting configured
  - [ ] Input validation enabled
  - [ ] Firewall rules configured

- [ ] **Performance**
  - [ ] Load testing completed
  - [ ] Caching configured
  - [ ] CDN optimized
  - [ ] Database optimized

- [ ] **Monitoring**
  - [ ] Health checks configured
  - [ ] Alerts set up
  - [ ] Log aggregation configured
  - [ ] Metrics collection enabled

## 📞 Support and Maintenance

### Regular Maintenance Tasks
- Monitor disk space and clean old videos
- Update dependencies monthly
- Review and rotate API keys
- Monitor performance metrics
- Backup configuration and data

### Troubleshooting Common Issues
- **Blender not found**: Ensure Blender is in PATH
- **Out of memory**: Increase container memory limits
- **Slow rendering**: Use GPU acceleration if available
- **API errors**: Check API key validity and quotas

---

**Ready to deploy your 3D Video Educational AI Platform! 🎬✨**
