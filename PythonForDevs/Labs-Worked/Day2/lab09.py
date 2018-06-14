# see /LabsDone/lab09_letters.py for another solution, possibly more performant

with open('../../LabsData/alice_in_wonderland.dat') as wonderland:
    letters = 0
    ez = 0
    for line in wonderland:
        nline = line.lower().replace(' ', '')  # make lowercase and remove whitespace
        line = ''.join(e for e in nline if e.isalnum())  # remove special characters
        ez += line.count('e')
        letters += len(line)
    percentage = float(ez)/float(letters)
print 'Percentage of e\'s in Alice in Wonderland is {:.1%}'.format(percentage)
wonderland.close()
