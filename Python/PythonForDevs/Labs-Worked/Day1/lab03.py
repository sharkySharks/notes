while True:
    temp = raw_input('Please input a Farenheit temperature to convert to Centigrade: ')
    if temp == 'q' or temp == 'Q': # q or Q is how you quit from the terminal
        break
    f = float(temp)
    c = 5.0/9.0*(f - 32)
    print '{0:.1f} Farenheit is {1:.1f} Centigrade.'.format(f, c)
