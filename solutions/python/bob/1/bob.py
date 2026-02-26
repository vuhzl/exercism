def response(hey_bob):
    new_hey_bob = hey_bob.strip(' ')
    if (not new_hey_bob) or (("\t" or "\r" or "\n") in new_hey_bob):
        return "Fine. Be that way!"
    elif '?' in new_hey_bob[-1]:
        if new_hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    elif new_hey_bob.isupper():
        return "Whoa, chill out!"
    return "Whatever."
