FROM python:3.10-slim

WORKDIR /app

COPY app/ /app/
RUN pip install schedule

VOLUME ["/var/lib/docker/volumes", "/var/backups"]
ENTRYPOINT ["python", "backup_manager.py"]
