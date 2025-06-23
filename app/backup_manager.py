import os, json, time, tarfile, schedule
from datetime import datetime, timedelta

with open("config.json") as f:
    config = json.load(f)

SRC = config["backup_source"]
DST = config["backup_destination"]
LOG = config["log_path"]
RETENTION = config["retention_days"]

def log(msg):
    with open(LOG, "a") as f:
        f.write(f"{datetime.now()} - {msg}\n")

def create_backup():
    now = datetime.now().strftime("%Y%m%d-%H%M%S")
    archive_name = os.path.join(DST, f"docker-volumes-backup-{now}.tar.gz")
    log(f"Starting backup: {archive_name}")
    
    with tarfile.open(archive_name, "w:gz") as tar:
        tar.add(SRC, arcname=os.path.basename(SRC))
    
    log(f"Backup complete: {archive_name}")
    cleanup_old_backups()

def cleanup_old_backups():
    now = datetime.now()
    for f in os.listdir(DST):
        path = os.path.join(DST, f)
        if f.endswith(".tar.gz"):
            mtime = datetime.fromtimestamp(os.path.getmtime(path))
            if now - mtime > timedelta(days=RETENTION):
                os.remove(path)
                log(f"Deleted old backup: {f}")

# Schedule
schedule.every(config["interval_minutes"]).minutes.do(create_backup)

log("Backup scheduler started.")
create_backup()  # Initial backup on container start

while True:
    schedule.run_pending()
    time.sleep(60)
