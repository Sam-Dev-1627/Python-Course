# =====================================================
# STRING IN PYTHON
# A string is a sequence of characters written inside quotes.
# Strings are immutable (cannot be changed after creation).
# =====================================================

name = "Sameer"   # name is a string


# =====================================================
# STRING SLICING
# Syntax: string[start : end]
# It starts from 'start' index and goes up to (but not including) 'end'.
# Indexing always starts from 0.
# =====================================================

nameshort = name[0:3]   # From index 0 to index 2 (3 is excluded)
print(nameshort)        # Output: Sam


# =====================================================
# STRING INDEXING
# Indexing is used to access a single character from string.
# =====================================================

character_1 = name[1]   # Character at index 1
print(character_1)      # Output: a


# =====================================================
# Index Position Explanation
#   S   a   m   e   e   r
#   0   1   2   3   4   5
# =====================================================