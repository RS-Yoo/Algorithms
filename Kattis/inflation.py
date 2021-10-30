# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def Solution():
    n = int(input())
    cans = list(map(int, input().split()))
    cans.sort()
    result = 1

    for i in range(1, n + 1):
        if cans[i - 1] > i:
            print("impossible")
            return

        if (cans[i - 1] / i) < result:
            result = cans[i - 1] / i

    print(result)
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Solution()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
