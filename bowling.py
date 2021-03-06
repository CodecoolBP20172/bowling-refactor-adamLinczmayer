import string


def score(game):
    result = 0
    frame = 1
    strike = ['X', 'x']
    spare = '/'
    in_first_half = True
    for i in range(len(game)):
        if game[i] == spare:
            result += 10 - last
        else:
            result += get_value(game[i])
        if frame < 10 and get_value(game[i]) == 10:
            if game[i] == spare:
                result += get_value(game[i+1])
            elif game[i] in strike:
                result += get_value(game[i+1])
                if game[i+2] == spare:
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])
        last = get_value(game[i])
        if not in_first_half or game[i] in strike:
            in_first_half = True
            frame += 1
        else:
            in_first_half = False
    return result


def get_value(char):
    if char in string.digits:
        return int(char)
    elif char in ['X', 'x', '/']:
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
