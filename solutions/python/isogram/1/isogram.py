def is_isogram(string):
    string = string.lower().replace('-', '').replace(' ', '')
    new = set(string.lower())
    if string == '':
        return True
    if sorted(new) != sorted(string):
        return False
    return True