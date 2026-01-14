def is_pangram(sentence):
    all_letter = 'abcdefghijklmnopqrstuvwxyz'
    for char in all_letter:
        if char not in sentence.lower():
            return False
    return True        
    
        
