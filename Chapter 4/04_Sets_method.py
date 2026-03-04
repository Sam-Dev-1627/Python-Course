# =====================================================
# SET METHODS IN PYTHON
# A set is an unordered collection of unique elements.
# Sets are mutable (can be modified).
# =====================================================

s = {2, 56, 87, 24, 5, 255, "sameer"}

# add()
# Adds a new element to the set
s.add(5.666)
print("After adding 5.666:", s)
print("Type of s:", type(s))


# remove()
# Removes the specified element.
# Gives error if element does not exist.
s.remove(2)
print("After removing 2:", s)


# discard()
# Removes element but does NOT give error if not found
s.discard(100)
print("After discarding 100:", s)


# pop()
# Removes and returns a random element (because set is unordered)
removed_value = s.pop()
print("Popped value:", removed_value)
print("After pop:", s)


# clear()
# Removes all elements from the set
# s.clear()
# print("After clear:", s)