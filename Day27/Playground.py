def add(*args):
    sum=0
   # sum= [sum,]
    for i in args:
        sum +=i
    print(sum)
# dynamic function  challenge

add(12,23,45,56,23,10)
#this kwarg give us the ability to name every variable
#there are store in dictionary
def calculate(**kwargs):
    #this  get method give us none instead of error if there is no variable 
    print(kwargs.get("adds"))
    print(kwargs["add"]*kwargs["mutiply"])

calculate(add=3, mutiply=5)