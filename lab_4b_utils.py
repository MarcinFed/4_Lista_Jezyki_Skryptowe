import os

PATH_POSITION = 1
BACKUP_NAME = "BACKUPS_DIR"
DEFAULT_BACKUP_PATH = ".backups"
DATE_FORMAT = "%Y%m%d-%H%M%S"
HISTORY_FILE_NAME = "backup_history.json"
JSON_TIMESTAMP = "time"
JSON_SOURCE = "source_dir"
JSON_FILENAME = "backup_filename"


def set_backup_env():
    if not os.getenv(BACKUP_NAME):
        os.environ[BACKUP_NAME] = DEFAULT_BACKUP_PATH