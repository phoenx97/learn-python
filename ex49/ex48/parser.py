class ParserError(Exception):
    pass


class Sentence(object):

    def __init__(self, num_subj, subject, verb, object):
        # remember we take ('noun', 'princess') tuples and convert them
        self.num_subjects = num_subj[1]
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]


def peek(word_list):
    if word_list:  # check if there's any words left
        word = word_list[0]  # word is the first tuple
        return word[0]  # return first element (type) of the tuple
    else:
        return None


def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)  # pop the first element

        # word is a tuple at this point
        # word[0] is the word type
        if word[0] == expecting:
            return word  # return the tuple if the type matches
        else:
            return None
    else:
        return None


def skip(word_list, word_type):
    # peek returns the type of the first word in the list
    # if it's of the target type, pop it from the word list (done in match)
    # moves to the next tuple until it's not of the target type
    while peek(word_list) == word_type:
        match(word_list, word_type)


# study drill - handle numbers
# using numbers to describe amount of subjects (can implement number of objects later)
def parse_number(word_list):
    next = peek(word_list)

    if next == 'number':
        return match(word_list, 'number')
    else:
        return ('number', 0)
        # raise ParserError("Expected a number next.")  # this should never be called, since never required


def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")


def parse_object(word_list):
    skip(word_list, 'stop')
    next = peek(word_list)

    if next == 'noun':
        return match(word_list, 'noun')
    if next == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")


def parse_subject(word_list, num_subj, subj):
    # (number of) subject(s) already identified/passed when entering this function (from parse_sentence)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(num_subj, subj, verb, obj)


def parse_sentence(word_list):
    skip(word_list, 'stop')
    start = peek(word_list)

    if start == 'number':
        num = parse_number(word_list)
        start = peek(word_list)
    else:
        num = ('number', None)  # probably a better way to do this when no number specified

    if start == 'noun':
        subj = match(word_list, 'noun')
        return parse_subject(word_list, num, subj)
    elif start == 'verb':
        # assume the subject is the player then
        return parse_subject(word_list, num, ('noun', 'player'))
    else:
        raise ParserError("Must start with the subject, object, or verb not: %s" % start)
