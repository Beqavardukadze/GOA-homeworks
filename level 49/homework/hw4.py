

def find_it(seq):
    return next(x for x in seq if seq.count(x) % 2 == 1)
