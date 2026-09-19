
# ============================================================
#                 КУТ КУРУЛУШ
#             СТРОИТЕЛЬНАЯ КОМПАНИЯ
#        СИСТЕМА УПРАВЛЕНИЯ КОМПАНИЕЙ
# ============================================================

from datetime import datetime


# ============================================================
# 1. ИНФОРМАЦИЯ О КОМПАНИИ
# ============================================================

company = {
    "name": "Кут Курулуш",
    "city": "Бишкек",
    "country": "Кыргызстан",
    "phone": "+996 555 123 456",
    "email": "kutkurulush@gmail.com",
    "website": "www.kutkurulush.kg",
    "year": 2015,
    "director": "Азамат Бакытбеков"
}


# ============================================================
# 2. СОТРУДНИКИ
# ============================================================

employees = [
    {
        "id": 1,
        "name": "Азамат Бакытбеков",
        "position": "Директор",
        "salary": 150000,
        "experience": 12,
        "phone": "+996 700 111 111",
        "status": "Работает"
    },
    {
        "id": 2,
        "name": "Нурбек Осмонов",
        "position": "Главный инженер",
        "salary": 110000,
        "experience": 9,
        "phone": "+996 700 222 222",
        "status": "Работает"
    },
    {
        "id": 3,
        "name": "Эрмек Садыков",
        "position": "Прораб",
        "salary": 85000,
        "experience": 7,
        "phone": "+996 700 333 333",
        "status": "Работает"
    },
    {
        "id": 4,
        "name": "Бекжан Токтосунов",
        "position": "Архитектор",
        "salary": 95000,
        "experience": 8,
        "phone": "+996 700 444 444",
        "status": "Работает"
    },
    {
        "id": 5,
        "name": "Руслан Иманов",
        "position": "Строитель",
        "salary": 65000,
        "experience": 5,
        "phone": "+996 700 555 555",
        "status": "Работает"
    },
    {
        "id": 6,
        "name": "Талантбек Жумаев",
        "position": "Электрик",
        "salary": 70000,
        "experience": 6,
        "phone": "+996 700 666 666",
        "status": "Работает"
    },
    {
        "id": 7,
        "name": "Каныбек Абдылдаев",
        "position": "Сантехник",
        "salary": 68000,
        "experience": 5,
        "phone": "+996 700 777 777",
        "status": "Работает"
    },
    {
        "id": 8,
        "name": "Марат Алиев",
        "position": "Водитель",
        "salary": 55000,
        "experience": 4,
        "phone": "+996 700 888 888",
        "status": "Работает"
    }
]


# ============================================================
# 3. КЛИЕНТЫ
# ============================================================

clients = [
    {
        "id": 1,
        "name": "Бек Асанбеков",
        "phone": "+996 555 111 222",
        "city": "Бишкек",
        "type": "Частный клиент",
        "projects": 1
    },
    {
        "id": 2,
        "name": "ОсОО Бишкек Бизнес",
        "phone": "+996 555 222 333",
        "city": "Бишкек",
        "type": "Компания",
        "projects": 2
    },
    {
        "id": 3,
        "name": "Нурлан Турсунов",
        "phone": "+996 555 333 444",
        "city": "Чолпон-Ата",
        "type": "Частный клиент",
        "projects": 1
    },
    {
        "id": 4,
        "name": "ОсОО Строй Инвест",
        "phone": "+996 555 444 555",
        "city": "Бишкек",
        "type": "Компания",
        "projects": 3
    }
]


# ============================================================
# 4. СТРОИТЕЛЬНЫЕ ПРОЕКТЫ
# ============================================================

projects = [
    {
        "id": 101,
        "name": "Большой жилой дом",
        "client": "Бек Асанбеков",
        "city": "Бишкек",
        "area": 240,
        "price": 12000000,
        "paid": 5000000,
        "status": "Строительство",
        "progress": 55,
        "workers": 8,
        "start": "2026-03-10",
        "end": "2027-01-20"
    },
    {
        "id": 102,
        "name": "Офисный центр",
        "client": "ОсОО Бишкек Бизнес",
        "city": "Бишкек",
        "area": 850,
        "price": 35000000,
        "paid": 15000000,
        "status": "Фундамент",
        "progress": 25,
        "workers": 15,
        "start": "2026-05-01",
        "end": "2027-05-01"
    },
    {
        "id": 103,
        "name": "Современный коттедж",
        "client": "Нурлан Турсунов",
        "city": "Чолпон-Ата",
        "area": 320,
        "price": 15000000,
        "paid": 12000000,
        "status": "Отделочные работы",
        "progress": 82,
        "workers": 10,
        "start": "2026-01-15",
        "end": "2026-11-30"
    },
    {
        "id": 104,
        "name": "Торговый комплекс",
        "client": "ОсОО Строй Инвест",
        "city": "Бишкек",
        "area": 1500,
        "price": 65000000,
        "paid": 20000000,
        "status": "Проектирование",
        "progress": 10,
        "workers": 5,
        "start": "2026-08-01",
        "end": "2028-01-15"
    }
]


# ============================================================
# 5. СТРОИТЕЛЬНЫЕ МАТЕРИАЛЫ
# ============================================================

materials = {
    "Цемент": {
        "price": 450,
        "unit": "мешок",
        "quantity": 500
    },
    "Кирпич": {
        "price": 18,
        "unit": "шт",
        "quantity": 15000
    },
    "Песок": {
        "price": 2500,
        "unit": "м3",
        "quantity": 100
    },
    "Щебень": {
        "price": 3000,
        "unit": "м3",
        "quantity": 80
    },
    "Арматура": {
        "price": 75000,
        "unit": "тонна",
        "quantity": 15
    },
    "Доска": {
        "price": 28000,
        "unit": "м3",
        "quantity": 40
    },
    "Утеплитель": {
        "price": 1200,
        "unit": "м2",
        "quantity": 800
    },
    "Плитка": {
        "price": 950,
        "unit": "м2",
        "quantity": 600
    },
    "Краска": {
        "price": 1800,
        "unit": "ведро",
        "quantity": 150
    }
}


# ============================================================
# 6. СТРОИТЕЛЬНАЯ ТЕХНИКА
# ============================================================

equipment = [
    {
        "id": 1,
        "name": "Экскаватор",
        "model": "CAT 320",
        "year": 2021,
        "status": "Работает",
        "price": 8500000
    },
    {
        "id": 2,
        "name": "Кран",
        "model": "Liebherr",
        "year": 2020,
        "status": "Свободен",
        "price": 12000000
    },
    {
        "id": 3,
        "name": "Бетономешалка",
        "model": "KAMAZ",
        "year": 2022,
        "status": "Работает",
        "price": 3500000
    },
    {
        "id": 4,
        "name": "Грузовик",
        "model": "MAN",
        "year": 2019,
        "status": "Ремонт",
        "price": 6000000
    },
    {
        "id": 5,
        "name": "Погрузчик",
        "model": "JCB",
        "year": 2023,
        "status": "Свободен",
        "price": 5000000
    }
]


# ============================================================
# 7. РАСХОДЫ
# ============================================================

expenses = [
    {
        "name": "Покупка цемента",
        "amount": 450000,
        "category": "Материалы"
    },
    {
        "name": "Покупка кирпича",
        "amount": 270000,
        "category": "Материалы"
    },
    {
        "name": "Топливо",
        "amount": 180000,
        "category": "Транспорт"
    },
    {
        "name": "Ремонт техники",
        "amount": 320000,
        "category": "Техника"
    },
    {
        "name": "Электричество",
        "amount": 85000,
        "category": "Коммунальные"
    }
]


# ============================================================
# 8. ИНФОРМАЦИЯ О КОМПАНИИ
# ============================================================

def show_company():
    print("\n" + "=" * 60)
    print("ИНФОРМАЦИЯ О КОМПАНИИ")
    print("=" * 60)

    print(f"Название: {company['name']}")
    print(f"Город: {company['city']}")
    print(f"Страна: {company['country']}")
    print(f"Телефон: {company['phone']}")
    print(f"Email: {company['email']}")
    print(f"Сайт: {company['website']}")
    print(f"Год основания: {company['year']}")
    print(f"Директор: {company['director']}")
    print(f"Сотрудников в базе: {len(employees)}")
    print(f"Проектов в базе: {len(projects)}")


# ============================================================
# 9. СОТРУДНИКИ
# ============================================================

def show_employees():
    print("\n" + "=" * 60)
    print("СОТРУДНИКИ")
    print("=" * 60)

    for employee in employees:
        print(f"""
ID: {employee['id']}
Имя: {employee['name']}
Должность: {employee['position']}
Зарплата: {employee['salary']:,} сом
Опыт: {employee['experience']} лет
Телефон: {employee['phone']}
Статус: {employee['status']}
----------------------------------------
""")


# ============================================================
# 10. КЛИЕНТЫ
# ============================================================

def show_clients():
    print("\n" + "=" * 60)
    print("КЛИЕНТЫ")
    print("=" * 60)

    for client in clients:
        print(f"""
ID: {client['id']}
Имя: {client['name']}
Телефон: {client['phone']}
Город: {client['city']}
Тип: {client['type']}
Количество проектов: {client['projects']}
----------------------------------------
""")


# ============================================================
# 11. ПРОЕКТЫ
# ============================================================

def show_projects():
    print("\n" + "=" * 60)
    print("ВСЕ ПРОЕКТЫ")
    print("=" * 60)

    for project in projects:
        print(f"""
ID: {project['id']}
Проект: {project['name']}
Клиент: {project['client']}
Город: {project['city']}
Площадь: {project['area']} м2
Стоимость: {project['price']:,} сом
Оплачено: {project['paid']:,} сом
Осталось оплатить: {project['price'] - project['paid']:,} сом
Статус: {project['status']}
Готовность: {project['progress']}%
Рабочих: {project['workers']}
Начало: {project['start']}
Окончание: {project['end']}
----------------------------------------
""")


# ============================================================
# 12. МАТЕРИАЛЫ
# ============================================================

def show_materials():
    print("\n" + "=" * 60)
    print("СКЛАД МАТЕРИАЛОВ")
    print("=" * 60)

    total = 0

    for name, data in materials.items():
        cost = data["price"] * data["quantity"]
        total += cost

        print(
            f"{name}: "
            f"{data['quantity']} {data['unit']} | "
            f"{data['price']:,} сом | "
            f"Стоимость: {cost:,} сом"
        )

    print("-" * 60)
    print(f"Общая стоимость склада: {total:,} сом")


# ============================================================
# 13. ТЕХНИКА
# ============================================================

def show_equipment():
    print("\n" + "=" * 60)
    print("СТРОИТЕЛЬНАЯ ТЕХНИКА")
    print("=" * 60)

    for item in equipment:
        print(f"""
ID: {item['id']}
Название: {item['name']}
Модель: {item['model']}
Год: {item['year']}
Статус: {item['status']}
Стоимость: {item['price']:,} сом
----------------------------------------
""")


# ============================================================
# 14. РАСЧЁТ СТРОИТЕЛЬСТВА
# ============================================================

def calculate_building():
    print("\n" + "=" * 60)
    print("РАСЧЁТ СТОИМОСТИ СТРОИТЕЛЬСТВА")
    print("=" * 60)

    try:
        area = float(input("Площадь здания (м2): "))
        price = float(input("Цена за 1 м2: "))

        if area <= 0 or price <= 0:
            print("Площадь и цена должны быть больше нуля.")
            return

        building_cost = area * price
        workers_cost = building_cost * 0.15
        transport_cost = building_cost * 0.05
        other_cost = building_cost * 0.10

        total = (
            building_cost
            + workers_cost
            + transport_cost
            + other_cost
        )

        print("\nРАСЧЁТ:")
        print(f"Основная стоимость: {building_cost:,.2f} сом")
        print(f"Работа: {workers_cost:,.2f} сом")
        print(f"Транспорт: {transport_cost:,.2f} сом")
        print(f"Дополнительные расходы: {other_cost:,.2f} сом")
        print("-" * 50)
        print(f"ИТОГО: {total:,.2f} сом")

    except ValueError:
        print("Ошибка! Введите числа.")


# ============================================================
# 15. ДОБАВИТЬ ПРОЕКТ
# ============================================================

def add_project():
    print("\n" + "=" * 60)
    print("ДОБАВЛЕНИЕ НОВОГО ПРОЕКТА")
    print("=" * 60)

    try:
        project_id = int(input("ID проекта: "))

        for project in projects:
            if project["id"] == project_id:
                print("Ошибка: такой ID проекта уже существует.")
                return

        name = input("Название: ").strip()
        client = input("Клиент: ").strip()
        city = input("Город: ").strip()
        area = float(input("Площадь: "))
        price = float(input("Стоимость: "))

        if area <= 0 or price <= 0:
            print("Площадь и стоимость должны быть больше нуля.")
            return

        project = {
            "id": project_id,
            "name": name,
            "client": client,
            "city": city,
            "area": area,
            "price": price,
            "paid": 0,
            "status": "Подготовка",
            "progress": 0,
            "workers": 0,
            "start": str(datetime.now().date()),
            "end": "Не указано"
        }

        projects.append(project)

        print("\nПроект успешно добавлен!")

    except ValueError:
        print("Ошибка! ID, площадь и стоимость должны быть числами.")


