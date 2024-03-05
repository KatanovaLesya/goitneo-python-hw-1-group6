from datetime import datetime, timedelta
from collections import defaultdict, OrderedDict

def get_birthdays_per_week(users):

    date_now = datetime.today().date()                                      #дізнаємось поточну дату
    birthdays_list = defaultdict(list)                                      #створюємо словник

    for user in users:
        birthday = user["birthday"].date()                                  #робимо значення birthday - датою без часу
        birthday_next = birthday.replace(year=date_now.year)                #замінюємо рік на поточний, отримуємо дату наступного birthday 
        if birthday_next < date_now:                                        #якщо день народження в цьому році вже був
            birthday_next = birthday.replace(year=date_now.year+1)          #то міняємо рік на поточний рік +1
        
        if date_now <= birthday_next <= date_now + timedelta(days=7):       #якщо birthday ще небуло і воно має відбутися не більше ніж за 7 днів
            day_week = birthday_next.strftime("%A")                         #день тижня = рядок з назвою робочого дня тижня з великої букви
            if day_week == "Saturday" or day_week == "Sunday":              #якщо день тижня субота чи неділя то обираємо день тижня - понеділок
                day_week = "Monday"
            birthdays_list[day_week].append(user["name"])                   #заповнюємо словник з імʼям працівника днем тижня

    for day, names in birthdays_list.items():                               # отримуємо і ключ і значення
        if names:
            print(f"{day}: {', '.join(names)}")                             # виводимо список


users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Lesia Katanova", "birthday": datetime(1982, 3, 8)},
    {"name": "Mykola Kalishenko", "birthday": datetime(1984, 3, 7)},
    {"name": "Svitlana Chelmekchi", "birthday": datetime(1968, 3, 6)},
    ]

get_birthdays_per_week(users)
