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


from datetime import datetime
import random


# ============================================================
#                  ✈️ AIRLINE SYSTEM ✈️
#              СИСТЕМА АВИАБИЛЕТОВ
# ============================================================


print("=" * 70)
print("              ✈️ WELCOME TO AIRLINE ✈️")
print("                 АВИАБИЛЕТЫ ONLINE")
print("=" * 70)


# ============================================================
#                     ДАННЫЕ СИСТЕМЫ
# ============================================================

airline_name = "AIRLINE INTERNATIONAL"

company_country = "Kyrgyzstan"

currency = "KGS"

system_version = "1.0.0"

current_year = 2026


# ============================================================
#                  СПИСОК АВИАКОМПАНИЙ
# ============================================================

airlines = [
    "AIRLINE INTERNATIONAL",
    "SKY AIR",
    "GLOBAL AIRWAYS",
    "FLY WORLD",
    "ASIA AIRLINES"
]


# ============================================================
#                  СПИСОК САМОЛЁТОВ
# ============================================================

planes = [
    "Boeing 737",
    "Boeing 777",
    "Airbus A320",
    "Airbus A350",
    "Boeing 787 Dreamliner"
]


# ============================================================
#                  ГОРОДА И НАПРАВЛЕНИЯ
# ============================================================

cities = [
    "Бишкек",
    "Ош",
    "Алматы",
    "Астана",
    "Дубай",
    "Стамбул",
    "Москва",
    "Лондон",
    "Париж",
    "Пекин",
    "Токио",
    "Сеул",
    "Нью-Йорк",
    "Доха",
    "Абу-Даби"
]


# ============================================================
#                  ЦЕНЫ НА БИЛЕТЫ
# ============================================================

ticket_prices = {
    "Бишкек-Дубай": 25000,
    "Бишкек-Стамбул": 30000,
    "Бишкек-Москва": 20000,
    "Бишкек-Алматы": 10000,
    "Бишкек-Астана": 15000,
    "Бишкек-Лондон": 60000,
    "Бишкек-Париж": 55000,
    "Бишкек-Пекин": 35000,
    "Бишкек-Токио": 50000,
    "Бишкек-Сеул": 45000,
    "Бишкек-Нью-Йорк": 90000,
    "Бишкек-Доха": 28000,
    "Бишкек-Абу-Даби": 27000
}


# ============================================================
#                  ВРЕМЯ ПОЛЁТА
# ============================================================

flight_times = {
    "Бишкек-Дубай": "4 часа 30 минут",
    "Бишкек-Стамбул": "5 часов 40 минут",
    "Бишкек-Москва": "4 часа 20 минут",
    "Бишкек-Алматы": "1 час",
    "Бишкек-Астана": "2 часа",
    "Бишкек-Лондон": "9 часов",
    "Бишкек-Париж": "8 часов 30 минут",
    "Бишкек-Пекин": "5 часов",
    "Бишкек-Токио": "7 часов",
    "Бишкек-Сеул": "6 часов 30 минут",
    "Бишкек-Нью-Йорк": "14 часов",
    "Бишкек-Доха": "4 часа 40 минут",
    "Бишкек-Абу-Даби": "4 часа 20 минут"
}


# ============================================================
#                  ВРЕМЯ ВЫЛЕТА
# ============================================================

departure_times = [
    "06:00",
    "08:30",
    "10:00",
    "12:45",
    "14:30",
    "16:00",
    "18:20",
    "21:00",
    "23:30"
]


# ============================================================
#                  ВРЕМЯ ПРИЛЁТА
# ============================================================

arrival_times = [
    "10:30",
    "13:00",
    "14:30",
    "17:15",
    "19:00",
    "20:30",
    "22:50",
    "01:30",
    "04:00"
]


# ============================================================
#                  КЛАССЫ БИЛЕТОВ
# ============================================================

ticket_classes = {
    "1": {
        "name": "Эконом",
        "price": 0,
        "baggage": "20 кг",
        "food": "Питание включено",
        "wifi": "Нет",
        "priority": "Нет"
    },

    "2": {
        "name": "Комфорт",
        "price": 10000,
        "baggage": "30 кг",
        "food": "Питание включено",
        "wifi": "Да",
        "priority": "Да"
    },

    "3": {
        "name": "Бизнес",
        "price": 30000,
        "baggage": "40 кг",
        "food": "Питание премиум",
        "wifi": "Да",
        "priority": "Да"
    }
}


# ============================================================
#                  БАГАЖ
# ============================================================

baggage_options = {
    "1": {
        "name": "Только ручная кладь",
        "price": 0,
        "weight": "7 кг"
    },

    "2": {
        "name": "Ручная кладь + багаж",
        "price": 5000,
        "weight": "23 кг"
    },

    "3": {
        "name": "Большой багаж",
        "price": 10000,
        "weight": "32 кг"
    }
}


# ============================================================
#                  ДОПОЛНИТЕЛЬНЫЕ УСЛУГИ
# ============================================================

extra_services = {
    "1": {
        "name": "Выбор места у окна",
        "price": 1500
    },

    "2": {
        "name": "Выбор места у прохода",
        "price": 1000
    },

    "3": {
        "name": "Дополнительное питание",
        "price": 2000
    },

    "4": {
        "name": "Доступ в VIP-зал",
        "price": 5000
    },

    "5": {
        "name": "Без дополнительных услуг",
        "price": 0
    }
}


# ============================================================
#                  ПЕРЕМЕННЫЕ ПОЛЬЗОВАТЕЛЯ
# ============================================================

users = []

current_user = None

bookings = []

selected_flight = None


# ============================================================
#                  ФУНКЦИЯ РЕГИСТРАЦИИ
# ============================================================

def register():

    print("\n" + "=" * 70)

    print("                  📝 РЕГИСТРАЦИЯ")

    print("=" * 70)

    name = input("Введите имя: ")

    surname = input("Введите фамилию: ")

    email = input("Введите email: ")

    phone = input("Введите номер телефона: ")

    password = input("Придумайте пароль: ")

    if name == "" or surname == "":

        print("❌ Имя и фамилия обязательны!")

        return

    for user in users:

        if user["email"] == email:

            print("❌ Такой email уже зарегистрирован!")

            return

    new_user = {

        "name": name,

        "surname": surname,

        "email": email,

        "phone": phone,

        "password": password,

        "bonus": 0,

        "bookings": []

    }

    users.append(new_user)

    print("\n✅ Регистрация успешно завершена!")

    print(f"Добро пожаловать, {name}!")


# ============================================================
#                  ФУНКЦИЯ ВХОДА
# ============================================================

def login():

    global current_user

    print("\n" + "=" * 70)

    print("                      🔐 ВХОД")

    print("=" * 70)

    email = input("Введите email: ")

    password = input("Введите пароль: ")

    for user in users:

        if user["email"] == email and user["password"] == password:

            current_user = user

            print("\n✅ Вы успешно вошли!")

            print(f"Здравствуйте, {user['name']}!")

            return True

    print("\n❌ Неверный email или пароль!")

    return False


# ============================================================
#                  ПОКАЗ ГОРОДОВ
# ============================================================

def show_cities():

    print("\n" + "=" * 70)

    print("                    🌍 ГОРОДА")

    print("=" * 70)

    for index, city in enumerate(cities, start=1):

        print(f"{index}. {city}")


# ============================================================
#                  ВЫБОР ГОРОДА
# ============================================================

def choose_city(message):

    show_cities()

    while True:

        choice = input(f"\n{message}: ")

        if choice.isdigit():

            number = int(choice)

            if 1 <= number <= len(cities):

                return cities[number - 1]

        print("❌ Выберите правильный номер города!")


# ============================================================
#                  ПОИСК РЕЙСА
# ============================================================

def search_flights():

    print("\n" + "=" * 70)

    print("                    🔎 ПОИСК РЕЙСА")

    print("=" * 70)

    from_city = choose_city("Откуда вы летите")

    to_city = choose_city("Куда вы летите")

    if from_city == to_city:

        print("❌ Города вылета и прилёта не должны совпадать!")

        return

    flight_date = input("Введите дату полёта: ")

    route = from_city + "-" + to_city

    reverse_route = to_city + "-" + from_city

    if route in ticket_prices:

        price = ticket_prices[route]

        duration = flight_times[route]

    elif reverse_route in ticket_prices:

        price = ticket_prices[reverse_route]

        duration = flight_times[reverse_route]

    else:

        price = random.randint(15000, 100000)

        duration = "От 2 до 12 часов"

    airline = random.choice(airlines)

    plane = random.choice(planes)

    departure = random.choice(departure_times)

    arrival = random.choice(arrival_times)

    flight_number = "FL" + str(random.randint(100, 999))

    flight = {

        "from": from_city,

        "to": to_city,

        "date": flight_date,

        "departure": departure,

        "arrival": arrival,

        "duration": duration,

        "price": price,

        "airline": airline,

        "plane": plane,

        "flight_number": flight_number

    }

    print("\n" + "=" * 70)

    print("                  ✈️ НАЙДЕННЫЙ РЕЙС")

    print("=" * 70)

    print(f"🛫 Откуда: {from_city}")

    print(f"🛬 Куда: {to_city}")

    print(f"📅 Дата: {flight_date}")

    print(f"⏰ Вылет: {departure}")

    print(f"🕒 Прилёт: {arrival}")

    print(f"⏱️ Время полёта: {duration}")

    print(f"✈️ Авиакомпания: {airline}")

    print(f"🛩️ Самолёт: {plane}")

    print(f"🎫 Номер рейса: {flight_number}")

    print(f"💰 Цена: {price} сом")

    print("=" * 70)

    choice = input("\nЗабронировать этот рейс? (да/нет): ")

    if choice.lower() == "да":

        book_flight(flight)


