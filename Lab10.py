def coinExchange(amount, coinList):
    coins = [10, 5, 2, 1]
    coinCount = [0, 0, 0, 0]
    totalCoins = 0
    print("Amount: ", amount)
    for i in range(len(coins)):
        while amount >= coins[i] and coinList[i] > 0:
            amount -= coins[i]
            coinList[i] -= 1
            coinCount[i] += 1
            totalCoins += 1
    if amount > 0:
        print("Coins are not enough.")
    else:
        print("Coin exchange result: ", coinCount)
        print("Number of coins: ", totalCoins)

class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def getName(self):
        return self.name
    
    def getPrice(self):
        return self.price
    
    def getWeight(self):
        return self.weight
    
    def getCost(self):
        return self.price / self.weight
    
def knapsack(amount, itemList):
    itemList.sort(key=lambda x: x.getCost(), reverse=True)
    totalValue = 0
    knapsackItems = []
    print("Knapsack Size:", amount, "kg")
    for item in itemList:
        if item.getWeight() <= amount:
            knapsackItems.append(item)
            amount -= item.getWeight()
            totalValue += item.getPrice()
    print("=" * 20)
    for item in knapsackItems:
        print(item.getName(), "->", item.getWeight(), "kg", "->", item.getPrice(), "THB")
    print("Total:", totalValue, "THB")

def main1():
    coinList = [10, 10, 10, 10]
    coinExchange(127, coinList)
    print()
    coinExchange(249, coinList)
    print()

def main2():
    item1 = Item('stereo', 3000, 3) 
    item2 = Item('laptop', 2000, 2) 
    item3 = Item('guitar', 1500, 1.5) 
    itemList = [item1, item2, item3] 
    knapsack(3.5, itemList)
    print()
    item1 = Item('tablet', 7000, 0.5) 
    item2 = Item('perfume', 6000, 0.5) 
    item3 = Item('guitar', 9000, 1) 
    item4 = Item('air purifier', 9000, 2) 
    item5= Item('watch', 8000, 0.5) 
    itemList = [item1, item2, item3, item4, item5]
    knapsack(3, itemList)

main1()
main2()