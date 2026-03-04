# =====================================================
# STRING FUNCTIONS (STRING METHODS)
# String methods are built-in functions used to
# perform operations on strings.
# =====================================================

name = "sameer"


# len() function
# Returns total number of characters in the string
print(len(name))   # Output: 6


# endswith()
# Checks if string ends with given value
# Returns True or False
print(name.endswith("eer"))   # True


# startswith()
# Checks if string starts with given value
# Returns True or False
print(name.startswith("sam"))  # True


# capitalize()
# Converts first letter to uppercase
print(name.capitalize())   # Sameer


# lower()
# Converts entire string to lowercase
print(name.lower())   # sameer


# upper()
# Converts entire string to uppercase
print(name.upper())   # SAMEER


# replace(old, new)
# Replaces all occurrences of old value with new value
print(name.replace("e", "b"))   # sambbr