#program to count the number of even & odd numbers from series of numbers
x = input('Enter the series of number---->')
x .split (',')
even = 0
odd = 0
for i in x:
    if int(i) % 2 == 0:
        even=even+1
    else:
        odd=odd+1
print("Number of even numbers :", even) 
print("Number of odd numbers :", odd)      