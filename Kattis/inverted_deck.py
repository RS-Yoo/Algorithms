
def invert_deck(n, li):
    sorted_li = sorted(li)
    left = 0
    right = n - 1

    while left < n and li[left] == sorted_li[left]:
        left += 1

    if left == n:
        left = n//2
        right = n//2
    else:
        while li[right] == sorted_li[right]:
            right -= 1

    result = []
    result = result + li[:left]
    result = result + list(reversed(li[left:right+1]))
    result = result + li[right+1:]
    if result != sorted_li:
        print("impossible")
        return
    else:
        print(left+1, right+1)
        return


if __name__ == '__main__':
    n = int(input())
    li = list(map(int, input().rstrip().split()))
    invert_deck(n, li)
