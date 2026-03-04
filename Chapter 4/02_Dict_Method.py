# =====================================================
# DICTIONARY METHODS IN PYTHON
# Dictionary stores data in key : value pairs.
# Dictionaries are mutable (can be changed).
# =====================================================

Marks = {
    "Sameer": 100,
    "Chirkut": 99,
    "Dibya": 77,
    0: "Abinash"
}

# items()
# Returns all key-value pairs as tuples
# print(Marks.items())

# keys()
# Returns all keys of the dictionary
# print(Marks.keys())

# values()
# Returns all values of the dictionary
# print(Marks.values())


# update()
# Updates existing key or adds new key-value pair
Marks.update({"Sam": 55, "Ash": 78})
print("After update:", Marks)

# Harry value changed from 100 to 55
# Ash added as new key


# get()
# Returns value of given key.
# If key does not exist, returns None (no error).
print("Using get():", Marks.get("Sameer2"))


# Accessing using square brackets []
# This will give error if key does not exist
# print(Marks["Sameer2"])   # KeyError