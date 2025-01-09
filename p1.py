# Python program to determine whether the number is Armstrong number or not.
# This program checks if a given number is an Armstrong number by calculating the sum of 
# its digits raised to the power of the number of digits.

# Function to calculate x raised to the power y
def power(x, y):
    """Calculate x raised to the power of y."""
    if y == 0:
        return 1
    if y % 2 == 0:
        return power(x, y // 2) * power(x, y // 2)
    return x * power(x, y // 2) * power(x, y // 2)

# Function to calculate order of the number
def order(x):
    """Return the number of digits in the number x."""
    n = 0
    while x != 0:
        n = n + 1
        x = x // 10
    return n

# Function to check whether the given number is Armstrong number or not
def is_armstrong(x):
    """Check if the number x is an Armstrong number."""
    n = order(x)
    temp = x
    sum1 = 0
    while temp != 0:
        r = temp % 10
        sum1 = sum1 + power(r, n)
        temp = temp // 10

	# If condition satisfies
    return sum1 == x

# Driver code
A = 153
print(is_armstrong(A))

B = 1253
print(is_armstrong(B))
