if __name__ == "__main__":
    arr = [(6, 24, 12), (60, 12, 6), (5, 5, 1)]
    ans = []
    k = 6

    for tu in arr:
        cnt = 0
        for i in tu:
            if i % k == 0:
                cnt += 1
            else:
                break

        if cnt == len(tu):
            # print(tu)
            ans.append(tu)

    print(ans)
