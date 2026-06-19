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

#TODO  1. Print the report of all the coffeee machine resources.

def report():
    print(
        f"Water: {resources['water']} ml\n"
        f"Milk: {resources['milk']} ml\n"
        f"Coffee: {resources['coffee']} g\n"
    )

def prompt(user_input):
    if user_input == "off":
        return
    elif user_input == "espresso":
        return
    elif user_input == "latte":
        return
    elif user_input == "cappuccino":
        return
    else :
        print("invalid statement please try again.")    


print(MENU)
report()

user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
prompt(user_input)