# Curzon Numbers : Challenge from https://edabit.com/challenge/HYjQKDXFfeppcWmLX

print(f'{((num := int(input('Enter a number to check if it is a curzon number: '))))} is { (text :='not' * (((2**num)+1)%((2*num)+1)!=0))}a curzon number since {((2**num)+1)} is{str(text)} a multiple of {(2*num)+1}')

# is_curzon(5) ➞ True
# # 2 ** 5 + 1 = 33
# # 2 * 5 + 1 = 11
# # 33 is a multiple of 11

# is_curzon(10) ➞ False
# # 2 ** 10 + 1 = 1025
# # 2 * 10 + 1 = 21
# # 1025 is not a multiple of 21

# is_curzon(14) ➞ True
# # 2 ** 14 + 1 = 16385
# # 2 * 14 + 1 = 29
# # 16385 is a multiple of 29