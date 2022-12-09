import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

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
''' It will work such that if user chooses one line it is the first line and 2 lines it is the second line etc..
	for line to win all chars on the row should be equal'''
#You can add more improvements later

def check_winnings(spins, lines, bet, values):
	winnings = 0
	winning_lines = []
	for line in range(lines):
		symbol = spins[0][line] #pick the first char of each row
		for column in spins:
			symbol_to_check = column[line]
			if symbol != symbol_to_check:
				break
		else:
			winnings += values[symbol] * bet
			winning_lines.append(line + 1)

	return winnings, winning_lines




def get_spin(rows, cols, symbols):
	all_symbols = []
	for symbol, symbol_count in symbols.items():
		for _ in range(symbol_count):
			all_symbols.append(symbol)

	all_columns = []

	for _ in range(cols):
		column = []
		current_symbols = all_symbols[:]
		for _ in range(rows):
			value = random.choice(current_symbols)
			current_symbols.remove(value)
			column.append(value)

		all_columns.append(column)
	
	return all_columns

def print_slot_machine(array):
	for row in range(len(array[0])):
		for i, col in enumerate(array):
			if i != len(array) - 1:
				print(col[row], " | ", end="")
			else:
				print(col[row])

def deposit():
	while True:
		amount = input("What would you like to deposit?: $")
		if amount.isdigit():
			amount = int(amount)
			if amount > 0: 
				break
			else:
				print("Amount must be greater than 0 !..")
		else:
			print("Amount must be a number")

	return amount

def get_no_of_lines():
	while True:
		lines = input("Enter the number of lines you would like to stake on [1 - "+str(MAX_LINES)+"] ? \n")
		if lines.isdigit():
			lines = int(lines)
			if 1 <= lines <= MAX_LINES: 
				break
			else:
				print("Lines must be greater than 0 !..")
		else:
			print("Lines must be a number")

	return lines

def get_bet():
	while True:
		amount = input("What amount would you like to stake on each line?: $")
		if amount.isdigit():
			amount = int(amount)
			if MIN_BET <= amount <= MAX_BET: 
				break
			else:
				print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
		else:
			print("Amount must be a number")

	return amount

def game(balance):
	lines = get_no_of_lines()
	while True:
		bet = get_bet()
		total_bet = bet * lines
		if total_bet > balance:
			print(f"You cannot stake more than you have in your balance; your balance is ${balance} and the total bet is ${total_bet}")
		else:
			break
	print(f"You are betting ${bet} on {lines}. Total bet is : ${total_bet}")

	slots = get_spin(ROWS, COLS, symbol_count)
	print_slot_machine(slots)
	winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
	print(f"You won ${winnings}")
	print(f"You won on lines:", *winning_lines, "\n")
	return winnings - total_bet


def main():
	balance = deposit()
	while True:
		print(f"Current balance is ${balance}")
		spin = input("Press enter to play (q to quit)")
		if spin == "q":
			break
		balance += game(balance)

	print(f"You left with ${balance}")

main()
