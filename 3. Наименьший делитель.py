num = int(input("Введите ваше число: "))


for i in range(2, num + 1):
    min_delitel = 0
    if num % i == 0:
        min_delitel = i
        break
print(f"Минимальный делитель для числа {num } - {min_delitel}")
