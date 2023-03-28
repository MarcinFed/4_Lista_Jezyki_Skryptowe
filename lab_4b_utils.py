import os

# Numer pozycji argumentu ścieżki w argv
PATH_POSITION = 1

# Nazwa zmiennej środowiskowej przechowującej ścieżkę do katalogu z backupami
BACKUP_NAME = "BACKUPS_DIR"

# Domyślna ścieżka do katalogu z backupami
DEFAULT_BACKUP_PATH = "./backups"

# Format daty i czasu używany do tworzenia kopii zapasowych
DATE_FORMAT = "%Y%m%d-%H%M%S"

# Nazwa pliku historii backupów
HISTORY_FILE_NAME = "backup_history.json"

# Klucze używane w pliku JSON przechowującym informacje o backupie
JSON_TIMESTAMP = "time"
JSON_SOURCE = "source_dir"
JSON_FILENAME = "backup_filename"


# Ustawienie domyślnej ścieżki do katalogu z backupami w zmiennej środowiskowej
def set_backup_env():
    if not os.getenv(BACKUP_NAME):
        os.environ[BACKUP_NAME] = DEFAULT_BACKUP_PATH