# ============================================================
# 16. ПОИСК ПРОЕКТА
# ============================================================

def search_project():
    print("\n" + "=" * 60)
    print("ПОИСК ПРОЕКТА")
    print("=" * 60)

    text = input("Введите название, город или клиента: ").strip().lower()

    if not text:
        print("Введите текст для поиска.")
        return

    found = False

    for project in projects:
        if (
            text in project["name"].lower()
            or text in project["city"].lower()
            or text in project["client"].lower()
        ):
            print(f"""
ID: {project['id']}
Проект: {project['name']}
Клиент: {project['client']}
Город: {project['city']}
Стоимость: {project['price']:,} сом
Статус: {project['status']}
Готовность: {project['progress']}%
""")
            found = True

    if not found:
        print("Ничего не найдено.")


# ============================================================
# 17. ИЗМЕНЕНИЕ СТАТУСА
# ============================================================

def change_status():
    try:
        project_id = int(input("Введите ID проекта: "))

        for project in projects:
            if project["id"] == project_id:
                print("Текущий статус:", project["status"])

                new_status = input("Новый статус: ").strip()

                if not new_status:
                    print("Статус не может быть пустым.")
                    return

                project["status"] = new_status

                print("Статус успешно изменён!")
                return

        print("Проект не найден.")

    except ValueError:
        print("Введите правильный ID.")


# ============================================================
# 18. ИЗМЕНЕНИЕ ПРОГРЕССА
# ============================================================

def change_progress():
    try:
        project_id = int(input("ID проекта: "))
        progress = int(input("Готовность от 0 до 100: "))

        if progress < 0 or progress > 100:
            print("Процент должен быть от 0 до 100.")
            return

        for project in projects:
            if project["id"] == project_id:
                project["progress"] = progress

                if progress == 100:
                    project["status"] = "Завершено"

                print("Готовность проекта обновлена!")
                return

        print("Проект не найден.")

    except ValueError:
        print("Введите числа.")


# ============================================================
# 19. ЗАРПЛАТНЫЙ ОТЧЁТ
# ============================================================

def salary_report():
    print("\n" + "=" * 60)
    print("ФОНД ЗАРПЛАТ")
    print("=" * 60)

    total = 0

    for employee in employees:
        total += employee["salary"]

    if employees:
        average = total / len(employees)
    else:
        average = 0

    print(f"Количество сотрудников: {len(employees)}")
    print(f"Общий фонд зарплаты: {total:,} сом")
    print(f"Средняя зарплата: {average:,.2f} сом")


# ============================================================
# 20. РАСХОДЫ
# ============================================================

def show_expenses():
    print("\n" + "=" * 60)
    print("РАСХОДЫ КОМПАНИИ")
    print("=" * 60)

    total = 0

    for expense in expenses:
        print(
            f"{expense['name']}: "
            f"{expense['amount']:,} сом "
            f"({expense['category']})"
        )

        total += expense["amount"]

    print("-" * 60)
    print(f"Общие расходы: {total:,} сом")


# ============================================================
# 21. ФИНАНСОВЫЙ ОТЧЁТ
# ============================================================

def financial_report():
    print("\n" + "=" * 60)
    print("ФИНАНСОВЫЙ ОТЧЁТ")
    print("=" * 60)

    income = 0

    for project in projects:
        income += project["paid"]

    expenses_total = 0

    for expense in expenses:
        expenses_total += expense["amount"]

    balance = income - expenses_total

    print(f"Получено от клиентов: {income:,} сом")
    print(f"Расходы компании: {expenses_total:,} сом")
    print(f"Баланс: {balance:,} сом")


# ============================================================
# 22. ДОБАВИТЬ ПЛАТЁЖ
# ============================================================

def add_payment():
    try:
        project_id = int(input("ID проекта: "))
        payment = float(input("Сумма платежа: "))

        if payment <= 0:
            print("Сумма платежа должна быть больше нуля.")
            return

        for project in projects:
            if project["id"] == project_id:

                remaining = project["price"] - project["paid"]

                if payment > remaining:
                    print(
                        f"Ошибка! Осталось оплатить "
                        f"{remaining:,.2f} сом."
                    )
                    return

                project["paid"] += payment

                print(
                    f"Платёж {payment:,.2f} сом добавлен!"
                )

                print(
                    f"Всего оплачено: "
                    f"{project['paid']:,.2f} сом"
                )

                return

        print("Проект не найден.")

    except ValueError:
        print("Введите правильные данные.")


# ============================================================
# 23. ДОБАВЛЕНИЕ МАТЕРИАЛА
# ============================================================

def add_material():
    print("\n" + "=" * 60)
    print("ДОБАВЛЕНИЕ МАТЕРИАЛА")
    print("=" * 60)

    name = input("Название материала: ").strip()

    if not name:
        print("Название не может быть пустым.")
        return

    try:
        price = float(input("Цена: "))
        quantity = float(input("Количество: "))
        unit = input("Единица измерения: ").strip()

        if price <= 0 or quantity < 0:
            print("Цена должна быть больше нуля, количество не может быть отрицательным.")
            return

        if not unit:
            print("Укажите единицу измерения.")
            return

        materials[name] = {
            "price": price,
            "unit": unit,
            "quantity": quantity
        }

        print("Материал добавлен на склад!")

    except ValueError:
        print("Ошибка! Цена и количество должны быть числами.")


# ============================================================
# 24. ДОБАВЛЕНИЕ РАСХОДА
# ============================================================

def add_expense():
    print("\n" + "=" * 60)
    print("ДОБАВЛЕНИЕ РАСХОДА")
    print("=" * 60)

    name = input("Название расхода: ").strip()
    category = input("Категория: ").strip()

    try:
        amount = float(input("Сумма: "))

        if amount <= 0:
            print("Сумма должна быть больше нуля.")
            return

        expenses.append({
            "name": name,
            "amount": amount,
            "category": category
        })

        print("Расход успешно добавлен!")

    except ValueError:
        print("Введите число.")


# ============================================================
# 25. СТАТИСТИКА ПРОЕКТОВ
# ============================================================

def project_statistics():
    print("\n" + "=" * 60)
    print("СТАТИСТИКА ПРОЕКТОВ")
    print("=" * 60)

    total = len(projects)
    construction = 0
    finished = 0
    preparation = 0

    for project in projects:
        status = project["status"].lower()

        if "строительство" in status:
            construction += 1

        if "заверш" in status:
            finished += 1

        if "подготов" in status:
            preparation += 1

    print(f"Всего проектов: {total}")
    print(f"В строительстве: {construction}")
    print(f"Завершено: {finished}")
    print(f"На подготовке: {preparation}")


# ============================================================
# 26. ОБЩАЯ СТОИМОСТЬ ПРОЕКТОВ
# ============================================================

def total_projects_cost():
    total = 0

    for project in projects:
        total += project["price"]

    print("\n" + "=" * 60)
    print("ОБЩАЯ СТОИМОСТЬ ПРОЕКТОВ")
    print("=" * 60)

    print(f"{total:,} сом")


# ============================================================
# 27. СТОИМОСТЬ ТЕХНИКИ
# ============================================================

def equipment_cost():
    total = 0

    for item in equipment:
        total += item["price"]

    print("\n" + "=" * 60)
    print("СТОИМОСТЬ ТЕХНИКИ")
    print("=" * 60)

    print(f"Общая стоимость техники: {total:,} сом")


# ============================================================
# 28. ДОБАВЛЕНИЕ СОТРУДНИКА
# ============================================================

def add_employee():
    print("\n" + "=" * 60)
    print("ДОБАВЛЕНИЕ СОТРУДНИКА")
    print("=" * 60)

    try:
        employee_id = int(input("ID сотрудника: "))

        for employee in employees:
            if employee["id"] == employee_id:
                print("Такой ID уже существует.")
                return

        name = input("Имя: ").strip()
        position = input("Должность: ").strip()
        salary = float(input("Зарплата: "))
        experience = int(input("Опыт работы: "))
        phone = input("Телефон: ").strip()

        if salary <= 0 or experience < 0:
            print("Проверьте зарплату и опыт.")
            return

        employees.append({
            "id": employee_id,
            "name": name,
            "position": position,
            "salary": salary,
            "experience": experience,
            "phone": phone,
            "status": "Работает"
        })

        print("Сотрудник успешно добавлен!")

    except ValueError:
        print("Ошибка ввода.")


# ============================================================
# 29. ПОИСК СОТРУДНИКА
# ============================================================

def search_employee():
    print("\n" + "=" * 60)
    print("ПОИСК СОТРУДНИКА")
    print("=" * 60)

    text = input("Введите имя или должность: ").strip().lower()

    if not text:
        print("Введите данные для поиска.")
        return

    found = False

    for employee in employees:
        if (
            text in employee["name"].lower()
            or text in employee["position"].lower()
        ):
            print(f"""
ID: {employee['id']}
Имя: {employee['name']}
Должность: {employee['position']}
Зарплата: {employee['salary']:,} сом
Телефон: {employee['phone']}
Статус: {employee['status']}
""")
            found = True

    if not found:
        print("Сотрудник не найден.")


# ============================================================
# 30. ОБЩИЙ ОТЧЁТ
# ============================================================

def full_report():
    print("\n" + "=" * 60)
    print("ОБЩИЙ ОТЧЁТ КОМПАНИИ")
    print("=" * 60)

    project_sum = sum(project["price"] for project in projects)
    paid_sum = sum(project["paid"] for project in projects)
    expense_sum = sum(expense["amount"] for expense in expenses)
    salary_sum = sum(employee["salary"] for employee in employees)
    equipment_sum = sum(item["price"] for item in equipment)

    print(f"Сотрудников: {len(employees)}")
    print(f"Клиентов: {len(clients)}")
    print(f"Проектов: {len(projects)}")
    print(f"Стоимость всех проектов: {project_sum:,} сом")
    print(f"Получено от клиентов: {paid_sum:,} сом")
    print(f"Расходы: {expense_sum:,} сом")
    print(f"Фонд зарплаты: {salary_sum:,} сом")
    print(f"Стоимость техники: {equipment_sum:,} сом")


# ============================================================
# 31. ГЛАВНОЕ МЕНЮ
# ============================================================

def main():

    while True:

        print("\n")
        print("=" * 65)
        print("              КУТ КУРУЛУШ")
        print("          СТРОИТЕЛЬНАЯ КОМПАНИЯ")
        print("=" * 65)

        print("""
1.  Информация о компании
2.  Сотрудники
3.  Клиенты
4.  Все проекты
5.  Материалы
6.  Строительная техника
7.  Рассчитать строительство
8.  Добавить проект
9.  Найти проект
10. Изменить статус проекта
11. Изменить готовность проекта
12. Зарплатный отчёт
13. Расходы
14. Финансовый отчёт
15. Добавить платёж
16. Добавить материал
17. Добавить расход
18. Статистика проектов
19. Общая стоимость проектов
20. Стоимость техники
21. Добавить сотрудника
22. Найти сотрудника
23. Общий отчёт
0.  Выход
""")

        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            show_company()

        elif choice == "2":
            show_employees()

        elif choice == "3":
            show_clients()

        elif choice == "4":
            show_projects()

        elif choice == "5":
            show_materials()

        elif choice == "6":
            show_equipment()

        elif choice == "7":
            calculate_building()

        elif choice == "8":
            add_project()

        elif choice == "9":
            search_project()

        elif choice == "10":
            change_status()

        elif choice == "11":
            change_progress()

        elif choice == "12":
            salary_report()

        elif choice == "13":
            show_expenses()

        elif choice == "14":
            financial_report()

        elif choice == "15":
            add_payment()

        elif choice == "16":
            add_material()

        elif choice == "17":
            add_expense()

        elif choice == "18":
            project_statistics()

        elif choice == "19":
            total_projects_cost()

        elif choice == "20":
            equipment_cost()

        elif choice == "21":
            add_employee()

        elif choice == "22":
            search_employee()

        elif choice == "23":
            full_report()

        elif choice == "0":
            print("\n" + "=" * 60)
            print("Спасибо за использование программы!")
            print("КУТ КУРУЛУШ")
            print("Строим качественно и надёжно!")
            print("=" * 60)
            break

        else:
            print("\nОшибка! Выберите пункт от 0 до 23.")


# ============================================================
# ЗАПУСК ПРОГРАММЫ
# ============================================================

