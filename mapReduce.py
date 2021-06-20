from collections import Counter
from functools import reduce, partial
import multiprocessing as mp
import re
import sys
import time

import nltk
import numpy as np
from nltk.corpus import stopwords
from sklearn.datasets import fetch_20newsgroups


def timing(f):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = f(*args, **kwargs)
        et = time.time()
        print(et - st)
        return res
    return wrapper

def mapper(doc, stop_words):
    return Counter([word.lower() for word in re.findall(r'[A-Za-z]{3,}', doc) if word.lower() not in stop_words])

def reducer(count1, count2):
    return count1 + count2

@timing
def mapReduce(news_groups, mapper, reducer, num_cores):
    with mp.Pool(num_cores) as pool:
        mapped = pool.map(mapper, news_groups['data'])
        reduced = reduce(reducer, pool.map(partial(reduce, reducer), np.array_split(mapped, pool._processes)))
    return reduced

def main(num_cores):
    news_groups = fetch_20newsgroups(data_home='.', subset='all')
    # nltk.download('stopwords', '.')
    stop_words = stopwords.words('english', '.')
    res = mapReduce(news_groups, partial(mapper, stop_words=stop_words), reducer, num_cores)
    print(res.most_common(10))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Please specify the number of cores to use.")
    else:
        main(num_cores=int(sys.argv[1]))