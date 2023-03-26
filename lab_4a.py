import sys, os, time, shutil, json
from lab_4b_utils import set_backup_env, BACKUP_NAME, DATE_FORMAT, HISTORY_FILE_NAME, JSON_TIMESTAMP, JSON_FILENAME, JSON_SOURCE

FORMAT = 'zip'

set_backup_env()
BACKUP_DIR = os.environ.get(BACKUP_NAME)


def create_dir():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)


def get_backup_filename(file_name):
    timestamp = time.strftime(DATE_FORMAT)
    return f"{timestamp}-{file_name}"


def make_backup(source, backup_path):
    shutil.make_archive(backup_path, FORMAT, source)


def update_history_file(source_dir, filename_of_backup):
    backup_history_file = os.path.join(BACKUP_DIR, HISTORY_FILE_NAME)
    backup_time = time.strftime(DATE_FORMAT)
    file_name = f"{filename_of_backup}.{FORMAT}"
    data = {JSON_TIMESTAMP: backup_time, JSON_SOURCE: source_dir, JSON_FILENAME: file_name}

    if not os.path.exists(backup_history_file):
        with open(backup_history_file, "w") as f:
            json.dump([data], f)
    else:
        with open(backup_history_file, "r") as f:
            existing_data = json.load(f)
        with open(backup_history_file, "w") as f:
            existing_data.append(data)
            json.dump(existing_data, f)


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
