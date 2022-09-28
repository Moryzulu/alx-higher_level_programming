#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    _names = dir(hidden_4)

    for i in range(len(_names)):
        if _names[i][:2] != '__':
            print(_names[i])
