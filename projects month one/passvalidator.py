def vp(pw):
    ch=False
    dig=False
    if len(pw)<8:
        print("password must contain atleast 8 characters")
    else:
        for ch in pw:
            if ch.isalpha()and ch.isdigit():
                    ch=True
                    dig=True
            return(ch and dig)

def main():
    print("password should be atleast 8 characters long\n")
    print("It should contain atleast one character and one digit\n")
    password= input("enter a secure password: ")
    print(vp(password))

main()

            