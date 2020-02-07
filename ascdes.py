import array as ar
import random
a=ar.array("i",[])

c=0
suma=0
rev=0
lb=int(input("Enter lower boundary:"))
ub=int(input("enter upper boundary:"))
if lb>=100:
    if ub>lb:
        n = int(input("Enter array size:"))
        for i in range(0,n):
            x=random.randrange(lb,ub,13)
            a.append(x)
        print(a)
        c=sum(a)
        print(c)
        lesser=a[0]
        while c!=0:
            suma=suma+(c%10)
            c=c//10
        print(suma)     
        if suma%2!=0:
            for i in range(0,n):
                for j in range(0,n):
                    if a[i]<a[j]:
                        temp=a[i]
                        a[i]=a[j]
                        a[j]=temp
            for i in range(1,n+1):
                print(a[-i],end="\t")
        elif suma%2==0:
            for i in range(0,n):
                for j in range(0,n):
                    if a[i]<a[j]:
                        temp=a[i]
                        a[i]=a[j]
                        a[j]=temp
            for i in range(0,n):
                print(a[i],end="\t")
    elif ub<lb:
            print("Upper boundry cant be less than lower boundary")
    else:
        print("Both the boundaries are equal so cant proceed further")
else:
    print("lower boundry should be a three digit number")
        
