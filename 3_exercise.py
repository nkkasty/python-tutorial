str = "pynative"

#1
for i in range(len(str)):
    if i % 2 == 0:
        print(str[i])


#2
for i in range (0, len(str),2):
    print(str[i])