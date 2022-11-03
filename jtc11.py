## The array of numbers are given as input
number=[int(i) for i in input("Enter the numbers into array ").split()]

## Sort the array
number.sort()
print("The sorted array is",number)

## an empty list to store resultant numbers     
new_array=[]

## continue loop till number array becomes empty

## pop last and first number from sorted array to new array

while number!=[]: 
    new_array.append(number.pop())
    if number!=[]: ## if list has odd number of values
        new_array.append(number.pop(0))
        
        
##resultant array

print("resultant array",new_array)