# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

# Input Format
# A single line containing a positive integer

# Constraints
# 1 <= n <= 100

if __name__ == '__main__':
    print("Weird" if (n:=int(input().strip())) or (n in range(6,21)) else "Not Weird" )
    
# n = 
# if n % 2 == 1:
#         print("Weird")
# else:
#     if (n in range(2, 6)) or (n > 20):
#         print("Not Weird")
#     else: #6 to 20
#         print("Weird")