# ============================================================
#                  ВЫБОР КЛАССА
# ============================================================

def choose_class():

    print("\n" + "=" * 70)

    print("                  💺 КЛАСС БИЛЕТА")

    print("=" * 70)

    for key, value in ticket_classes.items():

        print(f"\n{key}. {value['name']}")

        print(f"   Доплата: {value['price']} сом")

        print(f"   Багаж: {value['baggage']}")

        print(f"   Питание: {value['food']}")

        print(f"   Wi-Fi: {value['wifi']}")

        print(f"   Приоритет: {value['priority']}")

    while True:

        choice = input("\nВыберите класс: ")

        if choice in ticket_classes:

            return ticket_classes[choice]

        print("❌ Неверный выбор!")


# ============================================================
#                  ВЫБОР БАГАЖА
# ============================================================

def choose_baggage():

    print("\n" + "=" * 70)

    print("                    🧳 БАГАЖ")

    print("=" * 70)

    for key, value in baggage_options.items():

        print(
            f"{key}. {value['name']} — "
            f"{value['weight']} — "
            f"{value['price']} сом"
        )

    while True:

        choice = input("\nВыберите багаж: ")

        if choice in baggage_options:

            return baggage_options[choice]

        print("❌ Неверный выбор!")


# ============================================================
#                  ВЫБОР МЕСТА
# ============================================================

def choose_seat():

    print("\n" + "=" * 70)

    print("                  🪑 ВЫБОР МЕСТА")

    print("=" * 70)

    print("Доступные места:")

    print("1A  1B  1C  1D  1E  1F")

    print("2A  2B  2C  2D  2E  2F")

    print("3A  3B  3C  3D  3E  3F")

    print("4A  4B  4C  4D  4E  4F")

    print("5A  5B  5C  5D  5E  5F")

    print("6A  6B  6C  6D  6E  6F")

    print("7A  7B  7C  7D  7E  7F")

    print("8A  8B  8C  8D  8E  8F")

    print("9A  9B  9C  9D  9E  9F")

    print("10A 10B 10C 10D 10E 10F")

    seat = input("\nВведите место: ")

    if seat == "":

        seat = "12A"

    return seat.upper()


# ============================================================
#                  ДОПОЛНИТЕЛЬНЫЕ УСЛУГИ
# ============================================================

def choose_services():

    selected = []

    total = 0

    print("\n" + "=" * 70)

    print("                🛎️ ДОПОЛНИТЕЛЬНЫЕ УСЛУГИ")

    print("=" * 70)

    for key, value in extra_services.items():

        print(f"{key}. {value['name']} — {value['price']} сом")

    while True:

        choice = input(
            "\nВыберите услугу "
            "(5 — без услуг, 0 — закончить): "
        )

        if choice == "0":

            break

        if choice in extra_services:

            service = extra_services[choice]

            if service["name"] == "Без дополнительных услуг":

                break

            selected.append(service["name"])

            total += service["price"]

            print(f"✅ Добавлено: {service['name']}")

        else:

            print("❌ Неверный выбор!")

    return selected, total


# ============================================================
#                  СКИДКА
# ============================================================

def calculate_discount(price):

    print("\n" + "=" * 70)

    print("                    🎁 СКИДКА")

    print("=" * 70)

    print("1. Нет скидки")

    print("2. Студент — 5%")

    print("3. Постоянный клиент — 10%")

    print("4. Специальная акция — 15%")

    choice = input("Выберите скидку: ")

    if choice == "2":

        return price * 0.05

    elif choice == "3":

        return price * 0.10

    elif choice == "4":

        return price * 0.15

    else:

        return 0


# ============================================================
#                  БРОНИРОВАНИЕ
# ============================================================

def book_flight(flight):

    global selected_flight

    if current_user is None:

        print("❌ Сначала войдите в аккаунт!")

        return

    print("\n" + "=" * 70)

    print("                 🎫 БРОНИРОВАНИЕ")

    print("=" * 70)

    print(f"Пассажир: {current_user['name']}")

    print(f"Маршрут: {flight['from']} → {flight['to']}")

    print(f"Дата: {flight['date']}")

    ticket_class = choose_class()

    baggage = choose_baggage()

    seat = choose_seat()

    services, services_price = choose_services()

    base_price = flight["price"]

    class_price = ticket_class["price"]

    baggage_price = baggage["price"]

    subtotal = base_price + class_price + baggage_price + services_price

    discount = calculate_discount(subtotal)

    total_price = subtotal - discount

    ticket_number = random.randint(100000, 999999)

    booking = {

        "ticket_number": ticket_number,

        "passenger": current_user["name"] + " " + current_user["surname"],

        "from": flight["from"],

        "to": flight["to"],

        "date": flight["date"],

        "departure": flight["departure"],

        "arrival": flight["arrival"],

        "duration": flight["duration"],

        "airline": flight["airline"],

        "plane": flight["plane"],

        "flight_number": flight["flight_number"],

        "ticket_class": ticket_class["name"],

        "baggage": baggage["name"],

        "baggage_weight": baggage["weight"],

        "seat": seat,

        "services": services,

        "base_price": base_price,

        "class_price": class_price,

        "baggage_price": baggage_price,

        "services_price": services_price,

        "subtotal": subtotal,

        "discount": discount,

        "total_price": total_price,

        "status": "Забронирован",

        "created": datetime.now().strftime("%d.%m.%Y %H:%M")

    }

    bookings.append(booking)

    current_user["bookings"].append(booking)

    print("\n✅ БРОНИРОВАНИЕ УСПЕШНО СОЗДАНО!")

    print(f"🎫 Номер билета: {ticket_number}")

    print(f"💰 Итоговая цена: {total_price:.2f} сом")

    save_ticket_to_file(booking)


# ============================================================
#                  СОХРАНЕНИЕ БИЛЕТА
# ============================================================

def save_ticket_to_file(booking):

    filename = f"ticket_{booking['ticket_number']}.txt"

    with open(filename, "w", encoding="utf-8") as file:

        file.write("=" * 60 + "\n")

        file.write("             ✈️ AIRLINE TICKET\n")

        file.write("=" * 60 + "\n\n")

        file.write(f"Пассажир: {booking['passenger']}\n")

        file.write(f"Номер билета: {booking['ticket_number']}\n")

        file.write(f"Номер рейса: {booking['flight_number']}\n\n")

        file.write(f"Откуда: {booking['from']}\n")

        file.write(f"Куда: {booking['to']}\n")

        file.write(f"Дата: {booking['date']}\n")

        file.write(f"Вылет: {booking['departure']}\n")

        file.write(f"Прилёт: {booking['arrival']}\n")

        file.write(f"Время полёта: {booking['duration']}\n\n")

        file.write(f"Авиакомпания: {booking['airline']}\n")

        file.write(f"Самолёт: {booking['plane']}\n")

        file.write(f"Класс: {booking['ticket_class']}\n")

        file.write(f"Место: {booking['seat']}\n")

        file.write(f"Багаж: {booking['baggage']}\n")

        file.write(f"Вес багажа: {booking['baggage_weight']}\n\n")

        file.write(f"Цена билета: {booking['base_price']} сом\n")

        file.write(f"Класс: {booking['class_price']} сом\n")

        file.write(f"Багаж: {booking['baggage_price']} сом\n")

        file.write(f"Услуги: {booking['services_price']} сом\n")

        file.write(f"Скидка: {booking['discount']:.2f} сом\n")

        file.write(f"ИТОГО: {booking['total_price']:.2f} сом\n\n")

        file.write(f"Статус: {booking['status']}\n")

        file.write(f"Создано: {booking['created']}\n")

        file.write("=" * 60 + "\n")

    print(f"📄 Билет сохранён в файл: {filename}")


# ============================================================
#                  ПОКАЗАТЬ БИЛЕТ
# ============================================================

