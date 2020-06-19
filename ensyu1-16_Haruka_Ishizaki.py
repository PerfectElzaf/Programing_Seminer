import sys

data = sys.stdin.readlines()
target = 0
for i in range(len(data)):
    if len(data[target]) < len(data[i]):
        target = i
    else:
        i = i+1

print(len(data[target])-1)
