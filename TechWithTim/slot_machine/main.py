MAX_LINES = 3 #constant
MAX_BET  = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount  =  int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0")
        else:
            print("amount  must be digit")

    return amount

def get_number_of_lines():
    while True:
        lines  = input("Enter number of lines (1 - " + str(MAX_LINES)+ ")? ")
        if lines.isdigit():
            lines  =  int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("lines must be greater than 0 or less than" + str(MAX_LINES))
        else:
            print("lines  must be digit")

    return lines



def main():
    balance = deposit()
    lines  = get_number_of_lines()
    print (balance, lines)



main()
