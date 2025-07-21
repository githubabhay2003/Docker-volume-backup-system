# Docker Volume Backup System

This project provides an automated solution for backing up Docker volumes. It uses a Python-based scheduler inside a Docker container to create periodic `.tar.gz` backups of Docker volumes and stores them in a specified directory.

## 🧰 Features
- 📦 Backs up all Docker volumes using `tar`
- ⏲️ Configurable backup interval and retention policy
- 🗃️ Keeps only the most recent backups (via retention_days)
- 📄 Simple JSON-based configuration
- 📑 Logs actions to a file for auditing

## 📁 Project Structure
```
.
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
├── requirements.txt
└── app/
├── backup_manager.py
└── config.json
```
⚙️ Configuration (`app/config.json`)
Edit `config.json` to control how and where backups are stored:
```json
{
  "backup_source": "/var/lib/docker/volumes/",
  "backup_destination": "/var/backups/",
  "retention_days": 7,
  "interval_minutes": 1440,
  "log_path": "/var/log/backup.log"
}
```

Field	Description
backup_source	Path where Docker volumes are located
backup_destination	Directory to save .tar.gz backup files
retention_days	Delete backups older than N days
interval_minutes	Run backups every N minutes (e.g., 1440 = daily)
log_path	Log file path inside container

🚀 Usage
1. Clone the Repository
git clone https://github.com/githubabhay2003/Docker-volume-backup-system.git
cd Docker-volume-backup-system

2. Build and Start the Container
docker compose up --build -d

3. Check Logs
docker logs volume-backup
docker exec -it volume-backup cat /var/log/backup.log

4. View Backup Files
docker exec -it volume-backup ls -lh /var/backups/

🛠️ Manual Trigger (optional)
To run the backup script manually:
docker exec -it volume-backup python /app/backup_manager.py

📌 Requirements
Docker
Docker Compose

🔒 Security Note
Do not expose the container or volume paths publicly.
Store your backup files securely and consider encrypting them.
Use a secure method like SSH deploy key or PAT for repo access.
