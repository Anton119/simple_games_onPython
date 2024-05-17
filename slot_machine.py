import random

MIN_BET = 1
MAX_BET = 100
MAX_LINES = 3

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
             
    return winnings 

def get_slot_machine_spin (rows, cols, symbols):
    all_symbols = []
    for symbol, amount_of_symbols in symbols.items():
        for _ in range(amount_of_symbols):
            all_symbols.append(symbol)

    columns = []
    for i in range(cols):
        current_symbol = all_symbols[:]
        column = []
        for i in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        
        columns.append(column)

        
    return columns  

def print_slot_machine (columns):
    for y in range(len(columns[0])):
        print()
        for x in range(len(columns)):
            print(columns[y][x], end="|")


def deposit():
    while True:
        amount = input(f"What would you like to deposit (your deposit should be between ${MIN_BET} and ${MAX_BET})? $")
        if amount.isdigit():
            amount = int(amount)
            if  MIN_BET <= amount <= MAX_BET:
                print(f"Your current balance is ${amount}")
                break
            else:
                print(f"Your deposit should be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("You should type a number!")
    return amount 

def amount_of_lines ():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"The number of lines should be between 1 and {MAX_LINES}")
        else: 
            print("You should type a number!")
    return lines

def get_a_bet(balance, lines): 
    while True:
        user_bet = input("What would you like to bet on each line? $")
        if user_bet.isdigit():
            total_bet = int(user_bet) * int(lines)
            if total_bet > int(balance):
                print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
            else:
                print(f"You are betting ${user_bet} on {lines} lines. Total bet is equal to: ${total_bet}")
                break
        else:
            print("You should type a number!")

    #What would you like to bet on each line?

# всего линий 3 / if lines * user_bet > total_bet
#
#
    

def main():
    balance = deposit()
    lines = amount_of_lines()
    get_a_bet(balance, lines)
    result = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(result)
   






main()