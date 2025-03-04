from time_calculator import TimeCalculator

def main():
    """Interactive TimeCalculator program"""
    calculator = TimeCalculator()

    print("Time Calculator\n" + "="*20 + "\n")
    print("Enter duration in HH:MM format (e.g., 5:40)")
    print("Type 'exit' to quit\n")

    while True:
        duration = input("Enter duration: ").strip()
        if duration.lower() == 'exit':
            break

        print("-" * 40)
        result = calculator.format_output(duration)
        print(result + "\n")

if __name__ == "__main__":
    main()
