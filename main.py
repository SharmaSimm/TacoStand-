
import TacoStand
import UtilityBelt

def print_welcome():
    """
    Outputs a welcome message to start the program.
    """
    print( "Welcome to HU Taco Stand!")
    print( "┈┈┈┈╭╯╭╯╭╯┈┈┈┈┈")
    print( "┈┈┈╱▔▔▔▔▔╲▔╲┈┈┈")
    print( "┈┈╱┈╭╮┈╭╮┈╲╮╲┈┈")
    print( "┈┈▏┈▂▂▂▂▂┈▕╮▕┈┈")
    print( "┈┈▏┈╲▂▂▂╱┈▕╮▕┈┈")
    print( "┈┈╲▂▂▂▂▂▂▂▂╲╱┈┈")
    # ASCII art credit: https://mizbizbby.tumblr.com/post/12937794639/happy-taco-ascii-art-for-taco-thursday

def take_order():
    """
    Prints the menu, prompts the user for input for the kind of taco and number in order.
    If tacos are available, it updates the total funds and confirms the order with the user.
    Otherwise, an error message is displayed.
    """
    TacoStand.print_menu()
    option = UtilityBelt.read_int("Enter choice> ", 1, 4)
    num_tacos_ordered = UtilityBelt.read_int("Enter number of tacos you want>  ", 0, 4 )

    if TacoStand.are_tacos_available(option, num_tacos_ordered):
        TacoStand.update_total_funds(option, num_tacos_ordered)
        print_confirmation(num_tacos_ordered)
    else:
        print("Sorry, we don't have enough tacos for your order.")

def print_confirmation(num_tacos):
    
    
    print("Here you go, buen provecho!")
    print("🌮" * num_tacos)

def main():
    # """
    # Main function to run the taco stand program.
    # """
    global total_funds

    while True:
        print("\nMCC Taco Stand")
        print("1. Add Funds")
        print("2. Order Supplies")
        print("3. Open Stand")
        print("4. Exit")

        choice = UtilityBelt.read_int("Enter your choice: ", 1, 4)

        if choice == 1:
            funds_to_add = UtilityBelt.read_double("Enter amount to add: $", 0.01, float('inf'))
            TacoStand.add_total_funds(funds_to_add)
            print(f"Total funds updated: ${TacoStand.total_funds:.2f}")

        elif choice == 2:
            budget = UtilityBelt.read_double("Enter budget for supplies: $", 0.01, TacoStand.total_funds)
            if TacoStand.order_supplies(budget):
                print("Supplies ordered successfully.")
            else:
                print("Insufficient funds to order supplies.")

        elif choice == 3:
            if TacoStand.total_funds > 0:
                print("OPENING UP THE STAND...")
                print(TacoStand.get_status() + "\n\n")
                print_welcome()
                print("\n")
                take_order()
                print("--------CART IS CLOSED---------\n\n" + TacoStand.get_status())
            else:
                print("You need to add funds before opening the stand.")

        elif choice == 4:
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
