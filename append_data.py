# pylint: disable=missing-final-newline
# To append data (key:value) to a log file
# Example command to run on the terminal: python append_data.py test.log Bird Parrot

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


def appendToLogFile(logFile, inputKey, inputValue):
    """
    Appends a key:value pair to a given log file
    """
    global logDict
    global lineCount

    lastDictKey = list(logDict)[-1]
    lineCount = logDict[lastDictKey]

    file = open(logFile, "a+")
    file.write(f"{inputKey}:{inputValue}\n")
    lineCount += 1
    logDict[inputValue] = lineCount
    file.close()


def search(val):
    try:
        print(f"{val} found at line number {logDict[val]}")
        return logDict[val]
    except:
        print("The value does not exist in the file")


# print(search("test.log", "Santosh"))
# print(logDict)
# print(search("Satish"))

populateLogDict("test.log")
appendToLogFile(sys.argv[1], sys.argv[2], sys.argv[3])
#print(logDict)
#print(search("Aniket"))
