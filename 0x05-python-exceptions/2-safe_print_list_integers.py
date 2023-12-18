#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                if isinstance(my_list[i], int):
                    count += 1
            except (ValueError, TypeError):
                pass
        print("\nnb_print:", count)
    except IndexError:
        pass
    return count
