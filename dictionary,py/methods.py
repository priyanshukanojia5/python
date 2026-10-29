dict={
    "name":"priyanshu",
    "class" : "aimlB",
    "college":"nocomment",
    "age":"19 old"
}
#dict.keys will return all the keys
print(dict.keys())
print(list(dict.keys()))
print(len(list(dict.keys())))

#dict.values will return all the values
print(dict.values())
print(list(dict.values()))


#dict.items will return all the keys and value as tuple
print(dict.items())
pairs=(list(dict.items())) 
print(pairs[2])

#dict.gets will return all the key according to value
print(dict.get("age"))

#dict.update will add new key and value in  dictnary
dict.update({"hope":"future",})
print(dict)