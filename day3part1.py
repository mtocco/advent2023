# https://adventofcode.com/2023/day/3
# found resources:
#           https://stackoverflow.com/questions/54733936/splitting-a-string-on-non-digits
#           https://www.geeksforgeeks.org/python-remove-empty-strings-from-list-of-strings/
import re

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
                if (bool(re.match(r'^[^\d\n.]$', str(line[index-1])))):
                    testCase.append(sanitizeList[currentSanatizeIndex])
                    currentSanatizeIndex += 1
                    numericToggle = True
                    continue
                if (bool(re.match(r'^[^\d\n.]$', str(line[index+1])))):
                    testCase.append(sanitizeList[currentSanatizeIndex])
                    currentSanatizeIndex += 1
                    numericToggle = True
                    continue

                if previous_line is not None:
                    charAbove = previous_line[index]
                    try:
                        charAboveRight = previous_line[index + 1]
                    except IndexError:
                        charAboveRight = None
                    try:
                        charAboveLeft = previous_line[index - 1]
                    except IndexError:
                        charAboveLeft = None
                    if (bool(re.match(r'^[^\d\n.]$', str(charAbove)))):
                        testCase.append(sanitizeList[currentSanatizeIndex])
                        currentSanatizeIndex += 1
                        numericToggle = True
                        continue
                    if charAboveRight is not None and (bool(re.match(r'^[^\d\n.]$', str(charAboveRight)))):
                        testCase.append(sanitizeList[currentSanatizeIndex])
                        currentSanatizeIndex += 1
                        numericToggle = True
                        continue

                    if charAboveLeft is not None and (bool(re.match(r'^[^\d\n.]$', str(charAboveLeft)))):
                        testCase.append(sanitizeList[currentSanatizeIndex])
                        currentSanatizeIndex += 1
                        numericToggle = True
                        continue
            
                if next_line is not None:
                    charBelow = next_line[index]
                    try:
                        charBelowRight = next_line[index + 1]
                    except IndexError:
                        charBelowRight = None
                    try:
                        charBelowLeft = next_line[index - 1]
                    except IndexError:
                        charBelowLeft = None
                    if (bool(re.match(r'^[^\d\n.]$', str(charBelow)))):
                        testCase.append(sanitizeList[currentSanatizeIndex])
                        currentSanatizeIndex += 1
                        numericToggle = True
                        continue
                    if charBelowRight is not None and (bool(re.match(r'^[^\d\n.]$', str(charBelowRight)))):
                        testCase.append(sanitizeList[currentSanatizeIndex])
                        currentSanatizeIndex += 1
                        numericToggle = True
                        continue
                    if charBelowLeft is not None and (bool(re.match(r'^[^\d\n.]$', str(charBelowLeft)))):
                        testCase.append(sanitizeList[currentSanatizeIndex])
                        currentSanatizeIndex += 1
                        numericToggle = True
                        continue
            else:
                if index > 0 and line[index - 1].isdigit() and not numericToggle:
                    currentSanatizeIndex += 1
                numericToggle = False
        previous_line = line
    print("Sum is: " + str(sum(testCase)))

        
main()
