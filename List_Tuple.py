# Creating List
fruitList = ["Apple", "Orange", "Mango"]

# Print the entire List
print(fruitList)

# Determine the length of the list
print(len(fruitList))

# Print specific elements of the list
print(fruitList[1:3])

# Use 'if' in list
if "Orange" in fruitList:
    print('Yes, "Orange" has been found in the list')

# Replacing Elements of List
fruitList[1] = "Lichee"

# Printing after replacing
print(fruitList)

# Insert a Element to List (Specific Position)
fruitList.insert(2, "Banana")

# Printing after inserting
print(fruitList)

# Insert a Element to end of list
fruitList.append("Orange")

# Printing after inserting
print(fruitList)

# Combine two list
extension = ["Pineapple", "Cherry"]
fruitList.extend(extension)

# Printing after extension
print(fruitList)

# Determine the length again
print(len(fruitList))

# Remove a Element from of list
fruitList.remove("Lichee")

# Printing after remove
print(fruitList)

# Ascending list (For numeric it will numeric order, for Alphabet it will alphabetical order)
fruitList.sort()

# Printing after Ascending
print(fruitList)

# Descending list (For numeric it will numeric order, for Alphabet it will alphabetical order)
fruitList.sort(reverse=True)

# Printing after descending
print(fruitList)

# Copy List to another List
myFruitList = list(fruitList)
# Print after copy
print(myFruitList)


# Tuple
myTuple = ("Dhaka", "Sherpur", " Dhaka", "Mymensingh")
# Print & Length of tupple
print(myTuple)
print(len(myTuple))

# Accessing specific elements
print(myTuple[1])

# Slicing in tuple
print(myTuple[1:3])

# Unpack
(Capital, City, *Town) = myTuple

print(Capital)
print(City)
print(Town)

# Some topic may missing here. I am watching video for these.