if __name__ == "__main__":
    main()


# ============================================================
#                 КУТ КУРУЛУШ
#             СТРОИТЕЛЬНАЯ КОМПАНИЯ
#        СИСТЕМА УПРАВЛЕНИЯ КОМПАНИЕЙ
# ============================================================

from datetime import datetime


# ============================================================
# 1. ИНФОРМАЦИЯ О КОМПАНИИ
# ============================================================

company = {
    "name": "Кут Курулуш",
    "city": "Бишкек",
    "country": "Кыргызстан",
    "phone": "+996 555 123 456",
    "email": "kutkurulush@gmail.com",
    "website": "www.kutkurulush.kg",
    "year": 2015,
    "director": "Азамат Бакытбеков"
}


# ============================================================
# 2. СОТРУДНИКИ
# ============================================================

employees = [
    {
        "id": 1,
        "name": "Азамат Бакытбеков",
        "position": "Директор",
        "salary": 150000,
        "experience": 12,
        "phone": "+996 700 111 111",
        "status": "Работает"
    },
    {
        "id": 2,
        "name": "Нурбек Осмонов",
        "position": "Главный инженер",
        "salary": 110000,
        "experience": 9,
        "phone": "+996 700 222 222",
        "status": "Работает"
    },
    {
        "id": 3,
        "name": "Эрмек Садыков",
        "position": "Прораб",
        "salary": 85000,
        "experience": 7,
        "phone": "+996 700 333 333",
        "status": "Работает"
    },
    {
        "id": 4,
        "name": "Бекжан Токтосунов",
        "position": "Архитектор",
        "salary": 95000,
        "experience": 8,
        "phone": "+996 700 444 444",
        "status": "Работает"
    },
    {
        "id": 5,
        "name": "Руслан Иманов",
        "position": "Строитель",
        "salary": 65000,
        "experience": 5,
        "phone": "+996 700 555 555",
        "status": "Работает"
    },
    {
        "id": 6,
        "name": "Талантбек Жумаев",
        "position": "Электрик",
        "salary": 70000,
        "experience": 6,
        "phone": "+996 700 666 666",
        "status": "Работает"
    },
    {
        "id": 7,
        "name": "Каныбек Абдылдаев",
        "position": "Сантехник",
        "salary": 68000,
        "experience": 5,
        "phone": "+996 700 777 777",
        "status": "Работает"
    },
    {
        "id": 8,
        "name": "Марат Алиев",
        "position": "Водитель",
        "salary": 55000,
        "experience": 4,
        "phone": "+996 700 888 888",
        "status": "Работает"
    }
]


# ============================================================
# 3. КЛИЕНТЫ
# ============================================================

clients = [
    {
        "id": 1,
        "name": "Бек Асанбеков",
        "phone": "+996 555 111 222",
        "city": "Бишкек",
        "type": "Частный клиент",
        "projects": 1
    },
    {
        "id": 2,
        "name": "ОсОО Бишкек Бизнес",
        "phone": "+996 555 222 333",
        "city": "Бишкек",
        "type": "Компания",
        "projects": 2
    },
    {
        "id": 3,
        "name": "Нурлан Турсунов",
        "phone": "+996 555 333 444",
        "city": "Чолпон-Ата",
        "type": "Частный клиент",
        "projects": 1
    },
    {
        "id": 4,
        "name": "ОсОО Строй Инвест",
        "phone": "+996 555 444 555",
        "city": "Бишкек",
        "type": "Компания",
        "projects": 3
    }
]


# ============================================================
# 4. СТРОИТЕЛЬНЫЕ ПРОЕКТЫ
# ============================================================

projects = [
    {
        "id": 101,
        "name": "Большой жилой дом",
        "client": "Бек Асанбеков",
        "city": "Бишкек",
        "area": 240,
        "price": 12000000,
        "paid": 5000000,
        "status": "Строительство",
        "progress": 55,
        "workers": 8,
        "start": "2026-03-10",
        "end": "2027-01-20"
    },
    {
        "id": 102,
        "name": "Офисный центр",
        "client": "ОсОО Бишкек Бизнес",
        "city": "Бишкек",
        "area": 850,
        "price": 35000000,
        "paid": 15000000,
        "status": "Фундамент",
        "progress": 25,
        "workers": 15,
        "start": "2026-05-01",
        "end": "2027-05-01"
    },
    {
        "id": 103,
        "name": "Современный коттедж",
        "client": "Нурлан Турсунов",
        "city": "Чолпон-Ата",
        "area": 320,
        "price": 15000000,
        "paid": 12000000,
        "status": "Отделочные работы",
        "progress": 82,
        "workers": 10,
        "start": "2026-01-15",
        "end": "2026-11-30"
    },
    {
        "id": 104,
        "name": "Торговый комплекс",
        "client": "ОсОО Строй Инвест",
        "city": "Бишкек",
        "area": 1500,
        "price": 65000000,
        "paid": 20000000,
        "status": "Проектирование",
        "progress": 10,
        "workers": 5,
        "start": "2026-08-01",
        "end": "2028-01-15"
    }
]


# ============================================================
# 5. СТРОИТЕЛЬНЫЕ МАТЕРИАЛЫ
# ============================================================

materials = {
    "Цемент": {
        "price": 450,
        "unit": "мешок",
        "quantity": 500
    },
    "Кирпич": {
        "price": 18,
        "unit": "шт",
        "quantity": 15000
    },
    "Песок": {
        "price": 2500,
        "unit": "м3",
        "quantity": 100
    },
    "Щебень": {
        "price": 3000,
        "unit": "м3",
        "quantity": 80
    },
    "Арматура": {
        "price": 75000,
        "unit": "тонна",
        "quantity": 15
    },
    "Доска": {
        "price": 28000,
        "unit": "м3",
        "quantity": 40
    },
    "Утеплитель": {
        "price": 1200,
        "unit": "м2",
        "quantity": 800
    },
    "Плитка": {
        "price": 950,
        "unit": "м2",
        "quantity": 600
    },
    "Краска": {
        "price": 1800,
        "unit": "ведро",
        "quantity": 150
    }
}


# ============================================================
# 6. СТРОИТЕЛЬНАЯ ТЕХНИКА
# ============================================================

equipment = [
    {
        "id": 1,
        "name": "Экскаватор",
        "model": "CAT 320",
        "year": 2021,
        "status": "Работает",
        "price": 8500000
    },
    {
        "id": 2,
        "name": "Кран",
        "model": "Liebherr",
        "year": 2020,
        "status": "Свободен",
        "price": 12000000
    },
    {
        "id": 3,
        "name": "Бетономешалка",
        "model": "KAMAZ",
        "year": 2022,
        "status": "Работает",
        "price": 3500000
    },
    {
        "id": 4,
        "name": "Грузовик",
        "model": "MAN",
        "year": 2019,
        "status": "Ремонт",
        "price": 6000000
    },
    {
        "id": 5,
        "name": "Погрузчик",
        "model": "JCB",
        "year": 2023,
        "status": "Свободен",
        "price": 5000000
    }
]


# ============================================================
# 7. РАСХОДЫ
# ============================================================

expenses = [
    {
        "name": "Покупка цемента",
        "amount": 450000,
        "category": "Материалы"
    },
    {
        "name": "Покупка кирпича",
        "amount": 270000,
        "category": "Материалы"
    },
    {
        "name": "Топливо",
        "amount": 180000,
        "category": "Транспорт"
    },
    {
        "name": "Ремонт техники",
        "amount": 320000,
        "category": "Техника"
    },
    {
        "name": "Электричество",
        "amount": 85000,
        "category": "Коммунальные"
    }
]


# ============================================================
# 8. ИНФОРМАЦИЯ О КОМПАНИИ
# ============================================================

def show_company():
    print("\n" + "=" * 60)
    print("ИНФОРМАЦИЯ О КОМПАНИИ")
    print("=" * 60)

    print(f"Название: {company['name']}")
    print(f"Город: {company['city']}")
    print(f"Страна: {company['country']}")
    print(f"Телефон: {company['phone']}")
    print(f"Email: {company['email']}")
    print(f"Сайт: {company['website']}")
    print(f"Год основания: {company['year']}")
    print(f"Директор: {company['director']}")
    print(f"Сотрудников в базе: {len(employees)}")
    print(f"Проектов в базе: {len(projects)}")


# ============================================================
# 9. СОТРУДНИКИ
# ============================================================

def show_employees():
    print("\n" + "=" * 60)
    print("СОТРУДНИКИ")
    print("=" * 60)

    for employee in employees:
        print(f"""
ID: {employee['id']}
Имя: {employee['name']}
Должность: {employee['position']}
Зарплата: {employee['salary']:,} сом
Опыт: {employee['experience']} лет
Телефон: {employee['phone']}
Статус: {employee['status']}
----------------------------------------
""")


# ============================================================
# 10. КЛИЕНТЫ
# ============================================================

def show_clients():
    print("\n" + "=" * 60)
    print("КЛИЕНТЫ")
    print("=" * 60)

    for client in clients:
        print(f"""
ID: {client['id']}
Имя: {client['name']}
Телефон: {client['phone']}
Город: {client['city']}
Тип: {client['type']}
Количество проектов: {client['projects']}
----------------------------------------
""")


# ============================================================
# 11. ПРОЕКТЫ
# ============================================================

def show_projects():
    print("\n" + "=" * 60)
    print("ВСЕ ПРОЕКТЫ")
    print("=" * 60)

    for project in projects:
        print(f"""
ID: {project['id']}
Проект: {project['name']}
Клиент: {project['client']}
Город: {project['city']}
Площадь: {project['area']} м2
Стоимость: {project['price']:,} сом
Оплачено: {project['paid']:,} сом
Осталось оплатить: {project['price'] - project['paid']:,} сом
Статус: {project['status']}
Готовность: {project['progress']}%
Рабочих: {project['workers']}
Начало: {project['start']}
Окончание: {project['end']}
----------------------------------------
""")


# ============================================================
# 12. МАТЕРИАЛЫ
# ============================================================

def show_materials():
    print("\n" + "=" * 60)
    print("СКЛАД МАТЕРИАЛОВ")
    print("=" * 60)

    total = 0

    for name, data in materials.items():
        cost = data["price"] * data["quantity"]
        total += cost

        print(
            f"{name}: "
            f"{data['quantity']} {data['unit']} | "
            f"{data['price']:,} сом | "
            f"Стоимость: {cost:,} сом"
        )

    print("-" * 60)
    print(f"Общая стоимость склада: {total:,} сом")


# ============================================================
# 13. ТЕХНИКА
# ============================================================

def show_equipment():
    print("\n" + "=" * 60)
    print("СТРОИТЕЛЬНАЯ ТЕХНИКА")
    print("=" * 60)

    for item in equipment:
        print(f"""
ID: {item['id']}
Название: {item['name']}
Модель: {item['model']}
Год: {item['year']}
Статус: {item['status']}
Стоимость: {item['price']:,} сом
----------------------------------------
""")


# ============================================================
# 14. РАСЧЁТ СТРОИТЕЛЬСТВА
# ============================================================

def calculate_building():
    print("\n" + "=" * 60)
    print("РАСЧЁТ СТОИМОСТИ СТРОИТЕЛЬСТВА")
    print("=" * 60)

    try:
        area = float(input("Площадь здания (м2): "))
        price = float(input("Цена за 1 м2: "))

        if area <= 0 or price <= 0:
            print("Площадь и цена должны быть больше нуля.")
            return

        building_cost = area * price
        workers_cost = building_cost * 0.15
        transport_cost = building_cost * 0.05
        other_cost = building_cost * 0.10

        total = (
            building_cost
            + workers_cost
            + transport_cost
            + other_cost
        )

        print("\nРАСЧЁТ:")
        print(f"Основная стоимость: {building_cost:,.2f} сом")
        print(f"Работа: {workers_cost:,.2f} сом")
        print(f"Транспорт: {transport_cost:,.2f} сом")
        print(f"Дополнительные расходы: {other_cost:,.2f} сом")
        print("-" * 50)
        print(f"ИТОГО: {total:,.2f} сом")

    except ValueError:
        print("Ошибка! Введите числа.")


# ============================================================
# 15. ДОБАВИТЬ ПРОЕКТ
# ============================================================

def add_project():
    print("\n" + "=" * 60)
    print("ДОБАВЛЕНИЕ НОВОГО ПРОЕКТА")
    print("=" * 60)

    try:
        project_id = int(input("ID проекта: "))

        for project in projects:
            if project["id"] == project_id:
                print("Ошибка: такой ID проекта уже существует.")
                return

        name = input("Название: ").strip()
        client = input("Клиент: ").strip()
        city = input("Город: ").strip()
        area = float(input("Площадь: "))
        price = float(input("Стоимость: "))

        if area <= 0 or price <= 0:
            print("Площадь и стоимость должны быть больше нуля.")
            return

        project = {
            "id": project_id,
            "name": name,
            "client": client,
            "city": city,
            "area": area,
            "price": price,
            "paid": 0,
            "status": "Подготовка",
            "progress": 0,
            "workers": 0,
            "start": str(datetime.now().date()),
            "end": "Не указано"
        }

        projects.append(project)

        print("\nПроект успешно добавлен!")

    except ValueError:
        print("Ошибка! ID, площадь и стоимость должны быть числами.")


