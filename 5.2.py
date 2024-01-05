if __name__ == "__main__":

    my_dict = {
        "name" : "frodo baggins",
        "email" : "frodo@ringbearer.com",
        "city" : "shire"
    }

    print(my_dict)

    my_dict.pop("city")
    print(my_dict)

    my_dict.popitem()

    print(my_dict)

    my_dict.clear()

    print(my_dict)
