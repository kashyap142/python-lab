if __name__ == "__main__":
    arr = [("GFG", "IS", "BEST"), ("THIS", "IS", "GOOD"), ("Hehe", "Boi")]

    ans = []

    for tu in arr:
        cnt = 0
        for str in tu:
            if str.isupper():
                cnt += 1
            else:
                break

        if cnt == len(tu):
            ans.append(tu)

    print(ans)
