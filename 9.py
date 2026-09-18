from datetime import datetime
import json
import os


# ==========================================================
# НАСТРОЙКИ
# ==========================================================

CASH_FILE = "cash_register_data.json"
OPERATIONS_FILE = "cash_operations.json"


# ==========================================================
# ДАННЫЕ КАССЫ
# ==========================================================

cash_register = {
    "cash": 0.0,
    "card": 0.0,
    "total": 0.0,
    "orders": 0,
    "refunds": 0.0,
    "shift_open": False,
    "cashier": "",
    "shift_start": "",
    "shift_end": "",
    "opening_cash": 0.0
}

operations = []


# ==========================================================
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ==========================================================

def get_time():
    """Возвращает текущую дату и время."""
    return datetime.now().strftime("%d.%m.%Y %H:%M:%S")


def print_line():
    print("-" * 60)


def pause():
    input("\nНажмите Enter, чтобы продолжить...")


def money(value):
    """Красивый вывод суммы."""
    return f"{value:.2f} сом"


def save_data():
    """Сохраняет данные кассы в файл."""
    try:
        with open(CASH_FILE, "w", encoding="utf-8") as file:
            json.dump(cash_register, file, ensure_ascii=False, indent=4)

        with open(OPERATIONS_FILE, "w", encoding="utf-8") as file:
            json.dump(operations, file, ensure_ascii=False, indent=4)

    except Exception as error:
        print(f"Ошибка сохранения данных: {error}")


def load_data():
    """Загружает данные кассы из файлов."""
    global cash_register
    global operations

    if os.path.exists(CASH_FILE):
        try:
            with open(CASH_FILE, "r", encoding="utf-8") as file:
                saved_cash = json.load(file)

                for key in cash_register:
                    if key in saved_cash:
                        cash_register[key] = saved_cash[key]

        except Exception as error:
            print(f"Ошибка загрузки кассы: {error}")

    if os.path.exists(OPERATIONS_FILE):
        try:
            with open(OPERATIONS_FILE, "r", encoding="utf-8") as file:
                operations = json.load(file)

        except Exception as error:
            print(f"Ошибка загрузки операций: {error}")


def get_number(text):
    """Безопасный ввод числа."""
    while True:
        try:
            number = float(input(text).replace(",", "."))

            if number < 0:
                print("Число не может быть отрицательным.")
                continue

            return number

        except ValueError:
            print("Ошибка! Введите число.")


def get_positive_number(text):
    """Ввод положительного числа."""
    while True:
        number = get_number(text)

        if number <= 0:
            print("Сумма должна быть больше нуля.")
        else:
            return number


def add_operation(
    operation_type,
    amount=0,
    method="",
    order_number="",
    description=""
):
    """Добавляет операцию в историю."""
    operation = {
        "id": len(operations) + 1,
        "type": operation_type,
        "amount": round(amount, 2),
        "method": method,
        "order_number": order_number,
        "description": description,
        "time": get_time()
    }

    operations.append(operation)
    save_data()


# ==========================================================
# РАБОТА СО СМЕНОЙ
# ==========================================================

def open_shift():
    """Открытие кассовой смены."""
    print_line()
    print("ОТКРЫТИЕ КАССОВОЙ СМЕНЫ")
    print_line()

    if cash_register["shift_open"]:
        print("Смена уже открыта.")
        print(f"Кассир: {cash_register['cashier']}")
        print(f"Время открытия: {cash_register['shift_start']}")
        return

    cashier = input("Введите имя кассира: ").strip()

    if not cashier:
        cashier = "Главный кассир"

    opening_cash = get_number("Введите сумму в кассе в начале смены: ")

    cash_register["shift_open"] = True
    cash_register["cashier"] = cashier
    cash_register["shift_start"] = get_time()
    cash_register["shift_end"] = ""
    cash_register["opening_cash"] = opening_cash
    cash_register["cash"] = opening_cash
    cash_register["card"] = 0.0
    cash_register["total"] = 0.0
    cash_register["orders"] = 0
    cash_register["refunds"] = 0.0

    add_operation(
        operation_type="Открытие смены",
        amount=opening_cash,
        description=f"Кассир: {cashier}"
    )

    save_data()

    print("\nСмена успешно открыта!")
    print(f"Кассир: {cashier}")
    print(f"Начальная сумма: {money(opening_cash)}")


def close_shift():
    """Закрытие кассовой смены."""
    print_line()
    print("ЗАКРЫТИЕ КАССОВОЙ СМЕНЫ")
    print_line()

    if not cash_register["shift_open"]:
        print("Смена ещё не открыта.")
        return

    print(f"Кассир: {cash_register['cashier']}")
    print(f"Открытие смены: {cash_register['shift_start']}")
    print(f"Наличные: {money(cash_register['cash'])}")
    print(f"Карта: {money(cash_register['card'])}")
    print(f"Продажи: {money(cash_register['total'])}")
    print(f"Количество заказов: {cash_register['orders']}")
    print(f"Возвраты: {money(cash_register['refunds'])}")

    print_line()

    confirm = input("Вы точно хотите закрыть смену? (да/нет): ").lower()

    if confirm != "да":
        print("Закрытие смены отменено.")
        return

    cash_register["shift_open"] = False
    cash_register["shift_end"] = get_time()

    add_operation(
        operation_type="Закрытие смены",
        amount=cash_register["total"],
        description=f"Кассир: {cash_register['cashier']}"
    )

    save_data()

    print("\nСмена успешно закрыта!")
    print(f"Время закрытия: {cash_register['shift_end']}")


# ==========================================================
# ПРОВЕРКА КАССЫ
# ==========================================================

def check_shift():
    """Проверяет, открыта ли смена."""
    if not cash_register["shift_open"]:
        print("\nСначала необходимо открыть кассовую смену!")
        return False

    return True


def show_cash_status():
    """Показывает состояние кассы."""
    print_line()
    print("СОСТОЯНИЕ КАССЫ")
    print_line()

    status = "ОТКРЫТА" if cash_register["shift_open"] else "ЗАКРЫТА"

    print(f"Статус смены: {status}")
    print(f"Кассир: {cash_register['cashier'] or 'Не указан'}")
    print(f"Начало смены: {cash_register['shift_start'] or 'Нет данных'}")
    print(f"Конец смены: {cash_register['shift_end'] or 'Нет данных'}")
    print()
    print(f"Наличные: {money(cash_register['cash'])}")
    print(f"Банковская карта: {money(cash_register['card'])}")
    print(f"Всего продаж: {money(cash_register['total'])}")
    print(f"Возвраты: {money(cash_register['refunds'])}")
    print(f"Количество заказов: {cash_register['orders']}")

    expected_cash = (
        cash_register["opening_cash"]
        + cash_register["cash"]
        - cash_register["opening_cash"]
    )

    print(f"Ожидаемые наличные: {money(expected_cash)}")


# ==========================================================
# ОПЛАТА ЗАКАЗА
# ==========================================================

def choose_payment_method():
    """Выбор способа оплаты."""
    print_line()
    print("СПОСОБ ОПЛАТЫ")
    print_line()

    print("1. Наличные")
    print("2. Банковская карта")
    print("3. Перевод")

    while True:
        choice = input("Выберите способ оплаты: ")

        if choice == "1":
            return "Наличные"

        if choice == "2":
            return "Банковская карта"

        if choice == "3":
            return "Перевод"

        print("Неверный выбор.")


def payment():
    """Ручная оплата заказа."""
    print_line()
    print("ОПЛАТА ЗАКАЗА")
    print_line()

    if not check_shift():
        return

    order_number = input("Введите номер заказа: ").strip()

    if not order_number:
        print("Номер заказа не может быть пустым.")
        return

    amount = get_positive_number("Введите сумму заказа: ")
    method = choose_payment_method()

    received = amount

    if method == "Наличные":
        received = get_positive_number(
            "Сколько денег получил кассир: "
        )

        if received < amount:
            print("Недостаточно денег.")
            return

        change = received - amount
        print(f"Сдача: {money(change)}")
    else:
        print("Оплата картой или переводом подтверждена.")

    if method == "Наличные":
        cash_register["cash"] += amount

    elif method == "Банковская карта":
        cash_register["card"] += amount

    elif method == "Перевод":
        cash_register["card"] += amount

    cash_register["total"] += amount
    cash_register["orders"] += 1

    add_operation(
        operation_type="Оплата заказа",
        amount=amount,
        method=method,
        order_number=order_number,
        description="Заказ успешно оплачен"
    )

    save_data()

    print_line()
    print("ОПЛАТА УСПЕШНА")
    print_line()
    print(f"Номер заказа: {order_number}")
    print(f"Сумма: {money(amount)}")
    print(f"Способ оплаты: {method}")


def register_payment(order_number, amount, method):
    """
    Функция для подключения к ресторану.

    Её можно вызвать из restaurant.py,
    чтобы заказ автоматически попадал в кассу.
    """

    if not cash_register["shift_open"]:
        return False, "Кассовая смена закрыта."

    if amount <= 0:
        return False, "Сумма должна быть больше нуля."

    allowed_methods = [
        "Наличные",
        "Банковская карта",
        "Перевод"
    ]

    if method not in allowed_methods:
        return False, "Неизвестный способ оплаты."

    if method == "Наличные":
        cash_register["cash"] += amount
    else:
        cash_register["card"] += amount

    cash_register["total"] += amount
    cash_register["orders"] += 1

    add_operation(
        operation_type="Автоматическая оплата",
        amount=amount,
        method=method,
        order_number=order_number,
        description="Оплата из программы ресторана"
    )

    save_data()

    return True, "Оплата успешно зарегистрирована."


# ==========================================================
# ВОЗВРАТ ДЕНЕГ
# ==========================================================

def refund():
    """Возврат денег клиенту."""
    print_line()
    print("ВОЗВРАТ ДЕНЕГ")
    print_line()

    if not check_shift():
        return

    order_number = input("Введите номер заказа для возврата: ").strip()
    amount = get_positive_number("Введите сумму возврата: ")

    if amount > cash_register["total"]:
        print("Нельзя вернуть больше суммы продаж.")
        return

    print("Выберите способ возврата:")
    print("1. Наличные")
    print("2. Банковская карта")

    choice = input("Ваш выбор: ")

    if choice == "1":
        if amount > cash_register["cash"]:
            print("В кассе недостаточно наличных.")
            return

        cash_register["cash"] -= amount
        method = "Наличные"

    elif choice == "2":
        if amount > cash_register["card"]:
            print("Недостаточно средств по безналичной оплате.")
            return

        cash_register["card"] -= amount
        method = "Банковская карта"

    else:
        print("Неверный выбор.")
        return

    cash_register["total"] -= amount
    cash_register["refunds"] += amount

    add_operation(
        operation_type="Возврат",
        amount=amount,
        method=method,
        order_number=order_number,
        description="Деньги возвращены клиенту"
    )

    save_data()

    print("\nВозврат успешно выполнен.")
    print(f"Номер заказа: {order_number}")
    print(f"Возвращено: {money(amount)}")


