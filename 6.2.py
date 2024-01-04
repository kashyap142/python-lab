class Bank:
    def __init__(self, bank_name, cust_no):
        self.bank_name = bank_name
        self.cust_no = cust_no

    def print_details(self):
        print(f"Bank Name {self.bank_name}\nCustomer Number {self.cust_no}\n")


class Govt_Bank(Bank):
    def __init__(self, bank_name, cust_no, branch_name, IFSC_code):
        super().__init__(bank_name, cust_no)
        self.branch_name = branch_name
        self.IFSC_code = IFSC_code

    def print_details(self):
        print(f"Bank Name {self.bank_name}\nCustomer Number {self.cust_no}\nBranch Name {self.branch_name}\nIFSC Code {self.IFSC_code}\n")


class Pvt_Bank(Bank):
    def __init__(self, bank_name, cust_no, branch_name, IFSC_code):
        super().__init__(bank_name, cust_no)
        self.branch_name = branch_name
        self.IFSC_code = IFSC_code

    def print_details(self):
        print(f"Bank Name {self.bank_name}\nCustomer Number {self.cust_no}\nBranch Name {self.branch_name}\nIFSC Code {self.IFSC_code}\n")


if __name__ == "__main__":
    b1 = Bank("Main", 12)
    b1.print_details()

    b2 = Govt_Bank("Gov", 14, "MSR", "IFSC001")

    b3 = Pvt_Bank("Pvt", 56, "HR Layout", "IFSC002")

    b2.print_details()
    b3.print_details()
