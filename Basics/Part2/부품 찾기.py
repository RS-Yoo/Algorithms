n = int(input())
in_stock = list(map(int, input().split()))
m = int(input())
requested = list(map(int, input().split()))

in_stock.sort()


def binary_search(array, start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


for request in requested:
    hasRequest = binary_search(in_stock, 0, len(in_stock) - 1, request)
    if hasRequest:
        print("yes")
    else:
        print("no")
