import string
import sys


input = open('1.txt', 'r') #расскомментировать решая задачу локально
# input = sys.stdin //расскомментировать при сдаче задачи в системе
S = []
num = int(input.readline())
print("num " + str(num))

i = 1
count = 0
while(num):
    if(num < i):
        S[count - 1] = S[count - 1] + num
        num = 0
    else:
        S.append(i)
        num = num - i
        count = count + 1
    i = i + 1
#print(S)





print(count)

for i in range(0,count):
    sys.stdout.write(str(S[i]) + " ")
sys.stdout.flush()