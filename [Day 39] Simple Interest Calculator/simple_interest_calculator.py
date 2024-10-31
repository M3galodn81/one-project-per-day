# Assume the user will input the values correctly

# rate in percentage
# time in years

def simple_interest(principal,rate,time ):
    return f"The final amount is {(principal)*(1+rate*time):.2f} "

def main():
    print(simple_interest(1000,0.2,5))
    print(simple_interest(18000,0.4,10))
    print(simple_interest(71000,0.02,5))


if __name__ == "__main__":
    main()