#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        response = len(sentence), None
    else:
        response = len(sentence), sentence[0]
    return response
