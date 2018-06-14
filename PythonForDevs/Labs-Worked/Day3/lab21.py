def gen(start, stop):

    for x in xrange(start, stop):
        if x % 2 == 0:
            result = x
        else:
            result = 'odd'
        yield result


for y in gen(4,7):
    print y
print 'Generator Finished.'

next_gen = gen(4, 7)  #  this one you run manually in the python shell
while True:           #  can this even run on its own??
    try:
        print next_gen.next()
    except StopIteration:
        print 'Generator Finished.'
        break