# ==========================================================
# ДОПОЛНИТЕЛЬНЫЕ ОПЕРАЦИИ
# ==========================================================

def add_cash():
    """Внесение дополнительных наличных."""
    print_line()
    print("ВНЕСЕНИЕ НАЛИЧНЫХ")
    print_line()

    if not check_shift():
        return

    amount = get_positive_number("Введите сумму внесения: ")
    reason = input("Причина внесения: ").strip()

    cash_register["cash"] += amount

    add_operation(
        operation_type="Внесение наличных",
        amount=amount,
        method="Наличные",
        description=reason
    )

    save_data()

    print(f"Внесено в кассу: {money(amount)}")


def remove_cash():
    """Изъятие наличных."""
    print_line()
    print("ИЗЪЯТИЕ НАЛИЧНЫХ")
    print_line()

    if not check_shift():
        return

    amount = get_positive_number("Введите сумму изъятия: ")

    if amount > cash_register["cash"]:
        print("В кассе недостаточно наличных.")
        return

    reason = input("Причина изъятия: ").strip()

    cash_register["cash"] -= amount

    add_operation(
        operation_type="Изъятие наличных",
        amount=amount,
        method="Наличные",
        description=reason
    )

    save_data()

    print(f"Изъято из кассы: {money(amount)}")


def print_receipt():
    """Печать чека в консоль."""
    print_line()
    print("ПЕЧАТЬ ЧЕКА")
    print_line()

    if not operations:
        print("Операций пока нет.")
        return

    last_operation = operations[-1]

    print("                 РЕСТОРАН")
    print("              КАССОВЫЙ ЧЕК")
    print_line()
    print(f"Номер операции: {last_operation['id']}")
    print(f"Тип операции: {last_operation['type']}")
    print(f"Номер заказа: {last_operation['order_number']}")
    print(f"Сумма: {money(last_operation['amount'])}")
    print(f"Способ оплаты: {last_operation['method']}")
    print(f"Дата: {last_operation['time']}")
    print(f"Описание: {last_operation['description']}")
    print_line()
    print("       Спасибо за посещение!")


# ==========================================================
# ИСТОРИЯ ОПЕРАЦИЙ
# ==========================================================

def show_operations():
    """Показывает все операции."""
    print_line()
    print("ИСТОРИЯ ОПЕРАЦИЙ")
    print_line()

    if not operations:
        print("История пока пустая.")
        return

    for operation in operations:
        print(f"\nID операции: {operation['id']}")
        print(f"Тип: {operation['type']}")
        print(f"Сумма: {money(operation['amount'])}")
        print(f"Метод: {operation['method'] or 'Не указан'}")
        print(f"Заказ: {operation['order_number'] or 'Не указан'}")
        print(f"Время: {operation['time']}")
        print(f"Описание: {operation['description']}")
        print_line()


def search_order():
    """Поиск операций по номеру заказа."""
    print_line()
    print("ПОИСК ЗАКАЗА")
    print_line()

    order_number = input("Введите номер заказа: ").strip()

    found = False

    for operation in operations:
        if operation["order_number"] == order_number:
            found = True

            print(f"\nID: {operation['id']}")
            print(f"Тип: {operation['type']}")
            print(f"Сумма: {money(operation['amount'])}")
            print(f"Способ оплаты: {operation['method']}")
            print(f"Дата: {operation['time']}")
            print(f"Описание: {operation['description']}")

    if not found:
        print("Заказ не найден.")


def show_daily_report():
    """Показывает отчёт за текущий день."""
    print_line()
    print("ОТЧЁТ ЗА СЕГОДНЯ")
    print_line()

    today = datetime.now().strftime("%d.%m.%Y")

    daily_total = 0
    daily_refunds = 0
    daily_orders = 0

    for operation in operations:
        if operation["time"].startswith(today):
            if operation["type"] in [
                "Оплата заказа",
                "Автоматическая оплата"
            ]:
                daily_total += operation["amount"]
                daily_orders += 1

            elif operation["type"] == "Возврат":
                daily_refunds += operation["amount"]

    print(f"Дата: {today}")
    print(f"Количество заказов: {daily_orders}")
    print(f"Продажи: {money(daily_total)}")
    print(f"Возвраты: {money(daily_refunds)}")
    print(f"Итог: {money(daily_total - daily_refunds)}")


def clear_history():
    """Удаление истории операций."""
    print_line()
    print("ОЧИСТКА ИСТОРИИ")
    print_line()

    print("Внимание! Все операции будут удалены.")

    confirm = input("Введите УДАЛИТЬ для подтверждения: ")

    if confirm == "УДАЛИТЬ":
        operations.clear()
        save_data()
        print("История операций очищена.")
    else:
        print("Очистка отменена.")


# ==========================================================
# МЕНЮ КАССИРА
# ==========================================================

def cashier_menu():
    while True:
        print("\n")
        print("=" * 60)
        print("                 КАССА РЕСТОРАНА")
        print("=" * 60)

        print("1. Открыть смену")
        print("2. Закрыть смену")
        print("3. Оплатить заказ")
        print("4. Вернуть деньги")
        print("5. Состояние кассы")
        print("6. Внести наличные")
        print("7. Изъять наличные")
        print("8. История операций")
        print("9. Поиск заказа")
        print("10. Отчёт за сегодня")
        print("11. Напечатать последний чек")
        print("12. Очистить историю")
        print("0. Выход")

        print_line()

        choice = input("Выберите действие: ")

        if choice == "1":
            open_shift()
            pause()

        elif choice == "2":
            close_shift()
            pause()

        elif choice == "3":
            payment()
            pause()

        elif choice == "4":
            refund()
            pause()

        elif choice == "5":
            show_cash_status()
            pause()

        elif choice == "6":
            add_cash()
            pause()

        elif choice == "7":
            remove_cash()
            pause()

        elif choice == "8":
            show_operations()
            pause()

        elif choice == "9":
            search_order()
            pause()

        elif choice == "10":
            show_daily_report()
            pause()

        elif choice == "11":
            print_receipt()
            pause()

        elif choice == "12":
            clear_history()
            pause()

        elif choice == "0":
            print("Выход из кассы.")
            break

        else:
            print("Неверный выбор. Попробуйте ещё раз.")


# ==========================================================
# ЗАПУСК ПРОГРАММЫ
# ==========================================================

def main():
    load_data()

    print("=" * 60)
    print("Добро пожаловать в кассовую программу ресторана!")
    print("=" * 60)

    cashier_menu()


if __name__ == "__main__":
    main()


from datetime import datetime
import json
import os


# ==========================================================
# НАСТРОЙКИ
# ==========================================================

CASH_FILE = "cash_register_data.json"
OPERATIONS_FILE = "cash_operations.json"


# ==========================================================
# ДАННЫЕ КАССЫ
# ==========================================================

cash_register = {
    "cash": 0.0,
    "card": 0.0,
    "total": 0.0,
    "orders": 0,
    "refunds": 0.0,
    "shift_open": False,
    "cashier": "",
    "shift_start": "",
    "shift_end": "",
    "opening_cash": 0.0
}

operations = []


# ==========================================================
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ==========================================================

def get_time():
    """Возвращает текущую дату и время."""
    return datetime.now().strftime("%d.%m.%Y %H:%M:%S")


def print_line():
    print("-" * 60)


def pause():
    input("\nНажмите Enter, чтобы продолжить...")


def money(value):
    """Красивый вывод суммы."""
    return f"{value:.2f} сом"


def save_data():
    """Сохраняет данные кассы в файл."""
    try:
        with open(CASH_FILE, "w", encoding="utf-8") as file:
            json.dump(cash_register, file, ensure_ascii=False, indent=4)

        with open(OPERATIONS_FILE, "w", encoding="utf-8") as file:
            json.dump(operations, file, ensure_ascii=False, indent=4)

    except Exception as error:
        print(f"Ошибка сохранения данных: {error}")


def load_data():
    """Загружает данные кассы из файлов."""
    global cash_register
    global operations

    if os.path.exists(CASH_FILE):
        try:
            with open(CASH_FILE, "r", encoding="utf-8") as file:
                saved_cash = json.load(file)

                for key in cash_register:
                    if key in saved_cash:
                        cash_register[key] = saved_cash[key]

        except Exception as error:
            print(f"Ошибка загрузки кассы: {error}")

    if os.path.exists(OPERATIONS_FILE):
        try:
            with open(OPERATIONS_FILE, "r", encoding="utf-8") as file:
                operations = json.load(file)

        except Exception as error:
            print(f"Ошибка загрузки операций: {error}")


def get_number(text):
    """Безопасный ввод числа."""
    while True:
        try:
            number = float(input(text).replace(",", "."))

            if number < 0:
                print("Число не может быть отрицательным.")
                continue

            return number

        except ValueError:
            print("Ошибка! Введите число.")


def get_positive_number(text):
    """Ввод положительного числа."""
    while True:
        number = get_number(text)

        if number <= 0:
            print("Сумма должна быть больше нуля.")
        else:
            return number


def add_operation(
    operation_type,
    amount=0,
    method="",
    order_number="",
    description=""
):
    """Добавляет операцию в историю."""
    operation = {
        "id": len(operations) + 1,
        "type": operation_type,
        "amount": round(amount, 2),
        "method": method,
        "order_number": order_number,
        "description": description,
        "time": get_time()
    }

    operations.append(operation)
    save_data()


# ==========================================================
# РАБОТА СО СМЕНОЙ
# ==========================================================

def open_shift():
    """Открытие кассовой смены."""
    print_line()
    print("ОТКРЫТИЕ КАССОВОЙ СМЕНЫ")
    print_line()

    if cash_register["shift_open"]:
        print("Смена уже открыта.")
        print(f"Кассир: {cash_register['cashier']}")
        print(f"Время открытия: {cash_register['shift_start']}")
        return

    cashier = input("Введите имя кассира: ").strip()

    if not cashier:
        cashier = "Главный кассир"

    opening_cash = get_number("Введите сумму в кассе в начале смены: ")

    cash_register["shift_open"] = True
    cash_register["cashier"] = cashier
    cash_register["shift_start"] = get_time()
    cash_register["shift_end"] = ""
    cash_register["opening_cash"] = opening_cash
    cash_register["cash"] = opening_cash
    cash_register["card"] = 0.0
    cash_register["total"] = 0.0
    cash_register["orders"] = 0
    cash_register["refunds"] = 0.0

    add_operation(
        operation_type="Открытие смены",
        amount=opening_cash,
        description=f"Кассир: {cashier}"
    )

    save_data()

    print("\nСмена успешно открыта!")
    print(f"Кассир: {cashier}")
    print(f"Начальная сумма: {money(opening_cash)}")


