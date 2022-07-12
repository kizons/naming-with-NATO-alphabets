# For loop

# numbers = [1, 2, 3]
# new_list = []
# for num in numbers:
#     plus_1 = num + 1
#     new_list.append(plus_1)
# print(new_list)

# List Comprehension

# new_list = [new item for item in list]

# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# print(new_list)

# Letter list

# name = "Kizito"
# letter_list = [letter for letter in name]

# Conditional list Comprehension

# new_list = [new_item for item in list if test]

# to find square

# squared_number = [n * n for num in numbers] OR
# squared_number = [n** for num in numbers]

# Get data from each files and convert string value without space:

# f1 = open("file1.txt")
# data_list1 = []
# for line in f1:
#   data_list1.append(int(line.strip('\n')))
#
# f2 = open("file2.txt")
# data_list2 = []
# for line in f2:
#   data_list2.append(int(line.strip('\n')))
#
#
# # compare those two lists if common value
#
# result = [x for x in data_list1 if x in data_list2]
# print(result)
#
# with open("file1.txt") as julius:
#   jul = julius.readlines()
#
# with open("file2.txt") as ryan:
#   rya = ryan.readlines()
#
#
# result = [int(n) for n in jul if n in rya]
# # Write your code above 👆

#
# print(result)

# Dictionary Comprehension
# Example
# names = {'Alfred', 'James', 'Peter', 'John'}
# students_scores = {new_key:new_value for item in names}
# import random
# students_scores = {student:random.randint(1, 100) for student in names}
# score = students_scores.count()
#


# Conditional Dictionary comprehension

#new_dict = {new_key:new_value for (key:value) in dict_items if test}

# Example
#passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}


# names = {'Alfred', 'James', 'Peter', 'John'}

'''You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.

Try Googling to find out how to convert a sentence into a list of words.

Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.'''

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

# result = {word:len(word) for word in sentence.split()}
#
# print(result)

'''You are going to use Dictionary Comprehension to create a dictionary called weather_f
that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.'''

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# 🚨 Don't change code above 👆
# weather_f = {new_key:new_value for (key, value) in dictionary.items()}

# weather_f = {day:temp_c*9/5 + 32 for (day, temp_c) in weather_c.items()}

# Write your code 👇 below:



# print(weather_f)

# student_dict = {"student": ["Angela", "Tom", "Harry"],
#                 "score": [60, 80, 78]
# }

# looping through dictionaries
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

import pandas

# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# loop through a dataframe
# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

# loop through rows of a dataframe
# for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    # print(row.student)
    # print(row.score)
    # if row.student == "Angela":
    #     print(row)

# {new_key:new_value for (index, row) in df.iterrows()}
# TODO_1: create a dictionary in this format
# {"A":"Alpha", "B":"Bravo"}

# TODO_2: Create a list of phonetic code words from a word that the user inputs

phonetic_alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(phonetic_alphabets)
phonetic_dict = {row.letter:row.code for (index, row) in phonetic_alphabets.iterrows()}
print(phonetic_dict)
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)