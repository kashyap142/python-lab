import math


def solve():
    size = int(2e6 + 1)

    arr = [False] * size

    k = math.sqrt(size)
    for i in range(2, int(k), 1):
        if arr[i] == False:
            j = i * i
            for k in range(j, size, i):
                arr[k] = True

    total = 0 # 142913828922

    for i in range(2, size, 1):
        if arr[i] == False:
            total += i

    print(total)


if __name__ == "__main__":
    # sum = solve()
    solve()