def close_shift():
    """Закрытие кассовой смены."""
    print_line()
    print("ЗАКРЫТИЕ КАССОВОЙ СМЕНЫ")
    print_line()

    if not cash_register["shift_open"]:
        print("Смена ещё не открыта.")
        return

    print(f"Кассир: {cash_register['cashier']}")
    print(f"Открытие смены: {cash_register['shift_start']}")
    print(f"Наличные: {money(cash_register['cash'])}")
    print(f"Карта: {money(cash_register['card'])}")
    print(f"Продажи: {money(cash_register['total'])}")
    print(f"Количество заказов: {cash_register['orders']}")
    print(f"Возвраты: {money(cash_register['refunds'])}")

    print_line()

    confirm = input("Вы точно хотите закрыть смену? (да/нет): ").lower()

    if confirm != "да":
        print("Закрытие смены отменено.")
        return

    cash_register["shift_open"] = False
    cash_register["shift_end"] = get_time()

    add_operation(
        operation_type="Закрытие смены",
        amount=cash_register["total"],
        description=f"Кассир: {cash_register['cashier']}"
    )

    save_data()

    print("\nСмена успешно закрыта!")
    print(f"Время закрытия: {cash_register['shift_end']}")


# ==========================================================
# ПРОВЕРКА КАССЫ
# ==========================================================

def check_shift():
    """Проверяет, открыта ли смена."""
    if not cash_register["shift_open"]:
        print("\nСначала необходимо открыть кассовую смену!")
        return False

    return True


def show_cash_status():
    """Показывает состояние кассы."""
    print_line()
    print("СОСТОЯНИЕ КАССЫ")
    print_line()

    status = "ОТКРЫТА" if cash_register["shift_open"] else "ЗАКРЫТА"

    print(f"Статус смены: {status}")
    print(f"Кассир: {cash_register['cashier'] or 'Не указан'}")
    print(f"Начало смены: {cash_register['shift_start'] or 'Нет данных'}")
    print(f"Конец смены: {cash_register['shift_end'] or 'Нет данных'}")
    print()
    print(f"Наличные: {money(cash_register['cash'])}")
    print(f"Банковская карта: {money(cash_register['card'])}")
    print(f"Всего продаж: {money(cash_register['total'])}")
    print(f"Возвраты: {money(cash_register['refunds'])}")
    print(f"Количество заказов: {cash_register['orders']}")

    expected_cash = (
        cash_register["opening_cash"]
        + cash_register["cash"]
        - cash_register["opening_cash"]
    )

    print(f"Ожидаемые наличные: {money(expected_cash)}")


# ==========================================================
# ОПЛАТА ЗАКАЗА
# ==========================================================

def choose_payment_method():
    """Выбор способа оплаты."""
    print_line()
    print("СПОСОБ ОПЛАТЫ")
    print_line()

    print("1. Наличные")
    print("2. Банковская карта")
    print("3. Перевод")

    while True:
        choice = input("Выберите способ оплаты: ")

        if choice == "1":
            return "Наличные"

        if choice == "2":
            return "Банковская карта"

        if choice == "3":
            return "Перевод"

        print("Неверный выбор.")


def payment():
    """Ручная оплата заказа."""
    print_line()
    print("ОПЛАТА ЗАКАЗА")
    print_line()

    if not check_shift():
        return

    order_number = input("Введите номер заказа: ").strip()

    if not order_number:
        print("Номер заказа не может быть пустым.")
        return

    amount = get_positive_number("Введите сумму заказа: ")
    method = choose_payment_method()

    received = amount

    if method == "Наличные":
        received = get_positive_number(
            "Сколько денег получил кассир: "
        )

        if received < amount:
            print("Недостаточно денег.")
            return

        change = received - amount
        print(f"Сдача: {money(change)}")
    else:
        print("Оплата картой или переводом подтверждена.")

    if method == "Наличные":
        cash_register["cash"] += amount

    elif method == "Банковская карта":
        cash_register["card"] += amount

    elif method == "Перевод":
        cash_register["card"] += amount

    cash_register["total"] += amount
    cash_register["orders"] += 1

    add_operation(
        operation_type="Оплата заказа",
        amount=amount,
        method=method,
        order_number=order_number,
        description="Заказ успешно оплачен"
    )

    save_data()

    print_line()
    print("ОПЛАТА УСПЕШНА")
    print_line()
    print(f"Номер заказа: {order_number}")
    print(f"Сумма: {money(amount)}")
    print(f"Способ оплаты: {method}")


def register_payment(order_number, amount, method):
    """
    Функция для подключения к ресторану.

    Её можно вызвать из restaurant.py,
    чтобы заказ автоматически попадал в кассу.
    """

    if not cash_register["shift_open"]:
        return False, "Кассовая смена закрыта."

    if amount <= 0:
        return False, "Сумма должна быть больше нуля."

    allowed_methods = [
        "Наличные",
        "Банковская карта",
        "Перевод"
    ]

    if method not in allowed_methods:
        return False, "Неизвестный способ оплаты."

    if method == "Наличные":
        cash_register["cash"] += amount
    else:
        cash_register["card"] += amount

    cash_register["total"] += amount
    cash_register["orders"] += 1

    add_operation(
        operation_type="Автоматическая оплата",
        amount=amount,
        method=method,
        order_number=order_number,
        description="Оплата из программы ресторана"
    )

    save_data()

    return True, "Оплата успешно зарегистрирована."


# ==========================================================
# ВОЗВРАТ ДЕНЕГ
# ==========================================================

def refund():
    """Возврат денег клиенту."""
    print_line()
    print("ВОЗВРАТ ДЕНЕГ")
    print_line()

    if not check_shift():
        return

    order_number = input("Введите номер заказа для возврата: ").strip()
    amount = get_positive_number("Введите сумму возврата: ")

    if amount > cash_register["total"]:
        print("Нельзя вернуть больше суммы продаж.")
        return

    print("Выберите способ возврата:")
    print("1. Наличные")
    print("2. Банковская карта")

    choice = input("Ваш выбор: ")

    if choice == "1":
        if amount > cash_register["cash"]:
            print("В кассе недостаточно наличных.")
            return

        cash_register["cash"] -= amount
        method = "Наличные"

    elif choice == "2":
        if amount > cash_register["card"]:
            print("Недостаточно средств по безналичной оплате.")
            return

        cash_register["card"] -= amount
        method = "Банковская карта"

    else:
        print("Неверный выбор.")
        return

    cash_register["total"] -= amount
    cash_register["refunds"] += amount

    add_operation(
        operation_type="Возврат",
        amount=amount,
        method=method,
        order_number=order_number,
        description="Деньги возвращены клиенту"
    )

    save_data()

    print("\nВозврат успешно выполнен.")
    print(f"Номер заказа: {order_number}")
    print(f"Возвращено: {money(amount)}")


# ==========================================================
# ДОПОЛНИТЕЛЬНЫЕ ОПЕРАЦИИ
# ==========================================================

def add_cash():
    """Внесение дополнительных наличных."""
    print_line()
    print("ВНЕСЕНИЕ НАЛИЧНЫХ")
    print_line()

    if not check_shift():
        return

    amount = get_positive_number("Введите сумму внесения: ")
    reason = input("Причина внесения: ").strip()

    cash_register["cash"] += amount

    add_operation(
        operation_type="Внесение наличных",
        amount=amount,
        method="Наличные",
        description=reason
    )

    save_data()

    print(f"Внесено в кассу: {money(amount)}")


def remove_cash():
    """Изъятие наличных."""
    print_line()
    print("ИЗЪЯТИЕ НАЛИЧНЫХ")
    print_line()

    if not check_shift():
        return

    amount = get_positive_number("Введите сумму изъятия: ")

    if amount > cash_register["cash"]:
        print("В кассе недостаточно наличных.")
        return

    reason = input("Причина изъятия: ").strip()

    cash_register["cash"] -= amount

    add_operation(
        operation_type="Изъятие наличных",
        amount=amount,
        method="Наличные",
        description=reason
    )

    save_data()

    print(f"Изъято из кассы: {money(amount)}")


def print_receipt():
    """Печать чека в консоль."""
    print_line()
    print("ПЕЧАТЬ ЧЕКА")
    print_line()

    if not operations:
        print("Операций пока нет.")
        return

    last_operation = operations[-1]

    print("                 РЕСТОРАН")
    print("              КАССОВЫЙ ЧЕК")
    print_line()
    print(f"Номер операции: {last_operation['id']}")
    print(f"Тип операции: {last_operation['type']}")
    print(f"Номер заказа: {last_operation['order_number']}")
    print(f"Сумма: {money(last_operation['amount'])}")
    print(f"Способ оплаты: {last_operation['method']}")
    print(f"Дата: {last_operation['time']}")
    print(f"Описание: {last_operation['description']}")
    print_line()
    print("       Спасибо за посещение!")


# ==========================================================
# ИСТОРИЯ ОПЕРАЦИЙ
# ==========================================================

def show_operations():
    """Показывает все операции."""
    print_line()
    print("ИСТОРИЯ ОПЕРАЦИЙ")
    print_line()

    if not operations:
        print("История пока пустая.")
        return

    for operation in operations:
        print(f"\nID операции: {operation['id']}")
        print(f"Тип: {operation['type']}")
        print(f"Сумма: {money(operation['amount'])}")
        print(f"Метод: {operation['method'] or 'Не указан'}")
        print(f"Заказ: {operation['order_number'] or 'Не указан'}")
        print(f"Время: {operation['time']}")
        print(f"Описание: {operation['description']}")
        print_line()


def search_order():
    """Поиск операций по номеру заказа."""
    print_line()
    print("ПОИСК ЗАКАЗА")
    print_line()

    order_number = input("Введите номер заказа: ").strip()

    found = False

    for operation in operations:
        if operation["order_number"] == order_number:
            found = True

            print(f"\nID: {operation['id']}")
            print(f"Тип: {operation['type']}")
            print(f"Сумма: {money(operation['amount'])}")
            print(f"Способ оплаты: {operation['method']}")
            print(f"Дата: {operation['time']}")
            print(f"Описание: {operation['description']}")

    if not found:
        print("Заказ не найден.")


def show_daily_report():
    """Показывает отчёт за текущий день."""
    print_line()
    print("ОТЧЁТ ЗА СЕГОДНЯ")
    print_line()

    today = datetime.now().strftime("%d.%m.%Y")

    daily_total = 0
    daily_refunds = 0
    daily_orders = 0

    for operation in operations:
        if operation["time"].startswith(today):
            if operation["type"] in [
                "Оплата заказа",
                "Автоматическая оплата"
            ]:
                daily_total += operation["amount"]
                daily_orders += 1

            elif operation["type"] == "Возврат":
                daily_refunds += operation["amount"]

    print(f"Дата: {today}")
    print(f"Количество заказов: {daily_orders}")
    print(f"Продажи: {money(daily_total)}")
    print(f"Возвраты: {money(daily_refunds)}")
    print(f"Итог: {money(daily_total - daily_refunds)}")


