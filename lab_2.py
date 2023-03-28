import os
import sys

# stałe wykorzystywane w kodzie
PATH_NAME = "PATH"
DIRECTORY = "dir"
EXECUTABLE = "exe"
SEPARATOR = "______________________________________________"
COMMANDS_ARRAY = [DIRECTORY, EXECUTABLE]
VALID_ARGS_LENGTH = 2


# funkcja sprawdzająca poprawność liczby argumentów
def check_length(args):
    if len(args) != VALID_ARGS_LENGTH:
        raise Exception("Błedne/brak danych wywołania")


# funkcja sprawdzająca poprawność parametru wywołania skryptu
def check_command(command):
    if command not in COMMANDS_ARRAY:
        raise Exception(f"{command} nie jest parametrem obsługiwanym przez skrypt,"
                        f" użyj {DIRECTORY} lub {EXECUTABLE}")


# funkcja sprawdzająca, czy dany plik jest plikiem wykonywalnym
def is_executable(directory, file):
    return os.access(os.path.join(directory, file), os.X_OK)


# funkcja wypisująca elementy listy
def print_array(array):
    for elem in array:
        print(elem)


# funkcja wypisująca katalogi znajdujące się w zmiennej środowiskowej PATH
def print_path_directories(path_directories):
    splited_directories = path_directories.split(os.pathsep)
    print_array(splited_directories)


# funkcja wypisująca pliki wykonywalne z katalogów zdefiniowanych w zmiennej PATH
def print_path_executables(path_directories):
    splited_directories = path_directories.split(os.pathsep)
    for directory in splited_directories:
        print(SEPARATOR)
        print(directory)
        try:
            files = os.listdir(directory) # lista plików i katalogów znajdujących się w danym katalogu
        except OSError:
            print("Nie można wylistować katalogu")
        else:
            filtered_exe_files = list(filter(lambda file: is_executable(directory, file), files)) # wybór tylko plików wykonywalnych
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
