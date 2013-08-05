import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(ojbect):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True

# load up words from website
for word in urlopen(WORD_URL).readlines():  # readline until EOF
    WORDS.append(word.strip())  # strip removes whitespace


def convert(snippet, phrase):
    # get random sample from WORDS for number of occurences
    # of '%%%' in snippet and capitalize each
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    # get random sample from WORDS for number of occurences of '***' in snippet
    other_names = random.sample(WORDS, snippet.count("***"))

    results = []
    param_names = []

    # for i = 0; i < (occurences of '@@@' in snippet); i++
    for i in range(0, snippet.count("@@@")):
        # set parameter count between 1 and 3
        param_count = random.randint(1,3)
        # join parameters with a ,
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]  # copy the sentence list from first ele to last

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# keep going until user hits ctrl+d
try:
    while True:
        snippets = PHRASES.keys()  # copy of list of keys
        random.shuffle(snippets)  # shuffle the keys

        for snippet in snippets:
            # snippet is the key in PHRASES while phrase is the value
            phrase = PHRASES[snippet]
            # call convert on snippet/phrase to replace the %%%, ***, @@@
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                # swap if user option
                question, answer = answer, question

            print question

            raw_input("> ")
            print "ANSWER:  %s\n\n" % answer
except EOFError:
    print "\nBye"
