list =[3,4,29,8]
list.append(9) #add one value at the end 
print(f"appending the value at end {list}") 
list.sort(reverse=True) #arrange in ascending order
print(f"sorted{list}")
list.reverse() #rever the list
print(f"reversed {list}")
list.insert(2,7) #insrt the value at particularf index
print(f"inserting the value at particular index 2 {list}")
list.remove(3)#remove the particular value 
print(list)
list.pop(3) #it will remove the value from particular index
print(f"remove the value from index 3 {list}")