import mymodule as mm
import datetime

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