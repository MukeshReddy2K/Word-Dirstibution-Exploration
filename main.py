import glob
import os
import string
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize.casual import TweetTokenizer, casual_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from collections import Counter
from nltk.util import ngrams

import nltk
# nltk.download('punkt')
# nltk.download('stopwords')

import warnings
warnings.filterwarnings("ignore")


def tokenize_words(files):
    lst = []
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            words = word_tokenize(text)
            words = [word.lower() for word in words if word.isalnum()]
            lst.extend(words)
    return lst

def most_common_words(lst):
    word_counter = Counter()
    word_counter.update(lst)
    return word_counter

def most_common_bigrams(lst):
    bigram_counter = Counter()
    bi_grams = list(ngrams(lst, 2))
    bigram_counter.update(bi_grams)
    return bigram_counter

def stop_word_common_words(not_stop_words_list):
    word_counter = Counter()
    word_counter.update(not_stop_words_list)
    return word_counter

def stop_word_common_bigrams(not_stop_words_list):
    bigram_counter = Counter()
    bi_grams = list(ngrams(not_stop_words_list, 2))
    bigram_counter.update(bi_grams)
    return bigram_counter

corpus_dir = ['Corpus1','Corpus2']

corpus_files = []
for dir in corpus_dir:
    text_files = []
    for filename in os.listdir(str(os.getcwd())+'\\'+dir+'\\'):
        if filename.endswith('.txt'):
            file_path = os.path.join(dir, filename)
            text_files.append(file_path)
    corpus_files.append(text_files)

tokenized_words_corpus1 = tokenize_words(corpus_files[0])

tokenized_words_corpus2 = tokenize_words(corpus_files[1])

# Get the 30 most common words
top_30_words_corpus1 = most_common_words(tokenized_words_corpus1).most_common(30)

print("30 Most Common Words in Corpus 1:")
print(top_30_words_corpus1, end="\n\n")

# Get the 30 most common words
top_30_words_corpus2 = most_common_words(tokenized_words_corpus2).most_common(30)

print("30 Most Common Words in Corpus 2:")
print(top_30_words_corpus2, end="\n\n")

###### Bigrams

# Get the 30 most common words for ngram with n = 2
top_30_bigrams_corpus1 = most_common_bigrams(tokenized_words_corpus1).most_common(30)

# Print the 30 most common words for corpus1
print("30 Most Common bi-grams in Corpus 1:")
print(top_30_words_corpus1, end="\n\n")

# Get the 30 most common words for ngram with n = 2
top_30_bigrams_corpus2 = most_common_bigrams(tokenized_words_corpus2).most_common(30)

# Print the 30 most common words for corpus2
print("30 Most Common bi-grams in Corpus 2:")
print(top_30_bigrams_corpus2, end="\n\n")

stop_words = set(nltk.corpus.stopwords.words('english'))

not_stop_words_list1 = [word for word in tokenized_words_corpus1 if word not in stop_words]

not_stop_words_list2 = [word for word in tokenized_words_corpus2 if word not in stop_words]

# Get the 30 most common words
top_30_words_without_stopwords_corpus1 = stop_word_common_words(not_stop_words_list1).most_common(30)

# Print the 30 most common words without stopwords in corpus1
print("30 Most Common Words without stopwords in Corpus 1:")
print(top_30_words_without_stopwords_corpus1, end="\n\n")

# Get the 30 most common words
top_30_words_without_stopwords_corpus2 = stop_word_common_words(not_stop_words_list2).most_common(30)

# Print the 30 most common words without stopwords in corpus2
print("30 Most Common Words without stopwords in Corpus 2:")
print(top_30_words_without_stopwords_corpus2, end="\n\n")

######## Bigrams

# Get the 30 most common words
top_30_bigrams_without_stopwords_corpus1 = stop_word_common_words(not_stop_words_list1).most_common(30)

# Print the 30 most common words without stopwords in corpus1
print("30 Most Common bigrams without stopwords in Corpus 1:")
print(top_30_bigrams_without_stopwords_corpus1, end="\n\n")

# Get the 30 most common words
top_30_bigrams_without_stopwords_corpus2 = stop_word_common_words(not_stop_words_list2).most_common(30)

# Print the 30 most common words without stopwords in corpus2
print("30 Most Common bigrams without stopwords in Corpus 2:")
print(top_30_bigrams_without_stopwords_corpus2, end="\n\n")