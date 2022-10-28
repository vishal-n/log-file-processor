import sys
from populate_dict import logDict


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


try:
    appendToLogFile("test.log", sys.argv[1], sys.argv[2])
except IndexError:
    print("The command is entered incorrectly, Please provide the necessary parameters!")
    print("Example: python put.py Name Vishal")
