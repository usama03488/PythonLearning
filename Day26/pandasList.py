import pandas
Student_dict= {
    "Name": ["Angela","Umain","zafran"],
    "Score":[434,454,765]
}
data=pandas.DataFrame(Student_dict)
print(data)

#just like list and dict comprehension we can also perform thi functionality in pandas
#there is is function iterrows() which help us in reading and extracting dataframe data
for(index,row) in data.iterrows():
    print(row.Name)
#print(row)
