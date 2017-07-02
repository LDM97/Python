#Prints the numbers 1 - 100
#Multiples of three prints Fizz
#Multiples of five print Buzz
#If both, print FizzBuzz

for num in range(1,101):
    multiple_5 = num/5
    multiple_3 = num/3
    #.is_integer() checks if the float is a whole number
    if multiple_5.is_integer() == True and multiple_3.is_integer() == True:
        print ("Fizz Buzz")
    elif multiple_5.is_integer() == True:
        print("Buzz")
    elif multiple_3.is_integer() == True:
        print("Fizz")
    else:
        print (num)
input()