def clear_history():
    """Удаление истории операций."""
    print_line()
    print("ОЧИСТКА ИСТОРИИ")
    print_line()

    print("Внимание! Все операции будут удалены.")

    confirm = input("Введите УДАЛИТЬ для подтверждения: ")

    if confirm == "УДАЛИТЬ":
        operations.clear()
        save_data()
        print("История операций очищена.")
    else:
        print("Очистка отменена.")


# ==========================================================
# МЕНЮ КАССИРА
# ==========================================================

def cashier_menu():
    while True:
        print("\n")
        print("=" * 60)
        print("                 КАССА РЕСТОРАНА")
        print("=" * 60)

        print("1. Открыть смену")
        print("2. Закрыть смену")
        print("3. Оплатить заказ")
        print("4. Вернуть деньги")
        print("5. Состояние кассы")
        print("6. Внести наличные")
        print("7. Изъять наличные")
        print("8. История операций")
        print("9. Поиск заказа")
        print("10. Отчёт за сегодня")
        print("11. Напечатать последний чек")
        print("12. Очистить историю")
        print("0. Выход")

        print_line()

        choice = input("Выберите действие: ")

        if choice == "1":
            open_shift()
            pause()

        elif choice == "2":
            close_shift()
            pause()

        elif choice == "3":
            payment()
            pause()

        elif choice == "4":
            refund()
            pause()

        elif choice == "5":
            show_cash_status()
            pause()

        elif choice == "6":
            add_cash()
            pause()

        elif choice == "7":
            remove_cash()
            pause()

        elif choice == "8":
            show_operations()
            pause()

        elif choice == "9":
            search_order()
            pause()

        elif choice == "10":
            show_daily_report()
            pause()

        elif choice == "11":
            print_receipt()
            pause()

        elif choice == "12":
            clear_history()
            pause()

        elif choice == "0":
            print("Выход из кассы.")
            break

        else:
            print("Неверный выбор. Попробуйте ещё раз.")


# ==========================================================
# ЗАПУСК ПРОГРАММЫ
# ==========================================================

def main():
    load_data()

    print("=" * 60)
    print("Добро пожаловать в кассовую программу ресторана!")
    print("=" * 60)

    cashier_menu()


if __name__ == "__main__":
    main()


from datetime import datetime
import json
import os


# ==========================================================
# НАСТРОЙКИ
# ==========================================================

CASH_FILE = "cash_register_data.json"
OPERATIONS_FILE = "cash_operations.json"


# ==========================================================
# ДАННЫЕ КАССЫ
# ==========================================================

cash_register = {
    "cash": 0.0,
    "card": 0.0,
    "total": 0.0,
    "orders": 0,
    "refunds": 0.0,
    "shift_open": False,
    "cashier": "",
    "shift_start": "",
    "shift_end": "",
    "opening_cash": 0.0
}

operations = []


# ==========================================================
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ==========================================================

def get_time():
    """Возвращает текущую дату и время."""
    return datetime.now().strftime("%d.%m.%Y %H:%M:%S")


def print_line():
    print("-" * 60)


def pause():
    input("\nНажмите Enter, чтобы продолжить...")


def money(value):
    """Красивый вывод суммы."""
    return f"{value:.2f} сом"


def save_data():
    """Сохраняет данные кассы в файл."""
    try:
        with open(CASH_FILE, "w", encoding="utf-8") as file:
            json.dump(cash_register, file, ensure_ascii=False, indent=4)

        with open(OPERATIONS_FILE, "w", encoding="utf-8") as file:
            json.dump(operations, file, ensure_ascii=False, indent=4)

    except Exception as error:
        print(f"Ошибка сохранения данных: {error}")


def load_data():
    """Загружает данные кассы из файлов."""
    global cash_register
    global operations

    if os.path.exists(CASH_FILE):
        try:
            with open(CASH_FILE, "r", encoding="utf-8") as file:
                saved_cash = json.load(file)

                for key in cash_register:
                    if key in saved_cash:
                        cash_register[key] = saved_cash[key]

        except Exception as error:
            print(f"Ошибка загрузки кассы: {error}")

    if os.path.exists(OPERATIONS_FILE):
        try:
            with open(OPERATIONS_FILE, "r", encoding="utf-8") as file:
                operations = json.load(file)

        except Exception as error:
            print(f"Ошибка загрузки операций: {error}")


def get_number(text):
    """Безопасный ввод числа."""
    while True:
        try:
            number = float(input(text).replace(",", "."))

            if number < 0:
                print("Число не может быть отрицательным.")
                continue

            return number

        except ValueError:
            print("Ошибка! Введите число.")


def get_positive_number(text):
    """Ввод положительного числа."""
    while True:
        number = get_number(text)

        if number <= 0:
            print("Сумма должна быть больше нуля.")
        else:
            return number


def add_operation(
    operation_type,
    amount=0,
    method="",
    order_number="",
    description=""
):
    """Добавляет операцию в историю."""
    operation = {
        "id": len(operations) + 1,
        "type": operation_type,
        "amount": round(amount, 2),
        "method": method,
        "order_number": order_number,
        "description": description,
        "time": get_time()
    }

    operations.append(operation)
    save_data()


# ==========================================================
# РАБОТА СО СМЕНОЙ
# ==========================================================

def open_shift():
    """Открытие кассовой смены."""
    print_line()
    print("ОТКРЫТИЕ КАССОВОЙ СМЕНЫ")
    print_line()

    if cash_register["shift_open"]:
        print("Смена уже открыта.")
        print(f"Кассир: {cash_register['cashier']}")
        print(f"Время открытия: {cash_register['shift_start']}")
        return

    cashier = input("Введите имя кассира: ").strip()

    if not cashier:
        cashier = "Главный кассир"

    opening_cash = get_number("Введите сумму в кассе в начале смены: ")

    cash_register["shift_open"] = True
    cash_register["cashier"] = cashier
    cash_register["shift_start"] = get_time()
    cash_register["shift_end"] = ""
    cash_register["opening_cash"] = opening_cash
    cash_register["cash"] = opening_cash
    cash_register["card"] = 0.0
    cash_register["total"] = 0.0
    cash_register["orders"] = 0
    cash_register["refunds"] = 0.0

    add_operation(
        operation_type="Открытие смены",
        amount=opening_cash,
        description=f"Кассир: {cashier}"
    )

    save_data()

    print("\nСмена успешно открыта!")
    print(f"Кассир: {cashier}")
    print(f"Начальная сумма: {money(opening_cash)}")


def close_shift():
    """Закрытие кассовой смены."""
    print_line()
    print("ЗАКРЫТИЕ КАССОВОЙ СМЕНЫ")
    print_line()

    if not cash_register["shift_open"]:
        print("Смена ещё не открыта.")
        return

    print(f"Кассир: {cash_register['cashier']}")
    print(f"Открытие смены: {cash_register['shift_start']}")
    print(f"Наличные: {money(cash_register['cash'])}")
    print(f"Карта: {money(cash_register['card'])}")
    print(f"Продажи: {money(cash_register['total'])}")
    print(f"Количество заказов: {cash_register['orders']}")
    print(f"Возвраты: {money(cash_register['refunds'])}")

    print_line()

    confirm = input("Вы точно хотите закрыть смену? (да/нет): ").lower()

    if confirm != "да":
        print("Закрытие смены отменено.")
        return

    cash_register["shift_open"] = False
    cash_register["shift_end"] = get_time()

    add_operation(
        operation_type="Закрытие смены",
        amount=cash_register["total"],
        description=f"Кассир: {cash_register['cashier']}"
    )

    save_data()

    print("\nСмена успешно закрыта!")
    print(f"Время закрытия: {cash_register['shift_end']}")


# ==========================================================
# ПРОВЕРКА КАССЫ
# ==========================================================

def check_shift():
    """Проверяет, открыта ли смена."""
    if not cash_register["shift_open"]:
        print("\nСначала необходимо открыть кассовую смену!")
        return False

    return True


def show_cash_status():
    """Показывает состояние кассы."""
    print_line()
    print("СОСТОЯНИЕ КАССЫ")
    print_line()

    status = "ОТКРЫТА" if cash_register["shift_open"] else "ЗАКРЫТА"

    print(f"Статус смены: {status}")
    print(f"Кассир: {cash_register['cashier'] or 'Не указан'}")
    print(f"Начало смены: {cash_register['shift_start'] or 'Нет данных'}")
    print(f"Конец смены: {cash_register['shift_end'] or 'Нет данных'}")
    print()
    print(f"Наличные: {money(cash_register['cash'])}")
    print(f"Банковская карта: {money(cash_register['card'])}")
    print(f"Всего продаж: {money(cash_register['total'])}")
    print(f"Возвраты: {money(cash_register['refunds'])}")
    print(f"Количество заказов: {cash_register['orders']}")

    expected_cash = (
        cash_register["opening_cash"]
        + cash_register["cash"]
        - cash_register["opening_cash"]
    )

    print(f"Ожидаемые наличные: {money(expected_cash)}")


# ==========================================================
# ОПЛАТА ЗАКАЗА
# ==========================================================

def choose_payment_method():
    """Выбор способа оплаты."""
    print_line()
    print("СПОСОБ ОПЛАТЫ")
    print_line()

    print("1. Наличные")
    print("2. Банковская карта")
    print("3. Перевод")

    while True:
        choice = input("Выберите способ оплаты: ")

        if choice == "1":
            return "Наличные"

        if choice == "2":
            return "Банковская карта"

        if choice == "3":
            return "Перевод"

        print("Неверный выбор.")


def payment():
    """Ручная оплата заказа."""
    print_line()
    print("ОПЛАТА ЗАКАЗА")
    print_line()

    if not check_shift():
        return

    order_number = input("Введите номер заказа: ").strip()

    if not order_number:
        print("Номер заказа не может быть пустым.")
        return

    amount = get_positive_number("Введите сумму заказа: ")
    method = choose_payment_method()

    received = amount

    if method == "Наличные":
        received = get_positive_number(
            "Сколько денег получил кассир: "
        )

        if received < amount:
            print("Недостаточно денег.")
            return

        change = received - amount
        print(f"Сдача: {money(change)}")
    else:
        print("Оплата картой или переводом подтверждена.")

    if method == "Наличные":
        cash_register["cash"] += amount

    elif method == "Банковская карта":
        cash_register["card"] += amount

    elif method == "Перевод":
        cash_register["card"] += amount

    cash_register["total"] += amount
    cash_register["orders"] += 1

    add_operation(
        operation_type="Оплата заказа",
        amount=amount,
        method=method,
        order_number=order_number,
        description="Заказ успешно оплачен"
    )

    save_data()

    print_line()
    print("ОПЛАТА УСПЕШНА")
    print_line()
    print(f"Номер заказа: {order_number}")
    print(f"Сумма: {money(amount)}")
    print(f"Способ оплаты: {method}")


