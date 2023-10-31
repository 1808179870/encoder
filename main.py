def encoder(decoder_num):
    encoded_num=""#gather the list
    for i in str(decoder_num): # get every value in the encoder_num
        i=int(i)+3
        encoded_num+= str(i)
    return encoded_num


def decoded(encoded_num):
    decoded_num=""
    for i in str(encoded_num):
        i=int(i)-3
        decoded_num+=str(i)
    return decoded_num

def menu():# set the menu
    while True:
        print(f"Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        choice=input("Please enter an option:")
        if choice=="1":
            decoder_num=input("Please enter your password to encode:")
            x=encoder(decoder_num)
            y=decoded(x)
            print(f'Your password has been encoded and stored!')
        if choice=="2":
            print(f"The encoded password is {x}, and the original password is {y}.")
        if choice=="3":
            break
menu()
