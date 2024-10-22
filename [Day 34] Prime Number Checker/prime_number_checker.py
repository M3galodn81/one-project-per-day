import math

def is_prime(num):
    if num <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if (num % i == 0):
                return False
    return True
    

def main():
    print(is_prime(1))
    print(is_prime(10))
    print(is_prime(7))
    print(is_prime(17))
    print(is_prime(498))
    print(is_prime(499))
    print(is_prime(359))
    print(is_prime(170))
    print(is_prime(100))
    print(is_prime(173))

if __name__ == "__main__":
    main()