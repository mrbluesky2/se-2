# leap_year.py
# john pierre carr
# carrjoh@oregonstate.edu

# descripition:
# a program to take user input
# and determine if it's a leap
# year

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

def main():
    # get user input
    user_input = input('Enter a year: ')

    # exit if the user wants to
    if user_input == 'e' or user_input == 'exit':
        return

    # cast to int
    year = int(user_input)

    # determine if it's a leap year
    #   print the appropriate message
    if leap_year(year):     print('{} is a leap year.\n'.format(year))
    else:                   print('{} is not a leap year.\n'.format(year))

    # loop
    main()

main()