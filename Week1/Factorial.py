def factorial():
    number = input("Input value:")
    n = int(number)

    if n < 0:
        return "Value is lower than zero"

    elif 0 <= n <= 1:
        return 1

    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        print(f"The factorial of {n} is: {result}")
        return result


if __name__ == "__main__":
    ans = factorial()
    print("\n Final result:", ans)
