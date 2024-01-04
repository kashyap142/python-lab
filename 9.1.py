def is_symmetric(str):
    if len(str) % 2 == 1:
        print(f"'{str}' is not symmetric")
    else:
        n = len(str)
        first_half = str[0: n//2]
        other_half = str[n//2: n]

        if first_half == other_half:
            print(f"'{str}' is symmetric")
        else:
            print(f"'{str}' is not symmetric")

def is_palindrome(str):
    n = len(str)
    cond = True

    for i in range(0, n//2, 1):
        if str[i] != str[n - 1 - i]:
            cond = False

    if cond == False:
        print(f"{str} is not palindrome")
    else:
        print(f"{str} is palindrome")


if __name__ == "__main__":
    str = input("Enter string: ")

    is_symmetric(str)
    is_palindrome(str)

