def read_numbers():

    try:
        arr = list(map(int, input("Enter numbers: ").split()))
        return arr
    except ValueError:
        return []


def solve(arr):
    odd_sum = 0
    even_sum = 0

    for i in arr:
        if i & 1:
            odd_sum += i
        else:
            even_sum += i

    print(f"Odd sum: {odd_sum}\nEven sum : {even_sum}")


if __name__ == "__main__":
    arr = read_numbers()

    if len(arr) == 0:
        print("Invalid input")
    else:
        solve(arr)
