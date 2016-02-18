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

try:
    if len(sys.argv) != 2 or int(sys.argv[1]) < 1:
        raise ValueError()
    for num in range(1, int(sys.argv[1]) + 1):
        print(eval_number(num))
except ValueError as verr:
    print('Usage: python XoomPayPal.py [int > 0]')
