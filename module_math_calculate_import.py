# Declaring module: mymodule.py

Bangladesh = {
    "Capital": "Dhaka",
    "Birth": 1971,
    "Continent": "Asia"
}

India = {
    "Capital": "Delhi",
    "Birth": 1947,
    "Continent": "Asia"
}

Pakistan = {
    "Capital": "Islamabad",
    "Birth": 1947,
    "Continent": "Asia"
}

# import mymodule at main.py

import mymodule as mm
import datetime
import math

a = mm.Bangladesh["Birth"]
print(a)  

b = mm.Pakistan["Capital"]
print(b)  

c = mm.India["Continent"]
print(c)  

# Print the current year
x = datetime.datetime.now()
print(x.year)

# Calculate and print the age of Bangladesh
a = x.year - mm.Bangladesh["Birth"]
print("The age of Bangladesh is:", a)

# Calculate and print the age of Pakistan
b = x.year - mm.Pakistan["Birth"]
print("The age of Pakistan is:", b)

# Calculate and print the age of India
c = x.year - mm.India["Birth"]
print("The age of India is:", c)

# Find the smallest number from the given series
x = min(20, 40, 60)
print("The smallest number from the given series is:", x)

# Find the largest number of the series
y = max(20, 10, 25)
print("The largest number from the given series is:", y)

# For x power of y
z = pow(x, y)
print("The result is:", z)

# Import the value of pi
pi = math.pi
print("The value of pi is:", pi)

# For the nearest high
s = math.ceil(5.4)
print(s)

# For the nearest low
r = math.floor(4.4)
print(r)

# Taking input from user
username = input("Enter your Username: ")
print("Username is: " + username)

password = input("Enter your Password: ")
print("Password is: " + password)