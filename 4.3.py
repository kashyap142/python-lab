if __name__ == "__main__":

    arr_list = ['a', 'b']
    arr_tuple = ('a', 'b', 'c', 'a', 'a', 'b')

    for ele in arr_list:
        cnt = 0

        for ch in arr_tuple:
            if ch == ele:
                cnt += 1

        print(f"{ele} occurs {cnt} times in list")
