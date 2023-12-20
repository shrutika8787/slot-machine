import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}

symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}


def check_winnings(lines, bet, columns, value):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[lines]
            if symbol != symbol_to_check:
                break
        else:
            winnings += value[symbol] * bet
            winning_lines.append(lines + 1)

    return winnings, winning_lines


# eg. symbol = A and symbol_count = 2
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[
            :
        ]  # current_symbols is a copy of all symbols because we need to remove
        # symbol from the list so it needs to be a copy so that symbols are not removed from orignal list
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(
        len(columns[0])
    ):  # if there is no column there this statement will crash
        for i, column in enumerate(columns):
            if i != len(column) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    amount = input("Enter the amount you would like to deposit $ ")
    while True:
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("Please enter again valid number")

    return amount


def get_number_of_lines():
    lines = input("How many lines you want to bet on (1-" + str(MAX_LINES) + ")? ")
    while True:
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Lines must be between zero and {MAX_LINES}")
        else:
            print("Please enter again valid number")

    return lines


def get_bet():
    bet = input("How much will you like to bet on each line? ")
    while True:
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet value must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("Please enter again valid number")

    return bet


def spin(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough balance. You current balance is {balance}")
        else:
            break
    print(f"You are betting {bet} on {lines} lines. Your total bet is {total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(lines, bet, slots, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)

    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}.")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()
