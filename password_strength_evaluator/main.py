from checking_pwd_strength import checking_length,checking_lowercase,checking_uppercase,checking_special_character,checking_digit,checking_sequential
def main() :
    pwd = input("Please Enter your Password : ")
    if checking_lowercase(pwd) and checking_uppercase(pwd) and checking_length(pwd) and checking_special_character(pwd) and checking_digit(pwd) and checking_sequential(pwd):
        print("Strong Password \n Rating : 9/10")
    elif checking_lowercase(pwd) and checking_uppercase(pwd) and checking_length(pwd) and checking_special_character(pwd):
        print("Moderate Password \n Rating : 7/10")
    elif checking_lowercase(pwd) and checking_uppercase(pwd) and checking_length(pwd):
        print("Weak Password \n Rating : 5/10")
    else:
        print("Password is too small and Weak")
if __name__ == '__main__':
    main()