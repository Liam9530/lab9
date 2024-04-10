def encode(secret):
    encoded = []

    for num in secret:
        add = str(int(num) + 3)
        encoded.append(add)

    return encoded






run = True

while run:

    message = '''
Menu
-------------
1. Encode
2. Decode
3. Quit
    '''
    print(message)
    option = int(input("Please enter an option: "))

    if option == 1:
        secret = str(input("Please enter your password to encode: "))
        print("Your password has been encoded and stored!")


    elif option == 2:
        if "secret" in locals():
            print("".join(encode(secret)))

    elif option == 3:
        run = False
    else:
        print("error")


