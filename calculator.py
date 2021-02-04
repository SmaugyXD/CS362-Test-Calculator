import math

def calc(a,b):

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return math.inf

    if int(b) == 0:
        div = a * math.inf
    else:
        div = a/b

    return (a + b, a - b, a * b, div)
