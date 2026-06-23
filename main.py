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

# print(MENU["espresso"]["ingredients"]["water"])

def report():
    print(
        f"Water: {resources['water']} ml\n"
        f"Milk: {resources['milk']} ml\n"
        f"Coffee: {resources['coffee']} g\n"
    )

def prompt(user_input):
    if user_input == "espresso":
        check_enough_resource(user_input)
    elif user_input == "latte":
        check_enough_resource(user_input)
    elif user_input == "cappuccino":
        check_enough_resource(user_input)
    else :
        print("invalid statement please try again.")


def check_enough_resource(user_choice,):

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
            print(f"The cofee amount now is {resources["coffee"]}")
            print(f"The water amount now is {resources["water"]}")
            print(f"The milk amount now is {resources["milk"]}")
            print("Here you go with your espresso.")

     elif user_choice == "latte":
         if resources["water"] < MENU["latte"]['ingredients']['water']:
             print("insufficient water, please reload")
             return
         elif resources["milk"] < MENU["latte"]['ingredients']['milk']:
             print('insufficient milk  please try again')
             return
         elif resources["coffee"] < MENU["latte"]['ingredients']['coffee']:
             print("insufficient coffee please try again")
             return

         else:
             resources["water"] -= MENU["latte"]['ingredients']['water']
             resources["milk"] -= MENU["latte"]['ingredients']['milk']
             resources["coffee"] -= MENU["latte"]['ingredients']['coffee']
             print(f"The cofee amount now is {resources["coffee"]}")
             print(f"The water amount now is {resources["water"]}")
             print(f"The milk amount now is {resources["milk"]}")
             print(" Here you go with your latte")


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
             print(f"The cofee amount now is {resources["coffee"]}")
             print(f"The water amount now is {resources["water"]}")
             print(f"The milk amount now is {resources["milk"]}")
             print(" Here you go with your cappuccino")







user_coin = 0.0

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