def show_ticket(booking):

    print("\n" + "=" * 70)

    print("                     🎫 БИЛЕТ")

    print("=" * 70)

    print(f"👤 Пассажир: {booking['passenger']}")

    print(f"🎫 Номер билета: {booking['ticket_number']}")

    print(f"✈️ Номер рейса: {booking['flight_number']}")

    print("-" * 70)

    print(f"🛫 Откуда: {booking['from']}")

    print(f"🛬 Куда: {booking['to']}")

    print(f"📅 Дата: {booking['date']}")

    print(f"⏰ Вылет: {booking['departure']}")

    print(f"🕒 Прилёт: {booking['arrival']}")

    print(f"⏱️ Время полёта: {booking['duration']}")

    print("-" * 70)

    print(f"✈️ Авиакомпания: {booking['airline']}")

    print(f"🛩️ Самолёт: {booking['plane']}")

    print(f"💺 Класс: {booking['ticket_class']}")

    print(f"🪑 Место: {booking['seat']}")

    print(f"🧳 Багаж: {booking['baggage']}")

    print(f"⚖️ Вес: {booking['baggage_weight']}")

    print("-" * 70)

    print(f"💰 Цена билета: {booking['base_price']} сом")

    print(f"💺 Класс: {booking['class_price']} сом")

    print(f"🧳 Багаж: {booking['baggage_price']} сом")

    print(f"🛎️ Услуги: {booking['services_price']} сом")

    print(f"🎁 Скидка: {booking['discount']:.2f} сом")

    print(f"💵 ИТОГО: {booking['total_price']:.2f} сом")

    print("-" * 70)

    print(f"📌 Статус: {booking['status']}")

    print(f"🕒 Создано: {booking['created']}")

    print("=" * 70)


# ============================================================
#                  ИСТОРИЯ БИЛЕТОВ
# ============================================================

def booking_history():

    if current_user is None:

        print("❌ Сначала войдите в аккаунт!")

        return

    print("\n" + "=" * 70)

    print("                  📚 МОИ БИЛЕТЫ")

    print("=" * 70)

    if len(current_user["bookings"]) == 0:

        print("У вас пока нет бронирований.")

        return

    for index, booking in enumerate(current_user["bookings"], start=1):

        print(f"\nБилет №{index}")

        print(f"🎫 Номер: {booking['ticket_number']}")

        print(f"🛫 Маршрут: {booking['from']} → {booking['to']}")

        print(f"📅 Дата: {booking['date']}")

        print(f"💰 Цена: {booking['total_price']:.2f} сом")

        print(f"📌 Статус: {booking['status']}")

        print("-" * 50)


# ============================================================
#                  ПРОСМОТР КОНКРЕТНОГО БИЛЕТА
# ============================================================

def view_ticket():

    if current_user is None:

        print("❌ Сначала войдите в аккаунт!")

        return

    if len(current_user["bookings"]) == 0:

        print("❌ У вас нет билетов!")

        return

    number = input("Введите номер билета: ")

    for booking in current_user["bookings"]:

        if str(booking["ticket_number"]) == number:

            show_ticket(booking)

            return

    print("❌ Билет не найден!")


# ============================================================
#                  ОТМЕНА БИЛЕТА
# ============================================================

def cancel_booking():

    if current_user is None:

        print("❌ Сначала войдите в аккаунт!")

        return

    number = input("Введите номер билета для отмены: ")

    for booking in current_user["bookings"]:

        if str(booking["ticket_number"]) == number:

            if booking["status"] == "Отменён":

                print("❌ Билет уже отменён!")

                return

            booking["status"] = "Отменён"

            print("✅ Бронирование отменено!")

            return

    print("❌ Билет не найден!")


# ============================================================
#                  ПРОФИЛЬ ПОЛЬЗОВАТЕЛЯ
# ============================================================

def profile():

    if current_user is None:

        print("❌ Сначала войдите в аккаунт!")

        return

    print("\n" + "=" * 70)

    print("                    👤 ПРОФИЛЬ")

    print("=" * 70)

    print(f"Имя: {current_user['name']}")

    print(f"Фамилия: {current_user['surname']}")

    print(f"Email: {current_user['email']}")

    print(f"Телефон: {current_user['phone']}")

    print(f"Бонусы: {current_user['bonus']}")

    print(f"Количество билетов: {len(current_user['bookings'])}")


# ============================================================
#                  СПРАВКА
# ============================================================

def help_menu():

    print("\n" + "=" * 70)

    print("                    ℹ️ СПРАВКА")

    print("=" * 70)

    print("1. Зарегистрируйтесь.")

    print("2. Войдите в аккаунт.")

    print("3. Найдите рейс.")

    print("4. Выберите класс.")

    print("5. Выберите багаж.")

    print("6. Выберите место.")

    print("7. Подтвердите бронирование.")

    print("8. Получите номер билета.")

    print("9. Билет сохранится в TXT-файл.")

    print("\nДля выхода выберите 0.")


# ============================================================
#                  ГЛАВНОЕ МЕНЮ
# ============================================================

def main_menu():

    while True:

        print("\n" + "=" * 70)

        print("                 ✈️ AIRLINE ONLINE")

        print("=" * 70)

        if current_user:

            print(
                f"👤 Пользователь: "
                f"{current_user['name']} "
                f"{current_user['surname']}"
            )

        else:

            print("👤 Пользователь: Гость")

        print("-" * 70)

        print("1. 📝 Регистрация")

        print("2. 🔐 Вход")

        print("3. 🔎 Поиск рейса")

        print("4. 📚 Мои билеты")

        print("5. 🎫 Просмотреть билет")

        print("6. ❌ Отменить билет")

        print("7. 👤 Мой профиль")

        print("8. ℹ️ Помощь")

        print("0. 🚪 Выход")

        print("=" * 70)

        choice = input("Выберите действие: ")

        if choice == "1":

            register()

        elif choice == "2":

            login()

        elif choice == "3":

            search_flights()

        elif choice == "4":

            booking_history()

        elif choice == "5":

            view_ticket()

        elif choice == "6":

            cancel_booking()

        elif choice == "7":

            profile()

        elif choice == "8":

            help_menu()

        elif choice == "0":

            print("\nСпасибо за использование AIRLINE ✈️")

            print("До свидания!")

            break

        else:

            print("❌ Неверный выбор!")


# ============================================================
#                  ЗАПУСК ПРОГРАММЫ
# ============================================================

if __name__ == "__main__":

    main_menu()


from datetime import datetime
import random


# ============================================================
#                  ✈️ AIRLINE SYSTEM ✈️
#              СИСТЕМА АВИАБИЛЕТОВ
# ============================================================


print("=" * 70)
print("              ✈️ WELCOME TO AIRLINE ✈️")
print("                 АВИАБИЛЕТЫ ONLINE")
print("=" * 70)


# ============================================================
#                     ДАННЫЕ СИСТЕМЫ
# ============================================================

airline_name = "AIRLINE INTERNATIONAL"

company_country = "Kyrgyzstan"

currency = "KGS"

system_version = "1.0.0"

current_year = 2026


# ============================================================
#                  СПИСОК АВИАКОМПАНИЙ
# ============================================================

airlines = [
    "AIRLINE INTERNATIONAL",
    "SKY AIR",
    "GLOBAL AIRWAYS",
    "FLY WORLD",
    "ASIA AIRLINES"
]


# ============================================================
#                  СПИСОК САМОЛЁТОВ
# ============================================================

planes = [
    "Boeing 737",
    "Boeing 777",
    "Airbus A320",
    "Airbus A350",
    "Boeing 787 Dreamliner"
]


# ============================================================
#                  ГОРОДА И НАПРАВЛЕНИЯ
# ============================================================

cities = [
    "Бишкек",
    "Ош",
    "Алматы",
    "Астана",
    "Дубай",
    "Стамбул",
    "Москва",
    "Лондон",
    "Париж",
    "Пекин",
    "Токио",
    "Сеул",
    "Нью-Йорк",
    "Доха",
    "Абу-Даби"
]


# ============================================================
#                  ЦЕНЫ НА БИЛЕТЫ
# ============================================================

ticket_prices = {
    "Бишкек-Дубай": 25000,
    "Бишкек-Стамбул": 30000,
    "Бишкек-Москва": 20000,
    "Бишкек-Алматы": 10000,
    "Бишкек-Астана": 15000,
    "Бишкек-Лондон": 60000,
    "Бишкек-Париж": 55000,
    "Бишкек-Пекин": 35000,
    "Бишкек-Токио": 50000,
    "Бишкек-Сеул": 45000,
    "Бишкек-Нью-Йорк": 90000,
    "Бишкек-Доха": 28000,
    "Бишкек-Абу-Даби": 27000
}


# ============================================================
#                  ВРЕМЯ ПОЛЁТА
# ============================================================

flight_times = {
    "Бишкек-Дубай": "4 часа 30 минут",
    "Бишкек-Стамбул": "5 часов 40 минут",
    "Бишкек-Москва": "4 часа 20 минут",
    "Бишкек-Алматы": "1 час",
    "Бишкек-Астана": "2 часа",
    "Бишкек-Лондон": "9 часов",
    "Бишкек-Париж": "8 часов 30 минут",
    "Бишкек-Пекин": "5 часов",
    "Бишкек-Токио": "7 часов",
    "Бишкек-Сеул": "6 часов 30 минут",
    "Бишкек-Нью-Йорк": "14 часов",
    "Бишкек-Доха": "4 часа 40 минут",
    "Бишкек-Абу-Даби": "4 часа 20 минут"
}


