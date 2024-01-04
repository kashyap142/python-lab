class Time:
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __add__(self, other):
        total_second = (self.hour + other.hour) * 3600 + (self.minute + other.minute) * 60 + (self.second + other.second)

        h = total_second // 3600
        total_second = total_second % 3600

        m = total_second // 60
        total_second = total_second % 60

        s = total_second

        return Time(h, m, s)

    def __sub__(self, other):
        total_second = self.hour * 3600 + self.minute * 60 + self.second

        total_second -= other.hour * 3600 + other.minute * 60 + other.second

        total_second = abs(total_second)

        h = total_second // 3600
        total_second = total_second % 3600

        m = total_second // 60
        total_second = total_second % 60

        s = total_second

        return Time(h, m, s)

    def display(self):
        print(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")


if __name__ == "__main__":
    t1 = Time(1, 20, 40)
    t2 = Time(1, 40, 30)

    res = t1 + t2

    res.display()

    res = t1 - t2

    res.display()
