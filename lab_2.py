import os
import sys

PATH_NAME = "PATH"
DIRECTORY = "dir"
EXECUTABLE = "exe"
LISTING_ERROR = "Nie można wylistować katalogu"
SEPARATOR = "______________________________________________"
COMMANDS_ARRAY = [DIRECTORY, EXECUTABLE]
VALID_ARGS_LENGTH = 2


def check_length(args):
    if len(args) != VALID_ARGS_LENGTH:
        raise Exception("Błedne/brak danych wywołania")


def check_command(command):
    if command not in COMMANDS_ARRAY:
        raise Exception(f"{command} nie jest parametrem obsługiwanym przez skrypt,"
                        f" użyj {DIRECTORY} lub {EXECUTABLE}")


def is_executable(directory, file):
    return os.access(os.path.join(directory, file), os.X_OK)


def print_array(array):
    for elem in array:
        print(elem)


def print_path_directories(path_directories):
    splited_directories = path_directories.split(os.pathsep)
    print_array(splited_directories)


def print_path_executables(path_directories):
    splited_directories = path_directories.split(os.pathsep)
    for directory in splited_directories:
        print(SEPARATOR)
        print(directory)
        try:
            files = os.listdir(directory)
        except OSError:
            print(LISTING_ERROR)
        else:
            filtered_exe_files = list(filter(lambda file: is_executable(directory, file), files))
            print_array(filtered_exe_files)


def run_lab_2(args):
    check_length(args)

    run_command = args[1]
    check_command(run_command)

    path_directories = os.environ.get(PATH_NAME)

    if run_command == DIRECTORY:
        print_path_directories(path_directories)
    if run_command == EXECUTABLE:
        print_path_executables(path_directories)


if __name__ == "__main__":
    run_lab_2(sys.argv)
