import time
def PythoonDelaye(function):
    def Wrapper():
        time.sleep(2)
        function()
    return Wrapper

@PythoonDelaye
def printer():
    print("hello")

def Exit():
    print("bye")
#we can also pass another function like this too
decorFunction=PythoonDelaye(Exit)
#then we can call it like this
decorFunction()
