import logging

# logging.debug('DEBUG')
# logging.info('INFO')
# logging.warning('WARNING')
# logging.error('ERROR')
# logging.critical('CRITICAL')

logging.basicConfig(level=logging.DEBUG,
                    filename='logs.txt',
                    filemode='w',
                    format='LOG DATA: %(asctime)s | %(levelname)s | %(message)s')

a = 5
b = 2
c = '/'
result: int
flag = False

try:
    if c == '+':
        result = a + b
    elif c == '-':
        result = a - b
    elif c == '*':
        result = a * b
    elif c == '/':
        result = a / b
except BaseException as ex:
    flag = True
    # print(ex)
    logging.exception(ex)
finally:
    if flag:
        print(f'{a} || {b} are not digit')
    else:
        print(f'{a} {c} {b} = {result}')

