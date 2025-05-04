
#1)
def bool_to_word(b):
    return "Yes" if b else "No"


#2)
def get_char(c):
    return chr(c)

#3)

def odds(values):
    return list(filter(lambda x: x % 2 != 0, values))