# ============================================================
#                  ВРЕМЯ ВЫЛЕТА
# ============================================================

departure_times = [
    "06:00",
    "08:30",
    "10:00",
    "12:45",
    "14:30",
    "16:00",
    "18:20",
    "21:00",
    "23:30"
]


# ============================================================
#                  ВРЕМЯ ПРИЛЁТА
# ============================================================

arrival_times = [
    "10:30",
    "13:00",
    "14:30",
    "17:15",
    "19:00",
    "20:30",
    "22:50",
    "01:30",
    "04:00"
]


# ============================================================
#                  КЛАССЫ БИЛЕТОВ
# ============================================================

ticket_classes = {
    "1": {
        "name": "Эконом",
        "price": 0,
        "baggage": "20 кг",
        "food": "Питание включено",
        "wifi": "Нет",
        "priority": "Нет"
    },

    "2": {
        "name": "Комфорт",
        "price": 10000,
        "baggage": "30 кг",
        "food": "Питание включено",
        "wifi": "Да",
        "priority": "Да"
    },

    "3": {
        "name": "Бизнес",
        "price": 30000,
        "baggage": "40 кг",
        "food": "Питание премиум",
        "wifi": "Да",
        "priority": "Да"
    }
}


# ============================================================
#                  БАГАЖ
# ============================================================

baggage_options = {
    "1": {
        "name": "Только ручная кладь",
        "price": 0,
        "weight": "7 кг"
    },

    "2": {
        "name": "Ручная кладь + багаж",
        "price": 5000,
        "weight": "23 кг"
    },

    "3": {
        "name": "Большой багаж",
        "price": 10000,
        "weight": "32 кг"
    }
}


# ============================================================
#                  ДОПОЛНИТЕЛЬНЫЕ УСЛУГИ
# ============================================================

extra_services = {
    "1": {
        "name": "Выбор места у окна",
        "price": 1500
    },

    "2": {
        "name": "Выбор места у прохода",
        "price": 1000
    },

    "3": {
        "name": "Дополнительное питание",
        "price": 2000
    },

    "4": {
        "name": "Доступ в VIP-зал",
        "price": 5000
    },

    "5": {
        "name": "Без дополнительных услуг",
        "price": 0
    }
}


# ============================================================
#                  ПЕРЕМЕННЫЕ ПОЛЬЗОВАТЕЛЯ
# ============================================================

users = []

current_user = None

bookings = []

selected_flight = None


# ============================================================
#                  ФУНКЦИЯ РЕГИСТРАЦИИ
# ============================================================

def register():

    print("\n" + "=" * 70)

    print("                  📝 РЕГИСТРАЦИЯ")

    print("=" * 70)

    name = input("Введите имя: ")

    surname = input("Введите фамилию: ")

    email = input("Введите email: ")

    phone = input("Введите номер телефона: ")

    password = input("Придумайте пароль: ")

    if name == "" or surname == "":

        print("❌ Имя и фамилия обязательны!")

        return

    for user in users:

        if user["email"] == email:

            print("❌ Такой email уже зарегистрирован!")

            return

    new_user = {

        "name": name,

        "surname": surname,

        "email": email,

        "phone": phone,

        "password": password,

        "bonus": 0,

        "bookings": []

    }

    users.append(new_user)

    print("\n✅ Регистрация успешно завершена!")

    print(f"Добро пожаловать, {name}!")


# ============================================================
#                  ФУНКЦИЯ ВХОДА
# ============================================================

def login():

    global current_user

    print("\n" + "=" * 70)

    print("                      🔐 ВХОД")

    print("=" * 70)

    email = input("Введите email: ")

    password = input("Введите пароль: ")

    for user in users:

        if user["email"] == email and user["password"] == password:

            current_user = user

            print("\n✅ Вы успешно вошли!")

            print(f"Здравствуйте, {user['name']}!")

            return True

    print("\n❌ Неверный email или пароль!")

    return False


# ============================================================
#                  ПОКАЗ ГОРОДОВ
# ============================================================

def show_cities():

    print("\n" + "=" * 70)

    print("                    🌍 ГОРОДА")

    print("=" * 70)

    for index, city in enumerate(cities, start=1):

        print(f"{index}. {city}")


# ============================================================
#                  ВЫБОР ГОРОДА
# ============================================================

def choose_city(message):

    show_cities()

    while True:

        choice = input(f"\n{message}: ")

        if choice.isdigit():

            number = int(choice)

            if 1 <= number <= len(cities):

                return cities[number - 1]

        print("❌ Выберите правильный номер города!")


# ============================================================
#                  ПОИСК РЕЙСА
# ============================================================

def search_flights():

    print("\n" + "=" * 70)

    print("                    🔎 ПОИСК РЕЙСА")

    print("=" * 70)

    from_city = choose_city("Откуда вы летите")

    to_city = choose_city("Куда вы летите")

    if from_city == to_city:

        print("❌ Города вылета и прилёта не должны совпадать!")

        return

    flight_date = input("Введите дату полёта: ")

    route = from_city + "-" + to_city

    reverse_route = to_city + "-" + from_city

    if route in ticket_prices:

        price = ticket_prices[route]

        duration = flight_times[route]

    elif reverse_route in ticket_prices:

        price = ticket_prices[reverse_route]

        duration = flight_times[reverse_route]

    else:

        price = random.randint(15000, 100000)

        duration = "От 2 до 12 часов"

    airline = random.choice(airlines)

    plane = random.choice(planes)

    departure = random.choice(departure_times)

    arrival = random.choice(arrival_times)

    flight_number = "FL" + str(random.randint(100, 999))

    flight = {

        "from": from_city,

        "to": to_city,

        "date": flight_date,

        "departure": departure,

        "arrival": arrival,

        "duration": duration,

        "price": price,

        "airline": airline,

        "plane": plane,

        "flight_number": flight_number

    }

    print("\n" + "=" * 70)

    print("                  ✈️ НАЙДЕННЫЙ РЕЙС")

    print("=" * 70)

    print(f"🛫 Откуда: {from_city}")

    print(f"🛬 Куда: {to_city}")

    print(f"📅 Дата: {flight_date}")

    print(f"⏰ Вылет: {departure}")

    print(f"🕒 Прилёт: {arrival}")

    print(f"⏱️ Время полёта: {duration}")

    print(f"✈️ Авиакомпания: {airline}")

    print(f"🛩️ Самолёт: {plane}")

    print(f"🎫 Номер рейса: {flight_number}")

    print(f"💰 Цена: {price} сом")

    print("=" * 70)

    choice = input("\nЗабронировать этот рейс? (да/нет): ")

    if choice.lower() == "да":

        book_flight(flight)


# ============================================================
#                  ВЫБОР КЛАССА
# ============================================================

def choose_class():

    print("\n" + "=" * 70)

    print("                  💺 КЛАСС БИЛЕТА")

    print("=" * 70)

    for key, value in ticket_classes.items():

        print(f"\n{key}. {value['name']}")

        print(f"   Доплата: {value['price']} сом")

        print(f"   Багаж: {value['baggage']}")

        print(f"   Питание: {value['food']}")

        print(f"   Wi-Fi: {value['wifi']}")

        print(f"   Приоритет: {value['priority']}")

    while True:

        choice = input("\nВыберите класс: ")

        if choice in ticket_classes:

            return ticket_classes[choice]

        print("❌ Неверный выбор!")


# ============================================================
#                  ВЫБОР БАГАЖА
# ============================================================

def choose_baggage():

    print("\n" + "=" * 70)

    print("                    🧳 БАГАЖ")

    print("=" * 70)

    for key, value in baggage_options.items():

        print(
            f"{key}. {value['name']} — "
            f"{value['weight']} — "
            f"{value['price']} сом"
        )

    while True:

        choice = input("\nВыберите багаж: ")

        if choice in baggage_options:

            return baggage_options[choice]

        print("❌ Неверный выбор!")


# ============================================================
#                  ВЫБОР МЕСТА
# ============================================================

def choose_seat():

    print("\n" + "=" * 70)

    print("                  🪑 ВЫБОР МЕСТА")

    print("=" * 70)

    print("Доступные места:")

    print("1A  1B  1C  1D  1E  1F")

    print("2A  2B  2C  2D  2E  2F")

    print("3A  3B  3C  3D  3E  3F")

    print("4A  4B  4C  4D  4E  4F")

    print("5A  5B  5C  5D  5E  5F")

    print("6A  6B  6C  6D  6E  6F")

    print("7A  7B  7C  7D  7E  7F")

    print("8A  8B  8C  8D  8E  8F")

    print("9A  9B  9C  9D  9E  9F")

    print("10A 10B 10C 10D 10E 10F")

    seat = input("\nВведите место: ")

    if seat == "":

        seat = "12A"

    return seat.upper()


# ============================================================
#                  ДОПОЛНИТЕЛЬНЫЕ УСЛУГИ
# ============================================================

