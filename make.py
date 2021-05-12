#!/usr/bin/env python3

# %%
import os
from utils import compare, inputGenerator
from time import time as now
from prettytable import PrettyTable

ROOT = os.path.dirname(os.path.realpath(__file__))


class COLOR:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


SOLUTIONS = os.path.join(ROOT, "implementations")
OUTPUTS = os.path.join(ROOT, "outputs")


def create_input():
    inputFile = open("./in.txt", "w")
    inputFile.write(inputGenerator())
    inputFile.close()


def run_scripts():
    table = PrettyTable()
    table.field_names = ["IMPLEMENTATION", "TIME TO SOLVE"]
    table.align = "l"

    for x in os.listdir(SOLUTIONS):
        os.system(f"g++ {os.path.join(SOLUTIONS, x)}")
        start = now()
        os.system(f"./a.out <in.txt> {os.path.join(OUTPUTS,x[:-4])}.txt")
        end = now()
        time = end - start
        table.add_row([x[:-4], time])

    os.remove("./a.out")
    return table


def compare_solutions():
    files = []
    for x in os.listdir(OUTPUTS):
        helper = os.path.join(OUTPUTS, x[:-4] + ".txt")
        file = open(helper)
        text = file.readlines()
        files.append(text)
        file.close()

    return compare(files)


def returnError(message):
    inputFile = open("./in.txt", "r")
    error = f"""{COLOR.WARNING}{message} with: {COLOR.ENDC} {COLOR.BOLD} {inputFile.readlines()}  {COLOR.ENDC} """
    inputFile.close()
    return error


def main():
    comparison = True
    while comparison == True:
        try:
            create_input()
            table = run_scripts()
            comparison = compare_solutions()
            if comparison == False:
                print(returnError("Outputs differ with the input"))
            else:
                print(table)

        except:
            print(returnError("Something went wrong with"))
            break


if __name__ == "__main__":
    main()