# ============================================================
# 16. ПОИСК ПРОЕКТА
# ============================================================

def search_project():
    print("\n" + "=" * 60)
    print("ПОИСК ПРОЕКТА")
    print("=" * 60)

    text = input("Введите название, город или клиента: ").strip().lower()

    if not text:
        print("Введите текст для поиска.")
        return

    found = False

    for project in projects:
        if (
            text in project["name"].lower()
            or text in project["city"].lower()
            or text in project["client"].lower()
        ):
            print(f"""
ID: {project['id']}
Проект: {project['name']}
Клиент: {project['client']}
Город: {project['city']}
Стоимость: {project['price']:,} сом
Статус: {project['status']}
Готовность: {project['progress']}%
""")
            found = True

    if not found:
        print("Ничего не найдено.")


# ============================================================
# 17. ИЗМЕНЕНИЕ СТАТУСА
# ============================================================

def change_status():
    try:
        project_id = int(input("Введите ID проекта: "))

        for project in projects:
            if project["id"] == project_id:
                print("Текущий статус:", project["status"])

                new_status = input("Новый статус: ").strip()

                if not new_status:
                    print("Статус не может быть пустым.")
                    return

                project["status"] = new_status

                print("Статус успешно изменён!")
                return

        print("Проект не найден.")

    except ValueError:
        print("Введите правильный ID.")


# ============================================================
# 18. ИЗМЕНЕНИЕ ПРОГРЕССА
# ============================================================

def change_progress():
    try:
        project_id = int(input("ID проекта: "))
        progress = int(input("Готовность от 0 до 100: "))

        if progress < 0 or progress > 100:
            print("Процент должен быть от 0 до 100.")
            return

        for project in projects:
            if project["id"] == project_id:
                project["progress"] = progress

                if progress == 100:
                    project["status"] = "Завершено"

                print("Готовность проекта обновлена!")
                return

        print("Проект не найден.")

    except ValueError:
        print("Введите числа.")


# ============================================================
# 19. ЗАРПЛАТНЫЙ ОТЧЁТ
# ============================================================

def salary_report():
    print("\n" + "=" * 60)
    print("ФОНД ЗАРПЛАТ")
    print("=" * 60)

    total = 0

    for employee in employees:
        total += employee["salary"]

    if employees:
        average = total / len(employees)
    else:
        average = 0

    print(f"Количество сотрудников: {len(employees)}")
    print(f"Общий фонд зарплаты: {total:,} сом")
    print(f"Средняя зарплата: {average:,.2f} сом")


# ============================================================
# 20. РАСХОДЫ
# ============================================================

def show_expenses():
    print("\n" + "=" * 60)
    print("РАСХОДЫ КОМПАНИИ")
    print("=" * 60)

    total = 0

    for expense in expenses:
        print(
            f"{expense['name']}: "
            f"{expense['amount']:,} сом "
            f"({expense['category']})"
        )

        total += expense["amount"]

    print("-" * 60)
    print(f"Общие расходы: {total:,} сом")


# ============================================================
# 21. ФИНАНСОВЫЙ ОТЧЁТ
# ============================================================

def financial_report():
    print("\n" + "=" * 60)
    print("ФИНАНСОВЫЙ ОТЧЁТ")
    print("=" * 60)

    income = 0

    for project in projects:
        income += project["paid"]

    expenses_total = 0

    for expense in expenses:
        expenses_total += expense["amount"]

    balance = income - expenses_total

    print(f"Получено от клиентов: {income:,} сом")
    print(f"Расходы компании: {expenses_total:,} сом")
    print(f"Баланс: {balance:,} сом")


# ============================================================
# 22. ДОБАВИТЬ ПЛАТЁЖ
# ============================================================

def add_payment():
    try:
        project_id = int(input("ID проекта: "))
        payment = float(input("Сумма платежа: "))

        if payment <= 0:
            print("Сумма платежа должна быть больше нуля.")
            return

        for project in projects:
            if project["id"] == project_id:

                remaining = project["price"] - project["paid"]

                if payment > remaining:
                    print(
                        f"Ошибка! Осталось оплатить "
                        f"{remaining:,.2f} сом."
                    )
                    return

                project["paid"] += payment

                print(
                    f"Платёж {payment:,.2f} сом добавлен!"
                )

                print(
                    f"Всего оплачено: "
                    f"{project['paid']:,.2f} сом"
                )

                return

        print("Проект не найден.")

    except ValueError:
        print("Введите правильные данные.")


# ============================================================
# 23. ДОБАВЛЕНИЕ МАТЕРИАЛА
# ============================================================

def add_material():
    print("\n" + "=" * 60)
    print("ДОБАВЛЕНИЕ МАТЕРИАЛА")
    print("=" * 60)

    name = input("Название материала: ").strip()

    if not name:
        print("Название не может быть пустым.")
        return

    try:
        price = float(input("Цена: "))
        quantity = float(input("Количество: "))
        unit = input("Единица измерения: ").strip()

        if price <= 0 or quantity < 0:
            print("Цена должна быть больше нуля, количество не может быть отрицательным.")
            return

        if not unit:
            print("Укажите единицу измерения.")
            return

        materials[name] = {
            "price": price,
            "unit": unit,
            "quantity": quantity
        }

        print("Материал добавлен на склад!")

    except ValueError:
        print("Ошибка! Цена и количество должны быть числами.")


# ============================================================
# 24. ДОБАВЛЕНИЕ РАСХОДА
# ============================================================

def add_expense():
    print("\n" + "=" * 60)
    print("ДОБАВЛЕНИЕ РАСХОДА")
    print("=" * 60)

    name = input("Название расхода: ").strip()
    category = input("Категория: ").strip()

    try:
        amount = float(input("Сумма: "))

        if amount <= 0:
            print("Сумма должна быть больше нуля.")
            return

        expenses.append({
            "name": name,
            "amount": amount,
            "category": category
        })

        print("Расход успешно добавлен!")

    except ValueError:
        print("Введите число.")


# ============================================================
# 25. СТАТИСТИКА ПРОЕКТОВ
# ============================================================

def project_statistics():
    print("\n" + "=" * 60)
    print("СТАТИСТИКА ПРОЕКТОВ")
    print("=" * 60)

    total = len(projects)
    construction = 0
    finished = 0
    preparation = 0

    for project in projects:
        status = project["status"].lower()

        if "строительство" in status:
            construction += 1

        if "заверш" in status:
            finished += 1

        if "подготов" in status:
            preparation += 1

    print(f"Всего проектов: {total}")
    print(f"В строительстве: {construction}")
    print(f"Завершено: {finished}")
    print(f"На подготовке: {preparation}")


# ============================================================
# 26. ОБЩАЯ СТОИМОСТЬ ПРОЕКТОВ
# ============================================================

def total_projects_cost():
    total = 0

    for project in projects:
        total += project["price"]

    print("\n" + "=" * 60)
    print("ОБЩАЯ СТОИМОСТЬ ПРОЕКТОВ")
    print("=" * 60)

    print(f"{total:,} сом")


# ============================================================
# 27. СТОИМОСТЬ ТЕХНИКИ
# ============================================================

def equipment_cost():
    total = 0

    for item in equipment:
        total += item["price"]

    print("\n" + "=" * 60)
    print("СТОИМОСТЬ ТЕХНИКИ")
    print("=" * 60)

    print(f"Общая стоимость техники: {total:,} сом")


# ============================================================
# 28. ДОБАВЛЕНИЕ СОТРУДНИКА
# ============================================================

def add_employee():
    print("\n" + "=" * 60)
    print("ДОБАВЛЕНИЕ СОТРУДНИКА")
    print("=" * 60)

    try:
        employee_id = int(input("ID сотрудника: "))

        for employee in employees:
            if employee["id"] == employee_id:
                print("Такой ID уже существует.")
                return

        name = input("Имя: ").strip()
        position = input("Должность: ").strip()
        salary = float(input("Зарплата: "))
        experience = int(input("Опыт работы: "))
        phone = input("Телефон: ").strip()

        if salary <= 0 or experience < 0:
            print("Проверьте зарплату и опыт.")
            return

        employees.append({
            "id": employee_id,
            "name": name,
            "position": position,
            "salary": salary,
            "experience": experience,
            "phone": phone,
            "status": "Работает"
        })

        print("Сотрудник успешно добавлен!")

    except ValueError:
        print("Ошибка ввода.")


# ============================================================
# 29. ПОИСК СОТРУДНИКА
# ============================================================

def search_employee():
    print("\n" + "=" * 60)
    print("ПОИСК СОТРУДНИКА")
    print("=" * 60)

    text = input("Введите имя или должность: ").strip().lower()

    if not text:
        print("Введите данные для поиска.")
        return

    found = False

    for employee in employees:
        if (
            text in employee["name"].lower()
            or text in employee["position"].lower()
        ):
            print(f"""
ID: {employee['id']}
Имя: {employee['name']}
Должность: {employee['position']}
Зарплата: {employee['salary']:,} сом
Телефон: {employee['phone']}
Статус: {employee['status']}
""")
            found = True

    if not found:
        print("Сотрудник не найден.")


# ============================================================
# 30. ОБЩИЙ ОТЧЁТ
# ============================================================

def full_report():
    print("\n" + "=" * 60)
    print("ОБЩИЙ ОТЧЁТ КОМПАНИИ")
    print("=" * 60)

    project_sum = sum(project["price"] for project in projects)
    paid_sum = sum(project["paid"] for project in projects)
    expense_sum = sum(expense["amount"] for expense in expenses)
    salary_sum = sum(employee["salary"] for employee in employees)
    equipment_sum = sum(item["price"] for item in equipment)

    print(f"Сотрудников: {len(employees)}")
    print(f"Клиентов: {len(clients)}")
    print(f"Проектов: {len(projects)}")
    print(f"Стоимость всех проектов: {project_sum:,} сом")
    print(f"Получено от клиентов: {paid_sum:,} сом")
    print(f"Расходы: {expense_sum:,} сом")
    print(f"Фонд зарплаты: {salary_sum:,} сом")
    print(f"Стоимость техники: {equipment_sum:,} сом")


# ============================================================
# 31. ГЛАВНОЕ МЕНЮ
# ============================================================

def main():

    while True:

        print("\n")
        print("=" * 65)
        print("              КУТ КУРУЛУШ")
        print("          СТРОИТЕЛЬНАЯ КОМПАНИЯ")
        print("=" * 65)

        print("""
1.  Информация о компании
2.  Сотрудники
3.  Клиенты
4.  Все проекты
5.  Материалы
6.  Строительная техника
7.  Рассчитать строительство
8.  Добавить проект
9.  Найти проект
10. Изменить статус проекта
11. Изменить готовность проекта
12. Зарплатный отчёт
13. Расходы
14. Финансовый отчёт
15. Добавить платёж
16. Добавить материал
17. Добавить расход
18. Статистика проектов
19. Общая стоимость проектов
20. Стоимость техники
21. Добавить сотрудника
22. Найти сотрудника
23. Общий отчёт
0.  Выход
""")

        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            show_company()

        elif choice == "2":
            show_employees()

        elif choice == "3":
            show_clients()

        elif choice == "4":
            show_projects()

        elif choice == "5":
            show_materials()

        elif choice == "6":
            show_equipment()

        elif choice == "7":
            calculate_building()

        elif choice == "8":
            add_project()

        elif choice == "9":
            search_project()

        elif choice == "10":
            change_status()

        elif choice == "11":
            change_progress()

        elif choice == "12":
            salary_report()

        elif choice == "13":
            show_expenses()

        elif choice == "14":
            financial_report()

        elif choice == "15":
            add_payment()

        elif choice == "16":
            add_material()

        elif choice == "17":
            add_expense()

        elif choice == "18":
            project_statistics()

        elif choice == "19":
            total_projects_cost()

        elif choice == "20":
            equipment_cost()

        elif choice == "21":
            add_employee()

        elif choice == "22":
            search_employee()

        elif choice == "23":
            full_report()

        elif choice == "0":
            print("\n" + "=" * 60)
            print("Спасибо за использование программы!")
            print("КУТ КУРУЛУШ")
            print("Строим качественно и надёжно!")
            print("=" * 60)
            break

        else:
            print("\nОшибка! Выберите пункт от 0 до 23.")


# ============================================================
# ЗАПУСК ПРОГРАММЫ
# ============================================================

if __name__ == "__main__":
    main()


