#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    index = 0
    
    try:
        while count < x:
            try:
                value = my_list[index]
                if isinstance(value, int):
                    print("{:d}".format(value), end=" ")
                    count += 1
            except (ValueError, TypeError):
                pass
            index += 1
    except IndexError:
        pass
    
    print()
    return count
