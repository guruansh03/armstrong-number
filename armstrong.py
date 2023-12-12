n=int(input("enter no for factorial--"))
s=0
temp=n
while temp>0:
    d=temp%10
    f=1
    for i in range(1,d+1):
        f=f*i
    s=s+f
    temp=temp//10
print("factorial--",s)
