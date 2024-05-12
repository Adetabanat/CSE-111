#importing the random moudle to choose words from the list
import random
# Getting a determinar
def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner."""


# Randomly choose and return a determiner.
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    word = random.choice(words)
    return word

# Randomly choose and return a noun.
def get_noun(quantity):
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    noun = random.choice(nouns)
    return noun

# Randomly choose and return a verb.
def get_verb(quantity, tense):
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    verb = random.choice(verbs)
    return verb

# Randomly choose and return an adjective.
def get_adjective():
    adjectives = ["beautiful", "big", "small", "happy", "sad", "bright", "dark", "funny", "serious", "clever"]
    adjective = random.choice(adjectives)
    return adjective

# Randomly choose and return adverb.
def get_adverb():
    adverbs = ["quickly", "slowly", "happily", "sadly", "loudly", "quietly", "carefully", "eagerly", "calmly", "bravely"]
    adverb = random.choice(adverbs)
    return adverb

# Randomly choose and return a prepostional phrase.
def get_prepositional_phrase():
    prepositions = ["across", "near", "under", "without", "from", "behind", "on", "above"]
    determiner = get_determiner(1)
    noun = get_noun(1)
    preposition = random.choice(prepositions)
    prepositional_phrase = determiner + " " + noun + " " + preposition
    return prepositional_phrase

# Generating the Sentance.
def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    adverb = get_adverb()
    adjective = get_adjective()
    prepositional_phrase_1 = get_prepositional_phrase()
    prepositional_phrase_2 = get_prepositional_phrase()
    sentence = determiner + " " + adjective + " " + noun + " " + verb + " "+ adverb + " " + prepositional_phrase_1 + " " + prepositional_phrase_2 + "."
    sentence = sentence.capitalize()
    return sentence
    
# code to run the six sentences with "single quantity=1 and pural quantity=2"
def main():
    # Quantity: single, Verb Tense: past
    sentence_a = make_sentence(1, "past")
    print(sentence_a)

    # Quantity: single, Verb Tense: present
    sentence_b = make_sentence(1, "present")
    print(sentence_b)

    # Quantity: single, Verb Tense: future
    sentence_c = make_sentence(1, "future")
    print(sentence_c)

    # Quantity: plural, Verb Tense: past
    sentence_d = make_sentence(2, "past")
    print(sentence_d)

    # Quantity: plural, Verb Tense: present
    sentence_e = make_sentence(2, "present")
    print(sentence_e)

    # Quantity: plural, Verb Tense: future
    sentence_f = make_sentence(2, "future")
    print(sentence_f)

# Call the main function
main()
