#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_args` -- Arguing with the functions
=========================================

LAB_ARGS Learning Objective: Learn to modify, receive, and work with arguments to function.
::

 a. Create a function that accepts any number of positional arguments and
    keyword arguments and prints the argument values out to the screen.

 b. Create a function that takes in any number of positional arguments, turns
    those arguments into keyword arguments using "arg#" for the keyword names,
    and calls the print function you wrote in a.

 c. Write a validation function that takes in a variable number of positional
    arguments.  Validate that all the arguments passed in are integers and are
    greater than 0.  If the arguments validate, call the print function, if an
    argument doesn't validate raise a ValueError.

"""

print("a.")

def print_args(*args, **kwargs):
    print(args, kwargs)

print_args('a', {'b': 1}, ('c', 0))

print("b.")

def print_args_b(*args):
    kwargs = {}
    for i in args:
        kwargs[]
    print_args(kwargs)

print_args()
