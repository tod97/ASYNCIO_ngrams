import os
import time

import asyncio
from asyncio.events import AbstractEventLoop
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from typing import List

threads = [1, 2, 4, 6, 8, 16, 32]

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

async def get_ngrams_parallel(text, n, nThreads):
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
   text = text + text + text

   for i in range(3):
      text = text + text

      # SEQUENTIAL
      start = time.time()
      bigrams = get_ngrams(text, 2)
      trigrams = get_ngrams(text, 3)
      end = time.time()
      seqElapsed = end - start
      print(f'--------- SIZE = {len(text)} ---------')
      print(f'seq NGrams: {int(seqElapsed*1000)} ms')
      print('------------------')

      speedups = []
      # PARALLEL
      for nThreads in threads:
         start = time.time()
         bigrams = await get_ngrams_parallel(text, 2, nThreads)
         trigrams = await get_ngrams_parallel(text, 3, nThreads)
         end = time.time()
         elapsed = end - start
         print(f'par NGrams (t={nThreads}): {int(elapsed*1000)} ms')
         print(f'Speedup: {round(seqElapsed/elapsed, 3)}x')
         print('------------------')
         speedups.append(round(seqElapsed/elapsed, 3))

      print(f'Speedups: {speedups}, Size: {len(text)} chars ~ {len(text)/1000000} MB')

if __name__ == '__main__':
   asyncio.run(main())