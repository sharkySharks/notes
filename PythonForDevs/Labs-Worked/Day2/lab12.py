# temps = open('../../LabsData/tmpprecip2012.dat')  # first data set to test
temps = open('../../LabsData/tmpprecip.dat')  # second data set to test
months = []  # list of all the temperatures for each month, based on index
report = []

for i in range(13):
    months.append([])  # setup all month values with 0 to start

for data in temps:
    try:
        temp = float(data[14:16])
        month = int(data[0:2])
    except ValueError:
        print 'Value error!'
    else:
        months[month].append(temp)  # get all the temps into the months list

for vals in months[1:]:
    month = months.index(vals)
    average = round(sum(vals)/len(vals), 1)
    high = max(vals)
    low = min(vals)
    print '{} {} {} {} \n'.format(month, average, high, low),
