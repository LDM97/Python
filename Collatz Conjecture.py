#Collatz Conjecture
#Take a natural number
#If it is even then divide by 2 (n/2)
#If it is odd then times by 3 and add 1 (3n+1)
#See how many moves it takes to reach 1
#The number will always reach 1

print("The Collatz conjecture is a mathematical phenomenon.")
print("It states that if you take a whole number and repeat the process: ")
print("dividing the number by 2 if it is even")
print("and times the number by 3 and add 1 to it if it is odd.")
print("You will eventually reach the number 1.")

n = float(input("\nPlease enter a whole number to try it: "))
if n.is_integer() == False:
    while n.is_integer() == False:
        n = float(input("Please enter a whole number: "))
        if n.is_integer() == True:
            break

number_of_moves = 0
list_of_moves = []
list_of_moves.append(int(n))
if n != 1:
    while n != 1:
        even_check = n/2
        if even_check.is_integer() == True:
            n /= 2
            number_of_moves += 1
            list_of_moves.append(int(n))
        else:
            n = n * 3 + 1
            number_of_moves += 1
            list_of_moves.append(int(n))

        if n == 1:
            break

for item in list_of_moves:
    print(item)
print("\nIt took %s moves to reach 1" % (number_of_moves))
input()
