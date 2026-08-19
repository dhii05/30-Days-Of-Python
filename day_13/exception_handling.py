def get_input_number(message_input: str) -> float:
    while True:
        try:
            value = float(input(message_input))
            if value <= 0:
                print("[WARNING]: The value must be more than 0!")
                continue
            return value
        except ValueError:
            print("[ERROR]: Invalid input! Please enter numbers only.")

def calculate_share_allocation(total_capital: float, number_of_investors: int) -> float:
    try:
        distribution = total_capital / number_of_investors
        return distribution
    except ZeroDivisionError:
        print("[ERROR]: The number of investors cannot be zero (0)!")
        return 0.0

if __name__ == "__main__":
    print("=" * 45)
    print("Investment Capital Allocation System (SAFE-INPUT)")
    print("=" * 45)

    modal = get_input_number("Enter Capital Amount (RM): ")
    investors = get_input_number("Enter the number of investors: ")

    try:
        total_distribution_amount = calculate_share_allocation(modal, investors)
    except Exception as e:
        print(f"[UNEXPECTED ERROR]: {e}")
    else:
        print("\n" + "=" * 45)
        print(f"Every investor will receive: RM {total_distribution_amount:,.2f}")
        print("-" * 45)
    finally:
        print("Thank you for using the Capital Distribution System.\n")