n = int(input())
stockPrices = input().split()
profitsDict = {}
profitsList = []

for i in range(n):
    stockPrices[i] = int(stockPrices[i])

for i in range(n-1):
    tmpList = stockPrices[i+1:]
    profitsDict[i] = max(tmpList) - stockPrices[i]

for i in range(n-1):
    profitsList.append(profitsDict[i])

if max(profitsList) <= 0:
    print(0)

else:
    print(max(profitsList))
    for i in range(n-1):
        tmpList = stockPrices[i+1:]
        if profitsDict[i] == max(profitsList):
            print(stockPrices[i])
        if max(tmpList) - stockPrices[i] == max(profitsList):
            print(max(tmpList))