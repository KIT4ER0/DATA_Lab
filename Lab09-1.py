def insertionSort(list, last):
    comparisons = 0
    for i in range(1, last+1):
        key = list[i]
        j = i-1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
            comparisons += 1
        list[j+1] = key
        print(list)
    if comparisons == 0:
        comparisons = last
    else:
        comparisons = comparisons + last - 1
    print("Comparison times:", comparisons)

def selectionSort(list, last):
    comparisons = 0
    for i in range(last):
        min_index = i
        for j in range(i+1, last+1):
            if list[min_index] > list[j]:
                min_index = j
            comparisons += 1
        list[i], list[min_index] = list[min_index], list[i]
        print(list)
    print("Comparison times:", comparisons)

def bubbleSort(list, last):
    comparisons = 0
    for i in range(last):
        for j in range(last-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
            comparisons += 1
        print(list)
    print("Comparison times:", comparisons)

def main():
    insertionSort([503, 87, 512, 61, 908, 170, 897], 6)
    # selectionSort([23, 78, 45, 8, 32, 56], 21)
    # bubbleSort([23, 78, 45, 8, 32, 56], 5)

main()  