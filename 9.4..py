def solve(str):
    histogram = {}

    for ch in str:
        if ch.isalpha():
            histogram[ch] = histogram.get(ch, 0) + 1

    for x, y in histogram.items():
        print(f"{x} occurs {y} times")


if __name__ == "__main__":
    str = input("Enter string: ")

    solve(str)