#!/bin/python3

from collections import deque
import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    if len(start_word) != len(end_word):
        return None
    stack = []
    dictionary_file = get_text("words5.dict")
    dictionary = dictionary_file.split("\n")
    stack.append(start_word)
    dictionary.remove(start_word)
    xs = deque([])
    xs.append(stack)
    if start_word == end_word:
        return xs
    while len(xs) != 0:
        ref = xs.popleft()
        copy_dict = copy.copy(dictionary)
        for word in copy_dict:
            if _adjacent(word, ref[-1]):
                if word == end_word:
                    ref.append(word)
                    return ref
                lc = copy.copy(ref)
                lc.append(word)
                xs.append(lc)
                dictionary.remove(word)
    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if len(ladder) == 0:
        return False
    for i in range(len(ladder)):
        if i == len(ladder) - 1:
            return True
        if not _adjacent(ladder[i], ladder[i + 1]):
            return False


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    list = []
    if len(word1) != len(word2):
        return False
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            list += [i]
    if len(list) != 1:
        return False
    else:
        return True 


def get_text(filename):
    with open(filename, encoding='latin1') as f:
        text = f.read()
    return text
