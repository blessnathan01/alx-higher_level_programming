#!/usr/bin/python3
# import sys
def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except BaseException as err:
        # sys.stdout.write("Exception: " + str(err) + "\n")
        return
