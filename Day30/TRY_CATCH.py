
# its a try catch example but it works different in python we have
#try -> in this we give command which can give errors
#Except -> Except come after try and it gives us a way to execute commands at the time of error
#else -> it is executed when we have no error
#finally -> it executes everytime no matter what the situation is
try:
    file= open("file.txt")
except FileNotFoundError as error_message :
    # we can also mention error type with except so it will only handle that type of error
    print(f"File not found {error_message} ")
except TypeError as message:
    print("this exception will handle type errors")
else:
    print("we excuted try code and there was no error")
finally:
    print("this part always run no matter what happens up there")
    file.close()

# we can raise our own exception ----
height=int(input("Enter height:"))

if(height>3):
    raise ValueError("Human height should be less then 3")
# this raise will throw our custom error