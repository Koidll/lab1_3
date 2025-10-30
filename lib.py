

from collections import Counter
from typing import Iterable, Any


def common_elements_count(*lists: Iterable[Any], count_multiplicity: bool = False) -> int:

    if not lists:
        return 0

    # Преобразуем каждый аргумент в список/итерируемый контейнер
    lists = [list(l) for l in lists]

    if not all(isinstance(l, list) for l in lists):
        # на всякий случай — но выше уже привели к list
        lists = [list(l) for l in lists]

    if count_multiplicity:
        # Учитываем кратность: пересечением считается сумма минимальных вхождений
        counters = [Counter(l) for l in lists]
        # общие элементы — пересечение ключей
        common_keys = set(counters[0].keys())
        for c in counters[1:]:
            common_keys &= set(c.keys())
        total = 0
        for key in common_keys:
            # минимальное количество вхождений среди всех списков
            mins = min(c[key] for c in counters)
            total += mins
        return total
    else:
        # Учитываем только уникальные элементы, которые присутствуют в каждом списке
        sets = [set(l) for l in lists]
        common = sets[0]
        for s in sets[1:]:
            common &= s
        return len(common)


if __name__ == "__main__":
    # Небольшие демонстрации
    print(common_elements_count([1, 2, 2, 3], [2, 2, 4, 1], [2, 1]))  # -> 2 (1 и 2)
    print(common_elements_count([1, 2, 2, 3], [2, 2, 4, 1], [2, 1], count_multiplicity=True))  # -> 2
    print(common_elements_count([1, 1, 2], [1, 1, 1, 2], count_multiplicity=True))  # -> 3 (1 минимум 2, 2 минимум 1)
