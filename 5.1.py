if __name__ == "__main__":
    my_dict = dict()

    my_dict["name"] = "Frodo Baggins"
    my_dict["email"] = "frodo@shire.com"

    # update
    my_dict["email"] = "frodo@ringbearer.com"

    val = my_dict.get("email")
    print(val)

    val = my_dict["email"]
    print(val)

    print(my_dict)

    del my_dict["email"]

    print(my_dict)