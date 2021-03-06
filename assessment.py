"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    #break phrase up into a list of the words
    words = phrase.split()

    #make a dictionary to hold the results
    word_count_dict = {}

    for word in words:
        if word not in word_count_dict:
            word_count_dict[word] = 1
        else:
            word_count_dict[word] = word_count_dict[word] + 1

    return word_count_dict


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """
    melon_dict = {"Watermelon": 2.95, "Cantaloupe": 2.50, "Musk": 3.25,
                  "Christmas": 14.25}

    melon_price = melon_dict.get(melon_name, "No price found")
    return melon_price


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

        >>> word_length_sorted(["porcupine", "ok"])
        [(2, ['ok']), (9, ['porcupine'])]
    """
    word_length_dict = {}

    #loop through list and add to dictionary
    for word in words:
        if len(word) not in word_length_dict:
            word_length_dict[len(word)] = [word]
        else:
            word_length_dict[len(word)].append(word)
        #sort the list of words
        word_length_dict[len(word)].sort()

    #return the dictionary as a sorted list
    return sorted(word_length_dict.items())


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    pirate_dictionary = {"sir": "matey",
                         "hotel": "fleabag inn",
                         "student": "swabbie",
                         "man": "matey",
                         "professor": "foul blaggart",
                         "restaurant": "galley",
                         "your": "yer",
                         "excuse": "arr",
                         "students": "swabbies",
                         "are": "be",
                         "restroom": "head",
                         "my": "me",
                         "is": "be"}

    #split phrase into list of words
    phrase_list = list(phrase.split(" "))

    pirate_list = []

    for word in phrase_list:
        pirate_list.append(pirate_dictionary.get(word, word))

    return " ".join(pirate_list)


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    #put input list into dictionary
    names_dict = {}

    for name in names:
        if name not in names_dict:
            #dictionary is of the name and it's first letter and last letter
            names_dict[name] = [name[0:1], name[-1:]]
        #else nothing - can't have duplicates even if given

    #dictionary is not ordered, so I think I need to combine looking
    #for the next word in the original list with the first/last
    #info in the dictionary to find the next qualifying word in the list

    results = []

    #I know I am going to loop this but not sure how yet
    #add first word.  Maybe it's going to be while allowed_words,
    #since when that's empty it will be False?
    first_word = names[0]
    results.append(first_word)

    #maybe slice names from last word used forward to prevent me from
    #re-using words?
    allowed_words = names[1:]

    #next word is look up from dictionary word that starts with last
    #letter of my first word, but only if it's in the slice that
    #i'm still allowed to use?

    new_first_letter = names_dict.get(first_word, 0)[1]

    while allowed_words:
        for word in allowed_words:
            #if first letter is new first letter
            if names_dict.get(word)[0] == new_first_letter:
                #then append to the result
                results.append(word)
                #assign next new word
                new_first_letter = names_dict.get(word, 0)[1]
                #break out of this if and go to next word
                break

        #remove that word from allowed_words
        allowed_words.remove(word)
        #get out and start over with new first letter
        continue

    return results

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
