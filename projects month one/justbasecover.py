# single line comment
'''multiline
comment'''
'''a,b=input('enter two numbers').split()
print(a,b)
x,y=int(input('enter two numbers'))
sum = x+y
print(sum)
for i in range(5,0,-1):
    print(i)'''
def GetSum(x,y):
    sum = x + y
    return(sum)

print(GetSum(x=1,y=1))
print(GetSum(y=10,x=10))
def root(n):
    return n//2
print(root(4))