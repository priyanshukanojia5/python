# def greet(name , ending):
#     print("hello sir ," +name +ending)
# greet("prish " , "hello")


# n to binary
# n = 29
# binary = bin(n)[2:]
# octal = oct(n)[2:]
# hexa = hex(n)[2:]
# print("Binary:", binary[-2:])
# print("Octal:", octal[-2:])
# print("Hexadecimal:", hexa[-2:])

# reverse string
# s = "Python Programming"
# reverse = s[::-1]
# print("Reversed string:", reverse)

# #max min with out them
# numbers = [12, 45, 7, 89, 34]
# max= numbers[0]
# min=numbers[0]
# for n in numbers:
#     if n>max:
#         max=n
#     if n<min:
#         min=n
# print("maximum", max)
# print("minimum", min)

#even num inn tupple
# numbers=(10, 15, 22, 31, 40, 57)
# for n in numbers:
#     if n%2==0:
#        print(n)

#range 
# for i in range(5,16):
#     if i%3==0:
#        continue #skip the num
#     print(i)

#dictionary
# student={
#     "name":"priyanshu",
#     "roll no.":"24",
#     "class":"aiml",
# }
# for key in student:
#   print(key)
# for key, value in student.items():
#     print(key, value)
# for key in student:
#     print(student[key])

#abs() round() pow()
# a=4
# b=3
# absolute=abs(a-b) #Returns the absolute (positive) value of a number.
# round=round(a/b)
# power=pow(a,b)
# print("Absolute difference:", absolute)
# print("Rounded division:", round)
# print("Power:", power)

#multiple for 3 replace by div3
# numbers = [3, 7, 9, 12, 14, 18, 20, 21, 25, 30]
# for i in range(len(numbers)):
#     if numbers[i]%3==0:
#         numbers[i]="div3"
# print(numbers)

#f string 
# name="priyanshu"
# marks=44
# total=50
# avg= (marks/total)*100
# print(f"hello {name},you scored {marks} and your percent is {avg}%")

#sqr in range
# num=[]
# for i in range(2,21,2):
#     num.append(i**2)
# print(num)


#strinf dictionary count
string="programming"
frequency={}
for ch in string:
    if ch in frequency:
        frequency[ch]+=1
    else:
        frequency[ch]=1
print(frequency)

#recursion
# def factorial(n):
#     if n==0 or n==1:
#       return 1
#     else:
#        return n * factorial(n-1)
# a= int(input("enter the number"))
# b=factorial(a)
# print(b)

#find number

# numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# x= int (input("enter the number"))
# found= False
# for i in numbers:
#     if i==x:
#         found= True
#         break
# if found:
#     print("the number has been found")
# else:
#     print("not found")

#recurive cas and base case
#in this fucntion calls itself to solve a problem and it should have a base case so that it that condition meets 
# the function stop calling itself
# def print_list(numbers, index=0):
#     if index==len(numbers):
#         return
#     print(numbers[index])
#     print_list(numbers,index+1)
# numbers=[21,23,2,342,21,23,12]
# print_list(numbers)

#funtion 1 positional 2 keyword 3default 4 variable
