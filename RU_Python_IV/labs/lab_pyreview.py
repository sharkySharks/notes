#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

:mod:`lab_pyreview` -- Python review
=========================================

LAB PyReview Learning Objective: Review the topics from the previous courses

a. Load the data from the two dictionary files in the data directory into two
   list objects.  data/dictionary1.txt data/dictionary2.txt
   Print the number of entries in each list of words.

b. Use sets in Python to merge the two lists of words with no duplications (union).
   Print the number of words in the combined list.

c. Import the random library and use one of the functions to print out five random
   words from the combined list of words.

d. Use a list comprehension to find all the words that start with the letter 'a'.
   Print the number of words that begin with the letter 'a'.

e. Create a function called wordcount() with a yield that takes the list of
   all words as an argument and yields a tuple of
   (letter, number_of_words_starting_with_that_letter) with each iteration.

"""
import random
import string

print("a.")
all_text_1 = [line.strip() for line in open('../data/dictionary1.txt', "r")]
print(('# of lines in first: {}'.format(len(all_text_1))))

all_text_2 = [line.strip() for line in open('../data/dictionary2.txt', "r")]
print(('# of lines in second: {}'.format(len(all_text_2))))

print("b.")
combined = set(all_text_1).union(set(all_text_2))
print(len(combined))

print("c.")
print(random.sample(combined, 5))

print("d.")
a_count = 0
for word in combined:
    if word[0] == "a" or word[0] == "A":
        a_count+=1
print(a_count)

print("d. - alternative")
awords = [w for w in combined if w.startswith('a')]; # filter with list comprehension
print(len(awords));

print("e.")

def wordcount(wordlist):
    for letter in string.ascii_lowercase:
        words = [w for w in wordlist if w.startswith(letter)]
        yield (letter, len(words))

for wc in wordcount(combined):
    print(("# of words with {}: {}".format(wc[0], wc[1])))
