# Assignment No 07

## Python Program Steps

#### This program allow the user to input their name and three favorite numbers.it then perform various tasks such as checking wether the numbers are even or calculating the square of each number, and summing them all.

## STEPS TO CREATE PYTHON PROGRAM:

### 1. Initialize the list and get the user name

- First empty list is created to store the numbers.
- Second the user is asked for their name

```python
number_list:list=[]
name:str=input("Whats your name? ")
```

### 2. Input Three Favorite Numbers

- Use a for loop to collect three numbers from the user.
- The input numbers are stored in number list by append().
- Print the list.

```python
for x in range (1, 4):
    fav:int=int(input(f"Your {x} favorite number: "))
 # Stored in list
    number_list.append(fav)
print(number_list)
```

### 3. Greet the User.

- A simple greeting message is displayed to the user.

```python
 msg:str=input(f"Hello, {name}! Lets explore numbers.")
```

### 4. Check if the Number is Even or Odd.

- By using for loop and an if else condition.
- num %2==0 is use to find even number.

```python
for num in number_list:
   if num %2==0:
       print(f"The number {num} is an even. ")
   else:
       print(f"The number {num} is odd. ")
```

### 5. Calculating the Square of Each Number.

- The square of each number is calculated by using {num},{num\*\*2} and displayed
- Here we use for loop to find square of each number.

```python
for num in number_list:
   print(f"The number {num} and its square is ({num},{num**2})")
```

### 6. Sum of Three Numbers.

- The sum of three number is calculated by using sum()
- Use int to displayed sum in integers.

```python
total=int(sum(number_list))
print(f"Amazing! The sum of your number is {total}.")
```

### 7. Prime Number check Loop.

- A for loop runs from 2 up to the total number (total)
- if the total is divisible by any number within this range, is_prime is set to False, as it would mean that the total is not prime number.

```python
is_prime=True
if total <= 1:
    is_prime = False
for x in range(2, total):
    if total % x==0:
        is_prime=False
```

- After checking, if is_prime remains True, the program will print that the total is a prime number.
- Otherwise , it will print the total is not prime number.

```python
if is_prime:
    print(f"{total} is a prime number.")
else:
    print(f"{total} is not a prime number.")
```

      <-------------------------------------------->
