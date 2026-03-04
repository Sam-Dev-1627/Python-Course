# =====================================================
# SET IN PYTHON
# A set is a collection of unique elements.
# It does not allow duplicates.
# It is unordered and does not support indexing.
# =====================================================

numbers = {10, 20, 30, 10, 40, 20}

# Duplicate values (10 and 20) will be removed automatically
print("Numbers set:", numbers)


# Creating an empty set
empty_set = set()   # Correct way to create empty set
print("Empty set:", empty_set)


# Adding elements
numbers.add(50)
print("After adding 50:", numbers)


# Removing elements
numbers.remove(20)   # Removes 20 (error if not found)
print("After removing 20:", numbers)


# discard() removes element but does NOT give error if not found
numbers.discard(100)
print("After discard 100:", numbers)


# Checking membership
print("Is 30 present?", 30 in numbers)


# Length of set
print("Length of set:", len(numbers))


# Checking type
print("Type of numbers:", type(numbers))