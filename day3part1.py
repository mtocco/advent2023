# https://adventofcode.com/2023/day/3
# found resources:
#           https://stackoverflow.com/questions/54733936/splitting-a-string-on-non-digits
#           https://www.geeksforgeeks.org/python-remove-empty-strings-from-list-of-strings/
import re

def get_neighbor_chars(line, index):
    neighbor_chars = ""
    if index > 0:
        neighbor_chars += line[index - 1]
    if index < len(line) - 1:
        neighbor_chars += line[index + 1]
    return neighbor_chars

def main ():
    f = open("dataPart1.txt", "r")
    lineList = f.readlines()
    testCase = []
    previous_line = None         
    for lineNo, line in enumerate(lineList):
        if lineNo + 1 < len(lineList):
            next_line = lineList[lineNo + 1]
        else:
            next_line = None
        sanitizeList = [int(i) for i in re.findall(r'\d+', line)]
        currentSanatizeIndex = 0
        numericToggle = False
        for index, char in enumerate(line):
            if char.isdigit():
                if numericToggle: continue

                testChars = get_neighbor_chars(line, index)
                if previous_line is not None:
                    testChars += get_neighbor_chars(previous_line, index)
            
                if next_line is not None:
                    testChars += get_neighbor_chars(next_line, index)
                
                contains_invalid_chars = any(re.match(r'[^\d\n.]', char) for char in testChars)
                if contains_invalid_chars:
                    testCase.append(sanitizeList[currentSanatizeIndex])
                    currentSanatizeIndex += 1
                    numericToggle = True
                
                testChars = ""
            else:
                if index >= 0 and line[index - 1].isdigit() and not numericToggle:
                    currentSanatizeIndex += 1
                numericToggle = False
        previous_line = line
    print("Sum is: " + str(sum(testCase)))
        
main()
