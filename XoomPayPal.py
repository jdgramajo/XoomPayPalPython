import sys

def eval_number(number = 25):
    s = ''
    if number % 3 == 0:
        s += 'Xoom' 
    if number % 5 == 0:
        s += 'PayPal'
    if s == '':
        return number
    else:
        return s

for num in range(1, int(sys.argv[1]) + 1):
    print(eval_number(num))
