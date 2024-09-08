'''
Welcome to my first python program as Task. I am sorry in advance if there any mistake I have did. I promise to correct any types of mistake & also learn and practice further to not do these mistake again. Thank you.
'''
# I will print a random String & Integer First
print("Welcome to my new project")
print(2231081028)

#I will now take two variable & I will print their data types
firstVar = "Hello, Whats up"
secondVar = 2024

print(type(firstVar))
print(type(secondVar))

#I will now print three numb and convert their data types
firstVar = str(2024)
secondVar = float(2024)
thirdVar = int(2024.9)

print(firstVar)
print(secondVar)
print(thirdVar)

#Print multiple variable at once & take one input for multiple variable
a, b, c = "Messi","Neymar","Suarez"
print(a)
print(b)
print(c)

a = b = c = "Deep"
print(a)
print(b)
print(c)

#Now time to print all the tree variable at once
print(a, b, c)

#To make a variable fixed we need to use the keyword "global"

#Well now print some less than or greater than numeric
if 8>2 : print("8 is greater")
if 8>2 : print("2 is smaller")

#Lets make a list for British India  
britishIndia = ["Bangladesh","India","Pakistan"]
x,y,z = britishIndia
print(x,y,z)
#Lets print India only
print(y)

#To declare multiline string varible:
a= """Hello, I am Cristiano Ronaldo. I have scored 900th goal of mine recently."""
print(a)

#To determine length of a variable:
print(len(a))

# Printing array in string
a = "I am Deep. I am the GOAT."
print(a[5])

#Slicing that string
print(a[:7])
print(a[2:5])
print(a[-7:-3])

#Search in a string (Bool)
txt = "I am the GOAT."
print("the" in txt)
print("Deep" in txt)

#Search using if
if "am" in txt : print("Yes, am is found")

#Replacing in string
a = "Deep"
print(a.replace("D",("P")))

#Converting uppercase, lowercase
print(a.upper())
print(a.lower())

#Variable merging is possible by using +. Its possible between string only.
a = "I am Deep"
b = "I am from Sherpur"
c = a+b
print(c)
#To add a space between or comma
c =    a + "," + b
print(c)

#If we need to merge with string and int then we need to follow F-string
a=2100
txt = f"Postal code of Sherpur is {a}"
print(txt)

#For float we need to declare this
dollarRate = 120.90
txt = f"Todays Dollar rate is {dollarRate:.2f}"
print(txt)

#Boolean
print(9+5 == 10)
print(5==5)
print(5>4)
print(5<4)

#Some Mathematical Operation
a = 100
b = 200
#Addition
c =a + b
print (c)
#Substraction
c =a - b
print (c)
#Multiple
c =a * b
print (c)
#Division
c =a/b
print (c)
#Modulas
c =a % b
print (c)

#Assignment & Comparison Operation
print(a+3)
print(b-3)
print(a==b)
print(a!=b)

#Logical Operation
print (a > 50 and b > a)
print (a>b or a<b)
print (a<b and a>b)

#Identity Operation
print (a is b)
print (a is not b)