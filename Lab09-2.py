def card(card):
    deck = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9, "J": 10, "Q": 11, "K": 12, "A": 13}
    suit = {"♣": 0, "♦": 1, "♥": 2, "♠": 3}
    return (deck[card[:-1]], suit[card[-1]])

def insertionSort(list, last):
    comparisons = 0
    for i in range(1, last + 1):
        current = list[i]
        j = i - 1
        while j >= 0 and card(list[j]) > card(current):
            list[j + 1] = list[j]
            j -= 1
            comparisons += 1
        list[j + 1] = current
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
            if card(list[min_index]) > card(list[j]):
                min_index = j
            comparisons += 1
        list[i], list[min_index] = list[min_index], list[i]
        print(list)
    print("Comparison times:", comparisons)

def bubbleSort(list, last):
    comparisons = 0
    for i in range(last):
        for j in range(last-i):
            if card(list[j]) > card(list[j+1]):
                list[j], list[j+1] = list[j+1], list[j]
            comparisons += 1
        print(list)
    print("Comparison times:", comparisons)

def main():
    insertionSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)
    selectionSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)
    bubbleSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)

main()
