# I will make a dictionary here
Programming_Dictionary={"Bug":"it a thing which stops the prohrame to be execute in a correct way",
                        "Function": "there are methods which can be called from anywhere in the program"}

# Dictionaries have  a pair of key and value every info have a have to be extracted
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={}
# I will just run a loop here and add some checks to convert marks into grades
for key in student_scores:
    if(student_scores[key]>90):
        student_grades[key]="Outstanding"
    elif(student_scores[key]>80 and student_scores[key]<=90):
        student_grades[key]="Exceeds Expectations"
    elif (student_scores[key] > 70 and student_scores[key] <= 80):
        student_grades[key] = "Acceptable"
    elif (student_scores[key] <= 70 ):
        student_grades[key] = "Fail"
    print(f"{key}: {student_grades[key]} ")

