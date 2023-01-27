#    Q. Write a python function to sum all the numbers in a list.

size = int(input('Enter your size of list : '))
list =[]
sum= 0
for i in range(size):
    element = int(input('Enter the elements  : '))
    list.append(element)
for j in list:
    sum=sum+j
print('Sum of the list is', sum)



# print(list)
