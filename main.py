def arithmeticOperation(typeOperation: str):

    def operation1(a: int, b: int) -> float | str:
        try:
            a = float(a)
            b = float(b)
        except ValueError as ex:
            print(-1, ValueError)
        if typeOperation == '+':
            return a + b
        elif typeOperation == '-':
            return a - b
        elif typeOperation == '*':
            return a * b
        elif typeOperation == '/':
            try:
                return a / b
            except (ZeroDivisionError, TypeError) as error:
                print(-1, error)
        else:
            return f'operation \"{typeOperation}\" has not realization'
    return operation1


addition = arithmeticOperation('+')
value1 = 2
value2 = 5
subtraction = arithmeticOperation('-')
value3 = 4
value4 = 2
multiplication = arithmeticOperation('*')
value5 = 10
value6 = 2
division = arithmeticOperation('/')
value7 = 20
value8 = 0

result = addition(value1, value2)
result2 = subtraction(value3, value4)
result3 = multiplication(value5, value6)
result4 = division(value7, value8)

print(value1, '+', value2, '=', result, type(result))
print(value3, '-', value4, '=', result2, type(result2))
print(value5, '*', value6, '=', result3, type(result3))
print(value7, '/', value8, '=', result4, type(result4))
