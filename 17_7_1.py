multipl = 1
n = 1
# пока n меньше 10
while n < 10:
    # увеличиваем n на 1
    n += 1
    # если число четное
    if n % 2 == 0:
        # пропускаем итерацию
        continue
    # а если нечетное, перемножаем
    multipl *= n
# выводим multipl
print(multipl)