def choose_services():

    selected = []

    total = 0

    print("\n" + "=" * 70)

    print("                🛎️ ДОПОЛНИТЕЛЬНЫЕ УСЛУГИ")

    print("=" * 70)

    for key, value in extra_services.items():

        print(f"{key}. {value['name']} — {value['price']} сом")

    while True:

        choice = input(
            "\nВыберите услугу "
            "(5 — без услуг, 0 — закончить): "
        )

        if choice == "0":

            break

        if choice in extra_services:

            service = extra_services[choice]

            if service["name"] == "Без дополнительных услуг":

                break

            selected.append(service["name"])

            total += service["price"]

            print(f"✅ Добавлено: {service['name']}")

        else:

            print("❌ Неверный выбор!")

    return selected, total


# ============================================================
#                  СКИДКА
# ============================================================

def calculate_discount(price):

    print("\n" + "=" * 70)

    print("                    🎁 СКИДКА")

    print("=" * 70)

    print("1. Нет скидки")

    print("2. Студент — 5%")

    print("3. Постоянный клиент — 10%")

    print("4. Специальная акция — 15%")

    choice = input("Выберите скидку: ")

    if choice == "2":

        return price * 0.05

    elif choice == "3":

        return price * 0.10

    elif choice == "4":

        return price * 0.15

    else:

        return 0


# ============================================================
#                  БРОНИРОВАНИЕ
# ============================================================

def book_flight(flight):

    global selected_flight

    if current_user is None:

        print("❌ Сначала войдите в аккаунт!")

        return

    print("\n" + "=" * 70)

    print("                 🎫 БРОНИРОВАНИЕ")

    print("=" * 70)

    print(f"Пассажир: {current_user['name']}")

    print(f"Маршрут: {flight['from']} → {flight['to']}")

    print(f"Дата: {flight['date']}")

    ticket_class = choose_class()

    baggage = choose_baggage()

    seat = choose_seat()

    services, services_price = choose_services()

    base_price = flight["price"]

    class_price = ticket_class["price"]

    baggage_price = baggage["price"]

    subtotal = base_price + class_price + baggage_price + services_price

    discount = calculate_discount(subtotal)

    total_price = subtotal - discount

    ticket_number = random.randint(100000, 999999)

    booking = {

        "ticket_number": ticket_number,

        "passenger": current_user["name"] + " " + current_user["surname"],

        "from": flight["from"],

        "to": flight["to"],

        "date": flight["date"],

        "departure": flight["departure"],

        "arrival": flight["arrival"],

        "duration": flight["duration"],

        "airline": flight["airline"],

        "plane": flight["plane"],

        "flight_number": flight["flight_number"],

        "ticket_class": ticket_class["name"],

        "baggage": baggage["name"],

        "baggage_weight": baggage["weight"],

        "seat": seat,

        "services": services,

        "base_price": base_price,

        "class_price": class_price,

        "baggage_price": baggage_price,

        "services_price": services_price,

        "subtotal": subtotal,

        "discount": discount,

        "total_price": total_price,

        "status": "Забронирован",

        "created": datetime.now().strftime("%d.%m.%Y %H:%M")

    }

    bookings.append(booking)

    current_user["bookings"].append(booking)

    print("\n✅ БРОНИРОВАНИЕ УСПЕШНО СОЗДАНО!")

    print(f"🎫 Номер билета: {ticket_number}")

    print(f"💰 Итоговая цена: {total_price:.2f} сом")

    save_ticket_to_file(booking)


# ============================================================
#                  СОХРАНЕНИЕ БИЛЕТА
# ============================================================

def save_ticket_to_file(booking):

    filename = f"ticket_{booking['ticket_number']}.txt"

    with open(filename, "w", encoding="utf-8") as file:

        file.write("=" * 60 + "\n")

        file.write("             ✈️ AIRLINE TICKET\n")

        file.write("=" * 60 + "\n\n")

        file.write(f"Пассажир: {booking['passenger']}\n")

        file.write(f"Номер билета: {booking['ticket_number']}\n")

        file.write(f"Номер рейса: {booking['flight_number']}\n\n")

        file.write(f"Откуда: {booking['from']}\n")

        file.write(f"Куда: {booking['to']}\n")

        file.write(f"Дата: {booking['date']}\n")

        file.write(f"Вылет: {booking['departure']}\n")

        file.write(f"Прилёт: {booking['arrival']}\n")

        file.write(f"Время полёта: {booking['duration']}\n\n")

        file.write(f"Авиакомпания: {booking['airline']}\n")

        file.write(f"Самолёт: {booking['plane']}\n")

        file.write(f"Класс: {booking['ticket_class']}\n")

        file.write(f"Место: {booking['seat']}\n")

        file.write(f"Багаж: {booking['baggage']}\n")

        file.write(f"Вес багажа: {booking['baggage_weight']}\n\n")

        file.write(f"Цена билета: {booking['base_price']} сом\n")

        file.write(f"Класс: {booking['class_price']} сом\n")

        file.write(f"Багаж: {booking['baggage_price']} сом\n")

        file.write(f"Услуги: {booking['services_price']} сом\n")

        file.write(f"Скидка: {booking['discount']:.2f} сом\n")

        file.write(f"ИТОГО: {booking['total_price']:.2f} сом\n\n")

        file.write(f"Статус: {booking['status']}\n")

        file.write(f"Создано: {booking['created']}\n")

        file.write("=" * 60 + "\n")

    print(f"📄 Билет сохранён в файл: {filename}")


# ============================================================
#                  ПОКАЗАТЬ БИЛЕТ
# ============================================================

def show_ticket(booking):

    print("\n" + "=" * 70)

    print("                     🎫 БИЛЕТ")

    print("=" * 70)

    print(f"👤 Пассажир: {booking['passenger']}")

    print(f"🎫 Номер билета: {booking['ticket_number']}")

    print(f"✈️ Номер рейса: {booking['flight_number']}")

    print("-" * 70)

    print(f"🛫 Откуда: {booking['from']}")

    print(f"🛬 Куда: {booking['to']}")

    print(f"📅 Дата: {booking['date']}")

    print(f"⏰ Вылет: {booking['departure']}")

    print(f"🕒 Прилёт: {booking['arrival']}")

    print(f"⏱️ Время полёта: {booking['duration']}")

    print("-" * 70)

    print(f"✈️ Авиакомпания: {booking['airline']}")

    print(f"🛩️ Самолёт: {booking['plane']}")

    print(f"💺 Класс: {booking['ticket_class']}")

    print(f"🪑 Место: {booking['seat']}")

    print(f"🧳 Багаж: {booking['baggage']}")

    print(f"⚖️ Вес: {booking['baggage_weight']}")

    print("-" * 70)

    print(f"💰 Цена билета: {booking['base_price']} сом")

    print(f"💺 Класс: {booking['class_price']} сом")

    print(f"🧳 Багаж: {booking['baggage_price']} сом")

    print(f"🛎️ Услуги: {booking['services_price']} сом")

    print(f"🎁 Скидка: {booking['discount']:.2f} сом")

    print(f"💵 ИТОГО: {booking['total_price']:.2f} сом")

    print("-" * 70)

    print(f"📌 Статус: {booking['status']}")

    print(f"🕒 Создано: {booking['created']}")

    print("=" * 70)


# ============================================================
#                  ИСТОРИЯ БИЛЕТОВ
# ============================================================

def booking_history():

    if current_user is None:

        print("❌ Сначала войдите в аккаунт!")

        return

    print("\n" + "=" * 70)

    print("                  📚 МОИ БИЛЕТЫ")

    print("=" * 70)

    if len(current_user["bookings"]) == 0:

        print("У вас пока нет бронирований.")

        return

    for index, booking in enumerate(current_user["bookings"], start=1):

        print(f"\nБилет №{index}")

        print(f"🎫 Номер: {booking['ticket_number']}")

        print(f"🛫 Маршрут: {booking['from']} → {booking['to']}")

        print(f"📅 Дата: {booking['date']}")

        print(f"💰 Цена: {booking['total_price']:.2f} сом")

        print(f"📌 Статус: {booking['status']}")

        print("-" * 50)


# ============================================================
#                  ПРОСМОТР КОНКРЕТНОГО БИЛЕТА
# ============================================================

def view_ticket():

    if current_user is None:

        print("❌ Сначала войдите в аккаунт!")

        return

    if len(current_user["bookings"]) == 0:

        print("❌ У вас нет билетов!")

        return

    number = input("Введите номер билета: ")

    for booking in current_user["bookings"]:

        if str(booking["ticket_number"]) == number:

            show_ticket(booking)

            return

    print("❌ Билет не найден!")


# ============================================================
#                  ОТМЕНА БИЛЕТА
# ============================================================

def cancel_booking():

    if current_user is None:

        print("❌ Сначала войдите в аккаунт!")

        return

    number = input("Введите номер билета для отмены: ")

    for booking in current_user["bookings"]:

        if str(booking["ticket_number"]) == number:

            if booking["status"] == "Отменён":

                print("❌ Билет уже отменён!")

                return

            booking["status"] = "Отменён"

            print("✅ Бронирование отменено!")

            return

    print("❌ Билет не найден!")


