import string
import sys

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

input = open('1.txt', 'r') #расскомментировать решая задачу локально
# input = sys.stdin #расскомментировать при сдаче задачи в системе
str = input.readline()
print(str)

letters = list(set(str))

print(letters)
count = len(letters)
print(count)

freq = []
for i in range(0,count):
    freq.append(0)

for char in str:
    for i in range(0,count):
        if(char == letters[i]):
            freq[i] = freq[i] + 1
            break

print(freq)
print(type(freq))