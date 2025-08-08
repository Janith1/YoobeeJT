def sum_evenodd_num():
    number = input("Input value:")
    n = int(number)

    if n < 0:
        return "Value is lower than zero"

    elif 0 <= n <= 1:
        return 0

    else:
        result_even = 0
        print("\nEven Numbers:")
        for i in range(1, n + 1):
            if i % 2 == 0:
                result_even += i
                print(i, end=' ')
        print("\nSum of even numbers:", result_even)

        result_odd = 0
        print("\nOdd Numbers:")
        for i in range(1, n + 1):
            if i % 2 == 1:
                result_odd += i
                print(i, end=' ')
        print("\nSum of odd numbers:", result_odd)

        return 0
"""
        #Summation of even numbers using while loop
        for i in range(1, n + 1):
            if i % 2 == 0:
        i = 1   
        while i <= n:
            if i % 2 == 0:
                result += i
            i += 1
        return result
"""

if __name__ == "__main__":
    ans = sum_evenodd_num()
    #print("\nSum of even numbers:", ans)

