# =====================================================
# DICTIONARY IN PYTHON
# A dictionary stores data in key : value pairs.
# It is written using curly brackets {}.
# Keys must be unique.
# Dictionaries are mutable (can be changed).
# =====================================================


# Empty Dictionary
Name = {}  
print("Empty dictionary:", Name)


# Dictionary storing marks
Marks = {
    "Sai Krishna": 100,
    "Sameer": 99,
    "Dibya": 77
}

# Accessing value using key
# Syntax: dictionary[key]
print("Marks of Sameer:", Marks["Sameer"])


# -----------------------------------------------------

# Hindi to English word dictionary
Words = {
    "billi": "cat",
    "gaye": "cow",
    "kauwa": "crow",
    "hati": "elephant"
}

# Taking input from user
Word = input("Enter the word which you want meaning: ")

# Printing meaning using dictionary
print("Meaning is:", Words[Word])