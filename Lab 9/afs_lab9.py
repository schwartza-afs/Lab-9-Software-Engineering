def encode(password):
    encode = ""
    for i in password:
        if "0" <= i <= "9":
            encoded_i = str((int(i) + 3) % 10)
            encode += encoded_i
    return encode

#test case
print(encode("12345555"))
print(encode("00009962"))

def decode(password):
    encoded = ""
    for i in password:
        if i == "0":
            num = 7
        elif i == "1":
            num = 9
        elif i == "2":
            num = 9
        else:
            num = int(i)
            num -= 3
        encoded += str(num)
    return encoded
#test case
print(decode("45678888"))
print(decode("33332295"))
