from fibonacci import fibonacci_sequence


def main():
    # Demonstrate the fibonacci_sequence function with a few values
    for n in (0, 1, 5, 10):
        seq = fibonacci_sequence(n)
        print(f"First {n} Fibonacci numbers: {seq}")


if __name__ == "__main__":
    main()
