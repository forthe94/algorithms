import string
import sys

input = open('1.txt', 'r') #расскомментировать решая задачу локально
# input = sys.stdin //расскомментировать при сдаче задачи в системе
S = []  #

n, W = map(int, input.readline().split())

print("count " + str(n) + ", weight " + str(W))

costs = []
for i in range(1,n+1):
  x,y = map(int, input.readline().split())
  print(x,y)
  S.append([x,y])
  costs.append([i,x/y])

if(not n):
    print("%.3f" % 0)
else:
    def getKey(item):
        return item[1]
    costs.sort(key = getKey, reverse=1)

    print(S[0][1])
    print(costs[0][0])
    j = 0
    price = 0
    while(W and (j < n)):
        num = costs[j][0] - 1
        if((W - S[num][1]) >= 0):
            W = W - S[num][1]
            price = price + S[num][0]
            print(W)
        else:
            W = 0
        j = j + 1

    print("%.3f" % price)