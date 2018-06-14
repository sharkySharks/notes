
tempFileIn = open('../../LabsData/temps.dat')  # defaults to read when parameter not given
tempFileOut = open('./lab07DataOutput.dat', 'w')
for linein in tempFileIn:  # behind the scenes this is doing a readline()
    # if you add linein = tempFileIn.readline() <== this will be the next line in the iteration
    try:
        f = float(linein)
    except ValueError:
        tempFileOut.write('Wrong type for value - {} -! \n'.format(linein))
    else:
        c = 5.0/9.0*(f - 32)
        tempFileOut.write('{0:.1f} Farenheit is {1:.1f} Centigrade.'.format(f, c))
        tempFileOut.write('\n')
tempFileIn.close()
tempFileOut.close()  # python will close the file for you if you don't, but it is good practice to close it
