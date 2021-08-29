n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    curr_min = min(data)
    result = max(result, curr_min)

print(result)
