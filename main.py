

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

wallet = {
    "balance" : 0.0
}

quarters = 0.25
dimes=0.10
nickles = 0.05
pennies = 0.01
user_coin = 0.0

# print(MENU["espresso"]["ingredients"]["water"])

def report():
    print(
        f"Water: {resources['water']} ml\n"
        f"Milk: {resources['milk']} ml\n"
        f"Coffee: {resources['coffee']} g\n"
        f"Balance : {wallet['balance']} \n"
    )

def prompt(user_input):
    paid = insert_coin(user_input)

    if user_input == "espresso":
        if paid:
            check_enough_resource(user_input)
    elif user_input == "latte":
        if paid:
            check_enough_resource(user_input)
    elif user_input == "cappuccino":
        if paid:
            check_enough_resource(user_input)
    else :
        print("invalid statement please try again.")


def check_enough_resource(user_choice):

     if user_choice == "espresso":
        if resources["water"] < MENU["espresso"]["ingredients"]["water"] :
            print ("insufficient water, please reload ")
            return
        elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"] :
            print("insufficient coffee please reload")
            return
        else:
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            print(f"The cofee amount now is {resources['coffee']}")
            print(f"The water amount now is {resources['water']}")
            print(f"The milk amount now is {resources['milk']}")
            print("Here you go with your espresso.")
            report()

     elif user_choice == "latte":
         if resources["water"] < MENU["latte"]['ingredients']['water']:
             print("insufficient water, please reload")
             return
         elif resources["milk"] <MENU["latte"]['ingredients']['milk']:
             print('insufficient milk  please try again')
             return
         elif resources["coffee"] < MENU["latte"]['ingredients']['coffee']:
             print("insufficient coffee please try again")
             return

         else:
             resources["water"] -= MENU["latte"]['ingredients']['water']
             resources["milk"] -= MENU["latte"]['ingredients']['milk']
             resources["coffee"] -= MENU["latte"]['ingredients']['coffee']
             print(f"The cofee amount now is {resources['coffee']}")
             print(f"The water amount now is {resources['water']}")
             print(f"The milk amount now is {resources['milk']}")
             print(" Here you go with your latte")
             report()



     elif user_choice == "cappuccino":
        if resources["water"] < MENU["cappuccino"]['ingredients']['water']:
            print("insufficent water please reload")
            return


        elif resources["milk"] < MENU["cappuccino"]['ingredients']['milk']:
            print('insufficient milk  please try again')
            return

        elif resources["coffee"] < MENU["cappuccino"]['ingredients']['coffee']:
             print("insufficient coffee please try again")
             return
        else:
             resources["water"] -= MENU["cappuccino"]['ingredients']['water']
             resources["milk"] -= MENU["cappuccino"]['ingredients']['milk']
             resources["coffee"] -= MENU["cappuccino"]['ingredients']['coffee']
             print(f"The cofee amount now is {resources['coffee']}")
             print(f"The water amount now is {resources['water']}")
             print(f"The milk amount now is {resources['milk']}")
             print(" Here you go with your cappuccino")
             report()


     elif user_choice == "balance":
         print(f"Your balance is : {wallet['balance']}")


def load_coin(cost):
    loading = True

    while loading and wallet['balance'] <= cost:
        user_choice = input("What kind of coin do you want to load? penny,quater,nickel,or dime \n").lower()

        if user_choice == "off":
            print(f"Thank you for loading coins your amount is {wallet['balance']}")
            loading = False

        if user_choice == "quater":
             wallet['balance'] += quarters

        elif user_choice == "dimes":
            wallet['balance'] +=dimes

        elif user_choice == "nickle":
            wallet['balance'] += nickles

        elif user_choice == "penny":
            wallet['balance'] += pennies

        else:
             print("Invalid coin please try again")

        if wallet['balance'] >= cost:
            print("Your done loading")
            loading = False


def insert_coin(user_input):
    if user_input == "espresso":
        if wallet['balance'] < MENU["espresso"]["cost"]:
            print("Insufficient amount coin please load more coins")
            load_coin(MENU["espresso"]["cost"])
            if wallet['balance'] >= MENU["espresso"]["cost"]:
                wallet['balance'] -= MENU["espresso"]["cost"]
                return True
            else:
                print("Not enough money")
                return False

    elif user_input == "latte":
        if wallet['balance'] < MENU["latte"]["cost"]:
            print("Insufficient amount coin please load more coins")
            load_coin(MENU["latte"]["cost"])
            if wallet['balance'] >= MENU['latte']['cost']:
                wallet['balance'] -= MENU['latte']['cost']
                return True
            else:
                print("Not enough money")
                return False


    elif user_input == "cappuccino":
        if wallet['balance'] < MENU["cappuccino"]["cost"]:
            print("Insufficient amount coin please load more coins")
            load_coin(MENU["cappuccino"]["cost"])
            if wallet['balance'] >= MENU['cappuccino']['cost']:
                wallet['balance'] -= MENU["cappuccino"]["cost"]
                return True
            else:
                print("Not enough money")
                return False



print(MENU)
report()
want_to_buy = True
while want_to_buy:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        print("Thank you for your purchase !")
        want_to_buy = False
    else:
       prompt(user_input)

