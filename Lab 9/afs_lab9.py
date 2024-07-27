def encode(password):
    encode = ""
    for i in password:
        if "0" <= i <= "9":
            encoded_i = str((int(i) + 3) % 10)
            encode += encoded_i
    return encode

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

def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        choice = input("Please enter an option:")
        if choice == "1":
            password = input("Please enter the password to encode:")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif choice == "2":
            decoded_password = decode(encoded_password)
            print("The encoded password is", encoded_password, "and the original password is", decoded_password)
        elif choice == "3":
            break

if __name__ == "__main__":
    main()