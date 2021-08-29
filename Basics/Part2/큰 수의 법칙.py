n, m, k = map(int, input().split())
data = list(map(int, input().split()))

result = 0
data.sort(reverse=True)

count = (m//(k+1)) * k + m%(k+1)

result += data[0] * count
result += data[1] * (m-count)

print(result)
