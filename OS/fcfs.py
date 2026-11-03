# r=[53,42,14,12,78,176,48]
# h=54
# m=0
# for i in r:
#     m+=abs(h-1)
#     h=i
# print(m)

# #fcfs scheduling algorithm
# n = int(input("Enter number of processes: "))

# bt = []
# for i in range(n):
#     bt.append(int(input("Enter burst time: ")))

# time = 0
# tw = 0
# tt = 0

# print("\nP\tBT\tCT\tTAT\tWT")

# for i in range(n):
#     time += bt[i]
#     tat = time
#     wt = tat - bt[i]

#     tw += wt
#     tt += tat

#     print(i+1, "\t", bt[i], "\t", time, "\t", tat, "\t", wt)

# print("Average WT =", tw/n)
# print("Average TAT =", tt/n)

#sjf scheduling algorithm

# n = int(input("Enter number of processes: "))

# bt = []
# for i in range(n):
#     bt.append(int(input("Enter burst time: ")))

# bt.sort()

# time = 0
# tw = 0
# tt = 0

# print("\nP\tBT\tCT\tTAT\tWT")

# for i in range(n):
#     time += bt[i]
#     tat = time
#     wt = tat - bt[i]

#     tw += wt
#     tt += tat

#     print(i+1, "\t", bt[i], "\t", time, "\t", tat, "\t", wt)

# print("Average WT =", tw/n)
# print("Average TAT =", tt/n)

