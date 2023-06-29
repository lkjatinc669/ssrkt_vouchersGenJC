from num2words import num2words

def say_number(number):
    res = num2words(number)
    res = res.capitalize()
    return res