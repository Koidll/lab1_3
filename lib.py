def count_common_elements(*lists):
    if not lists:
        return 0
    common = set(lists[0])
    for lst in lists[1:]:
        common &= set(lst)
    return len(common)


if __name__ == "__main__":
    n = int(input("Введите количество списков: "))
    lists = []

    for i in range(n):
        lst = input(f"Введите элементы списка {i + 1}, разделённые пробелом: ").split()
        lists.append(lst)

    result = count_common_elements(*lists)
    print("Количество одинаковых элементов во всех списках:", result)
