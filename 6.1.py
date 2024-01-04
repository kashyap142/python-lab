class Car:

    def __init__(self, model_name="", color="", price=0, top_speed=0):
        self.model_name = model_name
        self.color = color
        self.price = price
        self.top_speed = top_speed

    def read_details(self):
        self.model_name = input("Enter model name: ")
        self.color = input("Enter color: ")
        self.price = float(input("Enter price: "))
        self.top_speed = float(input("Enter top speed: "))

    def print_details(self):
        print(f"Model Name: {self.model_name}\nColor: {self.color}\nPrice: {self.price}\nTop Speed: {self.top_speed}\n")


if __name__ == "__main__":
    gtr = Car("GTR", "Blue", 600000, 320)

    tesla_x = Car()
    tesla_x.read_details()

    tesla_x.print_details()
    gtr.print_details()