def register_payment(order_number, amount, method):
    """
    Функция для подключения к ресторану.

    Её можно вызвать из restaurant.py,
    чтобы заказ автоматически попадал в кассу.
    """

    if not cash_register["shift_open"]:
        return False, "Кассовая смена закрыта."

    if amount <= 0:
        return False, "Сумма должна быть больше нуля."

    allowed_methods = [
        "Наличные",
        "Банковская карта",
        "Перевод"
    ]

    if method not in allowed_methods:
        return False, "Неизвестный способ оплаты."

    if method == "Наличные":
        cash_register["cash"] += amount
    else:
        cash_register["card"] += amount

    cash_register["total"] += amount
    cash_register["orders"] += 1

    add_operation(
        operation_type="Автоматическая оплата",
        amount=amount,
        method=method,
        order_number=order_number,
        description="Оплата из программы ресторана"
    )

    save_data()

    return True, "Оплата успешно зарегистрирована."


# ==========================================================
# ВОЗВРАТ ДЕНЕГ
# ==========================================================

def refund():
    """Возврат денег клиенту."""
    print_line()
    print("ВОЗВРАТ ДЕНЕГ")
    print_line()

    if not check_shift():
        return

    order_number = input("Введите номер заказа для возврата: ").strip()
    amount = get_positive_number("Введите сумму возврата: ")

    if amount > cash_register["total"]:
        print("Нельзя вернуть больше суммы продаж.")
        return

    print("Выберите способ возврата:")
    print("1. Наличные")
    print("2. Банковская карта")

    choice = input("Ваш выбор: ")

    if choice == "1":
        if amount > cash_register["cash"]:
            print("В кассе недостаточно наличных.")
            return

        cash_register["cash"] -= amount
        method = "Наличные"

    elif choice == "2":
        if amount > cash_register["card"]:
            print("Недостаточно средств по безналичной оплате.")
            return

        cash_register["card"] -= amount
        method = "Банковская карта"

    else:
        print("Неверный выбор.")
        return

    cash_register["total"] -= amount
    cash_register["refunds"] += amount

    add_operation(
        operation_type="Возврат",
        amount=amount,
        method=method,
        order_number=order_number,
        description="Деньги возвращены клиенту"
    )

    save_data()

    print("\nВозврат успешно выполнен.")
    print(f"Номер заказа: {order_number}")
    print(f"Возвращено: {money(amount)}")


# ==========================================================
# ДОПОЛНИТЕЛЬНЫЕ ОПЕРАЦИИ
# ==========================================================

def add_cash():
    """Внесение дополнительных наличных."""
    print_line()
    print("ВНЕСЕНИЕ НАЛИЧНЫХ")
    print_line()

    if not check_shift():
        return

    amount = get_positive_number("Введите сумму внесения: ")
    reason = input("Причина внесения: ").strip()

    cash_register["cash"] += amount

    add_operation(
        operation_type="Внесение наличных",
        amount=amount,
        method="Наличные",
        description=reason
    )

    save_data()

    print(f"Внесено в кассу: {money(amount)}")


def remove_cash():
    """Изъятие наличных."""
    print_line()
    print("ИЗЪЯТИЕ НАЛИЧНЫХ")
    print_line()

    if not check_shift():
        return

    amount = get_positive_number("Введите сумму изъятия: ")

    if amount > cash_register["cash"]:
        print("В кассе недостаточно наличных.")
        return

    reason = input("Причина изъятия: ").strip()

    cash_register["cash"] -= amount

    add_operation(
        operation_type="Изъятие наличных",
        amount=amount,
        method="Наличные",
        description=reason
    )

    save_data()

    print(f"Изъято из кассы: {money(amount)}")


def print_receipt():
    """Печать чека в консоль."""
    print_line()
    print("ПЕЧАТЬ ЧЕКА")
    print_line()

    if not operations:
        print("Операций пока нет.")
        return

    last_operation = operations[-1]

    print("                 РЕСТОРАН")
    print("              КАССОВЫЙ ЧЕК")
    print_line()
    print(f"Номер операции: {last_operation['id']}")
    print(f"Тип операции: {last_operation['type']}")
    print(f"Номер заказа: {last_operation['order_number']}")
    print(f"Сумма: {money(last_operation['amount'])}")
    print(f"Способ оплаты: {last_operation['method']}")
    print(f"Дата: {last_operation['time']}")
    print(f"Описание: {last_operation['description']}")
    print_line()
    print("       Спасибо за посещение!")


# ==========================================================
# ИСТОРИЯ ОПЕРАЦИЙ
# ==========================================================

def show_operations():
    """Показывает все операции."""
    print_line()
    print("ИСТОРИЯ ОПЕРАЦИЙ")
    print_line()

    if not operations:
        print("История пока пустая.")
        return

    for operation in operations:
        print(f"\nID операции: {operation['id']}")
        print(f"Тип: {operation['type']}")
        print(f"Сумма: {money(operation['amount'])}")
        print(f"Метод: {operation['method'] or 'Не указан'}")
        print(f"Заказ: {operation['order_number'] or 'Не указан'}")
        print(f"Время: {operation['time']}")
        print(f"Описание: {operation['description']}")
        print_line()


def search_order():
    """Поиск операций по номеру заказа."""
    print_line()
    print("ПОИСК ЗАКАЗА")
    print_line()

    order_number = input("Введите номер заказа: ").strip()

    found = False

    for operation in operations:
        if operation["order_number"] == order_number:
            found = True

            print(f"\nID: {operation['id']}")
            print(f"Тип: {operation['type']}")
            print(f"Сумма: {money(operation['amount'])}")
            print(f"Способ оплаты: {operation['method']}")
            print(f"Дата: {operation['time']}")
            print(f"Описание: {operation['description']}")

    if not found:
        print("Заказ не найден.")


def show_daily_report():
    """Показывает отчёт за текущий день."""
    print_line()
    print("ОТЧЁТ ЗА СЕГОДНЯ")
    print_line()

    today = datetime.now().strftime("%d.%m.%Y")

    daily_total = 0
    daily_refunds = 0
    daily_orders = 0

    for operation in operations:
        if operation["time"].startswith(today):
            if operation["type"] in [
                "Оплата заказа",
                "Автоматическая оплата"
            ]:
                daily_total += operation["amount"]
                daily_orders += 1

            elif operation["type"] == "Возврат":
                daily_refunds += operation["amount"]

    print(f"Дата: {today}")
    print(f"Количество заказов: {daily_orders}")
    print(f"Продажи: {money(daily_total)}")
    print(f"Возвраты: {money(daily_refunds)}")
    print(f"Итог: {money(daily_total - daily_refunds)}")


def clear_history():
    """Удаление истории операций."""
    print_line()
    print("ОЧИСТКА ИСТОРИИ")
    print_line()

    print("Внимание! Все операции будут удалены.")

    confirm = input("Введите УДАЛИТЬ для подтверждения: ")

    if confirm == "УДАЛИТЬ":
        operations.clear()
        save_data()
        print("История операций очищена.")
    else:
        print("Очистка отменена.")


# ==========================================================
# МЕНЮ КАССИРА
# ==========================================================

def cashier_menu():
    while True:
        print("\n")
        print("=" * 60)
        print("                 КАССА РЕСТОРАНА")
        print("=" * 60)

        print("1. Открыть смену")
        print("2. Закрыть смену")
        print("3. Оплатить заказ")
        print("4. Вернуть деньги")
        print("5. Состояние кассы")
        print("6. Внести наличные")
        print("7. Изъять наличные")
        print("8. История операций")
        print("9. Поиск заказа")
        print("10. Отчёт за сегодня")
        print("11. Напечатать последний чек")
        print("12. Очистить историю")
        print("0. Выход")

        print_line()

        choice = input("Выберите действие: ")

        if choice == "1":
            open_shift()
            pause()

        elif choice == "2":
            close_shift()
            pause()

        elif choice == "3":
            payment()
            pause()

        elif choice == "4":
            refund()
            pause()

        elif choice == "5":
            show_cash_status()
            pause()

        elif choice == "6":
            add_cash()
            pause()

        elif choice == "7":
            remove_cash()
            pause()

        elif choice == "8":
            show_operations()
            pause()

        elif choice == "9":
            search_order()
            pause()

        elif choice == "10":
            show_daily_report()
            pause()

        elif choice == "11":
            print_receipt()
            pause()

        elif choice == "12":
            clear_history()
            pause()

        elif choice == "0":
            print("Выход из кассы.")
            break

        else:
            print("Неверный выбор. Попробуйте ещё раз.")


# ==========================================================
# ЗАПУСК ПРОГРАММЫ
# ==========================================================

def main():
    load_data()

    print("=" * 60)
    print("Добро пожаловать в кассовую программу ресторана!")
    print("=" * 60)

    cashier_menu()


if __name__ == "__main__":
    main()

from datetime import datetime
import json
import os


# ==========================================================
# НАСТРОЙКИ
# ==========================================================

CASH_FILE = "cash_register_data.json"
OPERATIONS_FILE = "cash_operations.json"


# ==========================================================
# ДАННЫЕ КАССЫ
# ==========================================================

cash_register = {
    "cash": 0.0,
    "card": 0.0,
    "total": 0.0,
    "orders": 0,
    "refunds": 0.0,
    "shift_open": False,
    "cashier": "",
    "shift_start": "",
    "shift_end": "",
    "opening_cash": 0.0
}

operations = []


# ==========================================================
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ==========================================================

def get_time():
    """Возвращает текущую дату и время."""
    return datetime.now().strftime("%d.%m.%Y %H:%M:%S")


def print_line():
    print("-" * 60)


def pause():
    input("\nНажмите Enter, чтобы продолжить...")


def money(value):
    """Красивый вывод суммы."""
    return f"{value:.2f} сом"


def save_data():
    """Сохраняет данные кассы в файл."""
    try:
        with open(CASH_FILE, "w", encoding="utf-8") as file:
            json.dump(cash_register, file, ensure_ascii=False, indent=4)

        with open(OPERATIONS_FILE, "w", encoding="utf-8") as file:
            json.dump(operations, file, ensure_ascii=False, indent=4)

    except Exception as error:
        print(f"Ошибка сохранения данных: {error}")


def load_data():
    """Загружает данные кассы из файлов."""
    global cash_register
    global operations

    if os.path.exists(CASH_FILE):
        try:
            with open(CASH_FILE, "r", encoding="utf-8") as file:
                saved_cash = json.load(file)

                for key in cash_register:
                    if key in saved_cash:
                        cash_register[key] = saved_cash[key]

        except Exception as error:
            print(f"Ошибка загрузки кассы: {error}")

    if os.path.exists(OPERATIONS_FILE):
        try:
            with open(OPERATIONS_FILE, "r", encoding="utf-8") as file:
                operations = json.load(file)

        except Exception as error:
            print(f"Ошибка загрузки операций: {error}")


