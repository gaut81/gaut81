print('Welcome to quadratic equation program')


def digital_input():
    while True:
        try:
            var = int(input())
        except ValueError:
            print('Incorrect symbol, please enter a numeric value')
        else:
            print('Correct, the numeric ', var, 'has been confirmed')
            return var
            break


def q_calc(a1, b1, c1):
    d = ((b1 ** 2) - (4 * a1 * c1))
    if d > 0:
        print('The equation has two solutions')
        print('x1 = ', (-b1 + d ** 0.5) / (2 * a1))
        print('x2 = ', (-b1 - d ** 0.5) / (2 * a1))
    elif d == 0:
        print('The equation has one solution')
        print('x = ', (-b1/2/a))
    elif d < 0:
        print('The equation has no solutions')

print("please input a")
a = digital_input()
print('please input b')
b = digital_input()
print('please input c')
c = digital_input()

q_calc(a,b,c)