# ============================================================
#                 КУТ КУРУЛУШ
#             СТРОИТЕЛЬНАЯ КОМПАНИЯ
#        СИСТЕМА УПРАВЛЕНИЯ КОМПАНИЕЙ
# ============================================================

from datetime import datetime


# ============================================================
# 1. ИНФОРМАЦИЯ О КОМПАНИИ
# ============================================================

company = {
    "name": "Кут Курулуш",
    "city": "Бишкек",
    "country": "Кыргызстан",
    "phone": "+996 555 123 456",
    "email": "kutkurulush@gmail.com",
    "website": "www.kutkurulush.kg",
    "year": 2015,
    "director": "Азамат Бакытбеков"
}


# ============================================================
# 2. СОТРУДНИКИ
# ============================================================

employees = [
    {
        "id": 1,
        "name": "Азамат Бакытбеков",
        "position": "Директор",
        "salary": 150000,
        "experience": 12,
        "phone": "+996 700 111 111",
        "status": "Работает"
    },
    {
        "id": 2,
        "name": "Нурбек Осмонов",
        "position": "Главный инженер",
        "salary": 110000,
        "experience": 9,
        "phone": "+996 700 222 222",
        "status": "Работает"
    },
    {
        "id": 3,
        "name": "Эрмек Садыков",
        "position": "Прораб",
        "salary": 85000,
        "experience": 7,
        "phone": "+996 700 333 333",
        "status": "Работает"
    },
    {
        "id": 4,
        "name": "Бекжан Токтосунов",
        "position": "Архитектор",
        "salary": 95000,
        "experience": 8,
        "phone": "+996 700 444 444",
        "status": "Работает"
    },
    {
        "id": 5,
        "name": "Руслан Иманов",
        "position": "Строитель",
        "salary": 65000,
        "experience": 5,
        "phone": "+996 700 555 555",
        "status": "Работает"
    },
    {
        "id": 6,
        "name": "Талантбек Жумаев",
        "position": "Электрик",
        "salary": 70000,
        "experience": 6,
        "phone": "+996 700 666 666",
        "status": "Работает"
    },
    {
        "id": 7,
        "name": "Каныбек Абдылдаев",
        "position": "Сантехник",
        "salary": 68000,
        "experience": 5,
        "phone": "+996 700 777 777",
        "status": "Работает"
    },
    {
        "id": 8,
        "name": "Марат Алиев",
        "position": "Водитель",
        "salary": 55000,
        "experience": 4,
        "phone": "+996 700 888 888",
        "status": "Работает"
    }
]


# ============================================================
# 3. КЛИЕНТЫ
# ============================================================

clients = [
    {
        "id": 1,
        "name": "Бек Асанбеков",
        "phone": "+996 555 111 222",
        "city": "Бишкек",
        "type": "Частный клиент",
        "projects": 1
    },
    {
        "id": 2,
        "name": "ОсОО Бишкек Бизнес",
        "phone": "+996 555 222 333",
        "city": "Бишкек",
        "type": "Компания",
        "projects": 2
    },
    {
        "id": 3,
        "name": "Нурлан Турсунов",
        "phone": "+996 555 333 444",
        "city": "Чолпон-Ата",
        "type": "Частный клиент",
        "projects": 1
    },
    {
        "id": 4,
        "name": "ОсОО Строй Инвест",
        "phone": "+996 555 444 555",
        "city": "Бишкек",
        "type": "Компания",
        "projects": 3
    }
]


# ============================================================
# 4. СТРОИТЕЛЬНЫЕ ПРОЕКТЫ
# ============================================================

projects = [
    {
        "id": 101,
        "name": "Большой жилой дом",
        "client": "Бек Асанбеков",
        "city": "Бишкек",
        "area": 240,
        "price": 12000000,
        "paid": 5000000,
        "status": "Строительство",
        "progress": 55,
        "workers": 8,
        "start": "2026-03-10",
        "end": "2027-01-20"
    },
    {
        "id": 102,
        "name": "Офисный центр",
        "client": "ОсОО Бишкек Бизнес",
        "city": "Бишкек",
        "area": 850,
        "price": 35000000,
        "paid": 15000000,
        "status": "Фундамент",
        "progress": 25,
        "workers": 15,
        "start": "2026-05-01",
        "end": "2027-05-01"
    },
    {
        "id": 103,
        "name": "Современный коттедж",
        "client": "Нурлан Турсунов",
        "city": "Чолпон-Ата",
        "area": 320,
        "price": 15000000,
        "paid": 12000000,
        "status": "Отделочные работы",
        "progress": 82,
        "workers": 10,
        "start": "2026-01-15",
        "end": "2026-11-30"
    },
    {
        "id": 104,
        "name": "Торговый комплекс",
        "client": "ОсОО Строй Инвест",
        "city": "Бишкек",
        "area": 1500,
        "price": 65000000,
        "paid": 20000000,
        "status": "Проектирование",
        "progress": 10,
        "workers": 5,
        "start": "2026-08-01",
        "end": "2028-01-15"
    }
]


# ============================================================
# 5. СТРОИТЕЛЬНЫЕ МАТЕРИАЛЫ
# ============================================================

materials = {
    "Цемент": {
        "price": 450,
        "unit": "мешок",
        "quantity": 500
    },
    "Кирпич": {
        "price": 18,
        "unit": "шт",
        "quantity": 15000
    },
    "Песок": {
        "price": 2500,
        "unit": "м3",
        "quantity": 100
    },
    "Щебень": {
        "price": 3000,
        "unit": "м3",
        "quantity": 80
    },
    "Арматура": {
        "price": 75000,
        "unit": "тонна",
        "quantity": 15
    },
    "Доска": {
        "price": 28000,
        "unit": "м3",
        "quantity": 40
    },
    "Утеплитель": {
        "price": 1200,
        "unit": "м2",
        "quantity": 800
    },
    "Плитка": {
        "price": 950,
        "unit": "м2",
        "quantity": 600
    },
    "Краска": {
        "price": 1800,
        "unit": "ведро",
        "quantity": 150
    }
}


# ============================================================
# 6. СТРОИТЕЛЬНАЯ ТЕХНИКА
# ============================================================

equipment = [
    {
        "id": 1,
        "name": "Экскаватор",
        "model": "CAT 320",
        "year": 2021,
        "status": "Работает",
        "price": 8500000
    },
    {
        "id": 2,
        "name": "Кран",
        "model": "Liebherr",
        "year": 2020,
        "status": "Свободен",
        "price": 12000000
    },
    {
        "id": 3,
        "name": "Бетономешалка",
        "model": "KAMAZ",
        "year": 2022,
        "status": "Работает",
        "price": 3500000
    },
    {
        "id": 4,
        "name": "Грузовик",
        "model": "MAN",
        "year": 2019,
        "status": "Ремонт",
        "price": 6000000
    },
    {
        "id": 5,
        "name": "Погрузчик",
        "model": "JCB",
        "year": 2023,
        "status": "Свободен",
        "price": 5000000
    }
]


# ============================================================
# 7. РАСХОДЫ
# ============================================================

expenses = [
    {
        "name": "Покупка цемента",
        "amount": 450000,
        "category": "Материалы"
    },
    {
        "name": "Покупка кирпича",
        "amount": 270000,
        "category": "Материалы"
    },
    {
        "name": "Топливо",
        "amount": 180000,
        "category": "Транспорт"
    },
    {
        "name": "Ремонт техники",
        "amount": 320000,
        "category": "Техника"
    },
    {
        "name": "Электричество",
        "amount": 85000,
        "category": "Коммунальные"
    }
]


# ============================================================
# 8. ИНФОРМАЦИЯ О КОМПАНИИ
# ============================================================

def show_company():
    print("\n" + "=" * 60)
    print("ИНФОРМАЦИЯ О КОМПАНИИ")
    print("=" * 60)

    print(f"Название: {company['name']}")
    print(f"Город: {company['city']}")
    print(f"Страна: {company['country']}")
    print(f"Телефон: {company['phone']}")
    print(f"Email: {company['email']}")
    print(f"Сайт: {company['website']}")
    print(f"Год основания: {company['year']}")
    print(f"Директор: {company['director']}")
    print(f"Сотрудников в базе: {len(employees)}")
    print(f"Проектов в базе: {len(projects)}")


# ============================================================
# 9. СОТРУДНИКИ
# ============================================================

def show_employees():
    print("\n" + "=" * 60)
    print("СОТРУДНИКИ")
    print("=" * 60)

    for employee in employees:
        print(f"""
ID: {employee['id']}
Имя: {employee['name']}
Должность: {employee['position']}
Зарплата: {employee['salary']:,} сом
Опыт: {employee['experience']} лет
Телефон: {employee['phone']}
Статус: {employee['status']}
----------------------------------------
""")


# ============================================================
# 10. КЛИЕНТЫ
# ============================================================

def show_clients():
    print("\n" + "=" * 60)
    print("КЛИЕНТЫ")
    print("=" * 60)

    for client in clients:
        print(f"""
ID: {client['id']}
Имя: {client['name']}
Телефон: {client['phone']}
Город: {client['city']}
Тип: {client['type']}
Количество проектов: {client['projects']}
----------------------------------------
""")


# ============================================================
# 11. ПРОЕКТЫ
# ============================================================

def show_projects():
    print("\n" + "=" * 60)
    print("ВСЕ ПРОЕКТЫ")
    print("=" * 60)

    for project in projects:
        print(f"""
ID: {project['id']}
Проект: {project['name']}
Клиент: {project['client']}
Город: {project['city']}
Площадь: {project['area']} м2
Стоимость: {project['price']:,} сом
Оплачено: {project['paid']:,} сом
Осталось оплатить: {project['price'] - project['paid']:,} сом
Статус: {project['status']}
Готовность: {project['progress']}%
Рабочих: {project['workers']}
Начало: {project['start']}
Окончание: {project['end']}
----------------------------------------
""")


# ============================================================
# 12. МАТЕРИАЛЫ
# ============================================================

def show_materials():
    print("\n" + "=" * 60)
    print("СКЛАД МАТЕРИАЛОВ")
    print("=" * 60)

    total = 0

    for name, data in materials.items():
        cost = data["price"] * data["quantity"]
        total += cost

        print(
            f"{name}: "
            f"{data['quantity']} {data['unit']} | "
            f"{data['price']:,} сом | "
            f"Стоимость: {cost:,} сом"
        )

    print("-" * 60)
    print(f"Общая стоимость склада: {total:,} сом")


# ============================================================
# 13. ТЕХНИКА
# ============================================================

def show_equipment():
    print("\n" + "=" * 60)
    print("СТРОИТЕЛЬНАЯ ТЕХНИКА")
    print("=" * 60)

    for item in equipment:
        print(f"""
ID: {item['id']}
Название: {item['name']}
Модель: {item['model']}
Год: {item['year']}
Статус: {item['status']}
Стоимость: {item['price']:,} сом
----------------------------------------
""")


# ============================================================
# 14. РАСЧЁТ СТРОИТЕЛЬСТВА
# ============================================================

def calculate_building():
    print("\n" + "=" * 60)
    print("РАСЧЁТ СТОИМОСТИ СТРОИТЕЛЬСТВА")
    print("=" * 60)

    try:
        area = float(input("Площадь здания (м2): "))
        price = float(input("Цена за 1 м2: "))

        if area <= 0 or price <= 0:
            print("Площадь и цена должны быть больше нуля.")
            return

        building_cost = area * price
        workers_cost = building_cost * 0.15
        transport_cost = building_cost * 0.05
        other_cost = building_cost * 0.10

        total = (
            building_cost
            + workers_cost
            + transport_cost
            + other_cost
        )

        print("\nРАСЧЁТ:")
        print(f"Основная стоимость: {building_cost:,.2f} сом")
        print(f"Работа: {workers_cost:,.2f} сом")
        print(f"Транспорт: {transport_cost:,.2f} сом")
        print(f"Дополнительные расходы: {other_cost:,.2f} сом")
        print("-" * 50)
        print(f"ИТОГО: {total:,.2f} сом")

    except ValueError:
        print("Ошибка! Введите числа.")


# ============================================================
# 15. ДОБАВИТЬ ПРОЕКТ
# ============================================================

def add_project():
    print("\n" + "=" * 60)
    print("ДОБАВЛЕНИЕ НОВОГО ПРОЕКТА")
    print("=" * 60)

    try:
        project_id = int(input("ID проекта: "))

        for project in projects:
            if project["id"] == project_id:
                print("Ошибка: такой ID проекта уже существует.")
                return

        name = input("Название: ").strip()
        client = input("Клиент: ").strip()
        city = input("Город: ").strip()
        area = float(input("Площадь: "))
        price = float(input("Стоимость: "))

        if area <= 0 or price <= 0:
            print("Площадь и стоимость должны быть больше нуля.")
            return

        project = {
            "id": project_id,
            "name": name,
            "client": client,
            "city": city,
            "area": area,
            "price": price,
            "paid": 0,
            "status": "Подготовка",
            "progress": 0,
            "workers": 0,
            "start": str(datetime.now().date()),
            "end": "Не указано"
        }

        projects.append(project)

        print("\nПроект успешно добавлен!")

    except ValueError:
        print("Ошибка! ID, площадь и стоимость должны быть числами.")