def get_number(text):
    """Безопасный ввод числа."""
    while True:
        try:
            number = float(input(text).replace(",", "."))

            if number < 0:
                print("Число не может быть отрицательным.")
                continue

            return number

        except ValueError:
            print("Ошибка! Введите число.")


def get_positive_number(text):
    """Ввод положительного числа."""
    while True:
        number = get_number(text)

        if number <= 0:
            print("Сумма должна быть больше нуля.")
        else:
            return number


def add_operation(
    operation_type,
    amount=0,
    method="",
    order_number="",
    description=""
):
    """Добавляет операцию в историю."""
    operation = {
        "id": len(operations) + 1,
        "type": operation_type,
        "amount": round(amount, 2),
        "method": method,
        "order_number": order_number,
        "description": description,
        "time": get_time()
    }

    operations.append(operation)
    save_data()


# ==========================================================
# РАБОТА СО СМЕНОЙ
# ==========================================================

def open_shift():
    """Открытие кассовой смены."""
    print_line()
    print("ОТКРЫТИЕ КАССОВОЙ СМЕНЫ")
    print_line()

    if cash_register["shift_open"]:
        print("Смена уже открыта.")
        print(f"Кассир: {cash_register['cashier']}")
        print(f"Время открытия: {cash_register['shift_start']}")
        return

    cashier = input("Введите имя кассира: ").strip()

    if not cashier:
        cashier = "Главный кассир"

    opening_cash = get_number("Введите сумму в кассе в начале смены: ")

    cash_register["shift_open"] = True
    cash_register["cashier"] = cashier
    cash_register["shift_start"] = get_time()
    cash_register["shift_end"] = ""
    cash_register["opening_cash"] = opening_cash
    cash_register["cash"] = opening_cash
    cash_register["card"] = 0.0
    cash_register["total"] = 0.0
    cash_register["orders"] = 0
    cash_register["refunds"] = 0.0

    add_operation(
        operation_type="Открытие смены",
        amount=opening_cash,
        description=f"Кассир: {cashier}"
    )

    save_data()

    print("\nСмена успешно открыта!")
    print(f"Кассир: {cashier}")
    print(f"Начальная сумма: {money(opening_cash)}")


def close_shift():
    """Закрытие кассовой смены."""
    print_line()
    print("ЗАКРЫТИЕ КАССОВОЙ СМЕНЫ")
    print_line()

    if not cash_register["shift_open"]:
        print("Смена ещё не открыта.")
        return

    print(f"Кассир: {cash_register['cashier']}")
    print(f"Открытие смены: {cash_register['shift_start']}")
    print(f"Наличные: {money(cash_register['cash'])}")
    print(f"Карта: {money(cash_register['card'])}")
    print(f"Продажи: {money(cash_register['total'])}")
    print(f"Количество заказов: {cash_register['orders']}")
    print(f"Возвраты: {money(cash_register['refunds'])}")

    print_line()

    confirm = input("Вы точно хотите закрыть смену? (да/нет): ").lower()

    if confirm != "да":
        print("Закрытие смены отменено.")
        return

    cash_register["shift_open"] = False
    cash_register["shift_end"] = get_time()

    add_operation(
        operation_type="Закрытие смены",
        amount=cash_register["total"],
        description=f"Кассир: {cash_register['cashier']}"
    )

    save_data()

    print("\nСмена успешно закрыта!")
    print(f"Время закрытия: {cash_register['shift_end']}")


# ==========================================================
# ПРОВЕРКА КАССЫ
# ==========================================================

def check_shift():
    """Проверяет, открыта ли смена."""
    if not cash_register["shift_open"]:
        print("\nСначала необходимо открыть кассовую смену!")
        return False

    return True


def show_cash_status():
    """Показывает состояние кассы."""
    print_line()
    print("СОСТОЯНИЕ КАССЫ")
    print_line()

    status = "ОТКРЫТА" if cash_register["shift_open"] else "ЗАКРЫТА"

    print(f"Статус смены: {status}")
    print(f"Кассир: {cash_register['cashier'] or 'Не указан'}")
    print(f"Начало смены: {cash_register['shift_start'] or 'Нет данных'}")
    print(f"Конец смены: {cash_register['shift_end'] or 'Нет данных'}")
    print()
    print(f"Наличные: {money(cash_register['cash'])}")
    print(f"Банковская карта: {money(cash_register['card'])}")
    print(f"Всего продаж: {money(cash_register['total'])}")
    print(f"Возвраты: {money(cash_register['refunds'])}")
    print(f"Количество заказов: {cash_register['orders']}")

    expected_cash = (
        cash_register["opening_cash"]
        + cash_register["cash"]
        - cash_register["opening_cash"]
    )

    print(f"Ожидаемые наличные: {money(expected_cash)}")


# ==========================================================
# ОПЛАТА ЗАКАЗА
# ==========================================================

def choose_payment_method():
    """Выбор способа оплаты."""
    print_line()
    print("СПОСОБ ОПЛАТЫ")
    print_line()

    print("1. Наличные")
    print("2. Банковская карта")
    print("3. Перевод")

    while True:
        choice = input("Выберите способ оплаты: ")

        if choice == "1":
            return "Наличные"

        if choice == "2":
            return "Банковская карта"

        if choice == "3":
            return "Перевод"

        print("Неверный выбор.")


def payment():
    """Ручная оплата заказа."""
    print_line()
    print("ОПЛАТА ЗАКАЗА")
    print_line()

    if not check_shift():
        return

    order_number = input("Введите номер заказа: ").strip()

    if not order_number:
        print("Номер заказа не может быть пустым.")
        return

    amount = get_positive_number("Введите сумму заказа: ")
    method = choose_payment_method()

    received = amount

    if method == "Наличные":
        received = get_positive_number(
            "Сколько денег получил кассир: "
        )

        if received < amount:
            print("Недостаточно денег.")
            return

        change = received - amount
        print(f"Сдача: {money(change)}")
    else:
        print("Оплата картой или переводом подтверждена.")

    if method == "Наличные":
        cash_register["cash"] += amount

    elif method == "Банковская карта":
        cash_register["card"] += amount

    elif method == "Перевод":
        cash_register["card"] += amount

    cash_register["total"] += amount
    cash_register["orders"] += 1

    add_operation(
        operation_type="Оплата заказа",
        amount=amount,
        method=method,
        order_number=order_number,
        description="Заказ успешно оплачен"
    )

    save_data()

    print_line()
    print("ОПЛАТА УСПЕШНА")
    print_line()
    print(f"Номер заказа: {order_number}")
    print(f"Сумма: {money(amount)}")
    print(f"Способ оплаты: {method}")


def register_payment(order_number, amount, method):
    """
    Функция для подключения к ресторану.

    Её можно вызвать из restaurant.py,
    чтобы заказ автоматически попадал в кассу.
    """

    if not cash_register["shift_open"]:
        return False, "Кассовая смена закрыта."

    if amount <= 0:
        return False, "Сумма должна быть больше нуля."

    allowed_methods = [
        "Наличные",
        "Банковская карта",
        "Перевод"
    ]

    if method not in allowed_methods:
        return False, "Неизвестный способ оплаты."

    if method == "Наличные":
        cash_register["cash"] += amount
    else:
        cash_register["card"] += amount

    cash_register["total"] += amount
    cash_register["orders"] += 1

    add_operation(
        operation_type="Автоматическая оплата",
        amount=amount,
        method=method,
        order_number=order_number,
        description="Оплата из программы ресторана"
    )

    save_data()

    return True, "Оплата успешно зарегистрирована."


# ==========================================================
# ВОЗВРАТ ДЕНЕГ
# ==========================================================

def refund():
    """Возврат денег клиенту."""
    print_line()
    print("ВОЗВРАТ ДЕНЕГ")
    print_line()

    if not check_shift():
        return

    order_number = input("Введите номер заказа для возврата: ").strip()
    amount = get_positive_number("Введите сумму возврата: ")

    if amount > cash_register["total"]:
        print("Нельзя вернуть больше суммы продаж.")
        return

    print("Выберите способ возврата:")
    print("1. Наличные")
    print("2. Банковская карта")

    choice = input("Ваш выбор: ")

    if choice == "1":
        if amount > cash_register["cash"]:
            print("В кассе недостаточно наличных.")
            return

        cash_register["cash"] -= amount
        method = "Наличные"

    elif choice == "2":
        if amount > cash_register["card"]:
            print("Недостаточно средств по безналичной оплате.")
            return

        cash_register["card"] -= amount
        method = "Банковская карта"

    else:
        print("Неверный выбор.")
        return

    cash_register["total"] -= amount
    cash_register["refunds"] += amount

    add_operation(
        operation_type="Возврат",
        amount=amount,
        method=method,
        order_number=order_number,
        description="Деньги возвращены клиенту"
    )

    save_data()

    print("\nВозврат успешно выполнен.")
    print(f"Номер заказа: {order_number}")
    print(f"Возвращено: {money(amount)}")


# ==========================================================
# ДОПОЛНИТЕЛЬНЫЕ ОПЕРАЦИИ
# ==========================================================

def add_cash():
    """Внесение дополнительных наличных."""
    print_line()
    print("ВНЕСЕНИЕ НАЛИЧНЫХ")
    print_line()

    if not check_shift():
        return

    amount = get_positive_number("Введите сумму внесения: ")
    reason = input("Причина внесения: ").strip()

    cash_register["cash"] += amount

    add_operation(
        operation_type="Внесение наличных",
        amount=amount,
        method="Наличные",
        description=reason
    )

    save_data()

    print(f"Внесено в кассу: {money(amount)}")


def remove_cash():
    """Изъятие наличных."""
    print_line()
    print("ИЗЪЯТИЕ НАЛИЧНЫХ")
    print_line()

    if not check_shift():
        return

    amount = get_positive_number("Введите сумму изъятия: ")

    if amount > cash_register["cash"]:
        print("В кассе недостаточно наличных.")
        return

    reason = input("Причина изъятия: ").strip()

    cash_register["cash"] -= amount

    add_operation(
        operation_type="Изъятие наличных",
        amount=amount,
        method="Наличные",
        description=reason
    )

    save_data()

    print(f"Изъято из кассы: {money(amount)}")


def print_receipt():
    """Печать чека в консоль."""
    print_line()
    print("ПЕЧАТЬ ЧЕКА")
    print_line()

    if not operations:
        print("Операций пока нет.")
        return

    last_operation = operations[-1]

    print("                 РЕСТОРАН")
    print("              КАССОВЫЙ ЧЕК")
    print_line()
    print(f"Номер операции: {last_operation['id']}")
    print(f"Тип операции: {last_operation['type']}")
    print(f"Номер заказа: {last_operation['order_number']}")
    print(f"Сумма: {money(last_operation['amount'])}")
    print(f"Способ оплаты: {last_operation['method']}")
    print(f"Дата: {last_operation['time']}")
    print(f"Описание: {last_operation['description']}")
    print_line()
    print("       Спасибо за посещение!")


