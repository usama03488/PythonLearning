student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
import csv
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass
#-------------------------CHALLENGE-------------------------

data=pandas.read_csv("nato_phonetic_alphabet.csv")
Framedata=pandas.DataFrame(data)
Alpha_dict={row.letter:row.code for (index,row) in Framedata.iterrows()}
print(Alpha_dict)

user_input=input("Enter any word: ")
user_input=user_input.upper()
input_list=list(user_input)
output_list=[code for (key,code) in Alpha_dict.items() if key in input_list ]
#======OR=====
output_list_update=[Alpha_dict[letter] for letter in user_input]
print(output_list)
print(output_list_update)
# done i complete challenge of Nato words
# phonetic_code=[word for word in Alpha_dict.values() ]
# print(phonetic_code)







# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

