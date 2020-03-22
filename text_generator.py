from .load_save import save_model, load_model
import random
import re
from nltk.tokenize.toktok import ToktokTokenizer
toktok = ToktokTokenizer()


class TextGenerator():

    def prepare_data(self, data_path=None):
        data_path = open(data_path, 'r')
        text = data_path.read()
        text = re.sub(r"i'm", "i am", text)
        text = re.sub(r"that's", "that is", text)
        text = re.sub(r"what's", "what is", text)
        text = re.sub(r"where's", "where is", text)
        text = re.sub(r"\'ll", " will", text)
        text = re.sub(r"\'ve", " have", text)
        text = re.sub(r"\'re", " are", text)
        text = re.sub(r"\'d", " would", text)
        text = re.sub(r"won't", "will not", text)
        text = re.sub(r"can't", "can not", text)
        words = toktok.tokenize(text)

        def excp(word):
            if word == ',':
                return True
            else:
                return word.isalpha()
        words = [word.lower() for word in words if excp(word)]
        for i in range(len(words)):
            if words[i] == ',':
               words[i - 1] = words[i-1] + words[i]
        while ',' in words:
            words.remove(',')
        return words

    def build_model(self, data, ngram_size=3, save_path='model.json'):
        self.ngram_size = ngram_size
        ngrams = {}
        for i in range(len(data)-ngram_size):
            gram = ' '.join(data[i:i+ngram_size])
            if gram not in ngrams.keys():
                ngrams[gram] = []
            ngrams[gram].append(data[i+ngram_size])
        save_model(save_path, ngrams)
        return ngrams

    def generate(self, length, model=None, saved_model_path="model.json"):
        model = load_model(saved_model_path)
        beginning = list(filter(lambda x: x[0] != ',', model.keys()))
        currentGram = random.choice(list(beginning))
        result = currentGram
        for i in range(length-self.ngram_size):
            if currentGram not in model.keys():
                break
            possibilities = model[currentGram]
            nextItem = possibilities[random.randrange(len(possibilities))]
            result += ' '+nextItem
            rwords = toktok.tokenize(result)
            for i in range(len(rwords)):
                if rwords[i] == ',':
                    rwords[i - 1] = rwords[i-1] + rwords[i]
            while ',' in rwords:
                rwords.remove(',')
            currentGram = ' '.join(rwords[len(rwords)-self.ngram_size:len(rwords)])
        result = result.split(' ')
        if result[-1] == ',':
            result = result[:-1]
        return result
