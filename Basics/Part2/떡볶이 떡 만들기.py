n, m = list(map(int, input().split(' ')))
cakes = list(map(int, input().split()))

start = 0
end = max(cakes)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    for cake in cakes:
        if cake > mid:
            total += cake - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1


print(result)
