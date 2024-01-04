if __name__ == "__main__":
    my_dict = {
        1: 5,
        2: 10,
        3: 15,
        4: 20
    }

    total = 0

    for i in my_dict.values():
        total += i

    # for x, y in my_dict.items():
    #     total += y

    print(total)
