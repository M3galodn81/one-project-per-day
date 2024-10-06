# Task
# The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .

# The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

# 0
# 1
# 4
# Input Format

# The first and only line contains the integer, .

# Constraints
# 1 <= n <= 20
n = 5

if __name__ == '__main__':
    [print(x**2) for x in range(0,int(input()))]