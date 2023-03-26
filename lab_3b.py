import json, os, sys, subprocess

EXECUTE_COMMAND = "python"
PROCESS_FILE_SCRIPT = "lab_3a.py"
LINES_NUMBER = "lines_num"
CHARS_SUM = "chars_num"
LINES_SUM = "lines_num"
WORDS_SUM = "words_num"
FREQUENT_CHAR = "most_frequent_char"
FREQUENT_WORD = "most_frequent_word"


def json_to_dict(file_data):
    return json.loads(file_data)


def files_data_array(dir_path):
    result = []
    for file_name in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, "r") as file:
            file_data = subprocess.check_output([EXECUTE_COMMAND, PROCESS_FILE_SCRIPT, file_path], stdin=file).decode("utf-8")
            result.append(json_to_dict(file_data))
    return result


def find_most_frequent_word(files_data):
    word_counter = {}
    for result in files_data:
        frequent_word = result[FREQUENT_WORD]
        if frequent_word in word_counter:
            word_counter[frequent_word]+=1
        else:
            word_counter[frequent_word]=1
    return max(word_counter, key=word_counter.get)


def find_most_frequent_char(files_data):
    char_counter = {}
    for result in files_data:
        frequent_char = result[FREQUENT_CHAR]
        if frequent_char in char_counter:
            char_counter[frequent_char]+=1
        else:
            char_counter[frequent_char]=1
    return max(char_counter, key=char_counter.get)


def calculate_data(files):
    number_of_files = len(files)
    lines_sum = sum(file[LINES_NUMBER] for file in files)
    chars_sum = sum(file[CHARS_SUM] for file in files)
    words_sum = sum(file[WORDS_SUM] for file in files)
    frequent_char = find_most_frequent_char(files)
    frequent_word = find_most_frequent_word(files)
    result_dict = {
        LINES_NUMBER: number_of_files,
        LINES_SUM: lines_sum,
        CHARS_SUM: chars_sum,
        WORDS_SUM: words_sum,
        FREQUENT_CHAR: frequent_char,
        FREQUENT_WORD: frequent_word
    }
    return result_dict


def run_lab_3b(path):
    files_data = files_data_array(path[1])
    calculate_data(files_data)
    result = calculate_data(files_data)
    print("Number of files read:", result[LINES_NUMBER])
    print("Total number of lines:", result[LINES_SUM])
    print("Total number of chars:", result[CHARS_SUM])
    print("Total number of words:", result[WORDS_SUM])
    print("Most frequent char:", result[FREQUENT_CHAR])
    print("Most frequent word:", result[FREQUENT_WORD])


if __name__ == "__main__":
    run_lab_3b(sys.argv)
