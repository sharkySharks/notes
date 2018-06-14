
tempFileIn = open('../../LabsData/temps.dat')  # defaults to read when parameter not given
tempFileOut = open('./lab13DataOutput.dat', 'w')


def f_to_c(f):
    return 5.0/9.0*(f - 32)

for linein in tempFileIn:
    try:
        f = float(linein)
    except ValueError:
        tempFileOut.write('Wrong type for value - {} -! \n'.format(linein))
    else:
        c = f_to_c(f)
        tempFileOut.write('{0:.1f} Farenheit is {1:.1f} Centigrade.'.format(f, c))
        tempFileOut.write('\n')
tempFileIn.close()
tempFileOut.close()
