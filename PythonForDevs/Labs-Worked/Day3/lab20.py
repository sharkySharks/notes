ol = range(2, 18, 3)
print ol

# filter
print filter(lambda x: x % 2 == 0, ol)

# map
print map(lambda x: x**2, ol)

# reduce
print reduce(lambda x, y: x+y, ol)
