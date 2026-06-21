import sys

if __name__ == "__main__":
    A = list(map(int, input().split()))

    if not A:
        print("Список пуст!", file=sys.stderr)
        exit(1)

    s = 0
    for item in A:
        if abs(item) < 5:
            s += item

    print(f"Сумма элементов, меньших по модулю 5: {s}")
