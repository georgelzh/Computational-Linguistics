#!Python3
# build_ngram_model.py
# It takes in an input file and outputs a file with the
# probabilities for each unigram, bigram, and trigram of
# the input text.
"""
You can run this program with following command:
./build_ngram_model.py <input_file> <output_file>
"""

import nltk
from math import log10
import sys


inFile = sys.argv[1]
outFile = sys.argv[2]

# write out the format of the result
result = "data\\\n"

words = []
clean_words = []

# open file
with open(inFile, "r", encoding='utf-8') as f:
    input_txt = f.read().lower().splitlines()

# add <s> and </s> for each sentence
for sentence in input_txt:
    sentence = "<s> " + sentence + " </s>"
    words.append(sentence)

for item in words:
    item = item.split()
    clean_words.append(item)

# make a dictionary of each character in the text
dic = {}
count_unigram = 0
unigram_result = "\\1-grams:\n"


for word in clean_words:
    for x in range(len(word)):
        count_unigram = count_unigram + 1
        if word[x] not in dic:
            dic[word[x]] = 1
        elif word[x] in dic:
            dic[word[x]] = dic[word[x]] + 1

print("uni dic")
# put all words from each list into only one list
final_clean_words = []
for word in clean_words:
    for x in range(len(word)):
        final_clean_words.append(word[x])

unigram_open = "ngram 1: type=" + str(len(dic)) + " token=" + str(count_unigram) + "\n"

print("uni dic done")

# 1-gram result
for x in dic:
        unigram_result = unigram_result + " " + str(dic[x] / count_unigram) +\
                         " " + str(log10(dic[x] / count_unigram)) + " " + x + "\n"

print("step 1")

# make bigrams from the the final_clean_words list
bigrams = []
bigrams_set = {}

bigrams = list(nltk.bigrams(final_clean_words))
bigrams_set = set(bigrams)

# count bigrams type with a dictionary
bigrams_dic = {}
bigrams_token_count = 0
bigrams_result = "\\2-grams:\n"

print("bi dic")
for x in bigrams:
    if x[0] == "</s>":
        continue
    bigrams_token_count = bigrams_token_count + 1
    if x not in bigrams_dic:
        if x not in bigrams_dic:
            bigrams_dic[x] = 1
        elif x in bigrams_dic:
            bigrams_dic[x] = bigrams_dic[x] + 1

bigrams_open = "ngram 2: type=" + str(len(bigrams_dic)) + " token=" +\
               str(bigrams_token_count) + "\n"

print("bi dic done")

# 2-gram result

for x in bigrams_dic:
    bigrams_result = bigrams_result + " " + str(bigrams_dic[x] / bigrams_token_count)\
                     + " " + str(log10(bigrams_dic[x] / bigrams_token_count)) +\
                     " " + str(x[0] + " " + x[1]) + "\n"

print("step 2")

# make trigram from the final clea_words list
trigrams = []
trigrams_set = {}

trigrams = list(nltk.trigrams(final_clean_words))
trigrams_set = set(trigrams)

# 3-gram count trigram with a dictionary
trigrams_dic = {}
trigrams_token_count = 0
trigrams_result = "\\3-grams:\n"

print("tri dic")

for x in trigrams:
    if x[0] == "</s>" or x[1] == "</s>":
        continue
    trigrams_token_count = trigrams_token_count + 1
    if x not in trigrams_dic:
        if x not in trigrams_dic:
            trigrams_dic[x] = 1
        elif x in trigrams_dic:
            trigrams_dic[x] = trigrams_dic[x] + 1

trigrams_open = "ngram 3: type=" + str(len(trigrams_dic)) + " token=" + \
                str(trigrams_token_count) + "\n"

print("tri dic done")

# 3-gram result

for x in trigrams_dic:
    trigrams_result = \
        trigrams_result + " " + str(trigrams_dic[x] / trigrams_token_count) + " " + \
        str(log10(trigrams_dic[x] / trigrams_token_count)) + " " +\
        str(x[0] + " " + x[1] + " " + x[2]) + "\n"
print("step 3")

# output
print("result")
result = result + unigram_open + bigrams_open + trigrams_open + \
         unigram_result + bigrams_result + trigrams_result


# write output
with open(outFile, "w", encoding='UTF-8') as o:
    output = o.write(result)



# reference
# How to print "\" ?  https://stackoverflow.com/questions/19095796/how-to-print-backslash-with-python
# Sadip helped with adding <s> into the text. List has a function append()
# Python Dictionary Loop get item: https://www.w3schools.com/python/showpython.asp?filename=demo_dictionary_loop
# Python Dictionary Loop get key: https://www.w3schools.com/python/showpython.asp?filename=demo_dictionary_loop2
# Justin helped me with the counting, we don't have to count (<s>,,</s>), or (<s>,,</s>, word)