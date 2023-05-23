def count_year(year):
    count = 0
    while year != 0:
        count += 1
        year //= 10
    return count

first_year = int(input("Введите первый год: "))
second_year = int(input("Введите второй год: "))

if (count_year(first_year) or count_year(second_year)) != 4:
    print("Неверный ввод, попробуйте еще раз")
else:
    print(f"Годы от {first_year} до {second_year} с тремя одинаковыми цифрами:")
    for i in range(first_year, second_year + 1):
        frst_num = i // 1000
        scnd_num = i // 100 % 10
        thrd_num = i // 10 % 10
        frth_num = i % 10
        if frst_num == scnd_num == thrd_num:
            print(frst_num, scnd_num, thrd_num, frth_num, sep = "" )
        elif frst_num == scnd_num == frth_num:
            print(frst_num, scnd_num, thrd_num, frth_num, sep = "")
        elif frst_num == thrd_num == frth_num:
            print(frst_num, scnd_num, thrd_num, frth_num, sep = "")
        elif scnd_num == thrd_num == frth_num:
             print(frst_num, scnd_num, thrd_num, frth_num, sep = "")




