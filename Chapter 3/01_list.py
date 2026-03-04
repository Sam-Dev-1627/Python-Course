# =====================================================
# LIST IN PYTHON
# A list is a collection of multiple values stored in
# a single variable.
# Lists are written using square brackets [].
# Lists are mutable (can be changed).
# =====================================================

friends = ["Sameer", "Abinash", "Sai Krishna", "1611", "278", "70707"]

# Accessing elements using index
# Index starts from 0
print(friends[0])   # Output: Sameer


# Lists are mutable (we can change values)
friends[0] = "Orange"   # Changing first element
print(friends[0])       # Output: Orange


# List Slicing
# Syntax: list[start:end]
# End index is excluded
print(friends[0:4])   # Prints elements from index 0 to 3


# Index position explanation:
# 0 → "Orange"
# 1 → "Abinash"
# 2 → "Sai Krishna"
# 3 → "1611"
# 4 → "278"
# 5 → "70707"