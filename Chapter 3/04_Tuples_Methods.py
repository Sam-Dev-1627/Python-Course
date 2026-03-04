# =====================================================
# TUPLE METHODS IN PYTHON
# Tuples are immutable (cannot be changed).
# They have limited methods compared to lists.
# Main methods: count() and index()
# =====================================================

Name_and_Number = (1, 45, 454, 6442, 7665, 6797, 75, 2, 4,
     "sameer", "ameer", "rohan",
     "Abinash", "Chirkut")

# Printing the tuple
print("Tuple:", Name_and_Number)


# count()
# Counts how many times a value appears in the tuple
no = Name_and_Number.count(45)
print("Count of 45:", no)


# index()
# Returns the index position of the first occurrence of value
i = Name_and_Number.index(6442)
print("Index of 6442:", i)


# len()
# Returns total number of elements in the tuple
print("Length of tuple:", len(Name_and_Number))