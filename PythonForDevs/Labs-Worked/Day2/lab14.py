# if you give it arguments it does not expect, it will throw an error
# so, if you pass key word args to the function below it will throw an error


def f_to_c(*f):
    for i in f:
        if isinstance(i, int) or isinstance(i, float):
            print 'F: {}, C: {:.2f}'.format(i, 5.0/9.0*(i - 32))

f_to_c(72, -10.5, '2e', 111, 55)

print '========================'

test = [72, -10.5, '2e', 111, 55]

f_to_c(*test)  # example passing a list with * to a function
