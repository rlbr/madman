# /usr/bin/env python
from __future__ import print_function


import fileinput
import nltk.data
import madman

brain = "twain"

text = ""

# Memory is cheap. Get all the text.
for line in fileinput.input():
    text += line

sent_detector = nltk.data.load("tokenizers/punkt/english.pickle")

sentences = sent_detector.tokenize(text)

m = madman.Madman(brain)

for sent in sentences:
    print(m.madlib(sent))
