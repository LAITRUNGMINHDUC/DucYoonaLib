def safe_division(x, y):
    return x/y if y != 0 else 0

def standardize_string(my_str):
    for char in INVALID_CHARACTERS:
        if char in my_str:
            my_str = my_str.replace(char, '---')
    my_str = my_str.strip().upper()
    return my_str