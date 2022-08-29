n=int(input())
g=n//2
for x in range(1,n+1):
    if x%2!=0:
        print(" "*g,end=" ")
        print("*"*x)
        g=g-1
    else:
        print(" ")
