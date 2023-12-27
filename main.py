import os
import time

import asyncio
from asyncio.events import AbstractEventLoop
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from typing import List

nThreads = 4

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

def get_ngrams_interval(text, n, i_from, i_to):
   ngrams = {}
   for i in range(i_from, i_to - n + 1):
      ngram = text[i:i+n]
      if ngram not in ngrams:
         ngrams[ngram] = 0
      ngrams[ngram] += 1
   return ngrams

async def get_ngrams_parallel(text, n):
   with ProcessPoolExecutor() as process_pool:
      loop: AbstractEventLoop = asyncio.get_event_loop()
      chunks = [0] + [int(len(text)/nThreads) * i for i in range(1, nThreads)] + [len(text)]
      calls: List[partial[int]] = [partial(get_ngrams_interval, text, n, chunks[i], chunks[i+1]) for i in range(nThreads)]
      call_coros = []
      for call in calls:
         call_coros.append(loop.run_in_executor(process_pool, call))
      results = await asyncio.gather(*call_coros)

      n_grams = {}
      for result in results:
         for key in result:
            if key not in n_grams:
               n_grams[key] = 0
            n_grams[key] += result[key]  

      return n_grams


async def main():
   text = textFromFile('mobydick.txt')
   text = text + text + text + text

   # SEQUENTIAL
   start = time.time()
   bigrams = get_ngrams(text, 2)
   trigrams = get_ngrams(text, 3)
   end = time.time()
   elapsed = end - start
   print(f'seq NGrams (n={len(text)}): {elapsed*1000} ms')
   print('------------------')

   # PARALLEL
   start = time.time()
   bigrams = await get_ngrams_parallel(text, 2)
   trigrams = await get_ngrams_parallel(text, 3)
   end = time.time()
   elapsed = end - start
   print(f'par NGrams (n={len(text)}, nThreads={nThreads}): {elapsed*1000} ms')
   print('------------------')

if __name__ == '__main__':
   asyncio.run(main())