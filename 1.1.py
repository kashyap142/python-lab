import math


def euclidian_distance(p1, p2):
    if len(p1) != len(p2):
        print("Points should have same number of coordinates")
        return

    sq_dist = sum((x1 - x2) ** 2 for x1, x2 in zip(p1, p2))

    return math.sqrt(sq_dist)


if __name__ == "__main__":
    p1 = tuple(map(int, input("Enter first coordinates: ").split()))

    p2 = tuple(map(int, input("Enter second coordinates: ").split()))

    ans = euclidian_distance(p1, p2)
    if ans is not None:
        print(f"dist is {ans}")
