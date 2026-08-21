def get_positive_input(message_input: str) -> float:
    while True:
        try:
            value = float(input(message_input))
            if value <= 0:
                print('The value must be more than 0.')
                continue
            return value
        except ValueError:
            print('Please enter numbers only.')

from typing import Dict, Union
def calculate_saving(
        target_saving: float,
        current_saving: float
):
    if target_saving <= 0:
        raise ValueError('Target Saving must be above 0.')
    if current_saving <= 0:
        raise ValueError('Current Saving must be above 0')

    pct = ((current_saving / target_saving) * 100)
    remaining = target_saving - current_saving

    return {
        'Percentage': pct,
        'Remaining balance': remaining,
        'Status': 'Target Achieved' if current_saving >= target_saving else 'In Progress'
}

def report_present(name, target_saving, current_saving, result):
    print('\nAnalysis Summary')
    print(f'Name of Student: {name}')
    print(f'Target Savings: RM {target_saving:,.2f}')
    print(f'Current Saving: RM {current_saving:,.2f}')
    print(f"Achievement: {result['Percentage']:,.2f}%")
    print(f"Remaining: RM {result['Remaining balance']:,.2f}")
    print(f"Status: {result['Status']}")

if __name__=='__main__':
    print('Saving Analysis System')

    amount = int(get_positive_input('Enter number of student: '))

    for i in range (amount):
        print(f'\nStudent {i + 1}')
        name = input('Student Name: ')
        target_saving = get_positive_input('How much is your target? ')
        current_saving = get_positive_input('How much does you save today? ')

        result = calculate_saving(target_saving, current_saving)

        report_present(name, target_saving, current_saving, result)