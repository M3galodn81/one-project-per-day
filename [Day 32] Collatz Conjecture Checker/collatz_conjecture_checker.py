# Assuming the input is an positive integer
def collatz_conjecture(num) -> int :
    i = 0
    while num != 1:
        match num % 2:
            case 0:
                num = num/2
            case 1:
                num = 3*num + 1
        i += 1
    return i

def main():
    print(collatz_conjecture(9))
    print(collatz_conjecture(19))

if __name__ == "__main__":
    main()