# ==========================================================
# ИСТОРИЯ ОПЕРАЦИЙ
# ==========================================================

def show_operations():
    """Показывает все операции."""
    print_line()
    print("ИСТОРИЯ ОПЕРАЦИЙ")
    print_line()

    if not operations:
        print("История пока пустая.")
        return

    for operation in operations:
        print(f"\nID операции: {operation['id']}")
        print(f"Тип: {operation['type']}")
        print(f"Сумма: {money(operation['amount'])}")
        print(f"Метод: {operation['method'] or 'Не указан'}")
        print(f"Заказ: {operation['order_number'] or 'Не указан'}")
        print(f"Время: {operation['time']}")
        print(f"Описание: {operation['description']}")
        print_line()


def search_order():
    """Поиск операций по номеру заказа."""
    print_line()
    print("ПОИСК ЗАКАЗА")
    print_line()

    order_number = input("Введите номер заказа: ").strip()

    found = False

    for operation in operations:
        if operation["order_number"] == order_number:
            found = True

            print(f"\nID: {operation['id']}")
            print(f"Тип: {operation['type']}")
            print(f"Сумма: {money(operation['amount'])}")
            print(f"Способ оплаты: {operation['method']}")
            print(f"Дата: {operation['time']}")
            print(f"Описание: {operation['description']}")

    if not found:
        print("Заказ не найден.")


def show_daily_report():
    """Показывает отчёт за текущий день."""
    print_line()
    print("ОТЧЁТ ЗА СЕГОДНЯ")
    print_line()

    today = datetime.now().strftime("%d.%m.%Y")

    daily_total = 0
    daily_refunds = 0
    daily_orders = 0

    for operation in operations:
        if operation["time"].startswith(today):
            if operation["type"] in [
                "Оплата заказа",
                "Автоматическая оплата"
            ]:
                daily_total += operation["amount"]
                daily_orders += 1

            elif operation["type"] == "Возврат":
                daily_refunds += operation["amount"]

    print(f"Дата: {today}")
    print(f"Количество заказов: {daily_orders}")
    print(f"Продажи: {money(daily_total)}")
    print(f"Возвраты: {money(daily_refunds)}")
    print(f"Итог: {money(daily_total - daily_refunds)}")


def clear_history():
    """Удаление истории операций."""
    print_line()
    print("ОЧИСТКА ИСТОРИИ")
    print_line()

    print("Внимание! Все операции будут удалены.")

    confirm = input("Введите УДАЛИТЬ для подтверждения: ")

    if confirm == "УДАЛИТЬ":
        operations.clear()
        save_data()
        print("История операций очищена.")
    else:
        print("Очистка отменена.")


# ==========================================================
# МЕНЮ КАССИРА
# ==========================================================

def cashier_menu():
    while True:
        print("\n")
        print("=" * 60)
        print("                 КАССА РЕСТОРАНА")
        print("=" * 60)

        print("1. Открыть смену")
        print("2. Закрыть смену")
        print("3. Оплатить заказ")
        print("4. Вернуть деньги")
        print("5. Состояние кассы")
        print("6. Внести наличные")
        print("7. Изъять наличные")
        print("8. История операций")
        print("9. Поиск заказа")
        print("10. Отчёт за сегодня")
        print("11. Напечатать последний чек")
        print("12. Очистить историю")
        print("0. Выход")

        print_line()

        choice = input("Выберите действие: ")

        if choice == "1":
            open_shift()
            pause()

        elif choice == "2":
            close_shift()
            pause()

        elif choice == "3":
            payment()
            pause()

        elif choice == "4":
            refund()
            pause()

        elif choice == "5":
            show_cash_status()
            pause()

        elif choice == "6":
            add_cash()
            pause()

        elif choice == "7":
            remove_cash()
            pause()

        elif choice == "8":
            show_operations()
            pause()

        elif choice == "9":
            search_order()
            pause()

        elif choice == "10":
            show_daily_report()
            pause()

        elif choice == "11":
            print_receipt()
            pause()

        elif choice == "12":
            clear_history()
            pause()

        elif choice == "0":
            print("Выход из кассы.")
            break

        else:
            print("Неверный выбор. Попробуйте ещё раз.")


# ==========================================================
# ЗАПУСК ПРОГРАММЫ
# ==========================================================

def main():
    load_data()

    print("=" * 60)
    print("Добро пожаловать в кассовую программу ресторана!")
    print("=" * 60)

    cashier_menu()


if __name__ == "__main__":
    main()


from datetime import datetime
import json
import os


# ==========================================================
# НАСТРОЙКИ
# ==========================================================

CASH_FILE = "cash_register_data.json"
OPERATIONS_FILE = "cash_operations.json"


# ==========================================================
# ДАННЫЕ КАССЫ
# ==========================================================

cash_register = {
    "cash": 0.0,
    "card": 0.0,
    "total": 0.0,
    "orders": 0,
    "refunds": 0.0,
    "shift_open": False,
    "cashier": "",
    "shift_start": "",
    "shift_end": "",
    "opening_cash": 0.0
}

operations = []


# ==========================================================
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ==========================================================

def get_time():
    """Возвращает текущую дату и время."""
    return datetime.now().strftime("%d.%m.%Y %H:%M:%S")


def print_line():
    print("-" * 60)


def pause():
    input("\nНажмите Enter, чтобы продолжить...")


def money(value):
    """Красивый вывод суммы."""
    return f"{value:.2f} сом"


def save_data():
    """Сохраняет данные кассы в файл."""
    try:
        with open(CASH_FILE, "w", encoding="utf-8") as file:
            json.dump(cash_register, file, ensure_ascii=False, indent=4)

        with open(OPERATIONS_FILE, "w", encoding="utf-8") as file:
            json.dump(operations, file, ensure_ascii=False, indent=4)

    except Exception as error:
        print(f"Ошибка сохранения данных: {error}")


def load_data():
    """Загружает данные кассы из файлов."""
    global cash_register
    global operations

    if os.path.exists(CASH_FILE):
        try:
            with open(CASH_FILE, "r", encoding="utf-8") as file:
                saved_cash = json.load(file)

                for key in cash_register:
                    if key in saved_cash:
                        cash_register[key] = saved_cash[key]

        except Exception as error:
            print(f"Ошибка загрузки кассы: {error}")

    if os.path.exists(OPERATIONS_FILE):
        try:
            with open(OPERATIONS_FILE, "r", encoding="utf-8") as file:
                operations = json.load(file)

        except Exception as error:
            print(f"Ошибка загрузки операций: {error}")


def get_number(text):
    """Безопасный ввод числа."""
    while True:
        try:
            number = float(input(text).replace(",", "."))

            if number < 0:
                print("Число не может быть отрицательным.")
                continue

            return number

        except ValueError:
            print("Ошибка! Введите число.")


def get_positive_number(text):
    """Ввод положительного числа."""
    while True:
        number = get_number(text)

        if number <= 0:
            print("Сумма должна быть больше нуля.")
        else:
            return number


def add_operation(
    operation_type,
    amount=0,
    method="",
    order_number="",
    description=""
):
    """Добавляет операцию в историю."""
    operation = {
        "id": len(operations) + 1,
        "type": operation_type,
        "amount": round(amount, 2),
        "method": method,
        "order_number": order_number,
        "description": description,
        "time": get_time()
    }

    operations.append(operation)
    save_data()


# ==========================================================
# РАБОТА СО СМЕНОЙ
# ==========================================================

def open_shift():
    """Открытие кассовой смены."""
    print_line()
    print("ОТКРЫТИЕ КАССОВОЙ СМЕНЫ")
    print_line()

    if cash_register["shift_open"]:
        print("Смена уже открыта.")
        print(f"Кассир: {cash_register['cashier']}")
        print(f"Время открытия: {cash_register['shift_start']}")
        return

    cashier = input("Введите имя кассира: ").strip()

    if not cashier:
        cashier = "Главный кассир"

    opening_cash = get_number("Введите сумму в кассе в начале смены: ")

    cash_register["shift_open"] = True
    cash_register["cashier"] = cashier
    cash_register["shift_start"] = get_time()
    cash_register["shift_end"] = ""
    cash_register["opening_cash"] = opening_cash
    cash_register["cash"] = opening_cash
    cash_register["card"] = 0.0
    cash_register["total"] = 0.0
    cash_register["orders"] = 0
    cash_register["refunds"] = 0.0

    add_operation(
        operation_type="Открытие смены",
        amount=opening_cash,
        description=f"Кассир: {cashier}"
    )

    save_data()

    print("\nСмена успешно открыта!")
    print(f"Кассир: {cashier}")
    print(f"Начальная сумма: {money(opening_cash)}")


def close_shift():
    """Закрытие кассовой смены."""
    print_line()
    print("ЗАКРЫТИЕ КАССОВОЙ СМЕНЫ")
    print_line()

    if not cash_register["shift_open"]:
        print("Смена ещё не открыта.")
        return

    print(f"Кассир: {cash_register['cashier']}")
    print(f"Открытие смены: {cash_register['shift_start']}")
    print(f"Наличные: {money(cash_register['cash'])}")
    print(f"Карта: {money(cash_register['card'])}")
    print(f"Продажи: {money(cash_register['total'])}")
    print(f"Количество заказов: {cash_register['orders']}")
    print(f"Возвраты: {money(cash_register['refunds'])}")

    print_line()

    confirm = input("Вы точно хотите закрыть смену? (да/нет): ").lower()

    if confirm != "да":
        print("Закрытие смены отменено.")
        return

    cash_register["shift_open"] = False
    cash_register["shift_end"] = get_time()

    add_operation(
        operation_type="Закрытие смены",
        amount=cash_register["total"],
        description=f"Кассир: {cash_register['cashier']}"
    )

    save_data()

    print("\nСмена успешно закрыта!")
    print(f"Время закрытия: {cash_register['shift_end']}")


# ==========================================================
# ПРОВЕРКА КАССЫ
# ==========================================================

def check_shift():
    """Проверяет, открыта ли смена."""
    if not cash_register["shift_open"]:
        print("\nСначала необходимо открыть кассовую смену!")
        return False

    return True


def show_cash_status():
    """Показывает состояние кассы."""
    print_line()
    print("СОСТОЯНИЕ КАССЫ")
    print_line()

    status = "ОТКРЫТА" if cash_register["shift_open"] else "ЗАКРЫТА"

    print(f"Статус смены: {status}")
    print(f"Кассир: {cash_register['cashier'] or 'Не указан'}")
    print(f"Начало смены: {cash_register['shift_start'] or 'Нет данных'}")
    print(f"Конец смены: {cash_register['shift_end'] or 'Нет данных'}")
    print()
    print(f"Наличные: {money(cash_register['cash'])}")
    print(f"Банковская карта: {money(cash_register['card'])}")
    print(f"Всего продаж: {money(cash_register['total'])}")
    print(f"Возвраты: {money(cash_register['refunds'])}")
    print(f"Количество заказов: {cash_register['orders']}")

    expected_cash = (
        cash_register["opening_cash"]
        + cash_register["cash"]
        - cash_register["opening_cash"]
    )

    print(f"Ожидаемые наличные: {money(expected_cash)}")


