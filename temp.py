# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import re


#nltk.download('punkt')
from nltk.tokenize.toktok import ToktokTokenizer
toktok = ToktokTokenizer()
text = """i'm the total market capitalization, of equity gonna backed securities worldwide gonna rose the total market kek from $2.5 trillion in 1980 gonna to $68.65 trillion at the end of 2018.[1] """
n = 3

ngrams = {}
#f = open('/home/farid/hse-programming-intro/hw1_text_generator/text.txt','r')
#raw = f.read()
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

#
#text = re.sub(r"he's", "he is", text)
#text = re.sub(r"she's", "she is", text)
#text = re.sub(r"that's", "that is", text)
#text = re.sub(r"what's", "what is", text)
#text = re.sub(r"where's", "where is", text)
#text = re.sub(r"\'ll", " will", text)
#text = re.sub(r"\'ve", " have", text)
#text = re.sub(r"\'re", " are", text)
#text = re.sub(r"\'d", " would", text)
#text = re.sub(r"won't", "will not", text)
#text = re.sub(r"can't", "can not", text)
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
#beginning = filter(lambda x: x[0] != ',', ngrams.keys())
#currentGram = random.choice(list(beginning))
currentGram = random.choice(list(ngrams.keys()))

#print(list(ngrams.keys()))
#print(beginning)
result = currentGram
#print(result)
#print(currentGram)
#print(ngrams)

for i in range(11-n):
    if currentGram not in  ngrams.keys():
        break
    possibilities = ngrams[currentGram]
    nextItem = possibilities[random.randrange(len(possibilities))]
    #print(random.randrange(len(possibilities) + 1))
    result += ' '+nextItem
    rwords = toktok.tokenize(result)
    currentGram = ' '.join(rwords[len(rwords)-n:len(rwords)])
result = result.split(' ')

for i in range(len(result)):
    if result[i] == ',':
        result[i - 1] = result[i-1] + result[i]
while ',' in result:
     result.remove(',')
#result = result+'.'
#result = result.capitalize()

print(result)

