#set is unorder and it shud be unique and mutable  

#but the elment present in set are immutable {{{hashable = immutable}}}

set_1 = {2,4,2,4,"prish", "ka","cricket"}
set_1.pop()
print(set_1)
print(type(set_1))
empty = set() # empty set shud be form like this syntax
print(type(empty))

#adding and removing element in set
empty.add(1)
empty.add(4)
empty.add(1)
empty.remove(1)
empty.clear()   #it will clear the set means make the set empty again
print(len(empty))

#union and intersection of set 
#in union it combine the set but not repeat the same element 
#in intersection it will give only common element present in set

set_2={12,31,43,23}
set_3={12,34,42,23}
print(set_2.union(set_3))
print(set_2.intersection(set_3))
#we can print both set separately without a change
print(set_2)
print(set_3)
