# Exercise 5: Check if the first and last number of a list is the same

# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

# 3 types of arrays

# 1 - tuple - immutable (неизменяемый)
ovoce = ("apple", "banana")
ovoce[1] = "pear"

# 2 - list
ovoce = ["apple", "banana"]
ovoce[1] = "pear"
ovoce

# 3 - dictionary (ключ + значение)
znamky_studentu = {"Wilson": 1, "Winona": 3, "Wigfrid": 2}
znamky_studentu["Winona"]

znamky_studentu["Wigfrid"] = 1



lst_1 = [10, 20, 30, 40, 10]
lst_2 = [75, 65, 35, 75, 30]

lst_1[0] == lst_1[-1]

def check(lst):

    print(f"Your list: {lst}")
    print(f"Result is: {lst[0] == lst[-1]}")

check(lst_1)
check(lst_2)