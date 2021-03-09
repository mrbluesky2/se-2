# input: int value
# output: 'Fizz' and or 'Buzz'
def fb_value(value):
    return 'Fizz' * (value % 3 < 1) + 'Buzz' * (value % 5 < 1)

# input: none
# output: 1-100 and their fizzbuzz string
def fizzbuzz():
    for i in range(100):
        print( '[{}]: {}'.format(i, fb_value(i)) )

fizzbuzz()