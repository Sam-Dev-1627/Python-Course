# =====================================================
# CONDITIONAL STATEMENTS IN PYTHON
# Used to perform different actions based on conditions.
# The main types: if, else, elif
# =====================================================

# Taking input from user
a = int(input("Enter your age: "))

# -----------------------------------------------------
# IF-ELSE STATEMENT
# Executes one block if condition is True, otherwise executes else block
# -----------------------------------------------------
if a >= 18:
    print("You are capable of voting")
    print("You can vote for Bjp, Bjd, Aam, Congress, etc.")
    print("Vote wisely!")
else:
    print("You are not capable of voting")
    print("Wait until you turn 18!")

# This will always execute, outside if-else
print("End of program")