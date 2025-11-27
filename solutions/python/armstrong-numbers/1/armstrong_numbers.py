def is_armstrong_number(number):
    n = number
    power = len(str(number))
    total = 0
    
    while n > 0:
        digit = n % 10
        total += digit ** power
        n //= 10
    
    if total == number:
        return True
    return False