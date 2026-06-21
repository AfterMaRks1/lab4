if __name__ == "__main__":
    # Ввести список вещественных чисел одной строкой
    A = list(map(float, input().split()))
    C = float(input("Введите C: "))

    # 1. Количество элементов, больших C
    count = 0
    for item in A:
        if item > C:
            count += 1

    print(f"Количество элементов, больших {C}: {count}")

    # 2. Найти индекс максимального по модулю элемента
    max_index = 0
    for i in range(1, len(A)):
        if abs(A[i]) > abs(A[max_index]):
            max_index = i

    # 3. Произведение элементов после максимального по модулю
    произведение = 1
    for i in range(max_index + 1, len(A)):
        произведение *= A[i]

    if max_index == len(A) - 1:
        print("После максимального по модулю элемента нет элементов")
    else:
        print(
            f"Произведение элементов после максимального по модулю: {произведение:.2f}"
        )