# ============================================================
# 16. ПОИСК ПРОЕКТА
# ============================================================

def search_project():
    print("\n" + "=" * 60)
    print("ПОИСК ПРОЕКТА")
    print("=" * 60)

    text = input("Введите название, город или клиента: ").strip().lower()

    if not text:
        print("Введите текст для поиска.")
        return

    found = False

    for project in projects:
        if (
            text in project["name"].lower()
            or text in project["city"].lower()
            or text in project["client"].lower()
        ):
            print(f"""
ID: {project['id']}
Проект: {project['name']}
Клиент: {project['client']}
Город: {project['city']}
Стоимость: {project['price']:,} сом
Статус: {project['status']}
Готовность: {project['progress']}%
""")
            found = True

    if not found:
        print("Ничего не найдено.")


# ============================================================
# 17. ИЗМЕНЕНИЕ СТАТУСА
# ============================================================

def change_status():
    try:
        project_id = int(input("Введите ID проекта: "))

        for project in projects:
            if project["id"] == project_id:
                print("Текущий статус:", project["status"])

                new_status = input("Новый статус: ").strip()

                if not new_status:
                    print("Статус не может быть пустым.")
                    return

                project["status"] = new_status

                print("Статус успешно изменён!")
                return

        print("Проект не найден.")

    except ValueError:
        print("Введите правильный ID.")


# ============================================================
# 18. ИЗМЕНЕНИЕ ПРОГРЕССА
# ============================================================

def change_progress():
    try:
        project_id = int(input("ID проекта: "))
        progress = int(input("Готовность от 0 до 100: "))

        if progress < 0 or progress > 100:
            print("Процент должен быть от 0 до 100.")
            return

        for project in projects:
            if project["id"] == project_id:
                project["progress"] = progress

                if progress == 100:
                    project["status"] = "Завершено"

                print("Готовность проекта обновлена!")
                return

        print("Проект не найден.")

    except ValueError:
        print("Введите числа.")


# ============================================================
# 19. ЗАРПЛАТНЫЙ ОТЧЁТ
# ============================================================

def salary_report():
    print("\n" + "=" * 60)
    print("ФОНД ЗАРПЛАТ")
    print("=" * 60)

    total = 0

    for employee in employees:
        total += employee["salary"]

    if employees:
        average = total / len(employees)
    else:
        average = 0

    print(f"Количество сотрудников: {len(employees)}")
    print(f"Общий фонд зарплаты: {total:,} сом")
    print(f"Средняя зарплата: {average:,.2f} сом")


# ============================================================
# 20. РАСХОДЫ
# ============================================================

def show_expenses():
    print("\n" + "=" * 60)
    print("РАСХОДЫ КОМПАНИИ")
    print("=" * 60)

    total = 0

    for expense in expenses:
        print(
            f"{expense['name']}: "
            f"{expense['amount']:,} сом "
            f"({expense['category']})"
        )

        total += expense["amount"]

    print("-" * 60)
    print(f"Общие расходы: {total:,} сом")


# ============================================================
# 21. ФИНАНСОВЫЙ ОТЧЁТ
# ============================================================

def financial_report():
    print("\n" + "=" * 60)
    print("ФИНАНСОВЫЙ ОТЧЁТ")
    print("=" * 60)

    income = 0

    for project in projects:
        income += project["paid"]

    expenses_total = 0

    for expense in expenses:
        expenses_total += expense["amount"]

    balance = income - expenses_total

    print(f"Получено от клиентов: {income:,} сом")
    print(f"Расходы компании: {expenses_total:,} сом")
    print(f"Баланс: {balance:,} сом")


# ============================================================
# 22. ДОБАВИТЬ ПЛАТЁЖ
# ============================================================

def add_payment():
    try:
        project_id = int(input("ID проекта: "))
        payment = float(input("Сумма платежа: "))

        if payment <= 0:
            print("Сумма платежа должна быть больше нуля.")
            return

        for project in projects:
            if project["id"] == project_id:

                remaining = project["price"] - project["paid"]

                if payment > remaining:
                    print(
                        f"Ошибка! Осталось оплатить "
                        f"{remaining:,.2f} сом."
                    )
                    return

                project["paid"] += payment

                print(
                    f"Платёж {payment:,.2f} сом добавлен!"
                )

                print(
                    f"Всего оплачено: "
                    f"{project['paid']:,.2f} сом"
                )

                return

        print("Проект не найден.")

    except ValueError:
        print("Введите правильные данные.")


# ============================================================
# 23. ДОБАВЛЕНИЕ МАТЕРИАЛА
# ============================================================

def add_material():
    print("\n" + "=" * 60)
    print("ДОБАВЛЕНИЕ МАТЕРИАЛА")
    print("=" * 60)

    name = input("Название материала: ").strip()

    if not name:
        print("Название не может быть пустым.")
        return

    try:
        price = float(input("Цена: "))
        quantity = float(input("Количество: "))
        unit = input("Единица измерения: ").strip()

        if price <= 0 or quantity < 0:
            print("Цена должна быть больше нуля, количество не может быть отрицательным.")
            return

        if not unit:
            print("Укажите единицу измерения.")
            return

        materials[name] = {
            "price": price,
            "unit": unit,
            "quantity": quantity
        }

        print("Материал добавлен на склад!")

    except ValueError:
        print("Ошибка! Цена и количество должны быть числами.")


# ============================================================
# 24. ДОБАВЛЕНИЕ РАСХОДА
# ============================================================

def add_expense():
    print("\n" + "=" * 60)
    print("ДОБАВЛЕНИЕ РАСХОДА")
    print("=" * 60)

    name = input("Название расхода: ").strip()
    category = input("Категория: ").strip()

    try:
        amount = float(input("Сумма: "))

        if amount <= 0:
            print("Сумма должна быть больше нуля.")
            return

        expenses.append({
            "name": name,
            "amount": amount,
            "category": category
        })

        print("Расход успешно добавлен!")

    except ValueError:
        print("Введите число.")


# ============================================================
# 25. СТАТИСТИКА ПРОЕКТОВ
# ============================================================

def project_statistics():
    print("\n" + "=" * 60)
    print("СТАТИСТИКА ПРОЕКТОВ")
    print("=" * 60)

    total = len(projects)
    construction = 0
    finished = 0
    preparation = 0

    for project in projects:
        status = project["status"].lower()

        if "строительство" in status:
            construction += 1

        if "заверш" in status:
            finished += 1

        if "подготов" in status:
            preparation += 1

    print(f"Всего проектов: {total}")
    print(f"В строительстве: {construction}")
    print(f"Завершено: {finished}")
    print(f"На подготовке: {preparation}")


# ============================================================
# 26. ОБЩАЯ СТОИМОСТЬ ПРОЕКТОВ
# ============================================================

def total_projects_cost():
    total = 0

    for project in projects:
        total += project["price"]

    print("\n" + "=" * 60)
    print("ОБЩАЯ СТОИМОСТЬ ПРОЕКТОВ")
    print("=" * 60)

    print(f"{total:,} сом")


# ============================================================
# 27. СТОИМОСТЬ ТЕХНИКИ
# ============================================================

def equipment_cost():
    total = 0

    for item in equipment:
        total += item["price"]

    print("\n" + "=" * 60)
    print("СТОИМОСТЬ ТЕХНИКИ")
    print("=" * 60)

    print(f"Общая стоимость техники: {total:,} сом")


# ============================================================
# 28. ДОБАВЛЕНИЕ СОТРУДНИКА
# ============================================================

def add_employee():
    print("\n" + "=" * 60)
    print("ДОБАВЛЕНИЕ СОТРУДНИКА")
    print("=" * 60)

    try:
        employee_id = int(input("ID сотрудника: "))

        for employee in employees:
            if employee["id"] == employee_id:
                print("Такой ID уже существует.")
                return

        name = input("Имя: ").strip()
        position = input("Должность: ").strip()
        salary = float(input("Зарплата: "))
        experience = int(input("Опыт работы: "))
        phone = input("Телефон: ").strip()

        if salary <= 0 or experience < 0:
            print("Проверьте зарплату и опыт.")
            return

        employees.append({
            "id": employee_id,
            "name": name,
            "position": position,
            "salary": salary,
            "experience": experience,
            "phone": phone,
            "status": "Работает"
        })

        print("Сотрудник успешно добавлен!")

    except ValueError:
        print("Ошибка ввода.")


# ============================================================
# 29. ПОИСК СОТРУДНИКА
# ============================================================

def search_employee():
    print("\n" + "=" * 60)
    print("ПОИСК СОТРУДНИКА")
    print("=" * 60)

    text = input("Введите имя или должность: ").strip().lower()

    if not text:
        print("Введите данные для поиска.")
        return

    found = False

    for employee in employees:
        if (
            text in employee["name"].lower()
            or text in employee["position"].lower()
        ):
            print(f"""
ID: {employee['id']}
Имя: {employee['name']}
Должность: {employee['position']}
Зарплата: {employee['salary']:,} сом
Телефон: {employee['phone']}
Статус: {employee['status']}
""")
            found = True

    if not found:
        print("Сотрудник не найден.")


# ============================================================
# 30. ОБЩИЙ ОТЧЁТ
# ============================================================

def full_report():
    print("\n" + "=" * 60)
    print("ОБЩИЙ ОТЧЁТ КОМПАНИИ")
    print("=" * 60)

    project_sum = sum(project["price"] for project in projects)
    paid_sum = sum(project["paid"] for project in projects)
    expense_sum = sum(expense["amount"] for expense in expenses)
    salary_sum = sum(employee["salary"] for employee in employees)
    equipment_sum = sum(item["price"] for item in equipment)

    print(f"Сотрудников: {len(employees)}")
    print(f"Клиентов: {len(clients)}")
    print(f"Проектов: {len(projects)}")
    print(f"Стоимость всех проектов: {project_sum:,} сом")
    print(f"Получено от клиентов: {paid_sum:,} сом")
    print(f"Расходы: {expense_sum:,} сом")
    print(f"Фонд зарплаты: {salary_sum:,} сом")
    print(f"Стоимость техники: {equipment_sum:,} сом")


# ============================================================
# 31. ГЛАВНОЕ МЕНЮ
# ============================================================

def main():

    while True:

        print("\n")
        print("=" * 65)
        print("              КУТ КУРУЛУШ")
        print("          СТРОИТЕЛЬНАЯ КОМПАНИЯ")
        print("=" * 65)

        print("""
1.  Информация о компании
2.  Сотрудники
3.  Клиенты
4.  Все проекты
5.  Материалы
6.  Строительная техника
7.  Рассчитать строительство
8.  Добавить проект
9.  Найти проект
10. Изменить статус проекта
11. Изменить готовность проекта
12. Зарплатный отчёт
13. Расходы
14. Финансовый отчёт
15. Добавить платёж
16. Добавить материал
17. Добавить расход
18. Статистика проектов
19. Общая стоимость проектов
20. Стоимость техники
21. Добавить сотрудника
22. Найти сотрудника
23. Общий отчёт
0.  Выход
""")

        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            show_company()

        elif choice == "2":
            show_employees()

        elif choice == "3":
            show_clients()

        elif choice == "4":
            show_projects()

        elif choice == "5":
            show_materials()

        elif choice == "6":
            show_equipment()

        elif choice == "7":
            calculate_building()

        elif choice == "8":
            add_project()

        elif choice == "9":
            search_project()

        elif choice == "10":
            change_status()

        elif choice == "11":
            change_progress()

        elif choice == "12":
            salary_report()

        elif choice == "13":
            show_expenses()

        elif choice == "14":
            financial_report()

        elif choice == "15":
            add_payment()

        elif choice == "16":
            add_material()

        elif choice == "17":
            add_expense()

        elif choice == "18":
            project_statistics()

        elif choice == "19":
            total_projects_cost()

        elif choice == "20":
            equipment_cost()

        elif choice == "21":
            add_employee()

        elif choice == "22":
            search_employee()

        elif choice == "23":
            full_report()

        elif choice == "0":
            print("\n" + "=" * 60)
            print("Спасибо за использование программы!")
            print("КУТ КУРУЛУШ")
            print("Строим качественно и надёжно!")
            print("=" * 60)
            break

        else:
            print("\nОшибка! Выберите пункт от 0 до 23.")


# ============================================================
# ЗАПУСК ПРОГРАММЫ
# ============================================================

if __name__ == "__main__":
    main()


