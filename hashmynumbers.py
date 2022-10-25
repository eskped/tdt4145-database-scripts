import math

import pandas as pd

numbers = [4521, 1104, 1631, 2347, 4300, 1121, 932, 7845, 6712, 4321, 3412, 1742, 1111]
modulo = 4


def hash_func(k):
    return "{0:0{length}b}".format(k % modulo, length=int(math.sqrt(modulo)))


def main():
    result = [hash_func(num) for num in numbers]
    data = {"Numbers": numbers, "Hashed": result}

    df = pd.DataFrame(data)

    print("-" * 20 + "\n")
    print(df)
    print("\n" + "-" * 20)


if __name__ == "__main__":
    main()
