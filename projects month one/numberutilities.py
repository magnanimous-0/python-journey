
def IsEven(n):
    if n%2==0:
        return(True)
    else:
        return(False)

def IsPrime(n):
    if n<2 :
        print("Not a prime number")
    else:
        for i in range(2,n):
            if n%i==0:
                return(False)
        return(True)
    
def fact(n):
    if n<0:
        print("factorial doesn't exist")
    elif n==0:
        return(1)
    else:
        r=1
        for i in range(1,n+1):
            r*=i
        return(r)
 
def SOD(n):
    s=0
    for i in range(0,n):
        s+=n%10
        n=n//10
    return(s)

def main():
    num=int(input("enter a number: "))
    print("if the nummber is an even number: ",IsEven(num))
    print("if the nummber is a prime number: ",IsPrime(num))
    print("factorial of the number: ",fact(num))
    print("sum of digits of the number: ",SOD(num))

main()