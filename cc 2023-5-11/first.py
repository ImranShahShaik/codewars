
# Write a function `greet` that returns "hello world!"
#PREP Parameters, Return i.e result needed, Examples 3, Pseudocode Steps & Write Code B/W
def greet(name=None):
    if name:
        print("Hello, " + name + "!")
    else:
        print("Hello, world!")
greet()