
def count_vowels(str):
    vowels = "aeiouAEIOU"
    cnt = 0
    for ch in str:
        if ch in vowels:
            cnt += 1

    print(cnt)


def print_without_SE(str):
    arr = "seSE"
    ans = ''
    for ch in str:
        if ch not in arr:
            ans += ch

    print(ans)


if __name__ == "__main__":
    str = input("Enter string: ")

    count_vowels(str)
    print_without_SE(str)
