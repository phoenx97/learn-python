directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
stops = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']

def scan(string):
    
    result = []
    sentence = string.split()

    for word in sentence:

        if word.lower() in directions:
            result.append(('direction', word))

        elif word.lower() in verbs:
            result.append(('verb', word))

        elif word.lower() in stops:
            result.append(('stop', word))

        elif word.lower() in nouns:
            result.append(('noun', word))

        elif convert_number(word) != None:
            result.append(('number', int(word)))

        else:
            result.append(('error', word))

    return result

def convert_number(c):

    try:
        return int(c)
    except:
        return None
