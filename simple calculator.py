x=float(input('enter first number'))
y=float(input('enter second number'))

operations=input('choose operations(*,+,-,/)')

match operations:
    case '*':
        print(x*y)
    case '-':
        print(x-y)
    case '+':
        print(x+y)
    case '/':
        print(x/y)
    case _:
        print('doesnot exist')