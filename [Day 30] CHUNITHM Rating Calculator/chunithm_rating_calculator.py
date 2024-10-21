while True:
    try:
        constant = float(input("Enter the constant of the chart: "))
        if constant < 1 or constant > 15.4:
            print("The constant must within 1.0 to 15.4")
            continue
        break
    except:
        print("The input must be a decimal number. ")
        continue

while True:
    try:
        score = int(input("Enter your score on that chart(no commas or any separators): "))
        if score > 1_010_000 or score < 0:
            print("The score must be between 0 and 1,010,000")
            continue
        break
    except:
        print("The input must be a whole number. ")
        continue

def get_rating(constant,score):
    if score >= 1_009_000:
        return constant + 2.15 #SSS+
    elif score >= 1_007_500:
        return constant + 2 + (score - 1_007_500)//100 * 0.01 #SSS
    elif score >= 1_005_000:
        return constant + 1.5 + (score - 1_005_000)//50 * 0.01 #SS+
    elif score >= 1_000_000:
        return constant + 1 + (score - 1_000_000)//100 * 0.01 #SS
    elif score >= 975_000:
        return constant + (score - 975_000)//250 * 0.01 #S-S+
    elif score >= 925_000:
        return constant - 3 + (score - 925_000)//500 * 0.03 #AA-AAA
    elif score >= 900_000:
        return constant - 5 + (score - 900_000)//125 * 0.01 #A
    elif score >= 800_000:
        return (constant - 5)*0.5 + score//20_000 * 0.01 *(constant - 5)*0.5 #BBB
    elif score >= 500_000:
        return score//60_000 * 0.01 *(constant - 5)*0.5 #C
    else:
        return 0
    
print(get_rating(constant,score))