# ==========================================================
# ОПЛАТА ЗАКАЗА
# ==========================================================

def choose_payment_method():
    """Выбор способа оплаты."""
    print_line()
    print("СПОСОБ ОПЛАТЫ")
    print_line()

    print("1. Наличные")
    print("2. Банковская карта")
    print("3. Перевод")

    while True:
        choice = input("Выберите способ оплаты: ")

        if choice == "1":
            return "Наличные"

        if choice == "2":
            return "Банковская карта"

        if choice == "3":
            return "Перевод"

        print("Неверный выбор.")


def payment():
    """Ручная оплата заказа."""
    print_line()
    print("ОПЛАТА ЗАКАЗА")
    print_line()

    if not check_shift():
        return

    order_number = input("Введите номер заказа: ").strip()

    if not order_number:
        print("Номер заказа не может быть пустым.")
        return

    amount = get_positive_number("Введите сумму заказа: ")
    method = choose_payment_method()

    received = amount

    if method == "Наличные":
        received = get_positive_number(
            "Сколько денег получил кассир: "
        )

        if received < amount:
            print("Недостаточно денег.")
            return

        change = received - amount
        print(f"Сдача: {money(change)}")
    else:
        print("Оплата картой или переводом подтверждена.")

    if method == "Наличные":
        cash_register["cash"] += amount

    elif method == "Банковская карта":
        cash_register["card"] += amount

    elif method == "Перевод":
        cash_register["card"] += amount

    cash_register["total"] += amount
    cash_register["orders"] += 1

    add_operation(
        operation_type="Оплата заказа",
        amount=amount,
        method=method,
        order_number=order_number,
        description="Заказ успешно оплачен"
    )

    save_data()

    print_line()
    print("ОПЛАТА УСПЕШНА")
    print_line()
    print(f"Номер заказа: {order_number}")
    print(f"Сумма: {money(amount)}")
    print(f"Способ оплаты: {method}")


def register_payment(order_number, amount, method):
    """
    Функция для подключения к ресторану.

    Её можно вызвать из restaurant.py,
    чтобы заказ автоматически попадал в кассу.
    """

    if not cash_register["shift_open"]:
        return False, "Кассовая смена закрыта."

    if amount <= 0:
        return False, "Сумма должна быть больше нуля."

    allowed_methods = [
        "Наличные",
        "Банковская карта",
        "Перевод"
    ]

    if method not in allowed_methods:
        return False, "Неизвестный способ оплаты."

    if method == "Наличные":
        cash_register["cash"] += amount
    else:
        cash_register["card"] += amount

    cash_register["total"] += amount
    cash_register["orders"] += 1

    add_operation(
        operation_type="Автоматическая оплата",
        amount=amount,
        method=method,
        order_number=order_number,
        description="Оплата из программы ресторана"
    )

    save_data()

    return True, "Оплата успешно зарегистрирована."


# ==========================================================
# ВОЗВРАТ ДЕНЕГ
# ==========================================================

def refund():
    """Возврат денег клиенту."""
    print_line()
    print("ВОЗВРАТ ДЕНЕГ")
    print_line()

    if not check_shift():
        return

    order_number = input("Введите номер заказа для возврата: ").strip()
    amount = get_positive_number("Введите сумму возврата: ")

    if amount > cash_register["total"]:
        print("Нельзя вернуть больше суммы продаж.")
        return

    print("Выберите способ возврата:")
    print("1. Наличные")
    print("2. Банковская карта")

    choice = input("Ваш выбор: ")

    if choice == "1":
        if amount > cash_register["cash"]:
            print("В кассе недостаточно наличных.")
            return

        cash_register["cash"] -= amount
        method = "Наличные"

    elif choice == "2":
        if amount > cash_register["card"]:
            print("Недостаточно средств по безналичной оплате.")
            return

        cash_register["card"] -= amount
        method = "Банковская карта"

    else:
        print("Неверный выбор.")
        return

    cash_register["total"] -= amount
    cash_register["refunds"] += amount

    add_operation(
        operation_type="Возврат",
        amount=amount,
        method=method,
        order_number=order_number,
        description="Деньги возвращены клиенту"
    )

    save_data()

    print("\nВозврат успешно выполнен.")
    print(f"Номер заказа: {order_number}")
    print(f"Возвращено: {money(amount)}")


# ==========================================================
# ДОПОЛНИТЕЛЬНЫЕ ОПЕРАЦИИ
# ==========================================================

def add_cash():
    """Внесение дополнительных наличных."""
    print_line()
    print("ВНЕСЕНИЕ НАЛИЧНЫХ")
    print_line()

    if not check_shift():
        return

    amount = get_positive_number("Введите сумму внесения: ")
    reason = input("Причина внесения: ").strip()

    cash_register["cash"] += amount

    add_operation(
        operation_type="Внесение наличных",
        amount=amount,
        method="Наличные",
        description=reason
    )

    save_data()

    print(f"Внесено в кассу: {money(amount)}")


def remove_cash():
    """Изъятие наличных."""
    print_line()
    print("ИЗЪЯТИЕ НАЛИЧНЫХ")
    print_line()

    if not check_shift():
        return

    amount = get_positive_number("Введите сумму изъятия: ")

    if amount > cash_register["cash"]:
        print("В кассе недостаточно наличных.")
        return

    reason = input("Причина изъятия: ").strip()

    cash_register["cash"] -= amount

    add_operation(
        operation_type="Изъятие наличных",
        amount=amount,
        method="Наличные",
        description=reason
    )

    save_data()

    print(f"Изъято из кассы: {money(amount)}")


def print_receipt():
    """Печать чека в консоль."""
    print_line()
    print("ПЕЧАТЬ ЧЕКА")
    print_line()

    if not operations:
        print("Операций пока нет.")
        return

    last_operation = operations[-1]

    print("                 РЕСТОРАН")
    print("              КАССОВЫЙ ЧЕК")
    print_line()
    print(f"Номер операции: {last_operation['id']}")
    print(f"Тип операции: {last_operation['type']}")
    print(f"Номер заказа: {last_operation['order_number']}")
    print(f"Сумма: {money(last_operation['amount'])}")
    print(f"Способ оплаты: {last_operation['method']}")
    print(f"Дата: {last_operation['time']}")
    print(f"Описание: {last_operation['description']}")
    print_line()
    print("       Спасибо за посещение!")


# ==========================================================
# ИСТОРИЯ ОПЕРАЦИЙ
# ==========================================================

def show_operations():
    """Показывает все операции."""
    print_line()
    print("ИСТОРИЯ ОПЕРАЦИЙ")
    print_line()

    if not operations:
        print("История пока пустая.")
        return

    for operation in operations:
        print(f"\nID операции: {operation['id']}")
        print(f"Тип: {operation['type']}")
        print(f"Сумма: {money(operation['amount'])}")
        print(f"Метод: {operation['method'] or 'Не указан'}")
        print(f"Заказ: {operation['order_number'] or 'Не указан'}")
        print(f"Время: {operation['time']}")
        print(f"Описание: {operation['description']}")
        print_line()


def search_order():
    """Поиск операций по номеру заказа."""
    print_line()
    print("ПОИСК ЗАКАЗА")
    print_line()

    order_number = input("Введите номер заказа: ").strip()

    found = False

    for operation in operations:
        if operation["order_number"] == order_number:
            found = True

            print(f"\nID: {operation['id']}")
            print(f"Тип: {operation['type']}")
            print(f"Сумма: {money(operation['amount'])}")
            print(f"Способ оплаты: {operation['method']}")
            print(f"Дата: {operation['time']}")
            print(f"Описание: {operation['description']}")

    if not found:
        print("Заказ не найден.")


def show_daily_report():
    """Показывает отчёт за текущий день."""
    print_line()
    print("ОТЧЁТ ЗА СЕГОДНЯ")
    print_line()

    today = datetime.now().strftime("%d.%m.%Y")

    daily_total = 0
    daily_refunds = 0
    daily_orders = 0

    for operation in operations:
        if operation["time"].startswith(today):
            if operation["type"] in [
                "Оплата заказа",
                "Автоматическая оплата"
            ]:
                daily_total += operation["amount"]
                daily_orders += 1

            elif operation["type"] == "Возврат":
                daily_refunds += operation["amount"]

    print(f"Дата: {today}")
    print(f"Количество заказов: {daily_orders}")
    print(f"Продажи: {money(daily_total)}")
    print(f"Возвраты: {money(daily_refunds)}")
    print(f"Итог: {money(daily_total - daily_refunds)}")


def clear_history():
    """Удаление истории операций."""
    print_line()
    print("ОЧИСТКА ИСТОРИИ")
    print_line()

    print("Внимание! Все операции будут удалены.")

    confirm = input("Введите УДАЛИТЬ для подтверждения: ")

    if confirm == "УДАЛИТЬ":
        operations.clear()
        save_data()
        print("История операций очищена.")
    else:
        print("Очистка отменена.")


# ==========================================================
# МЕНЮ КАССИРА
# ==========================================================

def cashier_menu():
    while True:
        print("\n")
        print("=" * 60)
        print("                 КАССА РЕСТОРАНА")
        print("=" * 60)

        print("1. Открыть смену")
        print("2. Закрыть смену")
        print("3. Оплатить заказ")
        print("4. Вернуть деньги")
        print("5. Состояние кассы")
        print("6. Внести наличные")
        print("7. Изъять наличные")
        print("8. История операций")
        print("9. Поиск заказа")
        print("10. Отчёт за сегодня")
        print("11. Напечатать последний чек")
        print("12. Очистить историю")
        print("0. Выход")

        print_line()

        choice = input("Выберите действие: ")

        if choice == "1":
            open_shift()
            pause()

        elif choice == "2":
            close_shift()
            pause()

        elif choice == "3":
            payment()
            pause()

        elif choice == "4":
            refund()
            pause()

        elif choice == "5":
            show_cash_status()
            pause()

        elif choice == "6":
            add_cash()
            pause()

        elif choice == "7":
            remove_cash()
            pause()

        elif choice == "8":
            show_operations()
            pause()

        elif choice == "9":
            search_order()
            pause()

        elif choice == "10":
            show_daily_report()
            pause()

        elif choice == "11":
            print_receipt()
            pause()

        elif choice == "12":
            clear_history()
            pause()

        elif choice == "0":
            print("Выход из кассы.")
            break

        else:
            print("Неверный выбор. Попробуйте ещё раз.")


# ==========================================================
# ЗАПУСК ПРОГРАММЫ
# ==========================================================

def main():
    load_data()

    print("=" * 60)
    print("Добро пожаловать в кассовую программу ресторана!")
    print("=" * 60)

    cashier_menu()


if __name__ == "__main__":
    main()


