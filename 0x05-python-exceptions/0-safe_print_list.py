#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for item in my_list[:x]:
            print("{}".format(item), end="")
            count += 1
    except BaseException:
        pass
    print()
    return count
