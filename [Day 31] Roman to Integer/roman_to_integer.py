def romanToInt(s: str) -> int:
        roman = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        num = 0
        prev = 0
        for i,char in enumerate(s):
            num += roman[char]
            if i == 0: continue
            if roman[char] > prev:
                match s[i-1]:
                    case "I":
                        if char in set("VX"): 
                            num -= 2
                    case "X":
                        if char in set("LC"): 
                            num -= 20
                    case "C":
                        if char in set("DM"): 
                            num -= 200

        return num

def main():
    print(romanToInt("MCM"))

if __name__ == "__main__":
    main()