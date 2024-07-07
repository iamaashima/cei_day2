#Create a program that takes user input to add multiple elements to an array, then prints the final array.
n=int(input("Enter the number of elements you want"))
array=[]
for i in range(0,n):
    n=int(input("Enter the element"))
    array.append(n)
print(array)
