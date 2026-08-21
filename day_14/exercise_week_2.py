def get_positive_input(message_input: str) -> float:
    while True:
        try:
            value = float(input(message_input))
            if value <= 0:
                print("[WARNING]: The value must be more than 0!")
                continue
            return value
        except ValueError:
            print("[ERROR]: Invalid input! Please enter numbers only.")

from typing import Dict, Union

def calculate_roi_cagr(
    modal: float,
    final_value: float,
    year: float
):
    
    if modal <= 0:
        raise ValueError("Initial Investment must be above 0")
    if year <= 0:
        raise ValueError("Duration of year must be above 0")

    Net_profit = final_value - modal
    ROI = ((final_value - modal) / modal) * 100
    CAGR = ((final_value / modal) ** (1 / year) - 1) * 100

    return {
        "ROI": ROI,
        "CAGR": CAGR,
        "Status": "Profit" if Net_profit >= 0 else "Loss"
    }

def report_present(name, modal, value, year, result):
    print("\nAnalysis Summary")
    print(f"Name of Investment: {name}")
    print(f"Initial Capital: RM {modal:,.2f}")
    print(f"Current Value: RM {value:,.2f}")
    print(f"Duration: {year:.0f} years")
    print(f"ROI: {result['ROI']:.2f}%")
    print(f"CAGR: {result['CAGR']:.2f}%")
    print(f"Status: {result['Status']}")

if __name__ == "__main__":
    print("Investment Portfolio Analysis System")

    amount = int(get_positive_input("Enter number of investments: "))

    for i in range(amount):
        print(f"\nInvestment {i + 1}")

        name = input("Asset name: ")
        modal = get_positive_input("Initial capital: RM ")
        value = get_positive_input("Current value: RM ")
        year = get_positive_input("Investment period (years): ")

        result = calculate_roi_cagr(modal, value, year)
        
        report_present(name, modal, value, year, result)