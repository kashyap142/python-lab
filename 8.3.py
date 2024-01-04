class Student:
    def __init__(self, name, roll, branch):
        self.name = name
        self.roll = roll
        self.branch = branch

    def print_details(self):
        print(f"Name: {self.name}\nRoll Number: {self.roll}\nBranch: {self.branch}\n")


def print_branch_student(arr, branch_name):
    for stud in arr:
        if stud.branch == branch_name:
            stud.print_details()


if __name__ == "__main__":
    n = int(input("Enter number of students: "))

    arr = []

    for i in range(0, n, 1):
        print(f"Enter details of student {i+1}")
        name = input("Enter name: ")
        roll = input("Enter roll: ")
        branch = input("Enter branch: ")

        print()
        arr.append(Student(name, roll, branch))
    to_find = input("Enter branch ")

    print_branch_student(arr, to_find)
