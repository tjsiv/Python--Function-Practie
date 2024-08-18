# Write the Following Functions
# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
print(max_num(25, 38, 17)) #expects 38

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(*a):
    product = 1
    for i in a:
        product *= i
    return product

print(mult_list(2, 3, 4, 5)) #expects 120

# Write a Python function called rev_string() to reverse a string.
def rev_string(a):
    return a[::-1]

print(rev_string("Hello, World!")) #expects "!dlroW,olleH"

# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(a, range):
    return a >= range[0] and a <= range[1]

print(num_within(3, (2, 4))) # expects True

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure Each number is the two numbers above it added together.

def pascal( n):
    res = [[1]]
    
    for i in range(n - 1):
        hold = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            row.append(hold[j] + hold[j + 1])
        res.append(row)
    return res;

print(pascal(5)) # expects the following output:
'''
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
'''

