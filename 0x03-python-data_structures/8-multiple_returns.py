#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (len(sentence), None)
    new_tuple = (0, '')
    new_tuple = (len(sentence), sentence[0])
    return (new_tuple)