# ============================================================
#                 КУТ КУРУЛУШ
#             СТРОИТЕЛЬНАЯ КОМПАНИЯ
#        СИСТЕМА УПРАВЛЕНИЯ КОМПАНИЕЙ
# ============================================================

from datetime import datetime


# ============================================================
# 1. ИНФОРМАЦИЯ О КОМПАНИИ
# ============================================================

company = {
    "name": "Кут Курулуш",
    "city": "Бишкек",
    "country": "Кыргызстан",
    "phone": "+996 555 123 456",
    "email": "kutkurulush@gmail.com",
    "website": "www.kutkurulush.kg",
    "year": 2015,
    "director": "Азамат Бакытбеков"
}


# ============================================================
# 2. СОТРУДНИКИ
# ============================================================

employees = [
    {
        "id": 1,
        "name": "Азамат Бакытбеков",
        "position": "Директор",
        "salary": 150000,
        "experience": 12,
        "phone": "+996 700 111 111",
        "status": "Работает"
    },
    {
        "id": 2,
        "name": "Нурбек Осмонов",
        "position": "Главный инженер",
        "salary": 110000,
        "experience": 9,
        "phone": "+996 700 222 222",
        "status": "Работает"
    },
    {
        "id": 3,
        "name": "Эрмек Садыков",
        "position": "Прораб",
        "salary": 85000,
        "experience": 7,
        "phone": "+996 700 333 333",
        "status": "Работает"
    },
    {
        "id": 4,
        "name": "Бекжан Токтосунов",
        "position": "Архитектор",
        "salary": 95000,
        "experience": 8,
        "phone": "+996 700 444 444",
        "status": "Работает"
    },
    {
        "id": 5,
        "name": "Руслан Иманов",
        "position": "Строитель",
        "salary": 65000,
        "experience": 5,
        "phone": "+996 700 555 555",
        "status": "Работает"
    },
    {
        "id": 6,
        "name": "Талантбек Жумаев",
        "position": "Электрик",
        "salary": 70000,
        "experience": 6,
        "phone": "+996 700 666 666",
        "status": "Работает"
    },
    {
        "id": 7,
        "name": "Каныбек Абдылдаев",
        "position": "Сантехник",
        "salary": 68000,
        "experience": 5,
        "phone": "+996 700 777 777",
        "status": "Работает"
    },
    {
        "id": 8,
        "name": "Марат Алиев",
        "position": "Водитель",
        "salary": 55000,
        "experience": 4,
        "phone": "+996 700 888 888",
        "status": "Работает"
    }
]


# ============================================================
# 3. КЛИЕНТЫ
# ============================================================

clients = [
    {
        "id": 1,
        "name": "Бек Асанбеков",
        "phone": "+996 555 111 222",
        "city": "Бишкек",
        "type": "Частный клиент",
        "projects": 1
    },
    {
        "id": 2,
        "name": "ОсОО Бишкек Бизнес",
        "phone": "+996 555 222 333",
        "city": "Бишкек",
        "type": "Компания",
        "projects": 2
    },
    {
        "id": 3,
        "name": "Нурлан Турсунов",
        "phone": "+996 555 333 444",
        "city": "Чолпон-Ата",
        "type": "Частный клиент",
        "projects": 1
    },
    {
        "id": 4,
        "name": "ОсОО Строй Инвест",
        "phone": "+996 555 444 555",
        "city": "Бишкек",
        "type": "Компания",
        "projects": 3
    }
]


# ============================================================
# 4. СТРОИТЕЛЬНЫЕ ПРОЕКТЫ
# ============================================================

projects = [
    {
        "id": 101,
        "name": "Большой жилой дом",
        "client": "Бек Асанбеков",
        "city": "Бишкек",
        "area": 240,
        "price": 12000000,
        "paid": 5000000,
        "status": "Строительство",
        "progress": 55,
        "workers": 8,
        "start": "2026-03-10",
        "end": "2027-01-20"
    },
    {
        "id": 102,
        "name": "Офисный центр",
        "client": "ОсОО Бишкек Бизнес",
        "city": "Бишкек",
        "area": 850,
        "price": 35000000,
        "paid": 15000000,
        "status": "Фундамент",
        "progress": 25,
        "workers": 15,
        "start": "2026-05-01",
        "end": "2027-05-01"
    },
    {
        "id": 103,
        "name": "Современный коттедж",
        "client": "Нурлан Турсунов",
        "city": "Чолпон-Ата",
        "area": 320,
        "price": 15000000,
        "paid": 12000000,
        "status": "Отделочные работы",
        "progress": 82,
        "workers": 10,
        "start": "2026-01-15",
        "end": "2026-11-30"
    },
    {
        "id": 104,
        "name": "Торговый комплекс",
        "client": "ОсОО Строй Инвест",
        "city": "Бишкек",
        "area": 1500,
        "price": 65000000,
        "paid": 20000000,
        "status": "Проектирование",
        "progress": 10,
        "workers": 5,
        "start": "2026-08-01",
        "end": "2028-01-15"
    }
]


# ============================================================
# 5. СТРОИТЕЛЬНЫЕ МАТЕРИАЛЫ
# ============================================================

materials = {
    "Цемент": {
        "price": 450,
        "unit": "мешок",
        "quantity": 500
    },
    "Кирпич": {
        "price": 18,
        "unit": "шт",
        "quantity": 15000
    },
    "Песок": {
        "price": 2500,
        "unit": "м3",
        "quantity": 100
    },
    "Щебень": {
        "price": 3000,
        "unit": "м3",
        "quantity": 80
    },
    "Арматура": {
        "price": 75000,
        "unit": "тонна",
        "quantity": 15
    },
    "Доска": {
        "price": 28000,
        "unit": "м3",
        "quantity": 40
    },
    "Утеплитель": {
        "price": 1200,
        "unit": "м2",
        "quantity": 800
    },
    "Плитка": {
        "price": 950,
        "unit": "м2",
        "quantity": 600
    },
    "Краска": {
        "price": 1800,
        "unit": "ведро",
        "quantity": 150
    }
}


# ============================================================
# 6. СТРОИТЕЛЬНАЯ ТЕХНИКА
# ============================================================

equipment = [
    {
        "id": 1,
        "name": "Экскаватор",
        "model": "CAT 320",
        "year": 2021,
        "status": "Работает",
        "price": 8500000
    },
    {
        "id": 2,
        "name": "Кран",
        "model": "Liebherr",
        "year": 2020,
        "status": "Свободен",
        "price": 12000000
    },
    {
        "id": 3,
        "name": "Бетономешалка",
        "model": "KAMAZ",
        "year": 2022,
        "status": "Работает",
        "price": 3500000
    },
    {
        "id": 4,
        "name": "Грузовик",
        "model": "MAN",
        "year": 2019,
        "status": "Ремонт",
        "price": 6000000
    },
    {
        "id": 5,
        "name": "Погрузчик",
        "model": "JCB",
        "year": 2023,
        "status": "Свободен",
        "price": 5000000
    }
]


# ============================================================
# 7. РАСХОДЫ
# ============================================================

expenses = [
    {
        "name": "Покупка цемента",
        "amount": 450000,
        "category": "Материалы"
    },
    {
        "name": "Покупка кирпича",
        "amount": 270000,
        "category": "Материалы"
    },
    {
        "name": "Топливо",
        "amount": 180000,
        "category": "Транспорт"
    },
    {
        "name": "Ремонт техники",
        "amount": 320000,
        "category": "Техника"
    },
    {
        "name": "Электричество",
        "amount": 85000,
        "category": "Коммунальные"
    }
]


# ============================================================
# 8. ИНФОРМАЦИЯ О КОМПАНИИ
# ============================================================

def show_company():
    print("\n" + "=" * 60)
    print("ИНФОРМАЦИЯ О КОМПАНИИ")
    print("=" * 60)

    print(f"Название: {company['name']}")
    print(f"Город: {company['city']}")
    print(f"Страна: {company['country']}")
    print(f"Телефон: {company['phone']}")
    print(f"Email: {company['email']}")
    print(f"Сайт: {company['website']}")
    print(f"Год основания: {company['year']}")
    print(f"Директор: {company['director']}")
    print(f"Сотрудников в базе: {len(employees)}")
    print(f"Проектов в базе: {len(projects)}")


# ============================================================
# 9. СОТРУДНИКИ
# ============================================================

def show_employees():
    print("\n" + "=" * 60)
    print("СОТРУДНИКИ")
    print("=" * 60)

    for employee in employees:
        print(f"""
ID: {employee['id']}
Имя: {employee['name']}
Должность: {employee['position']}
Зарплата: {employee['salary']:,} сом
Опыт: {employee['experience']} лет
Телефон: {employee['phone']}
Статус: {employee['status']}
----------------------------------------
""")


# ============================================================
# 10. КЛИЕНТЫ
# ============================================================

def show_clients():
    print("\n" + "=" * 60)
    print("КЛИЕНТЫ")
    print("=" * 60)

    for client in clients:
        print(f"""
ID: {client['id']}
Имя: {client['name']}
Телефон: {client['phone']}
Город: {client['city']}
Тип: {client['type']}
Количество проектов: {client['projects']}
----------------------------------------
""")


# ============================================================
# 11. ПРОЕКТЫ
# ============================================================

def show_projects():
    print("\n" + "=" * 60)
    print("ВСЕ ПРОЕКТЫ")
    print("=" * 60)

    for project in projects:
        print(f"""
ID: {project['id']}
Проект: {project['name']}
Клиент: {project['client']}
Город: {project['city']}
Площадь: {project['area']} м2
Стоимость: {project['price']:,} сом
Оплачено: {project['paid']:,} сом
Осталось оплатить: {project['price'] - project['paid']:,} сом
Статус: {project['status']}
Готовность: {project['progress']}%
Рабочих: {project['workers']}
Начало: {project['start']}
Окончание: {project['end']}
----------------------------------------
""")


# ============================================================
# 12. МАТЕРИАЛЫ
# ============================================================

def show_materials():
    print("\n" + "=" * 60)
    print("СКЛАД МАТЕРИАЛОВ")
    print("=" * 60)

    total = 0

    for name, data in materials.items():
        cost = data["price"] * data["quantity"]
        total += cost

        print(
            f"{name}: "
            f"{data['quantity']} {data['unit']} | "
            f"{data['price']:,} сом | "
            f"Стоимость: {cost:,} сом"
        )

    print("-" * 60)
    print(f"Общая стоимость склада: {total:,} сом")


# ============================================================
# 13. ТЕХНИКА
# ============================================================

def show_equipment():
    print("\n" + "=" * 60)
    print("СТРОИТЕЛЬНАЯ ТЕХНИКА")
    print("=" * 60)

    for item in equipment:
        print(f"""
ID: {item['id']}
Название: {item['name']}
Модель: {item['model']}
Год: {item['year']}
Статус: {item['status']}
Стоимость: {item['price']:,} сом
----------------------------------------
""")


# ============================================================
# 14. РАСЧЁТ СТРОИТЕЛЬСТВА
# ============================================================

def calculate_building():
    print("\n" + "=" * 60)
    print("РАСЧЁТ СТОИМОСТИ СТРОИТЕЛЬСТВА")
    print("=" * 60)

    try:
        area = float(input("Площадь здания (м2): "))
        price = float(input("Цена за 1 м2: "))

        if area <= 0 or price <= 0:
            print("Площадь и цена должны быть больше нуля.")
            return

        building_cost = area * price
        workers_cost = building_cost * 0.15
        transport_cost = building_cost * 0.05
        other_cost = building_cost * 0.10

        total = (
            building_cost
            + workers_cost
            + transport_cost
            + other_cost
        )

        print("\nРАСЧЁТ:")
        print(f"Основная стоимость: {building_cost:,.2f} сом")
        print(f"Работа: {workers_cost:,.2f} сом")
        print(f"Транспорт: {transport_cost:,.2f} сом")
        print(f"Дополнительные расходы: {other_cost:,.2f} сом")
        print("-" * 50)
        print(f"ИТОГО: {total:,.2f} сом")

    except ValueError:
        print("Ошибка! Введите числа.")


# ============================================================
# 15. ДОБАВИТЬ ПРОЕКТ
# ============================================================

def add_project():
    print("\n" + "=" * 60)
    print("ДОБАВЛЕНИЕ НОВОГО ПРОЕКТА")
    print("=" * 60)

    try:
        project_id = int(input("ID проекта: "))

        for project in projects:
            if project["id"] == project_id:
                print("Ошибка: такой ID проекта уже существует.")
                return

        name = input("Название: ").strip()
        client = input("Клиент: ").strip()
        city = input("Город: ").strip()
        area = float(input("Площадь: "))
        price = float(input("Стоимость: "))

        if area <= 0 or price <= 0:
            print("Площадь и стоимость должны быть больше нуля.")
            return

        project = {
            "id": project_id,
            "name": name,
            "client": client,
            "city": city,
            "area": area,
            "price": price,
            "paid": 0,
            "status": "Подготовка",
            "progress": 0,
            "workers": 0,
            "start": str(datetime.now().date()),
            "end": "Не указано"
        }

        projects.append(project)

        print("\nПроект успешно добавлен!")

    except ValueError:
        print("Ошибка! ID, площадь и стоимость должны быть числами.")


