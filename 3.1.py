def read_number():
    try:
        arr = list(map(int, input("Enter numbers ").split()))
        return arr
    except ValueError:
        print("Enter some numbers")
        return []

def solve(arr):
    x = 4
    y = 5

    for i in arr:
        if i % x == 0 and i % y != 0:
            print(i)


if __name__ == "__main__":
    arr = read_number()

    if len(arr) == 0:
        print("Invalid input")
    else:
        solve(arr)