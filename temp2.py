#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:10:03 2020

@author: farid
"""

import random
import re


#nltk.download('punkt')
from nltk.tokenize.toktok import ToktokTokenizer
toktok = ToktokTokenizer()
#text = """i'm the total market capitalization, of equity gonna backed, securities worldwide gonna rose the total market kek from $2.5 trillion in 1980 gonna to $68.65 trillion at the end of 2018.[1] """
n = 5

ngrams = {}
f = open('/home/farid/mb.txt','r')
text = f.read()
#tokens = nltk.word_tokenize(raw)
#text = nltk.Text(tokens)
text = re.sub(r"i'm", "i am", text)
text = re.sub(r"we're", "we are", text)
text = re.sub(r"that's", "that is", text)
text = re.sub(r"what's", "what is", text)
text = re.sub(r"where's", "where is", text)
text = re.sub(r"\'ll", " will", text)
text = re.sub(r"\'ve", " have", text)
text = re.sub(r"\'re", " are", text)
text = re.sub(r"\'d", " would", text)
text = re.sub(r"wouldn't", "would not", text)
text = re.sub(r"couldn't", "could not", text)
text = re.sub(r"shouldn't", "should not", text)
text = re.sub(r"won't", "will not", text)
text = re.sub(r"can't", "can not", text)

words = toktok.tokenize(text)

def f(word):
    if word == ',':
        return True
    else:
        return word.isalpha()
words=[word.lower() for word in words if f(word)]

for i in range(len(words)):
    if words[i] == ',':
        words[i - 1] = words[i-1] + words[i]
while ',' in words:
     words.remove(',')
#print(words)

#words = nltk.word_tokenize(text)

#words = toktok.tokenize(text)
#print(words)
for i in range(len(words)-n):
	gram = ' '.join(words[i:i+n])
	if gram not in ngrams.keys():
		ngrams[gram] = []
	ngrams[gram].append(words[i+n])

#currentGram = ' '.join(words[0:n])
#print(ngrams.keys())
beginning = list(filter(lambda x: x[0] != ',', ngrams.keys()))
currentGram = random.choice(list(beginning))
#currentGram = random.choice(list(ngrams.keys()))


#print(beginning)
result = currentGram
#print(result)
#print(currentGram)
#print(ngrams)
#print(list(ngrams.keys()))

for i in range(12-n):
    if currentGram not in ngrams.keys():
        break
    possibilities = ngrams[currentGram]
    #print(possibilities)
    nextItem = possibilities[random.randrange(len(possibilities))]
    #print(random.randrange(len(possibilities) + 1))
    result += ' '+nextItem
    rwords = toktok.tokenize(result)
    for i in range(len(rwords)):
        if rwords[i] == ',':
            rwords[i - 1] = rwords[i-1] + rwords[i]
    while ',' in rwords:
        rwords.remove(',')
    currentGram = ' '.join(rwords[len(rwords)-n:len(rwords)])
if result[-1] == ',':
    result = result[:-1]
result = result.split(' ')


result = ' '.join(result)
result = result+'.'
result = result.capitalize()

print(result)