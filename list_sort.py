"""
    Code to sort a list
    By Dolapo Atobiloye
    dxa6859@rit.edu
"""

def sortLst (lst):
    for num in range(len(lst)):
        item = [getMin(lst[num:])]
        unsortedLst = lst[num:]
        sortedLst = lst[:num]
        lst.clear()
        lst += sortedLst + [getMin(unsortedLst)] + unsortedLst

def getMin(lst):
    minItem = lst[0]
    for item in lst:
        if item < minItem:
            minItem = item
    lst.remove(minItem)
    return minItem

def main():
    lst = [5, 6, 2, 9, 3, 1]
    print(lst)
    sortLst(lst)
    print(lst)

main()
