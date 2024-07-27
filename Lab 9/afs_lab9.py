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