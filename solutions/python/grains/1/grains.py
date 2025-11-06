def square(number):
     if not(1 <= number <= 64):
        raise ValueError("square must be between 1 and 64")
     grains = 2 ** (number - 1)
     return grains


def total():
    list_grains = []
    for i in range (1, 64):
        new_grains = square(i)
        list_grains.append(new_grains)
    return sum(list_grains) * 2 + 1