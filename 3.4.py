def read_numbers():
    try:
        arr = list(map(int, input("Enter numbers ").split()))
        return arr
    except ValueError:
        return []


def solve(arr):
    i = 0

    while i < len(arr):
        j = i + 1
        while j < len(arr):
            if arr[i] == arr[j]:
                arr.pop(j)
            else:
                j += 1
        i += 1

    print(arr)


if __name__ == "__main__":
    arr = read_numbers()

    if len(arr) == 0:
        print("Invalid input")
    else:
        solve(arr)
