import os, json, sys, zipfile, datetime, shutil
from lab_4b_utils import set_backup_env, DATE_FORMAT, HISTORY_FILE_NAME, PATH_POSITION, JSON_TIMESTAMP, JSON_FILENAME, BACKUP_NAME, JSON_SOURCE

# Domyślna lokalizacja do przywrócenia kopii zapasowej
DEFAULT_RESTORE = './Test'


# Funkcja zwracająca ścieżkę, do której zostanie przywrócona kopia zapasowa
def restore_to():
    args = sys.argv
    if len(args) <= PATH_POSITION:
        return DEFAULT_RESTORE
    else:
        return args[PATH_POSITION]


set_backup_env()
BACKUPS_DIR = os.environ.get(BACKUP_NAME)

# Ścieżka, do której zostanie przywrócona kopia zapasowa
PATH_TO_RESTORE = restore_to()


# Funkcja zwracająca listę wszystkich kopii zapasowych wraz z ich danymi zapisanymi w pliku history
def get_backups():
    backups_file = os.path.join(BACKUPS_DIR, HISTORY_FILE_NAME)
    if not os.path.exists(backups_file):
        return []
    with open(backups_file, "r") as file:
        backups = json.load(file)
    backups.sort(key=lambda backup: datetime.datetime.strptime(backup[JSON_TIMESTAMP], DATE_FORMAT))
    return backups


# Wyświetla wszystkie kopie zapasowe z listy backups
def show_backups(backups):
    if not backups:
        print("Bark kopii zapasowych w tej lokalizacji")
        sys.exit(1)
    else:
        print("Kopie zapasowe: ")
        for i, backup in enumerate(backups):
            print(f'{i}. {backup[JSON_TIMESTAMP]} - {backup[JSON_SOURCE]} - {backup[JSON_FILENAME]}')


# Funkcja do wyboru kopii zapasowej do przywrócenia
def which_backup(backups):
    while True:
        choice = int(input("Wybierz kopię zapasową do przywrócenia: "))
        if len(backups) > choice >= 0:
            return choice
        else:
            print("Kopia zapasowa nie istnieje, spróbuj ponownie")


# Funkcja tworząca ścieżkę do przywracania kopii zapasowej oraz usuwająca starą ścieżkę, jeśli istnieje
def restore_to_dir():
    if os.path.exists(PATH_TO_RESTORE):
        shutil.rmtree(PATH_TO_RESTORE)
    os.makedirs(PATH_TO_RESTORE)


# Funkcja przywracająca kopię zapasową o podanej nazwie
def restore(backup, backup_path):
    with zipfile.ZipFile(backup_path, "r") as zipped:
        zipped.extractall(PATH_TO_RESTORE)
    print(f'Przywrócono kopię zapasową: {backup[JSON_FILENAME]} z: {backup[JSON_TIMESTAMP]} do lokalizacji: {PATH_TO_RESTORE}.')


def run_lab_4b():
        backups = get_backups()
        show_backups(backups)
        backup = backups[which_backup(backups)]
        path_to_backup = os.path.join(BACKUPS_DIR, backup[JSON_FILENAME])
        restore_to_dir()
        restore(backup, path_to_backup)


if __name__ == '__main__':
    run_lab_4b()