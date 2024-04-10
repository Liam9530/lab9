def encode(secret):
    list = []
    list.append(secret)
    for num in list:
        print(list)






run = True

while run:

    message = '''
Menu
-------------
1. Encode
2. Decode
3.Quit
    '''
    print(message)
    option = int(input("Please enter an option: "))

    if option == 1:
        secret = int(input("Please enter your password to encode: "))
        encode(secret)



    elif option == 2:
        print('2')
    elif option == 3:
        run = False
    else:
        print("error")


