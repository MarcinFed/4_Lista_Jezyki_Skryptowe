import sys, os, time, shutil, json
from lab_4b_utils import set_backup_env, BACKUP_NAME, DATE_FORMAT, HISTORY_FILE_NAME, JSON_TIMESTAMP, JSON_FILENAME, JSON_SOURCE

FORMAT = 'zip'

# Ustawia zmienną środowiskową, która przechowuje ścieżkę do katalogu backupu
set_backup_env()
BACKUP_DIR = os.environ.get(BACKUP_NAME)


# Tworzy katalog backupu, jeśli taki nie istnieje
def create_dir():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)


# Tworzy nazwę pliku z datą i czasem oraz nazwą pliku źródłowego, które są wykorzystywane w nazwie pliku backupu
def get_backup_filename(file_name):
    timestamp = time.strftime(DATE_FORMAT)
    return f"{timestamp}-{file_name}"


# Tworzy backup podanego źródła i zapisuje go w katalogu backupu
def make_backup(source, backup_path):
    shutil.make_archive(backup_path, FORMAT, source)


# Aktualizuje plik z historią backupów o informacje o nowym backupie
def update_history_file(source_dir, filename_of_backup):
    backup_history_file = os.path.join(BACKUP_DIR, HISTORY_FILE_NAME)
    backup_time = time.strftime(DATE_FORMAT)
    file_name = f"{filename_of_backup}.{FORMAT}"
    data = {JSON_TIMESTAMP: backup_time, JSON_SOURCE: source_dir, JSON_FILENAME: file_name}

    # Jeśli plik z historią nie istnieje, tworzy nowy plik i zapisuje w nim informację o nowym backupie
    if not os.path.exists(backup_history_file):
        with open(backup_history_file, "w") as f:
            json.dump([data], f)
    # Jeśli plik z historią istnieje, odczytuje jego zawartość, dodaje informacje o nowym backupie i zapisuje plik
    else:
        with open(backup_history_file, "r") as f:
            existing_data = json.load(f)
        with open(backup_history_file, "w") as f:
            existing_data.append(data)
            json.dump(existing_data, f)


# Tworzy backup dla podanego źródła
def create_backup(source):
    create_dir()
    dir = os.path.basename(source)
    backup_name = get_backup_filename(dir)
    backup_path = os.path.join(BACKUP_DIR, backup_name)
    make_backup(source, backup_path)
    update_history_file(source, backup_name)
    return backup_name


def run_lab_4a(args):
    backup = create_backup(args[1])
    print(f"Backup created: {backup}")


if __name__ == '__main__':
    run_lab_4a(sys.argv)
