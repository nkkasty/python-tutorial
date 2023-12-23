str = "pynative"

#
str[2:6]
str[:5]
str[3:]

#1
for i in range(len(str)):
    if i % 2 == 0:
        print(str[i])


#2
for i in range (0, len(str),2):
    print(str[i])


#3 - slicing
for pismeno in str[::2]:
    print(pismeno)