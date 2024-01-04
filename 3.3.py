def read_number():
    try:
        arr = list(map(int, input("Enter numbers: ").split()))
        return arr
    except ValueError:
        return []


def solve(arr):
    for i in range(1, len(arr), 2):
        print(arr[i], end = " ")

    print()


if __name__ == "__main__":
    arr = read_number()

    if len(arr) == 0:
        print("Invalid input")
    else:
        solve(arr)
