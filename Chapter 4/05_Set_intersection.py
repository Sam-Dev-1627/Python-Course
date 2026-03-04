# =====================================================
# COMPLETE SET METHODS & OPERATIONS IN PYTHON
# =====================================================

# Creating two sets
s1 = {5, 356, 45}
s2 = {5, 23, 67}

print("Set 1:", s1)
print("Set 2:", s2)


# -----------------------------------------------------
# UNION
# Combines all elements from both sets (no duplicates)
# -----------------------------------------------------
print("Union:", s1.union(s2))


# -----------------------------------------------------
# INTERSECTION
# Returns common elements from both sets
# -----------------------------------------------------
print("Intersection:", s1.intersection(s2))


# -----------------------------------------------------
# DIFFERENCE
# Elements present in first set but NOT in second set
# -----------------------------------------------------
print("Difference (s1 - s2):", s1.difference(s2))
print("Difference (s2 - s1):", s2.difference(s1))


# -----------------------------------------------------
# SYMMETRIC DIFFERENCE
# Elements present in either set but NOT in both
# -----------------------------------------------------
print("Symmetric Difference:", s1.symmetric_difference(s2))


# -----------------------------------------------------
# ADD
# Adds an element to the set
# -----------------------------------------------------
s1.add(100)
print("After adding 100 to s1:", s1)


# -----------------------------------------------------
# REMOVE
# Removes element (error if not present)
# -----------------------------------------------------
s1.remove(100)
print("After removing 100:", s1)


# -----------------------------------------------------
# DISCARD
# Removes element safely (no error if not found)
# -----------------------------------------------------
s1.discard(999)
print("After discarding 999:", s1)


# -----------------------------------------------------
# POP
# Removes a random element (because set is unordered)
# -----------------------------------------------------
removed_value = s1.pop()
print("Popped value:", removed_value)
print("After pop:", s1)


# -----------------------------------------------------
# SUBSET CHECK
# Checks if all elements of s1 are in s2
# -----------------------------------------------------
print("Is s1 subset of s2?", s1.issubset(s2))


# -----------------------------------------------------
# SUPERSET CHECK
# Checks if s1 contains all elements of s2
# -----------------------------------------------------
print("Is s1 superset of s2?", s1.issuperset(s2))


# -----------------------------------------------------
# LENGTH OF SET
# -----------------------------------------------------
print("Length of s1:", len(s1))