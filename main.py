from time_calculator import TimeCalculator

def main():
    """Main function to demonstrate the TimeCalculator usage"""
    calculator = TimeCalculator()
    
    # Example calculations
    durations = [
        "5:40",  # Valid duration
        "2:30",  # Valid duration
        "25:00", # Valid duration crossing day boundary
        "1:60",  # Invalid minutes
        "abc"    # Invalid format
    ]
    
    print("Time Calculator\n" + "="*20 + "\n")
    
    for duration in durations:
        print(f"\nCalculating for duration: {duration}")
        print("-" * 40)
        result = calculator.format_output(duration)
        print(result)

if __name__ == "__main__":
    main()
