#!/usr/bin/env python3
import random


def compare(files):
    some_answer = sum([int(x) for x in files[0][1].split(" ")])
    other_answer = sum([int(x) for x in files[1][1].split(" ")])
    if some_answer == other_answer:
        return True
    return False


def inputGenerator():
    answer = random.randint(3, 10**7)
    if answer % 2 == 0:
        return str(answer + 1)
    return str(answer)
