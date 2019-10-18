#!Python 3
# word_analogy - Project 5
# it calculates the similarity of different word and give the most similar word according to the given word by using
# Euclidean distance, manhattan distance and cosine similarity equation.
# Zhihong Li

"""
this program solves analogies such as 'dog is to cat as puppy is to ____'.
The program runs with the following command:

./word_analogy.py <vector_file> <input_directory> <output_directory> <eval_file>
<should_normalize> <similarity_type>
"""

import sys, os, numpy, shutil
from math import sqrt

inputVector = sys.argv[1]
googleTestSetFolder = sys.argv[2]
outPutFolder = sys.argv[3]
outPutFile = sys.argv[4]
shouldNormalize = int(sys.argv[5])
similarity_type = int(sys.argv[6])

dictionary = {}
with open(inputVector, "r", encoding='UTF-8') as v:
    lines = v.read().splitlines()

    # build the dictionary
for line in lines:
    dictionary[line.split()[0]] = line.split()[1:]


# convert the str to float
def convert_str_to_float(dic):
    for vv in dic.values():
        for i in range(len(vv)):
            vv[i] = float(vv[i])


# def get_mag(vector):
#     mag = 0
#     for value in vector:
#         mag = mag + value * value
#     mag = sqrt(mag)
#     return mag


def normalize(dic, should_normalize_type):
    if should_normalize_type == 1:
        for vector in dic.values():
            vector = vector / numpy.linalg.norm(vector)  # learnt from Stack over flow

            # # mag = get_mag(vector)
            # for value in vector:
            #     value = value / mag


def get_euclidean_distance(a, b, c):
    a = numpy.array(dictionary.get(a))
    b = numpy.array(dictionary.get(b))
    c = numpy.array(dictionary.get(c))
    final_array = c + b - a
    euclidean_distance = 99999
    most_similar_word = "none"
    # calculate euclidean distance between final_array and word in the dictionary
    for k, v in dictionary.items():
        temp = 0
        # calculate euclidean distance
        for i in range(len(v)):
            temp = temp + sqrt((final_array[i] - v[i]) ** 2)
        # compare and get the smaller euclidean distance, and the according word
        if euclidean_distance > temp:
            euclidean_distance = temp
            most_similar_word = k
    # return value
    return most_similar_word


def get_manhattan_distance(a, b, c):
    a = numpy.array(dictionary.get(a))
    b = numpy.array(dictionary.get(b))
    c = numpy.array(dictionary.get(c))
    final_array = c + b - a
    manhattan_distance = 99999
    most_similar_word = "none"
    for k, v in dictionary.items():
        vector = numpy.array(v)
        temp = numpy.sum(abs(final_array - vector))    # temporary variable to store manhattan distance
        if manhattan_distance > temp:
            manhattan_distance = temp
            most_similar_word = k
    # return value
    return most_similar_word


def get_cosine_distance(a, b, c):
    a = numpy.array(dictionary.get(a))
    b = numpy.array(dictionary.get(b))
    c = numpy.array(dictionary.get(c))
    final_array = c + b - a
    cosine_similarity = -9999
    most_similar_word = "none"
    for k, v in dictionary.items():
        vector = numpy.array(v)
        temp = final_array.dot(vector) / (sqrt(numpy.sum(final_array ** 2)) + sqrt(numpy.sum(vector ** 2)))
        if temp > cosine_similarity:
            cosine_similarity = temp
            most_similar_word = k
    return most_similar_word


def get_similar_word(file_path, similarity_calculate_method):
    with open(file_path, "r") as open_file:
        v = open_file.read().splitlines()
        correct_num = 0
        line_num = 0
        result = []
        for i in range(len(v)):
            v[i] = v[i].split()
            try:
                # loop the lines and calculate the similarity
                # check which similarity method we are using
                if similarity_calculate_method == 0:
                    similar_word = get_euclidean_distance(v[i][0], v[i][1], v[i][2])
                    result.append(v[i][0]+ " " + v[i][1] + " "+ v[i][2] + " " + similar_word + "\n")
                    line_num = line_num + 1
                    if similar_word == v[i][3]:
                        correct_num = correct_num + 1

                elif similarity_calculate_method == 1:
                    similar_word = get_manhattan_distance(v[i][0], v[i][1], v[i][2])
                    line_num = line_num + 1
                    result.append(v[i][0]+ " " + v[i][1] + " "+ v[i][2] + " " + similar_word + "\n")
                    if similar_word == v[i][3]:
                        correct_num = correct_num + 1

                elif similarity_calculate_method == 2:
                    similar_word = get_cosine_distance(v[i][0], v[i][1], v[i][2])
                    result.append(v[i][0]+ " " + v[i][1] + " "+ v[i][2] + " " + similar_word + "\n")
                    line_num = line_num + 1
                    if similar_word == v[i][3]:
                        correct_num = correct_num + 1

            except:
                print("Error list")

        # write out the result and Organize the output text
        with open(outPutFile, "a", encoding='UTF-8') as o:
            o.write(os.path.basename(file_path) + "\n" + "ACCURACY TOP1: " + str((correct_num / line_num) * 100) + "% " + "("
                    + str(correct_num) + "/" + str(line_num) + ")" + "\n")
        with open(outPutFolder + "\\" + os.path.basename(file_path), "w", encoding='UTF-8') as outputText:
            outputText.write(''.join(result))
        print(os.path.basename(file_path))
    # return an array correct number and total number.
    return [correct_num, line_num]


def open_files_in_directory(directory):
    # create a folder or delete old folder

    final_output_folder = os.path.abspath('.') + "\\" + outPutFolder
    if os.path.exists(final_output_folder):
        shutil.rmtree(final_output_folder)
    os.makedirs(final_output_folder)

    total_num = 0
    correct_num = 0
    for filename in os.listdir(directory):
        if filename.startswith('.'):
            continue
        if not filename.endswith('.txt'):
            continue
        file_path = os.path.join(directory, filename)
        temp = get_similar_word(file_path, similarity_type)
        correct_num = correct_num + temp[0]
        total_num = total_num + temp[1]
    with open(outPutFile, "a", encoding='UTF-8') as c:
        c.write("Total Accuracy: " + str(correct_num / total_num) + "%" + " (" + str(correct_num) + "/" + str(total_num) + ")")


convert_str_to_float(dictionary)
normalize(dictionary, shouldNormalize)
open_files_in_directory(googleTestSetFolder)


# Cedric helped me understand how to compare the similarity and get the similar word