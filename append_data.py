# pylint: disable=missing-final-newline
# To append data (key:value) to a log file
# Example command to run on the terminal: python append_data.py test.log Bird Parrot

import sys


def appendToLogFile(logFile, inputKey, inputValue):
    """
    Appends a key:value pair to a given log file
    """
    file = open(logFile, "a+")
    file.write(f"{inputKey}:{inputValue}\n")
    file.close()


appendToLogFile(sys.argv[1], sys.argv[2], sys.argv[3])
