# Day 1 - 30DaysOfPython Challenge

print(2 + 3)  # addition(+)
print(3 - 1)  # subtraction(-)
print(2 * 1)  # Multiplication(*)
print(3 / 2)  # division(/)
print(3 ** 2) # exponential(**)
print(3 % 2)  # modulus(%)
print(3 // 2) # Floor division Operator

# Checking Data Types
print(type(10))                   # Int
print(type(3.14))                 # Float
print(type(1 +3j))                # Complex Number
print(type("DANIAL"))             # String
print(type([1, 2, 3]))            # List    
print(type({'name':'DANIAL'} ))   # Dictionary
print(type({3.14, 9.81, 2.7}))    # Set
print(type((3.14, 9.81, 2.7)))    # Tuple

# Extra Notes
# explain about dictionary, tuple , list
# Sure thing! Let’s break down these three fundamental data structures in Python:
# Dictionary:
# Definition: A collection of key-value pairs. Each key is unique, and each key is associated with a value.
# Syntax: {key1: value1, key2: value2}
# Example: my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# Use Case: Ideal for situations where you need to quickly retrieve a value based on a unique key. Think of it like a real-world dictionary where you look up the definition (value) by the word (key).

# Tuple:
# Definition: An ordered, immutable collection of items. Once a tuple is created, its elements cannot be modified.
# Syntax: (item1, item2, item3)
# Example: my_tuple = (10, 20, 30)
# Use Case: Great for grouping related data together. Since they’re immutable, they can be used as keys in dictionaries or stored in sets.

# List:
# Definition: An ordered, mutable collection of items. You can add, remove, and modify elements.
# Syntax: [item1, item2, item3]
# Example: my_list = [1, 2, 3, 4, 5]
# Use Case: Perfect for ordered collections that need frequent updates. Think of it like a shopping list where you can add, remove, or change items.

# In summary:

# Use a dictionary for key-value pairs.
# Use a tuple for immutable, ordered data.
# Use a list for mutable, ordered collections.
