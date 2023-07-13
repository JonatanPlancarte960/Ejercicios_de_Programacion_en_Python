# *args y **kwargs

print("---------- *args ----------")
def function(argument, *arguments):
    print("First argument:", argument)
    
    n = 1
    for arg in arguments:
        print("Secondary argument", n, ":", arg)
        n = n + 1

function("python", "java", "php", "javascript", "html", "css", "c++", "c#")

print("---------- **kwargs ----------")

def say_hello(**kwargs):
    print("Hello")

    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

say_hello(name = "Jonatan", telephone = "XXXXXXXXXX")

print("--------------------", end="\n\n")

def function_2(name, *args, **kwargs):
    print("Owner:", name)
    print("--- Properties ---")

    for arg in args:
        print(arg)
    print("--- Contact ---")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

function_2("Jonatan", "Mexico", "Cloud", telephone = "XXXXXXXXXX", email = "example@example.com", age = 19)