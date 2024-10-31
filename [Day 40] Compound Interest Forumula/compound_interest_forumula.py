# Assume the user will input the values correctly

# rate in percentage
# time in years

def compound_interest(principal,rate,time,compounding_period):
    return f"The final amount is {principal * (1 + (rate/compounding_period)) ** (compounding_period*time) :.2f} "

def main():
    print(compound_interest(1000,0.2,5,12))

if __name__ == "__main__":
    main()