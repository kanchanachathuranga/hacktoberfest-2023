#Sum of the Odd Numbers
value = int(input("please enter the value : "))
Oddtotal = 0

for num in range(1, value + 1):
    if (num % 2!=0):
        print("{0}".format(num))
        Oddtotal = Oddtotal + num
        
print("Sum of odd numbers from 1 to {0} = {1}".format(num, Oddtotal))