# https://adventofcode.com/2023/day/3
# found resources:
#           https://stackoverflow.com/questions/54733936/splitting-a-string-on-non-digits
#           https://www.geeksforgeeks.org/python-remove-empty-strings-from-list-of-strings/

import time
import re
#import numpy as np

def main ():
    start_time = time.time() 
    f = open("dataPart1.txt", "r")
    lineList = f.readlines()
    testCase = []
    previous_line = None    
    gear_collection = { }     
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
                if (bool(re.match(r'\*', str(line[index-1])))):
                    gear_id = str(lineNo) + "-" + str(index-1)
                    gear_collection.setdefault(gear_id, []).append(sanitizeList[currentSanatizeIndex])
                    currentSanatizeIndex += 1
                    numericToggle = True
                    continue
                if (bool(re.match(r'\*', str(line[index+1])))):
                    gear_id = str(lineNo) + "-" + str(index+1)
                    gear_collection.setdefault(gear_id, []).append(sanitizeList[currentSanatizeIndex])
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
                    if (bool(re.match(r'\*', str(charAbove)))):
                        gear_id = str(lineNo - 1) + "-" + str(index)
                        gear_collection.setdefault(gear_id, []).append(sanitizeList[currentSanatizeIndex])
                        currentSanatizeIndex += 1
                        numericToggle = True
                        continue
                    if charAboveRight is not None and (bool(re.match(r'\*', str(charAboveRight)))):
                        gear_id = str(lineNo - 1) + "-" + str(index + 1)
                        gear_collection.setdefault(gear_id, []).append(sanitizeList[currentSanatizeIndex])
                        currentSanatizeIndex += 1
                        numericToggle = True
                        continue

                    if charAboveLeft is not None and (bool(re.match(r'\*', str(charAboveLeft)))):
                        gear_id = str(lineNo - 1) + "-" + str(index - 1)
                        gear_collection.setdefault(gear_id, []).append(sanitizeList[currentSanatizeIndex])
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
                    if (bool(re.match(r'\*', str(charBelow)))):
                        gear_id = str(lineNo + 1) + "-" + str(index)
                        gear_collection.setdefault(gear_id, []).append(sanitizeList[currentSanatizeIndex])
                        currentSanatizeIndex += 1
                        numericToggle = True
                        continue
                    if charBelowRight is not None and (bool(re.match(r'\*', str(charBelowRight)))):
                        gear_id = str(lineNo + 1) + "-" + str(index + 1)
                        gear_collection.setdefault(gear_id, []).append(sanitizeList[currentSanatizeIndex])
                        currentSanatizeIndex += 1
                        numericToggle = True
                        continue
                    if charBelowLeft is not None and (bool(re.match(r'\*', str(charBelowLeft)))):
                        gear_id = str(lineNo + 1) + "-" + str(index - 1)
                        gear_collection.setdefault(gear_id, []).append(sanitizeList[currentSanatizeIndex])
                        currentSanatizeIndex += 1
                        numericToggle = True
                        continue
            else:
                if index >= 0 and line[index - 1].isdigit() and not numericToggle:
                    currentSanatizeIndex += 1
                numericToggle = False
        previous_line = line
    

    totalSum = 0
    for key, value in dict(gear_collection).items():
        product = 1
        if len(value) > 1:
            for i in value:
                product *= i
            print(product)
            totalSum += product
        else:
            del gear_collection[key]
    print(gear_collection)
    print(totalSum)
    end_time = time.time()  # Record the end time
    execution_time = round(end_time - start_time, 5)
    print("Execution time:", execution_time, "seconds")
        
main()
