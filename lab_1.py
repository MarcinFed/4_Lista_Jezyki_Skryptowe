import os, sys


def print_env_vars(filter_list):
    #Pobranie zmiennych środowiskowych do listy
    env_vars = os.environ
    # Sprawdzenie, czy skrypt został wywołany z argumentami
    if len(filter_list) > 1:
        # Iteracja po wszystkich argumentach w linii komend
        for filter_pattern in filter_list[1:]:
            env_vars = {key: value for key, value in env_vars.items() if filter_pattern in key}

    for key, value in sorted(env_vars.items()):
        print(f"{key} = {value}")


if __name__ == "__main__":
   print_env_vars(sys.argv)
