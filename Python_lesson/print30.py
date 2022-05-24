import sys

def print3(*arg, sep=" ", end="\n", file=sys.stdout):
    output = ""
    first = True
    for arg in args:
        output += ("" if first else sep) + str(arg)
        first = False
    file.write(output + end)