#zadani 1
def FA(x):
     if x>2:
        return 7
     else: 
        return x-FA(x+1)
        
    
FA(-2)   


#zadani 2
result = []

def FA():
    a = input ("Zadej hodnotu: ")

    if a == ".":
       pass
    else:
        FA()
        FA() 
    result.append(a)

FA()

result


#zadani 3
result1 = []

def FB():
    b = input("Zadej b: ")
    if b == "*":
        FA()
    else:
        FB()
    b = input("Zadej b: ")
    result1.append(b)

def FA():
    a = input("Zadej a: ")

    if a == "*":
        result1.append(a)
    else:
        if a == "+":
            FB()
            a = input("Zadej a: ")
            result1.append(a)
        else:
            FA()
            result1.append(a)

result1

FA()