# ============================================================
#                  ПРОФИЛЬ ПОЛЬЗОВАТЕЛЯ
# ============================================================

def profile():

    if current_user is None:

        print("❌ Сначала войдите в аккаунт!")

        return

    print("\n" + "=" * 70)

    print("                    👤 ПРОФИЛЬ")

    print("=" * 70)

    print(f"Имя: {current_user['name']}")

    print(f"Фамилия: {current_user['surname']}")

    print(f"Email: {current_user['email']}")

    print(f"Телефон: {current_user['phone']}")

    print(f"Бонусы: {current_user['bonus']}")

    print(f"Количество билетов: {len(current_user['bookings'])}")


# ============================================================
#                  СПРАВКА
# ============================================================

def help_menu():

    print("\n" + "=" * 70)

    print("                    ℹ️ СПРАВКА")

    print("=" * 70)

    print("1. Зарегистрируйтесь.")

    print("2. Войдите в аккаунт.")

    print("3. Найдите рейс.")

    print("4. Выберите класс.")

    print("5. Выберите багаж.")

    print("6. Выберите место.")

    print("7. Подтвердите бронирование.")

    print("8. Получите номер билета.")

    print("9. Билет сохранится в TXT-файл.")

    print("\nДля выхода выберите 0.")


# ============================================================
#                  ГЛАВНОЕ МЕНЮ
# ============================================================

def main_menu():

    while True:

        print("\n" + "=" * 70)

        print("                 ✈️ AIRLINE ONLINE")

        print("=" * 70)

        if current_user:

            print(
                f"👤 Пользователь: "
                f"{current_user['name']} "
                f"{current_user['surname']}"
            )

        else:

            print("👤 Пользователь: Гость")

        print("-" * 70)

        print("1. 📝 Регистрация")

        print("2. 🔐 Вход")

        print("3. 🔎 Поиск рейса")

        print("4. 📚 Мои билеты")

        print("5. 🎫 Просмотреть билет")

        print("6. ❌ Отменить билет")

        print("7. 👤 Мой профиль")

        print("8. ℹ️ Помощь")

        print("0. 🚪 Выход")

        print("=" * 70)

        choice = input("Выберите действие: ")

        if choice == "1":

            register()

        elif choice == "2":

            login()

        elif choice == "3":

            search_flights()

        elif choice == "4":

            booking_history()

        elif choice == "5":

            view_ticket()

        elif choice == "6":

            cancel_booking()

        elif choice == "7":

            profile()

        elif choice == "8":

            help_menu()

        elif choice == "0":

            print("\nСпасибо за использование AIRLINE ✈️")

            print("До свидания!")

            break

        else:

            print("❌ Неверный выбор!")


# ============================================================
#                  ЗАПУСК ПРОГРАММЫ
# ============================================================

if __name__ == "__main__":

    main_menu()

from datetime import datetime
import random


# ============================================================
#                  ✈️ AIRLINE SYSTEM ✈️
#              СИСТЕМА АВИАБИЛЕТОВ
# ============================================================


print("=" * 70)
print("              ✈️ WELCOME TO AIRLINE ✈️")
print("                 АВИАБИЛЕТЫ ONLINE")
print("=" * 70)


# ============================================================
#                     ДАННЫЕ СИСТЕМЫ
# ============================================================

airline_name = "AIRLINE INTERNATIONAL"

company_country = "Kyrgyzstan"

currency = "KGS"

system_version = "1.0.0"

current_year = 2026


# ============================================================
#                  СПИСОК АВИАКОМПАНИЙ
# ============================================================

airlines = [
    "AIRLINE INTERNATIONAL",
    "SKY AIR",
    "GLOBAL AIRWAYS",
    "FLY WORLD",
    "ASIA AIRLINES"
]


# ============================================================
#                  СПИСОК САМОЛЁТОВ
# ============================================================

planes = [
    "Boeing 737",
    "Boeing 777",
    "Airbus A320",
    "Airbus A350",
    "Boeing 787 Dreamliner"
]


# ============================================================
#                  ГОРОДА И НАПРАВЛЕНИЯ
# ============================================================

cities = [
    "Бишкек",
    "Ош",
    "Алматы",
    "Астана",
    "Дубай",
    "Стамбул",
    "Москва",
    "Лондон",
    "Париж",
    "Пекин",
    "Токио",
    "Сеул",
    "Нью-Йорк",
    "Доха",
    "Абу-Даби"
]


# ============================================================
#                  ЦЕНЫ НА БИЛЕТЫ
# ============================================================

ticket_prices = {
    "Бишкек-Дубай": 25000,
    "Бишкек-Стамбул": 30000,
    "Бишкек-Москва": 20000,
    "Бишкек-Алматы": 10000,
    "Бишкек-Астана": 15000,
    "Бишкек-Лондон": 60000,
    "Бишкек-Париж": 55000,
    "Бишкек-Пекин": 35000,
    "Бишкек-Токио": 50000,
    "Бишкек-Сеул": 45000,
    "Бишкек-Нью-Йорк": 90000,
    "Бишкек-Доха": 28000,
    "Бишкек-Абу-Даби": 27000
}


# ============================================================
#                  ВРЕМЯ ПОЛЁТА
# ============================================================

flight_times = {
    "Бишкек-Дубай": "4 часа 30 минут",
    "Бишкек-Стамбул": "5 часов 40 минут",
    "Бишкек-Москва": "4 часа 20 минут",
    "Бишкек-Алматы": "1 час",
    "Бишкек-Астана": "2 часа",
    "Бишкек-Лондон": "9 часов",
    "Бишкек-Париж": "8 часов 30 минут",
    "Бишкек-Пекин": "5 часов",
    "Бишкек-Токио": "7 часов",
    "Бишкек-Сеул": "6 часов 30 минут",
    "Бишкек-Нью-Йорк": "14 часов",
    "Бишкек-Доха": "4 часа 40 минут",
    "Бишкек-Абу-Даби": "4 часа 20 минут"
}


# ============================================================
#                  ВРЕМЯ ВЫЛЕТА
# ============================================================

departure_times = [
    "06:00",
    "08:30",
    "10:00",
    "12:45",
    "14:30",
    "16:00",
    "18:20",
    "21:00",
    "23:30"
]


# ============================================================
#                  ВРЕМЯ ПРИЛЁТА
# ============================================================

arrival_times = [
    "10:30",
    "13:00",
    "14:30",
    "17:15",
    "19:00",
    "20:30",
    "22:50",
    "01:30",
    "04:00"
]


# ============================================================
#                  КЛАССЫ БИЛЕТОВ
# ============================================================

ticket_classes = {
    "1": {
        "name": "Эконом",
        "price": 0,
        "baggage": "20 кг",
        "food": "Питание включено",
        "wifi": "Нет",
        "priority": "Нет"
    },

    "2": {
        "name": "Комфорт",
        "price": 10000,
        "baggage": "30 кг",
        "food": "Питание включено",
        "wifi": "Да",
        "priority": "Да"
    },

    "3": {
        "name": "Бизнес",
        "price": 30000,
        "baggage": "40 кг",
        "food": "Питание премиум",
        "wifi": "Да",
        "priority": "Да"
    }
}


# ============================================================
#                  БАГАЖ
# ============================================================

baggage_options = {
    "1": {
        "name": "Только ручная кладь",
        "price": 0,
        "weight": "7 кг"
    },

    "2": {
        "name": "Ручная кладь + багаж",
        "price": 5000,
        "weight": "23 кг"
    },

    "3": {
        "name": "Большой багаж",
        "price": 10000,
        "weight": "32 кг"
    }
}


# ============================================================
#                  ДОПОЛНИТЕЛЬНЫЕ УСЛУГИ
# ============================================================

extra_services = {
    "1": {
        "name": "Выбор места у окна",
        "price": 1500
    },

    "2": {
        "name": "Выбор места у прохода",
        "price": 1000
    },

    "3": {
        "name": "Дополнительное питание",
        "price": 2000
    },

    "4": {
        "name": "Доступ в VIP-зал",
        "price": 5000
    },

    "5": {
        "name": "Без дополнительных услуг",
        "price": 0
    }
}


# ============================================================
#                  ПЕРЕМЕННЫЕ ПОЛЬЗОВАТЕЛЯ
# ============================================================

users = []

current_user = None

bookings = []

selected_flight = None


# ============================================================
#                  ФУНКЦИЯ РЕГИСТРАЦИИ
# ============================================================

