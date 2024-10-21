base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def ascii_to_b64(ascii_text):
    ascii_text = [bin(ord(char)).removeprefix("0b").zfill(8) for char in ascii_text]
    ascii_text = "".join(ascii_text)

    padding = len(ascii_text) % 6 
    if padding != 0:
        ascii_text += '0' * (6 - padding)

    sextets = [ascii_text[i:i+6] for i in range(0,len(ascii_text),6)]

    output = ""
    for sextet in sextets:
        output += base64_chars[int(sextet,2)]

    original_length = len(ascii_text) // 8
    output_padding = "=" * ((3 - (original_length % 3)) % 3)
    return output + output_padding

def main():
    print(ascii_to_b64("Test"))
    print(ascii_to_b64("Base 64"))
    print(ascii_to_b64("Oh no"))
    print(ascii_to_b64("TestBase 64Oh no"))

if __name__ == "__main__":
    main()