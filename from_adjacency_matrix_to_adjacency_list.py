n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

adjList = [[] for _ in range(n)] 


for row in range(len(arr)):
    for col in range(len(arr[0])):
        if arr[row][col] == 1:
            adjList[row].append(col + 1)
            
            
for i in range(len(adjList)):
    print(len(adjList[i]), *adjList[i])