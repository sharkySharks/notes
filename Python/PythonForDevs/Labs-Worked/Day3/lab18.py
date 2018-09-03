
centList = [(f, round(9.0/5.0*(f-32), 1)) for f in range(-40, 120, 10) if f != 50 and f != 0]
centSet = {(f, round(9.0/5.0*(f-32), 1)) for f in range(-40, 120, 10) if f != 50 and f != 0}
centDict = {f: round(9.0/5.0*(f-32), 1) for f in range(-40, 120, 10) if f != 50 and f != 0}

print centList,
print '\n ============================'
print centSet,
print '\n ============================'
print centDict,
