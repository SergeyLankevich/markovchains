from local import *


def file_editor(file):
    text = file.read()
    text = text.replace('\n', ' ')
    for i in text:
        if i in RU_ALPHABET or i in EN_ALPHABET or i in PUNCTUATION:
            pass
        else:
            text = text.replace(i, '')
    return text.split()


def unique_words_list(text):
    unique = []
    for w in text[:-1]:
        if w not in unique:
            unique.append(w)
    return unique


def start_words_list(text):
    start = []
    for w in text:
        if w.capitalize() == w:
            start.append(w)
    return start


def stop_words_list(text, finish_marks=('.', '!', '?')):
    stop = []
    for w in text:
        if w[-1] in finish_marks:
            stop.append(w)
    return stop


def chains_dict(text):
    chains = dict.fromkeys(unique_words, [])
    for i in range(len(text)):
        if text[i] in stop_words:
            pass
        elif text[i] in unique_words:
            if chains[text[i]] == []:
                chains.update({text[i]: [text[i + 1]]})
            else:
                chains[text[i]].append(text[i + 1])
    return chains


with open('input.txt', 'r', encoding='utf-8') as f_in:
    with open('output.txt', 'w', encoding='utf-8') as f_out:
        inputFile = file_editor(f_in)
        print(inputFile)
        unique_words = unique_words_list(inputFile)
        start_words = start_words_list(inputFile)
        stop_words = stop_words_list(inputFile)
        chains = chains_dict(inputFile)
