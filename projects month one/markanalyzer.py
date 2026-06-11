def GetTotal(t):
    total=0
    for i in range(0,5):
        total+=t[i]
    return(total)

def GetAvg(a):
    s=0
    n=0
    for i in range(0,5):
        s+=a[i]
        n+=1
    return(s/n)

def GetHigh(max):
    h=0
    for i in range(0,5):
        if max[i]>h:
            h=max[i]
    return(h)

def GetLow(low):
    l=100
    for i in range(0,5):
        if low[i]<l:
            l=low[i]
    return(l)
def main():
    m=[45,78,92,65,88]
    print('Total marks: ',GetTotal(m))
    print("Average marks scored: ",GetAvg(m))
    print("Highest mark scored: ",GetHigh(m))
    print("Lowest mark scored",GetLow(m))

main()
