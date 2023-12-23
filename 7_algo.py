a = 10 
while a > 1:
    b = 10
    while b > a:
        if a % 2 == 0:
            print ("A", end=" ")
        else:
            print ("B", end=" ")
        b = b - 1
    a = a - 1
print()