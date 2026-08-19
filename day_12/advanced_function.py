from typing import Dict, Union

def calculate_investment_performance(
    initial_investment: float,
    final_score: float,
    duration_year: float = 1.0
) -> Dict[str, Union[float, str]]:

    if initial_investment <= 0:
        raise ValueError('Initial Investment must be above 0')
    if duration_year <= 0:
        raise ValueError('Duration of year must be above 0')

    net_profit = final_score - initial_investment
    roi = ((final_score - initial_investment) / initial_investment) * 100
    cagr = ((final_score / initial_investment) ** (1 / duration_year) - 1 ) * 100

    return {
        'net_profit': net_profit,
        'roi_pct': roi,
        'cagr_pct': cagr,
        'status': 'Profitable' if net_profit >= 0 else 'Loss'
}

def report_present(
    modal: float,
    current_amount: float,
    year: float,
    result: Dict[str, Union[float, str]]
) -> None:

    print('\n' + '=' * 45)
    print('Report of investment performance (ROI & CAGR)')
    print('=' * 45)
    print(f'Initial: RM {modal:,.2f}')
    print(f'Final: RM {current_amount:,.2f}')
    print(f'Duration: {year:.1f} years')
    print('-' * 45)
    print(f"Status of Investment: {result['status']}")
    print(f"Net Profit/Loss: RM {result['net_profit']:,.2f}")
    print(f"ROI: {result['roi_pct']:,.2f}%")
    print(f"CAGR: {result['cagr_pct']:,.2f}%")
    print('=' * 45)

if __name__ == '__main__':
    try:
        modal_input = float(input('Fill in your Initial Investment (RM): '))
        final_input_amount = float(input('Fill in your Final Investment Amount (RM): '))
        year_input = float(input('Fill in your duration of Investment (Year): '))

        performance = calculate_investment_performance(
        initial_investment= modal_input,
        final_score= final_input_amount,
        duration_year= year_input
)
        report_present(modal_input, final_input_amount, year_input, performance)

    except ValueError as e:
        print(f'\n[Input Correction]: {e}')