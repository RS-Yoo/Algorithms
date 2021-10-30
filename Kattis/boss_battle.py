def Solution():
    # pillar -3 (player move)
    # +2 (boss move)
    # repeat until pillar <= 3

    pillars = int(input())
    if pillars <= 3:
        print(1)
    else:
        print(pillars - 1)


if __name__ == '__main__':
    Solution()

