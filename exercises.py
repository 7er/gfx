import sys

def print_starline(number):
    for each in '*' * number:
        sys.stdout.write('%s ' %  each)
    print

def print_numberline(number):
    for each in range(number):
        sys.stdout.write('%s ' %  each)
    print

def print_static_numberline(number):
    for each in range(10):
        sys.stdout.write('%s ' %  number)
    print

def print_increasing(number):
    for each in range(number + 1):
        sys.stdout.write('%s ' % each)
    print

def print_decreasing(number):
    for each in range(abs(number - 9)):
        sys.stdout.write('  ')
    for each in range(number + 1):
        sys.stdout.write('%s ' % each)
    print


# for each in range(9, -1, -1):
#     print_decreasing(each)

def print_table(number):
    for each in range(1, 10):
        product = number * each
        if len(str(product)) < 2:
            sys.stdout.write(' ')
        sys.stdout.write(str(product))
        sys.stdout.write('  ')
    print

# for each in range(1, 10):
#     print_table(each)
