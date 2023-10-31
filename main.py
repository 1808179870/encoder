def encoder(decoder_num):
    encoded_num=""#gather the list
    for i in str(decoder_num): # get every value in the encoder_num
        i=int(i)+3
        encoded_num+= str(i)
    return encoded_num


def decoder(u_input):   # u_input stands for user input
    d_password = ""
    for i in range(0, len(u_input)):
        decode_letter = int(u_input[i])
        if 2 < decode_letter <= 9:
            decode_letter -= 3
        elif decode_letter == 0:
            decode_letter = 7
        elif decode_letter == 1:
            decode_letter = 8
        elif decode_letter == 2:
            decode_letter = 9
        else:   # This else statement is here in case a non-numeric character is an input
            print("Incorrect value entered - Try again")
            break
        decode_letter = str(decode_letter)
        d_password += decode_letter
    return d_password  # d_password stands for decode password

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
