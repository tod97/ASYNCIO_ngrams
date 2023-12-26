import os
import time

def textFromFile(filename):
   with open(os.path.join(os.path.dirname(__file__), 'DATA/'+filename), 'r', encoding='utf-8') as file:
      text = file.read()
      text = text.replace('\n', '')
      text = text.replace(' ', '')
      text = text.lower()
   return text

def get_ngrams(text, n):
   ngrams = {}
   for i in range(len(text) - n + 1):
      ngram = text[i:i+n]
      if ngram not in ngrams:
         ngrams[ngram] = 0
      ngrams[ngram] += 1
   return ngrams

text = textFromFile('mobydick.txt')

# SEQUENTIAL
start = time.time()
bigrams = get_ngrams(text, 2)
trigrams = get_ngrams(text, 3)
end = time.time()
elapsed = end - start
print(f'seq NGrams (n={len(text)}): {elapsed*1000} ms')
