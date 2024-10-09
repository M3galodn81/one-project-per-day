import string
def query_IP(query) -> str:
    if len(query.split(".")) != 4 or len(query.split(":")) != 8:
        
            #IPv4
            if len(query.split(".")) == 4:
                for x in query.replace(".",""):
                    if x in string.ascii_letters:
                        return "Neither"
            
                for octet in query.split("."):
                    if octet == None or octet == "":
                        return "Neither"
                    if len(octet) > 4:
                        return "Neither"
                    if int(octet) > 255:
                        return "Neither"
                    if len(octet) > 1 and octet[0] == "0":
                        return "Neither"
                return "IPv4"

            if len(query.split(":")) == 8:
                for hextet in query.split(":"):
                    if len(hextet) > 4:
                        return("Neither")
                    
                    if hextet == None or hextet == "":
                        return "Neither"

                    valid_hex_chars = set('0123456789abcdefABCDEF')
                    for char in hextet:
                        if char not in valid_hex_chars:
                            return "Neither"
                return "IPv6"

    return "Neither"

print(query_IP("172.16.254.1"))
print(query_IP("2001:0db8:85a3:0:0:8A2E:0370:7334"))
print(query_IP("256.256.256.256"))