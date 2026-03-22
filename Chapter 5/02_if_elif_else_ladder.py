# =====================================================
# IF - ELIF - ELSE STATEMENT (LADDER)
# Used when there are multiple conditions to check.
# Python checks conditions from top to bottom.
# =====================================================

# Taking input from user
a = int(input("Enter your age: "))

# -----------------------------------------------------
# IF-ELIF-ELSE LADDER
# -----------------------------------------------------
if a >= 18:
    # Runs if age is 18 or above
    print("You are capable of voting")
    print("You can vote for Bjp, Bjd, Aam, Congress, etc.")
    print("Vote wisely!")

elif a < 0:
    # Runs if age is negative
    print("Sorry, age cannot be negative. You cannot vote.")

elif a == 0:
    # Runs if age is exactly 0
    print("You entered 0, which is not a valid age.")

else:
    # Runs if none of the above conditions are True
    print("You are below 18, so you cannot vote.")

# This always executes, outside the ladder
print("End of Program")