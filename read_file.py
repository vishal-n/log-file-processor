# pylint: disable=missing-final-newline
# To read the contents of a log file
import sys


def readFile(inputFile):
    try:
        with open(inputFile, "r") as file:
            for line in file:
                print(line)
        file.close()
    except:
        print("File not found!")


readFile(sys.argv[1])
