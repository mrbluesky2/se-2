# input: int year
# output: bool is_leap
def leap_year(year):
    ret = False
    # every 4 years
    if year % 4 == 0:
        # unless it's a mult. of 100
        if year % 100 == 0:
            # unless it's a mult. of 400
            if year % 400 == 0:
                ret = True
        else:
            ret = True
    return ret