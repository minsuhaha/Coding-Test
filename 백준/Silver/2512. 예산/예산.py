import sys
input = sys.stdin.readline

n = int(input())
prices = sorted(map(int, input().split()))
total_prices = int(input())

max_prices = prices[-1]
size = len(prices)
for price in prices:
    if price > (total_prices//size):
        max_prices = total_prices//size
        break
    total_prices -= price
    size -= 1

print(max_prices)
