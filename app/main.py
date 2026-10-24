import os, platform, psutil
from fastapi import FastAPI, Response
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI()
CPU = Gauge('system_cpu_usage_percent', 'CPU percent')
MEM = Gauge('system_memory_usage_percent', 'Memory percent')
DISK = Gauge('system_disk_usage_percent', 'Disk percent')

@app.get("/health")
def health():
    return {"status": "healthy", "env": os.getenv("APP_ENV", "local")}

@app.get("/system-info")
def info():
    return {
        "os": platform.system(),
        "cpu_cores": psutil.cpu_count(),
        "cpu_percent": psutil.cpu_percent(interval=0.2),
        "mem_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent
    }

@app.get("/metrics")
def metrics():
    CPU.set(psutil.cpu_percent())
    MEM.set(psutil.virtual_memory().percent)
    DISK.set(psutil.disk_usage('/').percent)
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)
