
with open('../../LabsData/tmpprecip2012.dat') as filein:
    days = 0;
    precip = 0;
    for line in filein:
        line = line[8:13]      # last two numbers are temperature
        try:
            line = float(line)
        except ValueError:
            continue
        else:
            if line > 0.0:
                days+=1
                precip+=line
    print 'days with precipitation: {}, total precipitation {}'.format(days, precip)
filein.close()
