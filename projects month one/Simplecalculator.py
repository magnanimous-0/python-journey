#calculator
def add(a,b):
    print(a+b)

def diff(a,b):
    print(a-b)  

def multiply(a,b):
    print(a*b)

def divide(a,b):
    print(a/b)

def show():
        print("1.add two numbers")
        print("2.susbtract two numbers")
        print("3.multiply two numbers")
        print("4.divide two numbers")
        print("5.exit")


def main():
        show()
        choice=(int(input("enter your choice(1-5): ")))
        if choice==5:
            print("Bye have a great day")
        elif choice>=1 and choice<=4:
            n=int(input("enter the first number: "))
            m=int(input("enter the second number: "))
            if choice==1:
                add(n,m)
            elif choice==2:
                diff(n,m)
            elif choice==3:
                multiply(n,m)
            else:
                if m==0:
                    print("cannot divide by zero")
                else:
                    divide(n,m)
        else:
            print("invalid choice try again(1-5)")

main()