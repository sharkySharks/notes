while True:
    temp = raw_input('Please input a Farenheit temperature to convert to Centigrade: ')
    if temp == 'q' or temp == 'Q': # q or Q is how you quit from the terminal
        print 'Thanks for playing!'
        break
    try:
        f = float(temp)
    except ValueError:
        print 'Wrong type for value - {} -, try again!'.format(temp)
        # can also add a continue here and skip the else below, bumping those last two lines out a level
        # works the same way, but breaks and continues make things a little more cluttered and not as clear
    else:
        c = 5.0/9.0*(f - 32)
        print '{0:.1f} Farenheit is {1:.1f} Centigrade.'.format(f, c)
