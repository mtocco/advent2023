# https://adventofcode.com/2023/day/4

import time

def main():
    start_time = time.time() 
    f = open("Data.txt", "r")
    lineList = f.readlines()
    totalPoints = 0
    for i in lineList:
        sanatizedlist = i[8:].replace("\n","").split("|")
        winningNumbers = sanatizedlist[0].split(" ")
        cardNumbers = sanatizedlist[1].split(" ")
        joinedData = list(set(winningNumbers).intersection(cardNumbers))
        sanatizedData = result = [x for x in joinedData if x]
        print(sanatizedData)
        if sanatizedData is not None:
            if len(sanatizedData) <= 2:
                totalPoints += 1 * len(sanatizedData)
            else:
                totalPoints += ((2 ** (len(sanatizedData) - 1)))
    print(totalPoints)
    end_time = time.time()  # Record the end time
    execution_time = round(end_time - start_time, 5)
    print("Execution time:", execution_time, "seconds")

main()
