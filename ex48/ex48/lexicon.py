directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
stops = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def scan(string):
    result = []
    sentence = string.split()

    for word in sentence:
        if word in directions:
            result.append(('direction', word))
        elif word in verbs:
            result.append(('verb', word))
        elif word in stops:
            result.append(('stop', word))
        elif word in nouns:
            result.append(('noun', word))
        elif is_number(word):
            result.append(('number', int(word)))
        else:
            result.append(('error', word))

    return result

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