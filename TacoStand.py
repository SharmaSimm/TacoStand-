


# CONSTANT VARIABLES
BAR = "----------------------------------------"

# STATIC VARIABLES
num_asada = 5
num_pollo = 12
num_lengua = 7
num_ultimate = 2
total_funds = 0.0

def print_menu():
    """
    Outputs the menu options (kinds of tacos) the customer can use to order.
    """
    print("Menu options:\n" + BAR)
    print("{:2}. {:<21} [${:5.2f}]".format(1, "Carne Asada (Steak)", 2.5))
    print("{:2}. {:<21} [${:5.2f}]".format(2, "Pollo Asado (Chicken)", 1.75))
    print("{:2}. {:<21} [${:5.2f}]".format(3, "Lengua (Beef Tongue)", 3.0))
    print("{:2}. {:<21} [${:5.2f}]".format(4, "Ultimate Taco", 18.0))
    print(BAR)

def get_status():
    """
    Returns a summary (all static variables) of the current status of the taco stand.

    Returns:
        str: A string containing the current values related to the taco stand, without a new line at the end.
    """
    return ("{}\nMCC Taco Stand Status\n{}\n{:<23}${:<7.2f}\n{}\n{:<23}{:2} tacos\n{:<23}{:2} tacos\n{:<23}{:2} tacos\n{:<23}{:2} tacos\n{}".format(
        BAR, BAR, "Funds Available:", total_funds, BAR, "# of Asada Left:", num_asada, "# of Pollo Left:", num_pollo,
        "# of Lengua Left:", num_lengua, "# of Ultimate Left:", num_ultimate, BAR))

def add_total_funds(funds):
    """
    Increases the total_funds static variable.

    Args:
        funds (float): The amount to add to the total funds (assumed to be greater than 0).
    """
    global total_funds
    total_funds += funds

def order_supplies(budget):
    # """
    # Checks if the proposed budget can be used to buy more supplies. If within the total funds,
    # it updates the total funds and increments the number of each taco option based on the budget.
    # Otherwise, no variables are changed.

    
    global total_funds, num_asada, num_pollo, num_lengua, num_ultimate

    # Tacos cost $0.75 each in supplies
    tacos_each = int(budget // 0.75 // 4)

    if budget <= total_funds:
        total_funds -= budget
        num_asada += tacos_each
        num_pollo += tacos_each
        num_lengua += tacos_each
        num_ultimate += tacos_each
        return True
    else:
        return False

def update_total_funds(taco_option, num_tacos):
    # """
    # Adds funds to the total (static variable) based on the kind of taco (different prices) and the number of tacos
    # in the order. It also updates the appropriate number of tacos left (static variables).

    # Args:
    #     taco_option (int): The menu option (kind of taco).
    #     num_tacos (int): The number of tacos as part of the order (assumed to be greater than 0).
    # """
    global total_funds, num_asada, num_pollo, num_lengua, num_ultimate

    price = {
        1: 2.5,
        2: 1.75,
        3: 3.0,
        4: 18.0
    }

    if are_tacos_available(taco_option, num_tacos):
        total_funds += price[taco_option] * num_tacos

        if taco_option == 1:
            num_asada -= num_tacos
        elif taco_option == 2:
            num_pollo -= num_tacos
        elif taco_option == 3:
            num_lengua -= num_tacos
        else:
            num_ultimate -= num_tacos

def are_tacos_available(taco_option, num_tacos):
    """
    Determines if the taco order can be fulfilled (if the number of tacos for the specific kind is available).

    Args:
        taco_option (int): The menu option (kind of taco).
        num_tacos (int): The number of tacos as part of the order.

    Returns:
        bool: True if the specific kind of tacos is available for the number in the order, False otherwise.
    """
    available_tacos = {
        1: num_asada,
        2: num_pollo,
        3: num_lengua,
        4: num_ultimate
    }

    return available_tacos[taco_option] >= num_tacos
