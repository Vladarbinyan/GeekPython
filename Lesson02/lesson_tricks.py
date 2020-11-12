nums = [
    [1, 2, 3],
    [4, 5, 6],
]
# Объединение списков
joined = sum(nums, [])
print(joined)

# Удалить дубликаты в списке (не оптимальное решение с точки зрения производительности)
unique = [1, 2, 3, 3, 5, 5]
unique = list(set(unique))
print(unique)

# Рокировка значений переменных
a, b = 10, 20
print(f'{a} {b}')
a, b = b, a
print(f'{a} {b}')

# Частотный поиск в списке
total = [1, 2, 3, 3, 5, 5, 5]
print(
    max(
        set(total),
        key=total.count
        )
    )
# Вывод списка с распаковкой
print(*total, end='', sep=',')
