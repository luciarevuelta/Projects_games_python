-- #VARIABLES GLOBALES--------
# COINS
QUARTER = 0.25
DIME = 0.1
NICKLE = 0.05
PENNIE = 0.01
# PRICE COFFEES
PRICE_ESPRESSO = 1.5
PRICE_LATTE = 2.5
PRICE_CAPPUCCINO = 3

------------------------------

def decision_coffe():
"""Función que pregunta al usuario qué tipo de café desea.
"""

    coffes = ["espresso", "latte", "cappuccino"]
    while True:
        decision_user = input(
            "What would you like,(espresso/latte/cappuccino)?: ")
        if any(coffe in decision_user for coffe in coffes):
            print(f"You choose a {decision_user} coffe. Great!")
            return decision_user
            break
        print("Choose a correct coffe.")

decision_coffe()



def insert_coins():
    decision_user = decision_coffe()
    if decision_user != "off":
        print("Please insert coins")
        while True:
            try:
                quarters = float(input("How many quartes?"))
                dimes = float(input("How many dimes?"))
                nickles = float(input("How many nickles?"))
                pennies = float(input("How many pennies"))
            except ValueError:
                    print("That's not a float value! Repeat again!")
            else:
                monetary_value = float(round(QUARTER * quarters + DIME * dimes + NICKLE * nickles + PENNIE * pennies,2))
                return monetary_value, decision_user
    
            #if (quarters.isnumeric() and dimes.isnumeric() and nickles.isnumeric() and pennies.isnumeric()):
                #monetary_value = round(QUARTER * quarters + DIME * dimes + NICKLE * nickles + PENNIE * pennies,2)
                #return monetary_value


def enough_money():
    decision_user = decision_coffe()
    monetary_value = insert_coins()
    if decision_user == "espresso" and monetary_value > PRICE_ESPRESSO:
        change_espresso = float(round(monetary_value - PRICE_ESPRESSO))
        print(f"Here is ${change_espresso} in change.")
        print(f"He is your {decision_user}. Enjoy!")
        return change_espresso
    if decision_user == "latte" and monetary_value > PRICE_LATTE:
        change_latte = float(round(monetary_value - PRICE_LATTE,2))
        print(f"Here is ${change_latte} in change.")
        print(f"He is your {decision_user}. Enjoy!")
        return change_latte
    if decision_user == "cappuccino" and monetary_value > PRICE_CAPPUCCINO:
        change_cappuccino = float(round(monetary_value - PRICE_CAPUCCINO))
        print(f"Here is ${change_cappuccino} in change.")
        print(f"He is your {decision_user}. Enjoy!")
        return change_capuccino
    else:
        print("Sorry taht's not enough money.")
enought_money()