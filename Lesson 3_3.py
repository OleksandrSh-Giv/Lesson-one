def split_list(lst):
    if len(lst) == 0:
        return [[], []]
    middle = (len(lst) + 1) // 2  # Для непарної кількості елементів перший список буде більший
    return [lst[:middle], lst[middle:]]

# Тести
print(split_list([1, 2, 3, 4, 5, 6]))  # [[1, 2, 3], [4, 5, 6]]
print(split_list([1, 2, 3]))           # [[1, 2], [3]]
print(split_list([1, 2, 3, 4, 5]))    # [[1, 2, 3], [4, 5]]
print(split_list([1]))                 # [[1], []]
print(split_list([]))                  # [[], []]
