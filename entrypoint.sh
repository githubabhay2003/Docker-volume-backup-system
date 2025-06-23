#!/bin/bash
chmod -R 777 /var/backups
exec python /app/backup_manager.py
