#with open("weather_data.csv") as data_file:
   # data_content=data_file.readlines()

import csv
import pandas

# with open("weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     temp = []
#     for row in data:
#         if(row[1]!="temp"):
#             temp.append(int(row[1]))
#
#     print(temp)
        # challenge extract temp from this list in a diff list
data= pandas.read_csv("weather_data.csv")
# data_dic=data.to_dict()
# print(data_dic)
#  list=data["temp"].to_list()
# average=sum(data["temp"]/len(list))
# # if we go withpanda library we can find average by using mean function
# print((data["temp"].max())).


# this will give us entire row
# print(data[data.temp== data.temp.max()])
# monday=data[data.day=="Monday"]
# Fahrenheit = (monday.temp * 9/5) + 32
# print(f"Temp in Fahrenheit {Fahrenheit}")



#create dataframe from scratch
# data_dict={
#     "Students":["Amy","Angela","Usama"],
#     "Scores":[57,75,80]
# }
# data=pandas.DataFrame(data_dict)
# data.to_csv("Mark_Sheet.csv")
# print(data)
#challenge to read sqirel file and make new file in which we display
data=pandas.read_csv("SquirlData.csv")
#this is a series method of value_counts which count with request to colors of squiells which we needed but it is from chat gpt
#fur_color_counts = data["Primary Fur Color"].value_counts()
black_Squirrels_count= len(data[data["Primary Fur Color"]=="Black"])
Red_Squirrels_count= len(data[data["Primary Fur Color"]=="Cinnamon"])
Grey_Squirrels_count= len(data[data["Primary Fur Color"]=="Gray"])
# print(Red_Squirrels_count)
# print(Grey_Squirrels_count)
# print(black_Squirrels_count)
Squiles_dict={
    "Color":["Black","Gray","Cinnamon"],
    "Sum":[black_Squirrels_count,Grey_Squirrels_count,Red_Squirrels_count]
}
new_file=pandas.DataFrame(Squiles_dict)
new_file.to_csv("Squirrels_Numbers.csv")
print(new_file)
# Get total number of squirrels with a recorded fur color
# total_squirrels = data["Primary Fur Color"].notna().sum()
# print(f"total sum is: {total_squirrels} ")
# print(f"types are {fur_color_counts}")