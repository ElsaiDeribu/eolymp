n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

count = 0
for row in range(len(arr)):
    for col in range(row + 1, len(arr[0])):
        if arr[row][col] == 1:
            count += 1

print(count)
