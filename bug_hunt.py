# Program: Bug Hunt
# Description: Calculates the sum of numbers from 1 to 5 with bug fixes documented.

count = 1
total = 0

# BUG: Missing colon (:) at the end of the while condition line caused a SyntaxError. Fixed by adding :.
# BUG: The condition 'count < 5' excluded 5 from the loop, causing an off-by-one logic error. Fixed by changing condition to 'count <= 5'.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Attempted to concatenate a string with an integer directly, causing a TypeError. Fixed by converting 'total' to str(total) or using an f-string.
print("Sum of 1 to 5 is: " + str(total))