# Nícolas Castellani Brisque
# Infinite Coins Algorithm

global ArraySets
ArraySets = []

"""
 The function SetQuartes below will append major possibilities of changes with quarters. It will:
 - Obtain the input "n"
 - Iterate over the quantity of times it is possible to divide n by 25
 - Check if it can use dimes
 - Check if it can use nickels
 - Append all iterations in the ArraySets
"""
def SetQuarters(n):
    total = n // 25
    for i in range(total):
        quarters = ((i + 1) * 25)
        if (n - quarters) >= 10:
            dimes = (n - quarters) // 10
            nickels = (n - quarters - dimes * 10) // 5
            pennies = n - quarters - dimes * 10 - nickels * 5
            NewSet = [i + 1, dimes, nickels, pennies]

        elif (n - quarters) >= 5:
            nickels = (n - quarters) // 5
            pennies = n - quarters - nickels * 5
            NewSet = [i + 1, 0, nickels, pennies]

        else:
            pennies = n - quarters
            NewSet = [i + 1, 0, 0, pennies]

        ArraySets.append(NewSet)

"""
 The function SetDimes below will append major possibilities of changes with dimes. It will:
 - Obtain the input n
 - Iterate over the quantity of times is possible to divide n by 10
 - Check if it can use nickels
 - Append all iterations in the ArraySets
"""
def SetDimes(n):
    total = n // 10
    for i in range(total):
        dimes = (i + 1) * 10

        if (n - dimes) >= 5:
            nickels = (n - dimes) // 5
            pennies = n - dimes - nickels * 5
            NewSet = [0, i + 1, nickels, pennies]
        else:
            pennies = n - dimes
            NewSet = [0, i + 1, 0, pennies]

        ArraySets.append(NewSet)

"""
 The function SetNickels below will append major possibilities of changes with nickles. It will:
 - Obtain the input n
 - Iterate over the quantity of times is possible to divide n by 5
 - Append all iterations in the ArraySets
"""
def SetNickels(n):
    total = n // 5
    for i in range(total):
        nickels = (i + 1) * 5
        pennies = n - nickels
        NewSet = [0, 0, i + 1, pennies]
        ArraySets.append(NewSet)
    
"""
 The function SetPennies below will append a Set with just one possibility of pennies. It will:
 - Obtain the input n
 - Use the same input as pennies since the ratio is 1:1
 - Append in the ArraySets
"""
def SetPennies(n):
    NewSet = [0, 0, 0, n]
    ArraySets.append(NewSet)

"""
 The function MakeChange below will:
 - Obtain the input n
 - Verify if it is a integer variable
 - Check the value to use correspondent functions
 - Return the Array with all created Sets 
"""
def MakeChange(n):
    try:
        coins = int(n)

    except:
        print("Please, input a valid number!")
        print()
        main()

    else:
        if coins >= 25:
            SetPennies(coins), SetNickels(coins), SetDimes(coins), SetQuarters(coins)
        elif coins >= 10:
            SetPennies(coins), SetNickels(coins), SetDimes(coins)
        elif coins >= 5:
            SetPennies(coins), SetNickels(coins)
        elif coins >= 1:
            SetPennies(coins)
        return ArraySets

def main():
    print("Input 0 if you want to quit this application!")
    while True:
        n = input("Number: ")
        try:
            if int(n) <= 0:
                break

        except:
            print("Invalid Input!")
            print()

        else:
            print(MakeChange(n))
            ArraySets.clear()
            print()

if __name__ == "__main__":
    main()