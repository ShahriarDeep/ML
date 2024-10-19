# Declaring Dictionary
thisdict = {
    "Name": "Deep",
    "Gender": "Male",
    "Birth": "2000"
}

print(thisdict)

# Determine Length
print(len(thisdict))

# Print Specific Value
print(thisdict["Name"])

# Accessing Dictionary with default value to avoid KeyError
x = thisdict.get("Year", "Key not found")
print(x)

# Access List of keys in Dictionary
y = thisdict.keys()
print(y)

# Add Keys in Dictionary
thisdict["Address"] = "Sherpur"

# Print updated dictionary keys
print(y)  # Automatically updated

# Print the values in the dictionary
z = thisdict.values()
print(z)

# Update a value, e.g., Address
thisdict["Address"] = "Dhaka"

# Print the updated values
print(z)  # Automatically updated

# Print keys, items together
a = thisdict.items()
print(a)

# Check if a value exists in the Dictionary
if "Name" in thisdict:
    print("Yes, Name is available")
else:
    print("No")

# Update a key:item pair
thisdict.update({"Address": "Uttara"})
print(thisdict)

# Add item in dictionary
thisdict["Weight"] = "63"
print(thisdict)

# Delete an item
thisdict.pop("Address")
print(thisdict)

# Copy dictionary
Info = thisdict.copy()
print(Info)

# Clear Dictionary
thisdict.clear()
print(thisdict)

# Nested Dictionary example
friends = {
    "friend1": {
        "Name": "Deep",
        "Birth": 2000
    },
    "friend2": {
        "Name": "Girl",
        "Year": 2001
    },
    "friend3": {
        "Name": "Boy",
        "Year": 2002
    }
}

# Access Specific name of a friend from the friends dictionary
print(friends["friend1"]["Name"])

# Loop through the nested dictionary
for x, obj in friends.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])

# If-else example
a = 2000
b = 1000
if a > b:
    print("a is greater")
elif a == b:
    print("a is equal to b")
else:
    print("b is greater")

# Short Hand if-else
print("A") if a > b else print("=") if a == b else print("B")

# While loop with continue statement
i = 1
while i < 8:
    i += 1
    if i == 3:
        continue
    print(i)

# For loop with range
for x in range(1, 4, 6):
    print(x)