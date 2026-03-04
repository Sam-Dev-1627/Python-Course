# =====================================================
# LIST METHODS IN PYTHON
# List methods are built-in functions used to modify lists.
# =====================================================

friends = ["Sameer", "Abinash", "Chirkut", "1611", "278", "70707"]

print("Original friends list:", friends)


# append()
# Adds an element at the end of the list
friends.append("Chirkut")
print("After append:", friends)


# -----------------------------------------------------

list = [1, 3, 54, 3966, 25, 77, 35, 67, 32, 778, 245]

print("Original number list:", list)


# sort()
# Sorts the list in ascending order
# list.sort()
# print("After sort:", list)


# reverse()
# Reverses the list
# list.reverse()
# print("After reverse:", list)


# insert(index, value)
# Inserts value at specific index
# list.insert(3, 3333)
# print("After insert:", list)


# pop(index)
# Removes and returns element at given index
# print("Popped value:", list.pop(8))
# print("After pop:", list)


# remove(value)
# Removes the first occurrence of the given value
list.remove(3)
print("After remove 3:", list)