# parameter and argument
#there are three types of argument
# 1.positional argument
def sum(a,b):
    print(f"the sum of two number is {a+b}")

sum(3,5)
# parameter is accepted and argument is given 

#2. default argument
def greeting(name, age):
    print(f"hello my dear {name} i know ur age is{age}")
greeting(age=20,name="priyanshu")
#  this method is also called keyword argument like in greeting name and age is keyword

# question
#1. pallindrome or not

def pallindrome(a):
    rev=""
    for i in range(len(a)-1,-1,-1):
        rev=rev+a[i]

    if rev==a:
        print(f"the given word {a}is pallindrome")
    else:
        print(f"the given word {a} is not pallindrome")
pallindrome("priyanshu")
pallindrome("naman")
