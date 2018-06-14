# if you give it arguments it does not expect, it will throw an error
# so, if you pass key word args to the function below it will throw an error

from sys import argv


def f_to_c(*f):
    for i in f:
        if isinstance(i, int) or isinstance(i, float):
            print 'F: {}, C: {:.2f}'.format(i, 5.0/9.0*(i - 32))

for x in argv[1:]:  # the first argument is the filename when you run it, ie `python lab15.py x y z`
    x = float(x)    # so you need to start at the second argument, thus the `argv[1:]`
    f_to_c(x)
