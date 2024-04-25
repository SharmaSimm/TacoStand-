

def print_centered(width, text):
    """
    Centers and prints the given text within the specified width, followed by a newline.

    Args:
        width (int): The minimum width for one line, assuming it is greater than the text length.
        text (str): The string value to be displayed in a centered format.
    """
    left_width = (width + len(text)) // 2
    spec = "%" + str(left_width) + "s"  # Automatically right-justified

    print(spec % text)

def read_int(prompt, lower, upper):
#   integer value entered by the user, within the given bounds.
    
    is_not_valid = True
    result = None

    while is_not_valid:
        try:
            temp = input(prompt)
            result = int(temp)
            is_not_valid = result < lower or result > upper

            if is_not_valid:
                print(f"ERROR: please enter a value between {lower} - {upper}")
        except ValueError:
            print("ERROR: integer input is required")

    return result

def read_double(prompt, lower, upper):
    
    # Reads input from the user until a valid double value is entered within the specified bounds.

  
    is_not_valid = True
    result = None

    while is_not_valid:
        try:
            temp = input(prompt)
            result = float(temp)
            is_not_valid = result < lower or result > upper

            if is_not_valid:
                print(f"ERROR: please enter a value between {lower} - {upper}")
        except ValueError:
            print("ERROR: double input is required")

    return result

def read_char(prompt, valid_chars):

    # Reads input from the user until a valid character value is entered from the specified valid characters.

    
    is_not_valid = True
    result = None

    while is_not_valid:
        try:
            temp = input(prompt)
            result = temp[0]
            is_not_valid = result not in valid_chars

            if is_not_valid:
                print(f"ERROR: please enter one of the following valid characters: {valid_chars}")
        except IndexError:
            print("ERROR: input type does not match")

    return result