def register():

    print("\n" + "=" * 70)

    print("                  📝 РЕГИСТРАЦИЯ")

    print("=" * 70)

    name = input("Введите имя: ")

    surname = input("Введите фамилию: ")

    email = input("Введите email: ")

    phone = input("Введите номер телефона: ")

    password = input("Придумайте пароль: ")

    if name == "" or surname == "":

        print("❌ Имя и фамилия обязательны!")

        return

    for user in users:

        if user["email"] == email:

            print("❌ Такой email уже зарегистрирован!")

            return

    new_user = {

        "name": name,

        "surname": surname,

        "email": email,

        "phone": phone,

        "password": password,

        "bonus": 0,

        "bookings": []

    }

    users.append(new_user)

    print("\n✅ Регистрация успешно завершена!")

    print(f"Добро пожаловать, {name}!")


# ============================================================
#                  ФУНКЦИЯ ВХОДА
# ============================================================

def login():

    global current_user

    print("\n" + "=" * 70)

    print("                      🔐 ВХОД")

    print("=" * 70)

    email = input("Введите email: ")

    password = input("Введите пароль: ")

    for user in users:

        if user["email"] == email and user["password"] == password:

            current_user = user

            print("\n✅ Вы успешно вошли!")

            print(f"Здравствуйте, {user['name']}!")

            return True

    print("\n❌ Неверный email или пароль!")

    return False


# ============================================================
#                  ПОКАЗ ГОРОДОВ
# ============================================================

def show_cities():

    print("\n" + "=" * 70)

    print("                    🌍 ГОРОДА")

    print("=" * 70)

    for index, city in enumerate(cities, start=1):

        print(f"{index}. {city}")


# ============================================================
#                  ВЫБОР ГОРОДА
# ============================================================

def choose_city(message):

    show_cities()

    while True:

        choice = input(f"\n{message}: ")

        if choice.isdigit():

            number = int(choice)

            if 1 <= number <= len(cities):

                return cities[number - 1]

        print("❌ Выберите правильный номер города!")


# ============================================================
#                  ПОИСК РЕЙСА
# ============================================================

def search_flights():

    print("\n" + "=" * 70)

    print("                    🔎 ПОИСК РЕЙСА")

    print("=" * 70)

    from_city = choose_city("Откуда вы летите")

    to_city = choose_city("Куда вы летите")

    if from_city == to_city:

        print("❌ Города вылета и прилёта не должны совпадать!")

        return

    flight_date = input("Введите дату полёта: ")

    route = from_city + "-" + to_city

    reverse_route = to_city + "-" + from_city

    if route in ticket_prices:

        price = ticket_prices[route]

        duration = flight_times[route]

    elif reverse_route in ticket_prices:

        price = ticket_prices[reverse_route]

        duration = flight_times[reverse_route]

    else:

        price = random.randint(15000, 100000)

        duration = "От 2 до 12 часов"

    airline = random.choice(airlines)

    plane = random.choice(planes)

    departure = random.choice(departure_times)

    arrival = random.choice(arrival_times)

    flight_number = "FL" + str(random.randint(100, 999))

    flight = {

        "from": from_city,

        "to": to_city,

        "date": flight_date,

        "departure": departure,

        "arrival": arrival,

        "duration": duration,

        "price": price,

        "airline": airline,

        "plane": plane,

        "flight_number": flight_number

    }

    print("\n" + "=" * 70)

    print("                  ✈️ НАЙДЕННЫЙ РЕЙС")

    print("=" * 70)

    print(f"🛫 Откуда: {from_city}")

    print(f"🛬 Куда: {to_city}")

    print(f"📅 Дата: {flight_date}")

    print(f"⏰ Вылет: {departure}")

    print(f"🕒 Прилёт: {arrival}")

    print(f"⏱️ Время полёта: {duration}")

    print(f"✈️ Авиакомпания: {airline}")

    print(f"🛩️ Самолёт: {plane}")

    print(f"🎫 Номер рейса: {flight_number}")

    print(f"💰 Цена: {price} сом")

    print("=" * 70)

    choice = input("\nЗабронировать этот рейс? (да/нет): ")

    if choice.lower() == "да":

        book_flight(flight)


# ============================================================
#                  ВЫБОР КЛАССА
# ============================================================

def choose_class():

    print("\n" + "=" * 70)

    print("                  💺 КЛАСС БИЛЕТА")

    print("=" * 70)

    for key, value in ticket_classes.items():

        print(f"\n{key}. {value['name']}")

        print(f"   Доплата: {value['price']} сом")

        print(f"   Багаж: {value['baggage']}")

        print(f"   Питание: {value['food']}")

        print(f"   Wi-Fi: {value['wifi']}")

        print(f"   Приоритет: {value['priority']}")

    while True:

        choice = input("\nВыберите класс: ")

        if choice in ticket_classes:

            return ticket_classes[choice]

        print("❌ Неверный выбор!")


# ============================================================
#                  ВЫБОР БАГАЖА
# ============================================================

def choose_baggage():

    print("\n" + "=" * 70)

    print("                    🧳 БАГАЖ")

    print("=" * 70)

    for key, value in baggage_options.items():

        print(
            f"{key}. {value['name']} — "
            f"{value['weight']} — "
            f"{value['price']} сом"
        )

    while True:

        choice = input("\nВыберите багаж: ")

        if choice in baggage_options:

            return baggage_options[choice]

        print("❌ Неверный выбор!")


# ============================================================
#                  ВЫБОР МЕСТА
# ============================================================

def choose_seat():

    print("\n" + "=" * 70)

    print("                  🪑 ВЫБОР МЕСТА")

    print("=" * 70)

    print("Доступные места:")

    print("1A  1B  1C  1D  1E  1F")

    print("2A  2B  2C  2D  2E  2F")

    print("3A  3B  3C  3D  3E  3F")

    print("4A  4B  4C  4D  4E  4F")

    print("5A  5B  5C  5D  5E  5F")

    print("6A  6B  6C  6D  6E  6F")

    print("7A  7B  7C  7D  7E  7F")

    print("8A  8B  8C  8D  8E  8F")

    print("9A  9B  9C  9D  9E  9F")

    print("10A 10B 10C 10D 10E 10F")

    seat = input("\nВведите место: ")

    if seat == "":

        seat = "12A"

    return seat.upper()


# ============================================================
#                  ДОПОЛНИТЕЛЬНЫЕ УСЛУГИ
# ============================================================

def choose_services():

    selected = []

    total = 0

    print("\n" + "=" * 70)

    print("                🛎️ ДОПОЛНИТЕЛЬНЫЕ УСЛУГИ")

    print("=" * 70)

    for key, value in extra_services.items():

        print(f"{key}. {value['name']} — {value['price']} сом")

    while True:

        choice = input(
            "\nВыберите услугу "
            "(5 — без услуг, 0 — закончить): "
        )

        if choice == "0":

            break

        if choice in extra_services:

            service = extra_services[choice]

            if service["name"] == "Без дополнительных услуг":

                break

            selected.append(service["name"])

            total += service["price"]

            print(f"✅ Добавлено: {service['name']}")

        else:

            print("❌ Неверный выбор!")

    return selected, total


# ============================================================
#                  СКИДКА
# ============================================================

def calculate_discount(price):

    print("\n" + "=" * 70)

    print("                    🎁 СКИДКА")

    print("=" * 70)

    print("1. Нет скидки")

    print("2. Студент — 5%")

    print("3. Постоянный клиент — 10%")

    print("4. Специальная акция — 15%")

    choice = input("Выберите скидку: ")

    if choice == "2":

        return price * 0.05

    elif choice == "3":

        return price * 0.10

    elif choice == "4":

        return price * 0.15

    else:

        return 0


# ============================================================
#                  БРОНИРОВАНИЕ
# ============================================================

def book_flight(flight):

    global selected_flight

    if current_user is None:

        print("❌ Сначала войдите в аккаунт!")

        return

    print("\n" + "=" * 70)

    print("                 🎫 БРОНИРОВАНИЕ")

    print("=" * 70)

    print(f"Пассажир: {current_user['name']}")

    print(f"Маршрут: {flight['from']} → {flight['to']}")

    print(f"Дата: {flight['date']}")

    ticket_class = choose_class()

    baggage = choose_baggage()

    seat = choose_seat()

    services, services_price = choose_services()

    base_price = flight["price"]

    class_price = ticket_class["price"]

    baggage_price = baggage["price"]

    subtotal = base_price + class_price + baggage_price + services_price

    discount = calculate_discount(subtotal)

    total_price = subtotal - discount

    ticket_number = random.randint(100000, 999999)

    booking = {

        "ticket_number": ticket_number,

        "passenger": current_user["name"] + " " + current_user["surname"],

        "from": flight["from"],

        "to": flight["to"],

        "date": flight["date"],

        "departure": flight["departure"],

        "arrival": flight["arrival"],

        "duration": flight["duration"],

        "airline": flight["airline"],

        "plane": flight["plane"],

        "flight_number": flight["flight_number"],

        "ticket_class": ticket_class["name"],

        "baggage": baggage["name"],

        "baggage_weight": baggage["weight"],

        "seat": seat,

        "services": services,

        "base_price": base_price,

        "class_price": class_price,

        "baggage_price": baggage_price,

        "services_price": services_price,

        "subtotal": subtotal,

        "discount": discount,

        "total_price": total_price,

        "status": "Забронирован",

        "created": datetime.now().strftime("%d.%m.%Y %H:%M")

    }

    bookings.append(booking)

    current_user["bookings"].append(booking)

    print("\n✅ БРОНИРОВАНИЕ УСПЕШНО СОЗДАНО!")

    print(f"🎫 Номер билета: {ticket_number}")

    print(f"💰 Итоговая цена: {total_price:.2f} сом")

    save_ticket_to_file(booking)


