# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.



def digitize(n):
    return [int(digit) for digit in str(n)][::-1]
