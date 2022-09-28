#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    b_s = max(a_dictionary.values(), default=None)
    for a, b in a_dictionary.items():
        if b == b_s:
            return a
