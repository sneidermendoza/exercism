def add_prefix_un(word):
    """
    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """

    return f"un{word}"


def make_word_groups(vocab_words):
    """

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """
    
    return f" :: {vocab_words[0]}".join(vocab_words)


def remove_suffix_ness(word):
    """

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    """
    remove = word[:-4]
    remove_list = list(remove)
    if remove_list[-1] == "i":
        remove_list[-1] = "y"
        new = "".join(remove_list)
        return new
    else:
        return remove   

def noun_to_verb(sentence, index):
    """

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """
    suffix = "en"
    index = int(index)
    new_list = sentence.split()
    verb = new_list[index]
    verb_list = list(verb)
    if verb_list[-1] == ".":
        verb_list[-1] = "en"
        new_verb = "".join(verb_list)
        return new_verb
    else:
        return f"{verb}{suffix}"