# ============================================================
# 16. ПОИСК ПРОЕКТА
# ============================================================

def search_project():
    print("\n" + "=" * 60)
    print("ПОИСК ПРОЕКТА")
    print("=" * 60)

    text = input("Введите название, город или клиента: ").strip().lower()

    if not text:
        print("Введите текст для поиска.")
        return

    found = False

    for project in projects:
        if (
            text in project["name"].lower()
            or text in project["city"].lower()
            or text in project["client"].lower()
        ):
            print(f"""
ID: {project['id']}
Проект: {project['name']}
Клиент: {project['client']}
Город: {project['city']}
Стоимость: {project['price']:,} сом
Статус: {project['status']}
Готовность: {project['progress']}%
""")
            found = True

    if not found:
        print("Ничего не найдено.")


# ============================================================
# 17. ИЗМЕНЕНИЕ СТАТУСА
# ============================================================

def change_status():
    try:
        project_id = int(input("Введите ID проекта: "))

        for project in projects:
            if project["id"] == project_id:
                print("Текущий статус:", project["status"])

                new_status = input("Новый статус: ").strip()

                if not new_status:
                    print("Статус не может быть пустым.")
                    return

                project["status"] = new_status

                print("Статус успешно изменён!")
                return

        print("Проект не найден.")

    except ValueError:
        print("Введите правильный ID.")


# ============================================================
# 18. ИЗМЕНЕНИЕ ПРОГРЕССА
# ============================================================

def change_progress():
    try:
        project_id = int(input("ID проекта: "))
        progress = int(input("Готовность от 0 до 100: "))

        if progress < 0 or progress > 100:
            print("Процент должен быть от 0 до 100.")
            return

        for project in projects:
            if project["id"] == project_id:
                project["progress"] = progress

                if progress == 100:
                    project["status"] = "Завершено"

                print("Готовность проекта обновлена!")
                return

        print("Проект не найден.")

    except ValueError:
        print("Введите числа.")


# ============================================================
# 19. ЗАРПЛАТНЫЙ ОТЧЁТ
# ============================================================

def salary_report():
    print("\n" + "=" * 60)
    print("ФОНД ЗАРПЛАТ")
    print("=" * 60)

    total = 0

    for employee in employees:
        total += employee["salary"]

    if employees:
        average = total / len(employees)
    else:
        average = 0

    print(f"Количество сотрудников: {len(employees)}")
    print(f"Общий фонд зарплаты: {total:,} сом")
    print(f"Средняя зарплата: {average:,.2f} сом")


# ============================================================
# 20. РАСХОДЫ
# ============================================================

def show_expenses():
    print("\n" + "=" * 60)
    print("РАСХОДЫ КОМПАНИИ")
    print("=" * 60)

    total = 0

    for expense in expenses:
        print(
            f"{expense['name']}: "
            f"{expense['amount']:,} сом "
            f"({expense['category']})"
        )

        total += expense["amount"]

    print("-" * 60)
    print(f"Общие расходы: {total:,} сом")


# ============================================================
# 21. ФИНАНСОВЫЙ ОТЧЁТ
# ============================================================

def financial_report():
    print("\n" + "=" * 60)
    print("ФИНАНСОВЫЙ ОТЧЁТ")
    print("=" * 60)

    income = 0

    for project in projects:
        income += project["paid"]

    expenses_total = 0

    for expense in expenses:
        expenses_total += expense["amount"]

    balance = income - expenses_total

    print(f"Получено от клиентов: {income:,} сом")
    print(f"Расходы компании: {expenses_total:,} сом")
    print(f"Баланс: {balance:,} сом")


# ============================================================
# 22. ДОБАВИТЬ ПЛАТЁЖ
# ============================================================

def add_payment():
    try:
        project_id = int(input("ID проекта: "))
        payment = float(input("Сумма платежа: "))

        if payment <= 0:
            print("Сумма платежа должна быть больше нуля.")
            return

        for project in projects:
            if project["id"] == project_id:

                remaining = project["price"] - project["paid"]

                if payment > remaining:
                    print(
                        f"Ошибка! Осталось оплатить "
                        f"{remaining:,.2f} сом."
                    )
                    return

                project["paid"] += payment

                print(
                    f"Платёж {payment:,.2f} сом добавлен!"
                )

                print(
                    f"Всего оплачено: "
                    f"{project['paid']:,.2f} сом"
                )

                return

        print("Проект не найден.")

    except ValueError:
        print("Введите правильные данные.")


# ============================================================
# 23. ДОБАВЛЕНИЕ МАТЕРИАЛА
# ============================================================

def add_material():
    print("\n" + "=" * 60)
    print("ДОБАВЛЕНИЕ МАТЕРИАЛА")
    print("=" * 60)

    name = input("Название материала: ").strip()

    if not name:
        print("Название не может быть пустым.")
        return

    try:
        price = float(input("Цена: "))
        quantity = float(input("Количество: "))
        unit = input("Единица измерения: ").strip()

        if price <= 0 or quantity < 0:
            print("Цена должна быть больше нуля, количество не может быть отрицательным.")
            return

        if not unit:
            print("Укажите единицу измерения.")
            return

        materials[name] = {
            "price": price,
            "unit": unit,
            "quantity": quantity
        }

        print("Материал добавлен на склад!")

    except ValueError:
        print("Ошибка! Цена и количество должны быть числами.")


# ============================================================
# 24. ДОБАВЛЕНИЕ РАСХОДА
# ============================================================

def add_expense():
    print("\n" + "=" * 60)
    print("ДОБАВЛЕНИЕ РАСХОДА")
    print("=" * 60)

    name = input("Название расхода: ").strip()
    category = input("Категория: ").strip()

    try:
        amount = float(input("Сумма: "))

        if amount <= 0:
            print("Сумма должна быть больше нуля.")
            return

        expenses.append({
            "name": name,
            "amount": amount,
            "category": category
        })

        print("Расход успешно добавлен!")

    except ValueError:
        print("Введите число.")


# ============================================================
# 25. СТАТИСТИКА ПРОЕКТОВ
# ============================================================

def project_statistics():
    print("\n" + "=" * 60)
    print("СТАТИСТИКА ПРОЕКТОВ")
    print("=" * 60)

    total = len(projects)
    construction = 0
    finished = 0
    preparation = 0

    for project in projects:
        status = project["status"].lower()

        if "строительство" in status:
            construction += 1

        if "заверш" in status:
            finished += 1

        if "подготов" in status:
            preparation += 1

    print(f"Всего проектов: {total}")
    print(f"В строительстве: {construction}")
    print(f"Завершено: {finished}")
    print(f"На подготовке: {preparation}")


# ============================================================
# 26. ОБЩАЯ СТОИМОСТЬ ПРОЕКТОВ
# ============================================================

def total_projects_cost():
    total = 0

    for project in projects:
        total += project["price"]

    print("\n" + "=" * 60)
    print("ОБЩАЯ СТОИМОСТЬ ПРОЕКТОВ")
    print("=" * 60)

    print(f"{total:,} сом")


# ============================================================
# 27. СТОИМОСТЬ ТЕХНИКИ
# ============================================================

def equipment_cost():
    total = 0

    for item in equipment:
        total += item["price"]

    print("\n" + "=" * 60)
    print("СТОИМОСТЬ ТЕХНИКИ")
    print("=" * 60)

    print(f"Общая стоимость техники: {total:,} сом")


# ============================================================
# 28. ДОБАВЛЕНИЕ СОТРУДНИКА
# ============================================================

def add_employee():
    print("\n" + "=" * 60)
    print("ДОБАВЛЕНИЕ СОТРУДНИКА")
    print("=" * 60)

    try:
        employee_id = int(input("ID сотрудника: "))

        for employee in employees:
            if employee["id"] == employee_id:
                print("Такой ID уже существует.")
                return

        name = input("Имя: ").strip()
        position = input("Должность: ").strip()
        salary = float(input("Зарплата: "))
        experience = int(input("Опыт работы: "))
        phone = input("Телефон: ").strip()

        if salary <= 0 or experience < 0:
            print("Проверьте зарплату и опыт.")
            return

        employees.append({
            "id": employee_id,
            "name": name,
            "position": position,
            "salary": salary,
            "experience": experience,
            "phone": phone,
            "status": "Работает"
        })

        print("Сотрудник успешно добавлен!")

    except ValueError:
        print("Ошибка ввода.")


# ============================================================
# 29. ПОИСК СОТРУДНИКА
# ============================================================

def search_employee():
    print("\n" + "=" * 60)
    print("ПОИСК СОТРУДНИКА")
    print("=" * 60)

    text = input("Введите имя или должность: ").strip().lower()

    if not text:
        print("Введите данные для поиска.")
        return

    found = False

    for employee in employees:
        if (
            text in employee["name"].lower()
            or text in employee["position"].lower()
        ):
            print(f"""
ID: {employee['id']}
Имя: {employee['name']}
Должность: {employee['position']}
Зарплата: {employee['salary']:,} сом
Телефон: {employee['phone']}
Статус: {employee['status']}
""")
            found = True

    if not found:
        print("Сотрудник не найден.")


# ============================================================
# 30. ОБЩИЙ ОТЧЁТ
# ============================================================

def full_report():
    print("\n" + "=" * 60)
    print("ОБЩИЙ ОТЧЁТ КОМПАНИИ")
    print("=" * 60)

    project_sum = sum(project["price"] for project in projects)
    paid_sum = sum(project["paid"] for project in projects)
    expense_sum = sum(expense["amount"] for expense in expenses)
    salary_sum = sum(employee["salary"] for employee in employees)
    equipment_sum = sum(item["price"] for item in equipment)

    print(f"Сотрудников: {len(employees)}")
    print(f"Клиентов: {len(clients)}")
    print(f"Проектов: {len(projects)}")
    print(f"Стоимость всех проектов: {project_sum:,} сом")
    print(f"Получено от клиентов: {paid_sum:,} сом")
    print(f"Расходы: {expense_sum:,} сом")
    print(f"Фонд зарплаты: {salary_sum:,} сом")
    print(f"Стоимость техники: {equipment_sum:,} сом")


# ============================================================
# 31. ГЛАВНОЕ МЕНЮ
# ============================================================

def main():

    while True:

        print("\n")
        print("=" * 65)
        print("              КУТ КУРУЛУШ")
        print("          СТРОИТЕЛЬНАЯ КОМПАНИЯ")
        print("=" * 65)

        print("""
1.  Информация о компании
2.  Сотрудники
3.  Клиенты
4.  Все проекты
5.  Материалы
6.  Строительная техника
7.  Рассчитать строительство
8.  Добавить проект
9.  Найти проект
10. Изменить статус проекта
11. Изменить готовность проекта
12. Зарплатный отчёт
13. Расходы
14. Финансовый отчёт
15. Добавить платёж
16. Добавить материал
17. Добавить расход
18. Статистика проектов
19. Общая стоимость проектов
20. Стоимость техники
21. Добавить сотрудника
22. Найти сотрудника
23. Общий отчёт
0.  Выход
""")

        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            show_company()

        elif choice == "2":
            show_employees()

        elif choice == "3":
            show_clients()

        elif choice == "4":
            show_projects()

        elif choice == "5":
            show_materials()

        elif choice == "6":
            show_equipment()

        elif choice == "7":
            calculate_building()

        elif choice == "8":
            add_project()

        elif choice == "9":
            search_project()

        elif choice == "10":
            change_status()

        elif choice == "11":
            change_progress()

        elif choice == "12":
            salary_report()

        elif choice == "13":
            show_expenses()

        elif choice == "14":
            financial_report()

        elif choice == "15":
            add_payment()

        elif choice == "16":
            add_material()

        elif choice == "17":
            add_expense()

        elif choice == "18":
            project_statistics()

        elif choice == "19":
            total_projects_cost()

        elif choice == "20":
            equipment_cost()

        elif choice == "21":
            add_employee()

        elif choice == "22":
            search_employee()

        elif choice == "23":
            full_report()

        elif choice == "0":
            print("\n" + "=" * 60)
            print("Спасибо за использование программы!")
            print("КУТ КУРУЛУШ")
            print("Строим качественно и надёжно!")
            print("=" * 60)
            break

        else:
            print("\nОшибка! Выберите пункт от 0 до 23.")


# ============================================================
# ЗАПУСК ПРОГРАММЫ
# ============================================================

if __name__ == "__main__":
    main()
