import json, sys


def find_most_frequent_char(content):
    char_counter = {}
    for char in content:
        if char in char_counter:
            char_counter[char] += 1
        else:
            char_counter[char] = 1
    return max(char_counter, key=char_counter.get)


def find_most_frequent_word(words):
    word_counter = {}
    for word in words:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1
    return max(word_counter, key=word_counter.get)


def analyze_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    splited = content.split()

    chars_num = len(content)
    words_num = len(splited)
    lines_num = content.count("\n") + 1
    most_frequent_char = find_most_frequent_char(content)
    most_frequent_word = find_most_frequent_word(splited)

    return {
        "file_path": file_path,
        "chars_num": chars_num,
        "words_num": words_num,
        "lines_num": lines_num,
        "most_frequent_char": most_frequent_char,
        "most_frequent_word": most_frequent_word
    }


def process_file(args):
    file_path = args[1]
    result = analyze_file(file_path)
    print(json.dumps(result))


if __name__ == "__main__":
    process_file(sys.argv)
