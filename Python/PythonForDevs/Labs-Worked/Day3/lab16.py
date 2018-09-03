import string
from operator import itemgetter


results = {}

with open('../../LabsData/alice_in_wonderland.dat') as wonderland:
    while True:
        l = wonderland.read(1).lower()

        if not l:  # end of file
            break
        elif l in string.punctuation or l in string.whitespace:
            continue
        else:
            if l in results:
                results[l] += 1
            else:
                results[l] = 1

wonderland.close()

report = results.items()
report.sort(key=itemgetter(1))

print 'Alice in Wonderland report: \n',

for items in report:
    print 'The character \'{}\' occurred this amount: {} \n'.format(items[0], items[1]),


#  also can write it this way:
#
#  for a, b in report:
#      print '{0:2s}{1:5d}'.format(a,b)
#
