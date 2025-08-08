def averageVal():
    number1 = input("input test value1: ")
    n1 = float(number1)
    number2 = input("input test value2: ")
    n2 = float(number2)
    number3 = input("input test value3: ")
    n3 = float(number3)

    average = (n1 + n2 + n3) / 3
    print(f'Average value: {average:.2f}')

def factorialVal():
    n4 = int(input("Input value for factorial: "))

    if (n4<0):
        print('Please enter a positive integer')
        return 0

    result = 1
    for i in range(1, n4 + 1):
        result *= i

    print(f'Factorial value: {result}')


if __name__ == '__main__':
    #averageVal()
    factorialVal()