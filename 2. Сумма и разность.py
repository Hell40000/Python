def summ_count(num):
    result_summ = 0
    while num != 0:
        last_digit = num % 10
        result_summ += last_digit
        num //= 10
    return result_summ

def num_count(num):
    count = 0
    while num != 0:
        count += 1
        num //= 10
    return count

num = int(input("Введите число: "))
print(f"Сумма чисел: {summ_count(num)} \nКоличество чисел: {num_count(num)} \nРазность суммы и количества цифр: {summ_count(num) - num_count(num)}")


