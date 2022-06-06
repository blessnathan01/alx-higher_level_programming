#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == ():
        response = len(sentence), None
    else:
        response = len(sentence), sentence[0]
    return response
