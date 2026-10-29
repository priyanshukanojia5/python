#file handling
#file is any name with extention is called file and when u want to handle it it becomse file handling
# p=open('fileHandling.py') #here u have to write the file path 
# print(p.read())
#  ================
#  there are four mode to use it in open
# 1. 'r' mode
p= open("file.txt", 'w')
p= open("file.txt", 'a')
p.write(" hello file i have created u on 8 oct 2026 at 12.29 am ")
p.write("2. appending kya be")
p.close()