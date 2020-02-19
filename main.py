import re

print("Welcome to our calculator")
last = 0
run = True


def calculation():
    global run
    global last
    equation = ""
    if last == 0:
        equation = input("Please Enter A Equation:")
    else:
        equation = input(str(last))
    if equation == 'quit':
        run = False
    else:
        equation1 = re.sub("[a-zA-Z.,':]", "", equation)
        if last==0:
            last=eval(equation1)
        else:
            last = eval(str(last) + equation1)
    print("Your calculation is:", last)


while run == True:
    calculation()
