#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# has a percent difference less than 2%
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""
import math

t1 = float(input("Enter one side of a triangle: "))
t2 = float(input("Enter the second side: "))
t3 = float(input("Enter the third side: "))

hyp = float(max(t1, t2, t3))
c = math.pow(hyp, 2)

sum = math.pow(t1, 2)+math.pow(t2, 2)+math.pow(t3, 2) - c

if c == sum:
    print("This is a right triangle")

if c > sum:
    print("This is an obtuse triangle")

if c < sum:
    print("This is an acute triangle")