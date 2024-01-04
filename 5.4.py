if __name__ == "__main__":
    dict1 = {
        "Brand" : "Nissan",
        "Model" : "GTR",
        "Top Speed" : 320
    }

    dict2 = {
        "Top Speed" : 290,
        "Cost" : 600000
    }

    dict1.update(dict2)

    print(dict1)
    print(dict2)