# ============================================================
#                  СОХРАНЕНИЕ БИЛЕТА
# ============================================================

def save_ticket_to_file(booking):

    filename = f"ticket_{booking['ticket_number']}.txt"

    with open(filename, "w", encoding="utf-8") as file:

        file.write("=" * 60 + "\n")

        file.write("             ✈️ AIRLINE TICKET\n")

        file.write("=" * 60 + "\n\n")

        file.write(f"Пассажир: {booking['passenger']}\n")

        file.write(f"Номер билета: {booking['ticket_number']}\n")

        file.write(f"Номер рейса: {booking['flight_number']}\n\n")

        file.write(f"Откуда: {booking['from']}\n")

        file.write(f"Куда: {booking['to']}\n")

        file.write(f"Дата: {booking['date']}\n")

        file.write(f"Вылет: {booking['departure']}\n")

        file.write(f"Прилёт: {booking['arrival']}\n")

        file.write(f"Время полёта: {booking['duration']}\n\n")

        file.write(f"Авиакомпания: {booking['airline']}\n")

        file.write(f"Самолёт: {booking['plane']}\n")

        file.write(f"Класс: {booking['ticket_class']}\n")

        file.write(f"Место: {booking['seat']}\n")

        file.write(f"Багаж: {booking['baggage']}\n")

        file.write(f"Вес багажа: {booking['baggage_weight']}\n\n")

        file.write(f"Цена билета: {booking['base_price']} сом\n")

        file.write(f"Класс: {booking['class_price']} сом\n")

        file.write(f"Багаж: {booking['baggage_price']} сом\n")

        file.write(f"Услуги: {booking['services_price']} сом\n")

        file.write(f"Скидка: {booking['discount']:.2f} сом\n")

        file.write(f"ИТОГО: {booking['total_price']:.2f} сом\n\n")

        file.write(f"Статус: {booking['status']}\n")

        file.write(f"Создано: {booking['created']}\n")

        file.write("=" * 60 + "\n")

    print(f"📄 Билет сохранён в файл: {filename}")


# ============================================================
#                  ПОКАЗАТЬ БИЛЕТ
# ============================================================

def show_ticket(booking):

    print("\n" + "=" * 70)

    print("                     🎫 БИЛЕТ")

    print("=" * 70)

    print(f"👤 Пассажир: {booking['passenger']}")

    print(f"🎫 Номер билета: {booking['ticket_number']}")

    print(f"✈️ Номер рейса: {booking['flight_number']}")

    print("-" * 70)

    print(f"🛫 Откуда: {booking['from']}")

    print(f"🛬 Куда: {booking['to']}")

    print(f"📅 Дата: {booking['date']}")

    print(f"⏰ Вылет: {booking['departure']}")

    print(f"🕒 Прилёт: {booking['arrival']}")

    print(f"⏱️ Время полёта: {booking['duration']}")

    print("-" * 70)

    print(f"✈️ Авиакомпания: {booking['airline']}")

    print(f"🛩️ Самолёт: {booking['plane']}")

    print(f"💺 Класс: {booking['ticket_class']}")

    print(f"🪑 Место: {booking['seat']}")

    print(f"🧳 Багаж: {booking['baggage']}")

    print(f"⚖️ Вес: {booking['baggage_weight']}")

    print("-" * 70)

    print(f"💰 Цена билета: {booking['base_price']} сом")

    print(f"💺 Класс: {booking['class_price']} сом")

    print(f"🧳 Багаж: {booking['baggage_price']} сом")

    print(f"🛎️ Услуги: {booking['services_price']} сом")

    print(f"🎁 Скидка: {booking['discount']:.2f} сом")

    print(f"💵 ИТОГО: {booking['total_price']:.2f} сом")

    print("-" * 70)

    print(f"📌 Статус: {booking['status']}")

    print(f"🕒 Создано: {booking['created']}")

    print("=" * 70)


# ============================================================
#                  ИСТОРИЯ БИЛЕТОВ
# ============================================================

def booking_history():

    if current_user is None:

        print("❌ Сначала войдите в аккаунт!")

        return

    print("\n" + "=" * 70)

    print("                  📚 МОИ БИЛЕТЫ")

    print("=" * 70)

    if len(current_user["bookings"]) == 0:

        print("У вас пока нет бронирований.")

        return

    for index, booking in enumerate(current_user["bookings"], start=1):

        print(f"\nБилет №{index}")

        print(f"🎫 Номер: {booking['ticket_number']}")

        print(f"🛫 Маршрут: {booking['from']} → {booking['to']}")

        print(f"📅 Дата: {booking['date']}")

        print(f"💰 Цена: {booking['total_price']:.2f} сом")

        print(f"📌 Статус: {booking['status']}")

        print("-" * 50)


# ============================================================
#                  ПРОСМОТР КОНКРЕТНОГО БИЛЕТА
# ============================================================

def view_ticket():

    if current_user is None:

        print("❌ Сначала войдите в аккаунт!")

        return

    if len(current_user["bookings"]) == 0:

        print("❌ У вас нет билетов!")

        return

    number = input("Введите номер билета: ")

    for booking in current_user["bookings"]:

        if str(booking["ticket_number"]) == number:

            show_ticket(booking)

            return

    print("❌ Билет не найден!")


# ============================================================
#                  ОТМЕНА БИЛЕТА
# ============================================================

def cancel_booking():

    if current_user is None:

        print("❌ Сначала войдите в аккаунт!")

        return

    number = input("Введите номер билета для отмены: ")

    for booking in current_user["bookings"]:

        if str(booking["ticket_number"]) == number:

            if booking["status"] == "Отменён":

                print("❌ Билет уже отменён!")

                return

            booking["status"] = "Отменён"

            print("✅ Бронирование отменено!")

            return

    print("❌ Билет не найден!")


# ============================================================
#                  ПРОФИЛЬ ПОЛЬЗОВАТЕЛЯ
# ============================================================

def profile():

    if current_user is None:

        print("❌ Сначала войдите в аккаунт!")

        return

    print("\n" + "=" * 70)

    print("                    👤 ПРОФИЛЬ")

    print("=" * 70)

    print(f"Имя: {current_user['name']}")

    print(f"Фамилия: {current_user['surname']}")

    print(f"Email: {current_user['email']}")

    print(f"Телефон: {current_user['phone']}")

    print(f"Бонусы: {current_user['bonus']}")

    print(f"Количество билетов: {len(current_user['bookings'])}")


# ============================================================
#                  СПРАВКА
# ============================================================

def help_menu():

    print("\n" + "=" * 70)

    print("                    ℹ️ СПРАВКА")

    print("=" * 70)

    print("1. Зарегистрируйтесь.")

    print("2. Войдите в аккаунт.")

    print("3. Найдите рейс.")

    print("4. Выберите класс.")

    print("5. Выберите багаж.")

    print("6. Выберите место.")

    print("7. Подтвердите бронирование.")

    print("8. Получите номер билета.")

    print("9. Билет сохранится в TXT-файл.")

    print("\nДля выхода выберите 0.")


# ============================================================
#                  ГЛАВНОЕ МЕНЮ
# ============================================================

def main_menu():

    while True:

        print("\n" + "=" * 70)

        print("                 ✈️ AIRLINE ONLINE")

        print("=" * 70)

        if current_user:

            print(
                f"👤 Пользователь: "
                f"{current_user['name']} "
                f"{current_user['surname']}"
            )

        else:

            print("👤 Пользователь: Гость")

        print("-" * 70)

        print("1. 📝 Регистрация")

        print("2. 🔐 Вход")

        print("3. 🔎 Поиск рейса")

        print("4. 📚 Мои билеты")

        print("5. 🎫 Просмотреть билет")

        print("6. ❌ Отменить билет")

        print("7. 👤 Мой профиль")

        print("8. ℹ️ Помощь")

        print("0. 🚪 Выход")

        print("=" * 70)

        choice = input("Выберите действие: ")

        if choice == "1":

            register()

        elif choice == "2":

            login()

        elif choice == "3":

            search_flights()

        elif choice == "4":

            booking_history()

        elif choice == "5":

            view_ticket()

        elif choice == "6":

            cancel_booking()

        elif choice == "7":

            profile()

        elif choice == "8":

            help_menu()

        elif choice == "0":

            print("\nСпасибо за использование AIRLINE ✈️")

            print("До свидания!")

            break

        else:

            print("❌ Неверный выбор!")


# ============================================================
#                  ЗАПУСК ПРОГРАММЫ
# ============================================================

if __name__ == "__main__":

    main_menu()