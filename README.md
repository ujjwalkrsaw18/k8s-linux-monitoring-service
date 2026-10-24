# Cloud-Native Linux System Monitoring Microservice

A Python (FastAPI) microservice exposing real-time Linux host metrics (`/health`, `/system-info`, `/metrics`), containerized with Docker, monitored via Prometheus & Grafana, and orchestrated on Kubernetes with Horizontal Pod Autoscaling (HPA).

## Tech Stack
- **Backend:** Python 3.11, FastAPI, Uvicorn, Psutil
- **Containerization:** Docker, Docker Compose
- **Monitoring:** Prometheus, Grafana
- **Orchestration:** Kubernetes (Deployments, Service, ConfigMaps, Secrets, HPA)
- **OS:** Linux (Ubuntu)

## API Endpoints
- `GET /health` - Service health check
- `GET /system-info` - Real-time Linux CPU, Memory, Disk metrics
- `GET /metrics` - Prometheus metrics endpoint
