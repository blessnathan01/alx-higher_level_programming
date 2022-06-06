#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == ():
        return len(sentence), ''
    else:
        response = len(sentence), sentence[0]
        return response
