# get the volume of a cube
def cube_volume(side):
    try:
        volume = side * side * side
    except ValueError:
        raise ValueError

    # negative lengths result in zero volume
    if side <= 0:
        return 0

    return volume

# find the average of a list
def average_list(list):
    # empty lists result in a zero average
    if len(list) < 1:
        return 0

    try:
        average = sum(list) / len(list)
    except ValueError:
        raise ValueError

    return average

# make a full name with a first, last pair
def make_name(first, last):
    try:
        fullname = first + ' ' + last
    except ValueError:
        raise ValueError
    
    if fullname == ' ':
        return ''

    return fullname