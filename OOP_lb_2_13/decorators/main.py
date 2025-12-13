from functions import compute, difference


def main():
    print("compute(5.7, 8.2) =", compute(5.7, 8.2))
    print("difference(3.9, 10.1) =", difference(3.9, 10.1))

    try:
        print(compute(5, "abc"))
    except TypeError as e:
        print("Помилка:", e)


if __name__ == "__main__":
    main()
