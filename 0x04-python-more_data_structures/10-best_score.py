#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        list_dict = list(a_dictionary)
        key = list_dict[0]
        for x in list_dict:
            if a_dictionary[key] < a_dictionary[x]:
                key = x
        return key
    else:
        return
