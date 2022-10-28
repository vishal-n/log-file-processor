import sys
from populate_dict import logDict

#print(logDict)

def search(val):
    try:
        print(f"{val} found at line number {logDict[val]}")
        return logDict[val]
    except:
        print(f"The value {val} does not exist in the file")


try:
    search(sys.argv[1])
except IndexError:
    print("The command is entered incorrectly, Please provide the necessary parameters!")
    print("Example: python get.py Aniket")
