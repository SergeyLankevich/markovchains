from local import *
from random import random

def file_editor(file):
    text = file.read()
    text = text.replace('\n', ' ')
    for i in text:
        if i in RU_ALPHABET or i in EN_ALPHABET or i in NUMBERS or i in PUNCTUATION:
            pass
        else:
            text = text.replace(i, '')
    return text.split()


def unique_words_list(text):
    unique = []
    for w in text[:]:
        if w not in unique:
            unique.append(w)
    return unique


def start_words_list(text):
    start = []
    for w in text:
        if w.capitalize() == w and w[0] not in NUMBERS:
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


def sentence_generator(current_word, minlength, maxlength, n=1):
    '''

    :param current_word: current word being considered for use
    :param minlength: minimum length of sentences
    :param maxlength: maximum length of sentences
    :param n: amount of words on current step of recursion
    :return: tuple whose first element is current end of sentence
             and second element is flag for the correct operation of generation
    '''
    if n >= minlength and current_word in stop_words:
        return (current_word, False)
    elif n >= maxlength:
        stop_word_index = round(random() * (len(stop_words)) - 1)
        stop_word = stop_words[stop_word_index]
        return (stop_word, False)
    elif n < minlength and current_word in stop_words:
        return (current_word, True)

    next_word_index = round(random() * (len(chains[current_word]) - 1))
    next_word = chains[current_word][next_word_index]
    response = sentence_generator(next_word, minlength, maxlength, n + 1)
    banned_words = stop_words
    while response[1]:
        banned_words.append(response[0])
        for word in chains[current_word]:
            if word not in banned_words:
                while next_word in banned_words:
                    next_word_index = round(random() * (len(chains[current_word]) - 1))
                    next_word = chains[current_word][next_word_index]
                break
        else:
            return (current_word, True)
        response = sentence_generator(next_word, minlength, maxlength, n + 1)

    return (current_word + ' ' + response[0], False)


def text_generator(minlength: int, maxlength: int, n: int):
    '''

    :param minlength: minimum length of sentences
    :param maxlength: maximum length of sentences
    :param n: amount of sentences
    :return: generated text
    '''
    text = ''
    for _ in range(n):
        start_word_index = round(random() * (len(start_words) - 1))
        start_word = start_words[start_word_index]
        if start_word in stop_words:
            text += start_word + ' '
            continue
        else:
            sentence = sentence_generator(start_word, minlength, maxlength)
            banned_words = []
            while sentence[1]:
                banned_words.append(start_word)
                for word in start_words:
                    if word not in banned_words:
                        while start_word in banned_words:
                            start_word_index = round(random() * (len(start_words) - 1))
                            start_word = start_words[start_word_index]
                        break
                else:
                    return 'ERROR. Cannot generate a sentence for the given input.'
                sentence = sentence_generator(start_word, minlength, maxlength)
            text += sentence[0] + ' '
    return text


with open('input.txt', 'r', encoding='utf-8') as f_in, open('output.txt', 'w', encoding='utf-8') as f_out:
    inputFile = file_editor(f_in)
    unique_words = unique_words_list(inputFile)
    start_words = start_words_list(inputFile)
    stop_words = stop_words_list(inputFile)
    chains = chains_dict(inputFile)
    print(text_generator(5, 20, 10))
