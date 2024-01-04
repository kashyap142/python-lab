
def calculate_bill(unit_cnt):
    rate = 1.5
    additional_charges = 25

    if unit_cnt <= 100:
        rate = 1.5
        additional_charges = 25
    elif unit_cnt <= 200:
        rate = 2.5
        additional_charges = 50
    elif unit_cnt <= 300:
        rate = 4
        additional_charges = 5
    elif unit_cnt <= 350:
        rate = 7
        additional_charges = 100
    else:
        rate = 0
        additional_charges = 1500

    return unit_cnt * rate + additional_charges


if __name__ == "__main__":
    unit_cnt = int(input("Enter units consumed "))

    bill_amt = calculate_bill(unit_cnt)

    print(f"Bill amount is {bill_amt}")