# lamda,map and filter
a = lambda c,d : c+d
square = lambda i:i*i
print(a(2,30))
print(square(9))

# Filter function without using lamda
def evenNumbers(n):
    return n%2==0

list1 = [1,2,3,57,4,66,9]
even = list(filter(evenNumbers,list1))
print(even)

# Filter function using lamda
list1 = [1,2,3,57,4,66,9]
even = list(filter(lambda list1: list1%2==0,list1))
print("Output of filter function\n")
print(even)

# Doing exactly same task using map function
list1 = [1,2,3,57,4,66,9]
even2 = list(map(lambda list1: list1%2==0,list1))
print("Output of map function\n")
print(even2)


# Example 1 using map function
list1 = [1,2,3,57,4,66,9]
even2 = list(map(lambda list1: list1*2,list1))
print("Output of map function\n")
print(even2)

# Example 2 using map function
#   You can give multiple iterable(here it is list) to map
#   Filter can use only 1 iterable

list1 = [1,2,3,57,4,66,9]
list2 = [10,20,30,570,40,66,90]
output = list(map(lambda list1,list2 : list1==list2,list1,list2))
print("Output is ",output)

#   Using map with defined function
def add(n):
    return n+2
list2 = [1,2,3,57,4,66,9]
listPlus2 = list(map(add,list2))
print("listPlus2=",listPlus2)


