# enter the user's name
number_list:list=[]
name:str=input("Whats your name? ")

# Three favorite number

for x in range (1, 4):
    fav:int=int(input(f"Your {x} favorite number: "))
 # Stored in list
    number_list.append(fav)
print(number_list)

# Write a messages

msg:str=input(f"Hello, {name}! Lets explore numbers.")

# Even or odd
for num in number_list:
    if num %2==0:
        print(f"The number {num} is an even. ")
    else:
        print(f"The number {num} is odd. ")

# number and its square
for num in number_list:
    print(f"The number {num} and its square is ({num},{num**2})")

# sum of three numbers  
total=int(sum(number_list))
print(f"Amazing! The sum of your number is {total}.")


# sum of number is prime or not

is_prime=True
if total <= 1:
    is_prime = False
for x in range(2, total):
    if total % x==0:
        is_prime=False 
if is_prime:
    print(f"{total} is a prime number.") 
else:
    print(f"{total} is not a prime number.")       

    
