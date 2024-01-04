def remove_initial_word(str):
    words = str.split(maxsplit=1)
    print(words)
    if len(words) > 1:
        return words[1]

    return ""


if __name__ == "__main__":
    str = input("Enter string: ")

    ans = remove_initial_word(str)

    print(ans)