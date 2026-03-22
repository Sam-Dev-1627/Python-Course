# =====================================================
# MULTIPLE IF STATEMENTS IN PYTHON
# You can use several if or if-elif-else blocks independently.
# =====================================================

# Taking input from user
a = int(input("Enter your age:"))

# -----------------------------------------------------
# IF STATEMENT NO: 1
# Checking if age is even or odd
# -----------------------------------------------------
if a % 2 == 0:
    print("Age is even")
else:
    print("Age is odd")
# End of IF statement no: 1

# -----------------------------------------------------
# IF STATEMENT NO: 2
# Checking voting eligibility using if-elif-else ladder
# -----------------------------------------------------
if a >= 18:
    print("You are capable of voting")
    print("You can vote for Bjp, Bjd, Aam, Congress, etc.")
    print("Vote wisely!")

elif a < 0:
    print("Sorry, age cannot be negative. You cannot vote.")

elif a == 0:
    print("You entered 0, which is not a valid age.")

else:
    print("You are below 18, so you cannot vote")

# This always executes
print("End of Program")
# End of IF statement no: 2