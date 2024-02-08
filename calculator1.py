# Demonstrates defining a function with a return value


def square(n: float) -> float:
    return n * n


def add(x: float, y: float) -> float:
    return x + y


def multiply(x: float, y: float) -> float:
    return x * y


def divide(x: float, y: float) -> float:
    return x / y


def main() -> None:
    x = float(input("What's x? "))
    print("x squared is", square(x))

# Main function
if __name__ == "__main__":
    main()
