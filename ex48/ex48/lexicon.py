directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
stops = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def scan(string):
    result = []
    sentence = string.split()

    for word in sentence:
        if is_direction(word):
            result.append(('direction', word))
        elif is_verb(word):
            result.append(('verb', word))
        elif is_stop(word):
            result.append(('stop', word))
        elif is_noun(word):
            result.append(('noun', word))
        elif is_number(word):
            result.append(('number', int(word)))
        else:
            result.append(('error', word))

    return result

def is_direction(string):
    for word in directions:
        if word == string:
            return True

    return False

def is_verb(string):
    for word in verbs:
        if word == string:
            return True

    return False

def is_stop(string):
    for word in stops:
        if word == string:
            return True

    return False

def is_noun(string):
    for word in nouns:
        if word == string:
            return True

    return False

def is_number(string):
    for char in string:
        c = convert_number(char)
        if c != None and c in numbers:
            pass
        else:
            return False

    return True

def convert_number(c):
    try:
        return int(c)
    except:
        return None