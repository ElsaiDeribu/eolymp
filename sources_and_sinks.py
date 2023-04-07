n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]
exiting = set()
entering = set()

sink = []
source = []

for row in range(len(arr)):
    for col in range(len(arr[0])):
        if arr[row][col] == 1:
            exiting.add(row)
            entering.add(col)

for i in range(n):
    if i not in exiting:
        sink.append(i + 1)
        
    if i not in entering:
        source.append(i + 1)
        
print(len(source), *sorted(source))
print(len(sink), *sorted(sink))
        