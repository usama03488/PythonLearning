
Nested_Dictionary={
    "France":["paris","lillie","Dijon"],
    "Pakistan":{
        "Islamabad": ["Cheezious","Savaour food","Ranchers","Tehzeeb"],
        "Lahore":["Waqas Biryani","Jheela food","Jalal sons"]

    }

}
# we will do this if we have to get only one data from list of dictionary
list=Nested_Dictionary["France"]
##print(list[1])
print(Nested_Dictionary["France"][1])

#now if we have to get a piece of data nested in 2 dictionaries
#*******dic=Nested_Dictionary["Pakistan"]
#sec_list=dic["Islamabad"]
#print(sec_list[1])********
print(Nested_Dictionary["Pakistan"]["Lahore"][1])

