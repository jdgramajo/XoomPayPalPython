def eval_number(number = 25):
    s = ''
    if number % 3 = 0:
        s += 'Xoom' 
    if number % 5 == 0:
        s += 'PayPal'
    return s if s != '' else number

for num in range(1, int(sys.argv[0]) + 1):
    print(eval_number(num))
