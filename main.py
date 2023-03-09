# Программа, которая будет подсчитывать общую стоимость билетов на мероприятие

summ_tickets = int(input("Введите желаемое количество билетов на мероприятие - "))
print(summ_tickets)

count = 0
summ_money = 0

while count < summ_tickets:
    count += 1
    age = int(input("Введите возраст участника - "))
    print(age)
    if 18 <= age < 25:
        summ_money += 990
        print(summ_money)
    elif age >=25:
        summ_money += 1390
        print(summ_money)
    else:
        print(summ_money)

print("Итоговая стоимость билетов равна:")
print(summ_money)
