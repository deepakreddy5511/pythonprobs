
def random(balance,n):
    count=0
    import random
    v=random.randrange(222222,999999,234)
    print("\nyour otp is:",v)
    k=int(input("Please enter your otp: "))
    if(k==v):
        c=check(balance,n)
        return c
    elif k!=v:
        for i in range(0,2):
            count=count+1
            print("\notp is incorrect please try again")
            v=random.randrange(222222,999922,234)
            print("\nyour otp is:",v)
            k=int(input("Please neter your otp: "))
            if(k==v):
                c=check(balance,n)
                return c
            if count>3:
                print("exceeded no of tries exiting the program")
                exit
        
def check(balance,n):
    print("\nOtp verification successfull")
    print("\nMoney withdrawed succesfuly")
    a=balance-n
    return a
def deposit(balance):
    n=int(input("\nPlease enter the amount to deposit:"))
    balance=balance+n
    return balance
def withdraw(balance):
    k=balance
    n=int(input("\nPlease enter the amount to withdraw:"))
    if n>balance:
        print("you have insufficient balance:")
        return balance
    elif n<=balance:
        v=random(k,n)
        return v
balance=20000
while True:
    print("\n\n\nWelcome to the bank of bank of zurg")
    print("please select the service from below:")
    print("\n1.balance check \n2.Deposit \n3.Withdraw \n4.Exit")
    n=int(input("Please select a choice:"))
    if n==1:
        print("\nAvailable balance is:",balance)
    elif n==2:
        a=deposit(balance)
        print("\nthe total balance is:",a)
    elif n==3:
        s=withdraw(balance)
        balance=s
        if(s==None):
            print("\nExceeded no of tries")
        else:
            print("\nthe balance is:",s)
    elif n==4:
        exit(0)
    else:
        print("Please enter the correct choice")

