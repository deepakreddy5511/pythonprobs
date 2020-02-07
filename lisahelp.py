def noofdays(bd,bm):
    cd=15
    cm=8
    if bm<cm:
        months=((12-cm)+bm-1)  #this helps to get the number of months except the current month and the birthday month
        totaldays=(months*30)+((30-cd)+bd)   #this will multiply the 30 days in a month concept and adds the remaining days from current month and birthday month
        print(totaldays,"days to go")
    if bm>cm:
        months=((bm-1)-cm) #when the birthday is after the current month we can get the remaining months excluding current and birthday months upto the 12th month
        totaldays=(months*30)+((30-cd)+bd)
        print(totaldays,"days to go")
    if bm==cm:
        if bd==cd:
            print("Happy birthday")
        elif bd>cd:
            print(bd-cd,"days to go") #when it is in current month and birthday date is after the current date we can just minus the birthday date with current date
        elif bd<cd:
            months=((12-cm)+bm-1)
            totaldays=(months*30)+((30-cd)+bd)
            print(totaldays,"days to go")
rd=int(input("Please enter the birth date:"))
rm=int(input("Please enter the birth month:"))
noofdays(rd,rm)
