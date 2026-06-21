import sys

if __name__ == "__main__":
    # Ввести кортеж одной строкой
    A = tuple(map(int, input().split()))

    # Проверить количество элементов кортежа
    if len(A) != 10:
        print("Неверный размер кортежа", file=sys.stderr)
        exit(1)

    # Найти сумму элементов, меньших по модулю 5
    s = 0
    for item in A:
        if abs(item) < 5:
            s += item

    print(s)
