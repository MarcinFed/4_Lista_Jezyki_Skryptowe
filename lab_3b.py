import json, os, sys, subprocess

# stałe wykorzystywane w kodzie
EXECUTE_COMMAND = "python"
PROCESS_FILE_SCRIPT = "lab_3a.py"
LINES_NUMBER = "lines_num"
CHARS_NUM = "chars_num"
LINES_NUM = "lines_num"
WORDS_NUM = "words_num"
FREQUENT_CHAR = "most_frequent_char"
FREQUENT_WORD = "most_frequent_word"


# funkcja konwertująca dane w formacie JSON do słownika
def json_to_dict(file_data):
    return json.loads(file_data)


# funkcja zwracająca listę słowników reprezentujących analizy plików w podanym katalogu
def files_data_array(dir_path):
    result = []
    for file_name in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, "r") as file:
            file_data = subprocess.check_output([EXECUTE_COMMAND, PROCESS_FILE_SCRIPT, file_path], stdin=file).decode("utf-8")
            result.append(json_to_dict(file_data))
    return result


# funkcja zwracająca najczęściej występujące słowo we wszystkich analizowanych plikach
def find_most_frequent_word(files_data):
    word_counter = {}
    for result in files_data:
        frequent_word = result[FREQUENT_WORD]
        if frequent_word in word_counter:
            word_counter[frequent_word]+=1
        else:
            word_counter[frequent_word]=1
    return max(word_counter, key=word_counter.get)


# funkcja zwracająca najczęściej występujący znak we wszystkich analizowanych plikach
def find_most_frequent_char(files_data):
    char_counter = {}
    for result in files_data:
        frequent_char = result[FREQUENT_CHAR]
        if frequent_char in char_counter:
            char_counter[frequent_char]+=1
        else:
            char_counter[frequent_char]=1
    return max(char_counter, key=char_counter.get)


# funkcja agregująca statystyki dla wszystkich plików
def calculate_data(files):
    number_of_files = len(files)
    lines_sum = sum(file[LINES_NUM] for file in files)
    chars_sum = sum(file[CHARS_NUM] for file in files)
    words_sum = sum(file[WORDS_NUM] for file in files)
    frequent_char = find_most_frequent_char(files)
    frequent_word = find_most_frequent_word(files)
    result_dict = {
        LINES_NUMBER: number_of_files,
        LINES_NUM: lines_sum,
        CHARS_NUM: chars_sum,
        WORDS_NUM: words_sum,
        FREQUENT_CHAR: frequent_char,
        FREQUENT_WORD: frequent_word
    }
    return result_dict


def run_lab_3b(path):
    files_data = files_data_array(path[1])
    result = calculate_data(files_data)
    print("Number of files read:", result[LINES_NUMBER])
    print("Total number of lines:", result[LINES_NUM])
    print("Total number of chars:", result[CHARS_NUM])
    print("Total number of words:", result[WORDS_NUM])
    print("Most frequent char:", result[FREQUENT_CHAR])
    print("Most frequent word:", result[FREQUENT_WORD])


if __name__ == "__main__":
    run_lab_3b(sys.argv)
