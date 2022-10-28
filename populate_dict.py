# pylint: disable=missing-final-newline


import sys

logDict = {}
lineCount = 0


def populateLogDict(inputFile):
    global logDict
    global lineCount

    try:
        with open(inputFile, "r") as file:
            for line in file:
                split_line = line.split(":")
                lineCount += 1
                logDict[split_line[1][:-1]] = lineCount
        file.close()
    except:
        print("File not found!")


populateLogDict("test.log")
