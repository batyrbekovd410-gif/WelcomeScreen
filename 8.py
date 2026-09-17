# ============================================================
#                  🍔 TASTY FOOD RESTAURANT 🍔
# ============================================================
#                 БОЛЬШОЙ ПРОЕКТ НА PYTHON
# ============================================================

import datetime
import random


# ============================================================
#                 НАСТРОЙКИ РЕСТОРАНА
# ============================================================

RESTAURANT_NAME = "TASTY FOOD"
RESTAURANT_ADDRESS = "Бишкек, Кыргызстан"
RESTAURANT_PHONE = "+996 555 123 456"
CURRENCY = "сом"


# ============================================================
#                 ДАННЫЕ РЕСТОРАНА
# ============================================================

restaurant_info = {

    "name": RESTAURANT_NAME,

    "address": RESTAURANT_ADDRESS,

    "phone": RESTAURANT_PHONE,

    "working_hours": "10:00 - 23:00",

    "tables": 20,

    "rating": 4.8,

    "orders_today": 0,

    "revenue": 0

}


# ============================================================
#                 МЕНЮ РЕСТОРАНА
# ============================================================

menu = {

    1: {
        "name": "Пицца Маргарита",
        "price": 450,
        "category": "Пицца",
        "description": "Томатный соус, сыр, базилик"
    },

    2: {
        "name": "Пицца Пепперони",
        "price": 550,
        "category": "Пицца",
        "description": "Сыр, пепперони, томатный соус"
    },

    3: {
        "name": "Пицца Четыре сыра",
        "price": 650,
        "category": "Пицца",
        "description": "Моцарелла, чеддер, пармезан"
    },

    4: {
        "name": "Пицца Грибная",
        "price": 500,
        "category": "Пицца",
        "description": "Грибы, сыр, соус"
    },

    5: {
        "name": "Пицца Мясная",
        "price": 700,
        "category": "Пицца",
        "description": "Мясо, сыр, овощи"
    },

    6: {
        "name": "Бургер Классический",
        "price": 300,
        "category": "Бургеры",
        "description": "Котлета, салат, соус"
    },

    7: {
        "name": "Чизбургер",
        "price": 350,
        "category": "Бургеры",
        "description": "Котлета, сыр, овощи"
    },

    8: {
        "name": "Двойной бургер",
        "price": 500,
        "category": "Бургеры",
        "description": "Две котлеты, двойной сыр"
    },

    9: {
        "name": "Чикенбургер",
        "price": 320,
        "category": "Бургеры",
        "description": "Курица, салат, соус"
    },

    10: {
        "name": "Бургер BBQ",
        "price": 450,
        "category": "Бургеры",
        "description": "Мясо, BBQ соус, сыр"
    },

    11: {
        "name": "Картошка Фри",
        "price": 150,
        "category": "Закуски",
        "description": "Хрустящая картошка"
    },

    12: {
        "name": "Наггетсы",
        "price": 250,
        "category": "Закуски",
        "description": "Куриные кусочки"
    },

    13: {
        "name": "Крылышки BBQ",
        "price": 400,
        "category": "Закуски",
        "description": "Куриные крылышки"
    },

    14: {
        "name": "Луковые кольца",
        "price": 180,
        "category": "Закуски",
        "description": "Хрустящие кольца"
    },

    15: {
        "name": "Сырные палочки",
        "price": 220,
        "category": "Закуски",
        "description": "Сыр в панировке"
    },

    16: {
        "name": "Кола",
        "price": 100,
        "category": "Напитки",
        "description": "Газированный напиток"
    },

    17: {
        "name": "Спрайт",
        "price": 100,
        "category": "Напитки",
        "description": "Лимонный напиток"
    },

    18: {
        "name": "Фанта",
        "price": 100,
        "category": "Напитки",
        "description": "Апельсиновый напиток"
    },

    19: {
        "name": "Сок Апельсиновый",
        "price": 120,
        "category": "Напитки",
        "description": "Натуральный сок"
    },

    20: {
        "name": "Лимонад",
        "price": 180,
        "category": "Напитки",
        "description": "Домашний лимонад"
    },

    21: {
        "name": "Кофе",
        "price": 150,
        "category": "Напитки",
        "description": "Горячий кофе"
    },

    22: {
        "name": "Капучино",
        "price": 220,
        "category": "Напитки",
        "description": "Кофе с молоком"
    },

    23: {
        "name": "Мороженое",
        "price": 180,
        "category": "Десерты",
        "description": "Сливочное мороженое"
    },

    24: {
        "name": "Шоколадный торт",
        "price": 250,
        "category": "Десерты",
        "description": "Шоколадный десерт"
    },

    25: {
        "name": "Чизкейк",
        "price": 300,
        "category": "Десерты",
        "description": "Классический чизкейк"
    },

    26: {
        "name": "Панкейки",
        "price": 280,
        "category": "Десерты",
        "description": "Панкейки с сиропом"
    },

    27: {
        "name": "Фруктовый салат",
        "price": 250,
        "category": "Десерты",
        "description": "Свежие фрукты"
    },

    28: {
        "name": "Стейк",
        "price": 950,
        "category": "Основные блюда",
        "description": "Мясной стейк"
    },

    29: {
        "name": "Курица с рисом",
        "price": 450,
        "category": "Основные блюда",
        "description": "Курица, рис, овощи"
    },

    30: {
        "name": "Паста Карбонара",
        "price": 500,
        "category": "Основные блюда",
        "description": "Паста с соусом"
    }

}


# ============================================================
#                 ГЛОБАЛЬНЫЕ ДАННЫЕ
# ============================================================

cart = []

orders = []

bookings = []

reviews = []

current_order_number = 1000


# ============================================================
#                 ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ============================================================

def line():

    print("=" * 65)


def title(text):

    line()

    print(text.center(65))

    line()


def pause():

    input("\nНажмите Enter, чтобы продолжить...")


def get_time():

    return datetime.datetime.now().strftime(
        "%d.%m.%Y %H:%M:%S"
    )


def money(value):

    return f"{value:.2f} {CURRENCY}"


# ============================================================
#                 ИНФОРМАЦИЯ О РЕСТОРАНЕ
# ============================================================

def show_restaurant_info():

    title("🍔 ИНФОРМАЦИЯ О РЕСТОРАНЕ 🍔")

    print(f"Название: {restaurant_info['name']}")

    print(f"Адрес: {restaurant_info['address']}")

    print(f"Телефон: {restaurant_info['phone']}")

    print(f"Время работы: {restaurant_info['working_hours']}")

    print(f"Количество столиков: {restaurant_info['tables']}")

    print(f"Рейтинг: {restaurant_info['rating']}")

    print(f"Заказов сегодня: {restaurant_info['orders_today']}")

    print(f"Выручка: {money(restaurant_info['revenue'])}")


# ============================================================
#                 ПОКАЗ МЕНЮ
# ============================================================

def show_menu():

    title("🍕 МЕНЮ РЕСТОРАНА 🍕")

    for number, product in menu.items():

        print(
            f"{number:02d}. "
            f"{product['name']:<25}"
            f"{money(product['price'])}"
        )

    line()


# ============================================================
#                 ПОДРОБНОЕ МЕНЮ
# ============================================================

def detailed_menu():

    title("📋 ПОДРОБНОЕ МЕНЮ")

    for number, product in menu.items():

        print(f"\nНомер: {number}")

        print(f"Название: {product['name']}")

        print(f"Категория: {product['category']}")

        print(f"Цена: {money(product['price'])}")

        print(f"Описание: {product['description']}")

        print("-" * 65)


# ============================================================
#                 ПОИСК БЛЮДА
# ============================================================

def search_food():

    title("🔎 ПОИСК БЛЮДА")

    search = input(
        "Введите название или категорию: "
    ).lower()

    found = False

    for number, product in menu.items():

        if (
            search in product["name"].lower()
            or search in product["category"].lower()
        ):

            print(
                f"{number}. "
                f"{product['name']} — "
                f"{money(product['price'])}"
            )

            found = True

    if not found:

        print("Ничего не найдено.")


# ============================================================
#                 ДОБАВЛЕНИЕ В КОРЗИНУ
# ============================================================

def add_to_cart():

    show_menu()

    try:

        number = int(
            input("Введите номер блюда: ")
        )

        if number not in menu:

            print("Такого блюда нет!")

            return

        quantity = int(
            input("Введите количество: ")
        )

        if quantity <= 0:

            print("Количество должно быть больше нуля!")

            return

        product = menu[number]

        item = {

            "id": number,

            "name": product["name"],

            "price": product["price"],

            "quantity": quantity

        }

        cart.append(item)

        print(
            f"\n✅ {product['name']} добавлено в корзину!"
        )

        print(
            f"Сумма: {money(product['price'] * quantity)}"
        )

    except ValueError:

        print("Ошибка! Введите число.")


# ============================================================
#                 ПРОСМОТР КОРЗИНЫ
# ============================================================

def show_cart():

    title("🛒 ВАША КОРЗИНА")

    if not cart:

        print("Корзина пустая.")

        return

    total = 0

    for index, item in enumerate(cart, start=1):

        item_total = (
            item["price"] * item["quantity"]
        )

        print(
            f"{index}. {item['name']}"
        )

        print(
            f"   Количество: {item['quantity']}"
        )

        print(
            f"   Цена: {money(item['price'])}"
        )

        print(
            f"   Сумма: {money(item_total)}"
        )

        print("-" * 65)

        total += item_total

    print(f"ИТОГО: {money(total)}")


# ============================================================
#                 УДАЛЕНИЕ ИЗ КОРЗИНЫ
# ============================================================

def remove_from_cart():

    if not cart:

        print("Корзина пустая!")

        return

    show_cart()

    try:

        number = int(
            input("Введите номер позиции: ")
        )

        if number < 1 or number > len(cart):

            print("Неверный номер!")

            return

        removed = cart.pop(number - 1)

        print(
            f"❌ {removed['name']} удалено."
        )

    except ValueError:

        print("Введите число!")


# ============================================================
#                 ОЧИСТКА КОРЗИНЫ
# ============================================================

def clear_cart():

    if not cart:

        print("Корзина уже пустая!")

        return

    confirm = input(
        "Очистить корзину? (да/нет): "
    ).lower()

    if confirm == "да":

        cart.clear()

        print("Корзина очищена.")

    else:

        print("Отмена.")


# ============================================================
#                 СКИДКА
# ============================================================

def calculate_discount(total):

    if total >= 3000:

        return total * 0.15

    elif total >= 2000:

        return total * 0.10

    elif total >= 1000:

        return total * 0.05

    return 0


# ============================================================
#                 ДОСТАВКА
# ============================================================

def choose_delivery():

    title("🚚 СПОСОБ ПОЛУЧЕНИЯ")

    print("1. Самовывоз")

    print("2. Доставка")

    choice = input("Выберите: ")

    if choice == "1":

        return "Самовывоз", 0

    elif choice == "2":

        address = input("Введите адрес: ")

        return f"Доставка: {address}", 150

    else:

        print("Неверный выбор!")

        return None, 0


# ============================================================
#                 ОФОРМЛЕНИЕ ЗАКАЗА
# ============================================================

def checkout():

    global current_order_number

    if not cart:

        print("Корзина пустая!")

        return

    title("🧾 ОФОРМЛЕНИЕ ЗАКАЗА")

    name = input("Ваше имя: ")

    phone = input("Ваш телефон: ")

    delivery_type, delivery_price = choose_delivery()

    if delivery_type is None:

        return

    total = sum(
        item["price"] * item["quantity"]
        for item in cart
    )

    discount = calculate_discount(total)

    final_total = (
        total - discount + delivery_price
    )

    print(f"\nСумма блюд: {money(total)}")

    print(f"Скидка: {money(discount)}")

    print(f"Доставка: {money(delivery_price)}")

    print(f"Итого: {money(final_total)}")

    print("\n1. Наличные")

    print("2. Банковская карта")

    payment_choice = input("Способ оплаты: ")

    if payment_choice == "1":

        payment = "Наличные"

    elif payment_choice == "2":

        payment = "Банковская карта"

    else:

        print("Неверный способ оплаты!")

        return

    current_order_number += 1

    order = {

        "number": current_order_number,

        "name": name,

        "phone": phone,

        "items": cart.copy(),

        "total": final_total,

        "date": get_time(),

        "delivery": delivery_type,

        "payment": payment,

        "status": "Принят"

    }

    orders.append(order)

    restaurant_info["orders_today"] += 1

    restaurant_info["revenue"] += final_total

    print("\n" + "=" * 65)

    print("              ✅ ЗАКАЗ ОФОРМЛЕН!")

    print("=" * 65)

    print(f"Номер заказа: #{order['number']}")

    print(f"Клиент: {name}")

    print(f"Сумма: {money(final_total)}")

    print(f"Статус: {order['status']}")

    print("=" * 65)

    cart.clear()


# ============================================================
#                 ИСТОРИЯ ЗАКАЗОВ
# ============================================================

def order_history():

    title("📦 ИСТОРИЯ ЗАКАЗОВ")

    if not orders:

        print("Заказов пока нет.")

        return

    for order in orders:

        print(f"\nЗаказ #{order['number']}")

        print(f"Клиент: {order['name']}")

        print(f"Дата: {order['date']}")

        print(f"Сумма: {money(order['total'])}")

        print(f"Получение: {order['delivery']}")

        print(f"Оплата: {order['payment']}")

        print(f"Статус: {order['status']}")

        print("-" * 65)


# ============================================================
#                 БРОНИРОВАНИЕ СТОЛИКА
# ============================================================

def book_table():

    title("🪑 БРОНИРОВАНИЕ СТОЛИКА")

    name = input("Введите ваше имя: ")

    phone = input("Введите телефон: ")

    date = input(
        "Введите дату (например 20.09.2026): "
    )

    time = input(
        "Введите время (например 19:30): "
    )

    try:

        people = int(
            input("Количество людей: ")
        )

        if people <= 0:

            print("Неверное количество!")

            return

    except ValueError:

        print("Введите число!")

        return

    # Проверка формата даты
    try:

        booking_date = datetime.datetime.strptime(
            date,
            "%d.%m.%Y"
        ).date()

        today = datetime.date.today()

        if booking_date < today:

            print("Нельзя бронировать прошедшую дату!")

            return

    except ValueError:

        print(
            "Неверный формат даты! "
            "Используйте ДД.ММ.ГГГГ"
        )

        return

    # Проверка времени
    try:

        booking_time = datetime.datetime.strptime(
            time,
            "%H:%M"
        ).time()

        if booking_time < datetime.time(10, 0) \
                or booking_time > datetime.time(22, 0):

            print(
                "Ресторан работает с 10:00 до 23:00."
            )

            return

    except ValueError:

        print(
            "Неверный формат времени! "
            "Используйте ЧЧ:ММ"
        )

        return

    # Проверка количества людей
    if people > 12:

        print(
            "Для компании больше 12 человек "
            "позвоните в ресторан."
        )

        return

    # Проверка занятых столиков
    occupied_tables = [

        booking["table"]

        for booking in bookings

        if booking["date"] == date
        and booking["time"] == time

    ]

    free_tables = [

        table

        for table in range(1, 21)

        if table not in occupied_tables

    ]

    if not free_tables:

        print(
            "На это время свободных столиков нет."
        )

        return

    table_number = free_tables[0]

    booking = {

        "number": random.randint(10000, 99999),

        "name": name,

        "phone": phone,

        "date": date,

        "time": time,

        "people": people,

        "table": table_number,

        "status": "Забронирован"

    }

    bookings.append(booking)

    print("\n" + "=" * 65)

    print("       ✅ СТОЛИК УСПЕШНО ЗАБРОНИРОВАН")

    print("=" * 65)

    print(f"Номер брони: #{booking['number']}")

    print(f"Имя: {name}")

    print(f"Телефон: {phone}")

    print(f"Дата: {date}")

    print(f"Время: {time}")

    print(f"Количество людей: {people}")

    print(f"Столик №: {table_number}")

    print(f"Статус: {booking['status']}")

    print("=" * 65)


# ============================================================
#                 ПРОСМОТР БРОНИРОВАНИЙ
# ============================================================

def show_bookings():

    title("📅 ВСЕ БРОНИРОВАНИЯ")

    if not bookings:

        print("Бронирований пока нет.")

        return

    for booking in bookings:

        print(
            f"\nБронь #{booking['number']}"
        )

        print(f"Имя: {booking['name']}")

        print(f"Телефон: {booking['phone']}")

        print(f"Дата: {booking['date']}")

        print(f"Время: {booking['time']}")

        print(f"Людей: {booking['people']}")

        print(f"Столик: №{booking['table']}")

        print(f"Статус: {booking['status']}")

        print("-" * 65)


# ============================================================
#                 ОТМЕНА БРОНИРОВАНИЯ
# ============================================================

def cancel_booking():

    if not bookings:

        print("Бронирований нет.")

        return

    show_bookings()

    try:

        number = int(
            input("Введите номер брони: ")
        )

        for booking in bookings:

            if booking["number"] == number:

                booking["status"] = "Отменён"

                print("Бронирование отменено!")

                return

        print("Бронь не найдена.")

    except ValueError:

        print("Введите число!")


# ============================================================
#                 ОЦЕНКА РЕСТОРАНА
# ============================================================

def rate_restaurant():

    title("⭐ ОЦЕНКА РЕСТОРАНА")

    name = input("Ваше имя: ")

    try:

        rating = int(
            input("Оценка от 1 до 5: ")
        )

        if rating < 1 or rating > 5:

            print("Оценка должна быть от 1 до 5!")

            return

    except ValueError:

        print("Введите число!")

        return

    comment = input("Ваш комментарий: ")

    review = {

        "name": name,

        "rating": rating,

        "comment": comment,

        "date": get_time()

    }

    reviews.append(review)

    print("\nСпасибо за вашу оценку!")

    print(f"Оценка: {rating}/5")

    print(f"Комментарий: {comment}")


# ============================================================
#                 ПРОСМОТР ОТЗЫВОВ
# ============================================================

def show_reviews():

    title("⭐ ОТЗЫВЫ КЛИЕНТОВ")

    if not reviews:

        print("Отзывов пока нет.")

        return

    for review in reviews:

        print(f"\nИмя: {review['name']}")

        print(f"Оценка: {review['rating']}/5")

        print(f"Комментарий: {review['comment']}")

        print(f"Дата: {review['date']}")

        print("-" * 65)


# ============================================================
#                 ГЛАВНОЕ МЕНЮ
# ============================================================

def main_menu():

    while True:

        title("🍔 TASTY FOOD RESTAURANT 🍔")

        print("1. Посмотреть меню")

        print("2. Подробное меню")

        print("3. Поиск блюда")

        print("4. Добавить блюдо")

        print("5. Посмотреть корзину")

        print("6. Удалить блюдо")

        print("7. Очистить корзину")

        print("8. Оформить заказ")

        print("9. История заказов")

        print("10. Забронировать столик")

        print("11. Посмотреть бронирования")

        print("12. Отменить бронирование")

        print("13. Оценить ресторан")

        print("14. Посмотреть отзывы")

        print("15. Информация о ресторане")

        print("16. Выход")

        line()

        choice = input("Выберите действие: ")

        if choice == "1":

            show_menu()

        elif choice == "2":

            detailed_menu()

        elif choice == "3":

            search_food()

        elif choice == "4":

            add_to_cart()

        elif choice == "5":

            show_cart()

        elif choice == "6":

            remove_from_cart()

        elif choice == "7":

            clear_cart()

        elif choice == "8":

            checkout()

        elif choice == "9":

            order_history()

        elif choice == "10":

            book_table()

        elif choice == "11":

            show_bookings()

        elif choice == "12":

            cancel_booking()

        elif choice == "13":

            rate_restaurant()

        elif choice == "14":

            show_reviews()

        elif choice == "15":

            show_restaurant_info()

        elif choice == "16":

            print("Спасибо за посещение!")

            break

        else:

            print("Неверный выбор!")


# ============================================================
#                 ЗАПУСК ПРОГРАММЫ
# ============================================================

def main():

    print("=" * 65)

    print("        🍔 ДОБРО ПОЖАЛОВАТЬ В TASTY FOOD 🍔")

    print("=" * 65)

    print("Режим: Ресторан")

    print("Регистрация отключена.")

    print("=" * 65)

    main_menu()
101

if __name__ == "__main__":

    main()

# ============================================================
#                  🍔 TASTY FOOD RESTAURANT 🍔
# ============================================================
#                 БОЛЬШОЙ ПРОЕКТ НА PYTHON
# ============================================================

import datetime
import random


# ============================================================
#                 НАСТРОЙКИ РЕСТОРАНА
# ============================================================

RESTAURANT_NAME = "TASTY FOOD"
RESTAURANT_ADDRESS = "Бишкек, Кыргызстан"
RESTAURANT_PHONE = "+996 555 123 456"
CURRENCY = "сом"


# ============================================================
#                 ДАННЫЕ РЕСТОРАНА
# ============================================================

restaurant_info = {

    "name": RESTAURANT_NAME,

    "address": RESTAURANT_ADDRESS,

    "phone": RESTAURANT_PHONE,

    "working_hours": "10:00 - 23:00",

    "tables": 20,

    "rating": 4.8,

    "orders_today": 0,

    "revenue": 0

}


# ============================================================
#                 МЕНЮ РЕСТОРАНА
# ============================================================

menu = {

    1: {
        "name": "Пицца Маргарита",
        "price": 450,
        "category": "Пицца",
        "description": "Томатный соус, сыр, базилик"
    },

    2: {
        "name": "Пицца Пепперони",
        "price": 550,
        "category": "Пицца",
        "description": "Сыр, пепперони, томатный соус"
    },

    3: {
        "name": "Пицца Четыре сыра",
        "price": 650,
        "category": "Пицца",
        "description": "Моцарелла, чеддер, пармезан"
    },

    4: {
        "name": "Пицца Грибная",
        "price": 500,
        "category": "Пицца",
        "description": "Грибы, сыр, соус"
    },

    5: {
        "name": "Пицца Мясная",
        "price": 700,
        "category": "Пицца",
        "description": "Мясо, сыр, овощи"
    },

    6: {
        "name": "Бургер Классический",
        "price": 300,
        "category": "Бургеры",
        "description": "Котлета, салат, соус"
    },

    7: {
        "name": "Чизбургер",
        "price": 350,
        "category": "Бургеры",
        "description": "Котлета, сыр, овощи"
    },

    8: {
        "name": "Двойной бургер",
        "price": 500,
        "category": "Бургеры",
        "description": "Две котлеты, двойной сыр"
    },

    9: {
        "name": "Чикенбургер",
        "price": 320,
        "category": "Бургеры",
        "description": "Курица, салат, соус"
    },

    10: {
        "name": "Бургер BBQ",
        "price": 450,
        "category": "Бургеры",
        "description": "Мясо, BBQ соус, сыр"
    },

    11: {
        "name": "Картошка Фри",
        "price": 150,
        "category": "Закуски",
        "description": "Хрустящая картошка"
    },

    12: {
        "name": "Наггетсы",
        "price": 250,
        "category": "Закуски",
        "description": "Куриные кусочки"
    },

    13: {
        "name": "Крылышки BBQ",
        "price": 400,
        "category": "Закуски",
        "description": "Куриные крылышки"
    },

    14: {
        "name": "Луковые кольца",
        "price": 180,
        "category": "Закуски",
        "description": "Хрустящие кольца"
    },

    15: {
        "name": "Сырные палочки",
        "price": 220,
        "category": "Закуски",
        "description": "Сыр в панировке"
    },

    16: {
        "name": "Кола",
        "price": 100,
        "category": "Напитки",
        "description": "Газированный напиток"
    },

    17: {
        "name": "Спрайт",
        "price": 100,
        "category": "Напитки",
        "description": "Лимонный напиток"
    },

    18: {
        "name": "Фанта",
        "price": 100,
        "category": "Напитки",
        "description": "Апельсиновый напиток"
    },

    19: {
        "name": "Сок Апельсиновый",
        "price": 120,
        "category": "Напитки",
        "description": "Натуральный сок"
    },

    20: {
        "name": "Лимонад",
        "price": 180,
        "category": "Напитки",
        "description": "Домашний лимонад"
    },

    21: {
        "name": "Кофе",
        "price": 150,
        "category": "Напитки",
        "description": "Горячий кофе"
    },

    22: {
        "name": "Капучино",
        "price": 220,
        "category": "Напитки",
        "description": "Кофе с молоком"
    },

    23: {
        "name": "Мороженое",
        "price": 180,
        "category": "Десерты",
        "description": "Сливочное мороженое"
    },

    24: {
        "name": "Шоколадный торт",
        "price": 250,
        "category": "Десерты",
        "description": "Шоколадный десерт"
    },

    25: {
        "name": "Чизкейк",
        "price": 300,
        "category": "Десерты",
        "description": "Классический чизкейк"
    },

    26: {
        "name": "Панкейки",
        "price": 280,
        "category": "Десерты",
        "description": "Панкейки с сиропом"
    },

    27: {
        "name": "Фруктовый салат",
        "price": 250,
        "category": "Десерты",
        "description": "Свежие фрукты"
    },

    28: {
        "name": "Стейк",
        "price": 950,
        "category": "Основные блюда",
        "description": "Мясной стейк"
    },

    29: {
        "name": "Курица с рисом",
        "price": 450,
        "category": "Основные блюда",
        "description": "Курица, рис, овощи"
    },

    30: {
        "name": "Паста Карбонара",
        "price": 500,
        "category": "Основные блюда",
        "description": "Паста с соусом"
    }

}


# ============================================================
#                 ГЛОБАЛЬНЫЕ ДАННЫЕ
# ============================================================

cart = []

orders = []

bookings = []

reviews = []

current_order_number = 1000


# ============================================================
#                 ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ============================================================

def line():

    print("=" * 65)


def title(text):

    line()

    print(text.center(65))

    line()


def pause():

    input("\nНажмите Enter, чтобы продолжить...")


def get_time():

    return datetime.datetime.now().strftime(
        "%d.%m.%Y %H:%M:%S"
    )


def money(value):

    return f"{value:.2f} {CURRENCY}"


# ============================================================
#                 ИНФОРМАЦИЯ О РЕСТОРАНЕ
# ============================================================

def show_restaurant_info():

    title("🍔 ИНФОРМАЦИЯ О РЕСТОРАНЕ 🍔")

    print(f"Название: {restaurant_info['name']}")

    print(f"Адрес: {restaurant_info['address']}")

    print(f"Телефон: {restaurant_info['phone']}")

    print(f"Время работы: {restaurant_info['working_hours']}")

    print(f"Количество столиков: {restaurant_info['tables']}")

    print(f"Рейтинг: {restaurant_info['rating']}")

    print(f"Заказов сегодня: {restaurant_info['orders_today']}")

    print(f"Выручка: {money(restaurant_info['revenue'])}")


# ============================================================
#                 ПОКАЗ МЕНЮ
# ============================================================

def show_menu():

    title("🍕 МЕНЮ РЕСТОРАНА 🍕")

    for number, product in menu.items():

        print(
            f"{number:02d}. "
            f"{product['name']:<25}"
            f"{money(product['price'])}"
        )

    line()


# ============================================================
#                 ПОДРОБНОЕ МЕНЮ
# ============================================================

def detailed_menu():

    title("📋 ПОДРОБНОЕ МЕНЮ")

    for number, product in menu.items():

        print(f"\nНомер: {number}")

        print(f"Название: {product['name']}")

        print(f"Категория: {product['category']}")

        print(f"Цена: {money(product['price'])}")

        print(f"Описание: {product['description']}")

        print("-" * 65)


# ============================================================
#                 ПОИСК БЛЮДА
# ============================================================

def search_food():

    title("🔎 ПОИСК БЛЮДА")

    search = input(
        "Введите название или категорию: "
    ).lower()

    found = False

    for number, product in menu.items():

        if (
            search in product["name"].lower()
            or search in product["category"].lower()
        ):

            print(
                f"{number}. "
                f"{product['name']} — "
                f"{money(product['price'])}"
            )

            found = True

    if not found:

        print("Ничего не найдено.")


# ============================================================
#                 ДОБАВЛЕНИЕ В КОРЗИНУ
# ============================================================

def add_to_cart():

    show_menu()

    try:

        number = int(
            input("Введите номер блюда: ")
        )

        if number not in menu:

            print("Такого блюда нет!")

            return

        quantity = int(
            input("Введите количество: ")
        )

        if quantity <= 0:

            print("Количество должно быть больше нуля!")

            return

        product = menu[number]

        item = {

            "id": number,

            "name": product["name"],

            "price": product["price"],

            "quantity": quantity

        }

        cart.append(item)

        print(
            f"\n✅ {product['name']} добавлено в корзину!"
        )

        print(
            f"Сумма: {money(product['price'] * quantity)}"
        )

    except ValueError:

        print("Ошибка! Введите число.")


# ============================================================
#                 ПРОСМОТР КОРЗИНЫ
# ============================================================

def show_cart():

    title("🛒 ВАША КОРЗИНА")

    if not cart:

        print("Корзина пустая.")

        return

    total = 0

    for index, item in enumerate(cart, start=1):

        item_total = (
            item["price"] * item["quantity"]
        )

        print(
            f"{index}. {item['name']}"
        )

        print(
            f"   Количество: {item['quantity']}"
        )

        print(
            f"   Цена: {money(item['price'])}"
        )

        print(
            f"   Сумма: {money(item_total)}"
        )

        print("-" * 65)

        total += item_total

    print(f"ИТОГО: {money(total)}")


# ============================================================
#                 УДАЛЕНИЕ ИЗ КОРЗИНЫ
# ============================================================

def remove_from_cart():

    if not cart:

        print("Корзина пустая!")

        return

    show_cart()

    try:

        number = int(
            input("Введите номер позиции: ")
        )

        if number < 1 or number > len(cart):

            print("Неверный номер!")

            return

        removed = cart.pop(number - 1)

        print(
            f"❌ {removed['name']} удалено."
        )

    except ValueError:

        print("Введите число!")


# ============================================================
#                 ОЧИСТКА КОРЗИНЫ
# ============================================================

def clear_cart():

    if not cart:

        print("Корзина уже пустая!")

        return

    confirm = input(
        "Очистить корзину? (да/нет): "
    ).lower()

    if confirm == "да":

        cart.clear()

        print("Корзина очищена.")

    else:

        print("Отмена.")


# ============================================================
#                 СКИДКА
# ============================================================

def calculate_discount(total):

    if total >= 3000:

        return total * 0.15

    elif total >= 2000:

        return total * 0.10

    elif total >= 1000:

        return total * 0.05

    return 0


# ============================================================
#                 ДОСТАВКА
# ============================================================

def choose_delivery():

    title("🚚 СПОСОБ ПОЛУЧЕНИЯ")

    print("1. Самовывоз")

    print("2. Доставка")

    choice = input("Выберите: ")

    if choice == "1":

        return "Самовывоз", 0

    elif choice == "2":

        address = input("Введите адрес: ")

        return f"Доставка: {address}", 150

    else:

        print("Неверный выбор!")

        return None, 0


# ============================================================
#                 ОФОРМЛЕНИЕ ЗАКАЗА
# ============================================================

def checkout():

    global current_order_number

    if not cart:

        print("Корзина пустая!")

        return

    title("🧾 ОФОРМЛЕНИЕ ЗАКАЗА")

    name = input("Ваше имя: ")

    phone = input("Ваш телефон: ")

    delivery_type, delivery_price = choose_delivery()

    if delivery_type is None:

        return

    total = sum(
        item["price"] * item["quantity"]
        for item in cart
    )

    discount = calculate_discount(total)

    final_total = (
        total - discount + delivery_price
    )

    print(f"\nСумма блюд: {money(total)}")

    print(f"Скидка: {money(discount)}")

    print(f"Доставка: {money(delivery_price)}")

    print(f"Итого: {money(final_total)}")

    print("\n1. Наличные")

    print("2. Банковская карта")

    payment_choice = input("Способ оплаты: ")

    if payment_choice == "1":

        payment = "Наличные"

    elif payment_choice == "2":

        payment = "Банковская карта"

    else:

        print("Неверный способ оплаты!")

        return

    current_order_number += 1

    order = {

        "number": current_order_number,

        "name": name,

        "phone": phone,

        "items": cart.copy(),

        "total": final_total,

        "date": get_time(),

        "delivery": delivery_type,

        "payment": payment,

        "status": "Принят"

    }

    orders.append(order)

    restaurant_info["orders_today"] += 1

    restaurant_info["revenue"] += final_total

    print("\n" + "=" * 65)

    print("              ✅ ЗАКАЗ ОФОРМЛЕН!")

    print("=" * 65)

    print(f"Номер заказа: #{order['number']}")

    print(f"Клиент: {name}")

    print(f"Сумма: {money(final_total)}")

    print(f"Статус: {order['status']}")

    print("=" * 65)

    cart.clear()


# ============================================================
#                 ИСТОРИЯ ЗАКАЗОВ
# ============================================================

def order_history():

    title("📦 ИСТОРИЯ ЗАКАЗОВ")

    if not orders:

        print("Заказов пока нет.")

        return

    for order in orders:

        print(f"\nЗаказ #{order['number']}")

        print(f"Клиент: {order['name']}")

        print(f"Дата: {order['date']}")

        print(f"Сумма: {money(order['total'])}")

        print(f"Получение: {order['delivery']}")

        print(f"Оплата: {order['payment']}")

        print(f"Статус: {order['status']}")

        print("-" * 65)


# ============================================================
#                 БРОНИРОВАНИЕ СТОЛИКА
# ============================================================

def book_table():

    title("🪑 БРОНИРОВАНИЕ СТОЛИКА")

    name = input("Введите ваше имя: ")

    phone = input("Введите телефон: ")

    date = input(
        "Введите дату (например 20.09.2026): "
    )

    time = input(
        "Введите время (например 19:30): "
    )

    try:

        people = int(
            input("Количество людей: ")
        )

        if people <= 0:

            print("Неверное количество!")

            return

    except ValueError:

        print("Введите число!")

        return

    # Проверка формата даты
    try:

        booking_date = datetime.datetime.strptime(
            date,
            "%d.%m.%Y"
        ).date()

        today = datetime.date.today()

        if booking_date < today:

            print("Нельзя бронировать прошедшую дату!")

            return

    except ValueError:

        print(
            "Неверный формат даты! "
            "Используйте ДД.ММ.ГГГГ"
        )

        return

    # Проверка времени
    try:

        booking_time = datetime.datetime.strptime(
            time,
            "%H:%M"
        ).time()

        if booking_time < datetime.time(10, 0) \
                or booking_time > datetime.time(22, 0):

            print(
                "Ресторан работает с 10:00 до 23:00."
            )

            return

    except ValueError:

        print(
            "Неверный формат времени! "
            "Используйте ЧЧ:ММ"
        )

        return

    # Проверка количества людей
    if people > 12:

        print(
            "Для компании больше 12 человек "
            "позвоните в ресторан."
        )

        return

    # Проверка занятых столиков
    occupied_tables = [

        booking["table"]

        for booking in bookings

        if booking["date"] == date
        and booking["time"] == time

    ]

    free_tables = [

        table

        for table in range(1, 21)

        if table not in occupied_tables

    ]

    if not free_tables:

        print(
            "На это время свободных столиков нет."
        )

        return

    table_number = free_tables[0]

    booking = {

        "number": random.randint(10000, 99999),

        "name": name,

        "phone": phone,

        "date": date,

        "time": time,

        "people": people,

        "table": table_number,

        "status": "Забронирован"

    }

    bookings.append(booking)

    print("\n" + "=" * 65)

    print("       ✅ СТОЛИК УСПЕШНО ЗАБРОНИРОВАН")

    print("=" * 65)

    print(f"Номер брони: #{booking['number']}")

    print(f"Имя: {name}")

    print(f"Телефон: {phone}")

    print(f"Дата: {date}")

    print(f"Время: {time}")

    print(f"Количество людей: {people}")

    print(f"Столик №: {table_number}")

    print(f"Статус: {booking['status']}")

    print("=" * 65)


# ============================================================
#                 ПРОСМОТР БРОНИРОВАНИЙ
# ============================================================

def show_bookings():

    title("📅 ВСЕ БРОНИРОВАНИЯ")

    if not bookings:

        print("Бронирований пока нет.")

        return

    for booking in bookings:

        print(
            f"\nБронь #{booking['number']}"
        )

        print(f"Имя: {booking['name']}")

        print(f"Телефон: {booking['phone']}")

        print(f"Дата: {booking['date']}")

        print(f"Время: {booking['time']}")

        print(f"Людей: {booking['people']}")

        print(f"Столик: №{booking['table']}")

        print(f"Статус: {booking['status']}")

        print("-" * 65)


# ============================================================
#                 ОТМЕНА БРОНИРОВАНИЯ
# ============================================================

def cancel_booking():

    if not bookings:

        print("Бронирований нет.")

        return

    show_bookings()

    try:

        number = int(
            input("Введите номер брони: ")
        )

        for booking in bookings:

            if booking["number"] == number:

                booking["status"] = "Отменён"

                print("Бронирование отменено!")

                return

        print("Бронь не найдена.")

    except ValueError:

        print("Введите число!")


# ============================================================
#                 ОЦЕНКА РЕСТОРАНА
# ============================================================

def rate_restaurant():

    title("⭐ ОЦЕНКА РЕСТОРАНА")

    name = input("Ваше имя: ")

    try:

        rating = int(
            input("Оценка от 1 до 5: ")
        )

        if rating < 1 or rating > 5:

            print("Оценка должна быть от 1 до 5!")

            return

    except ValueError:

        print("Введите число!")

        return

    comment = input("Ваш комментарий: ")

    review = {

        "name": name,

        "rating": rating,

        "comment": comment,

        "date": get_time()

    }

    reviews.append(review)

    print("\nСпасибо за вашу оценку!")

    print(f"Оценка: {rating}/5")

    print(f"Комментарий: {comment}")


# ============================================================
#                 ПРОСМОТР ОТЗЫВОВ
# ============================================================

def show_reviews():

    title("⭐ ОТЗЫВЫ КЛИЕНТОВ")

    if not reviews:

        print("Отзывов пока нет.")

        return

    for review in reviews:

        print(f"\nИмя: {review['name']}")

        print(f"Оценка: {review['rating']}/5")

        print(f"Комментарий: {review['comment']}")

        print(f"Дата: {review['date']}")

        print("-" * 65)


# ============================================================
#                 ГЛАВНОЕ МЕНЮ
# ============================================================

def main_menu():

    while True:

        title("🍔 TASTY FOOD RESTAURANT 🍔")

        print("1. Посмотреть меню")

        print("2. Подробное меню")

        print("3. Поиск блюда")

        print("4. Добавить блюдо")

        print("5. Посмотреть корзину")

        print("6. Удалить блюдо")

        print("7. Очистить корзину")

        print("8. Оформить заказ")

        print("9. История заказов")

        print("10. Забронировать столик")

        print("11. Посмотреть бронирования")

        print("12. Отменить бронирование")

        print("13. Оценить ресторан")

        print("14. Посмотреть отзывы")

        print("15. Информация о ресторане")

        print("16. Выход")

        line()

        choice = input("Выберите действие: ")

        if choice == "1":

            show_menu()

        elif choice == "2":

            detailed_menu()

        elif choice == "3":

            search_food()

        elif choice == "4":

            add_to_cart()

        elif choice == "5":

            show_cart()

        elif choice == "6":

            remove_from_cart()

        elif choice == "7":

            clear_cart()

        elif choice == "8":

            checkout()

        elif choice == "9":

            order_history()

        elif choice == "10":

            book_table()

        elif choice == "11":

            show_bookings()

        elif choice == "12":

            cancel_booking()

        elif choice == "13":

            rate_restaurant()

        elif choice == "14":

            show_reviews()

        elif choice == "15":

            show_restaurant_info()

        elif choice == "16":

            print("Спасибо за посещение!")

            break

        else:

            print("Неверный выбор!")


# ============================================================
#                 ЗАПУСК ПРОГРАММЫ
# ============================================================

def main():

    print("=" * 65)

    print("        🍔 ДОБРО ПОЖАЛОВАТЬ В TASTY FOOD 🍔")

    print("=" * 65)

    print("Режим: Ресторан")

    print("Регистрация отключена.")

    print("=" * 65)

    main_menu()


if __name__ == "__main__":

    main()

# ============================================================
#                  🍔 TASTY FOOD RESTAURANT 🍔
# ============================================================
#                 БОЛЬШОЙ ПРОЕКТ НА PYTHON
# ============================================================

import datetime
import random


# ============================================================
#                 НАСТРОЙКИ РЕСТОРАНА
# ============================================================

RESTAURANT_NAME = "TASTY FOOD"
RESTAURANT_ADDRESS = "Бишкек, Кыргызстан"
RESTAURANT_PHONE = "+996 555 123 456"
CURRENCY = "сом"


# ============================================================
#                 ДАННЫЕ РЕСТОРАНА
# ============================================================

restaurant_info = {

    "name": RESTAURANT_NAME,

    "address": RESTAURANT_ADDRESS,

    "phone": RESTAURANT_PHONE,

    "working_hours": "10:00 - 23:00",

    "tables": 20,

    "rating": 4.8,

    "orders_today": 0,

    "revenue": 0

}


# ============================================================
#                 МЕНЮ РЕСТОРАНА
# ============================================================

menu = {

    1: {
        "name": "Пицца Маргарита",
        "price": 450,
        "category": "Пицца",
        "description": "Томатный соус, сыр, базилик"
    },

    2: {
        "name": "Пицца Пепперони",
        "price": 550,
        "category": "Пицца",
        "description": "Сыр, пепперони, томатный соус"
    },

    3: {
        "name": "Пицца Четыре сыра",
        "price": 650,
        "category": "Пицца",
        "description": "Моцарелла, чеддер, пармезан"
    },

    4: {
        "name": "Пицца Грибная",
        "price": 500,
        "category": "Пицца",
        "description": "Грибы, сыр, соус"
    },

    5: {
        "name": "Пицца Мясная",
        "price": 700,
        "category": "Пицца",
        "description": "Мясо, сыр, овощи"
    },

    6: {
        "name": "Бургер Классический",
        "price": 300,
        "category": "Бургеры",
        "description": "Котлета, салат, соус"
    },

    7: {
        "name": "Чизбургер",
        "price": 350,
        "category": "Бургеры",
        "description": "Котлета, сыр, овощи"
    },

    8: {
        "name": "Двойной бургер",
        "price": 500,
        "category": "Бургеры",
        "description": "Две котлеты, двойной сыр"
    },

    9: {
        "name": "Чикенбургер",
        "price": 320,
        "category": "Бургеры",
        "description": "Курица, салат, соус"
    },

    10: {
        "name": "Бургер BBQ",
        "price": 450,
        "category": "Бургеры",
        "description": "Мясо, BBQ соус, сыр"
    },

    11: {
        "name": "Картошка Фри",
        "price": 150,
        "category": "Закуски",
        "description": "Хрустящая картошка"
    },

    12: {
        "name": "Наггетсы",
        "price": 250,
        "category": "Закуски",
        "description": "Куриные кусочки"
    },

    13: {
        "name": "Крылышки BBQ",
        "price": 400,
        "category": "Закуски",
        "description": "Куриные крылышки"
    },

    14: {
        "name": "Луковые кольца",
        "price": 180,
        "category": "Закуски",
        "description": "Хрустящие кольца"
    },

    15: {
        "name": "Сырные палочки",
        "price": 220,
        "category": "Закуски",
        "description": "Сыр в панировке"
    },

    16: {
        "name": "Кола",
        "price": 100,
        "category": "Напитки",
        "description": "Газированный напиток"
    },

    17: {
        "name": "Спрайт",
        "price": 100,
        "category": "Напитки",
        "description": "Лимонный напиток"
    },

    18: {
        "name": "Фанта",
        "price": 100,
        "category": "Напитки",
        "description": "Апельсиновый напиток"
    },

    19: {
        "name": "Сок Апельсиновый",
        "price": 120,
        "category": "Напитки",
        "description": "Натуральный сок"
    },

    20: {
        "name": "Лимонад",
        "price": 180,
        "category": "Напитки",
        "description": "Домашний лимонад"
    },

    21: {
        "name": "Кофе",
        "price": 150,
        "category": "Напитки",
        "description": "Горячий кофе"
    },

    22: {
        "name": "Капучино",
        "price": 220,
        "category": "Напитки",
        "description": "Кофе с молоком"
    },

    23: {
        "name": "Мороженое",
        "price": 180,
        "category": "Десерты",
        "description": "Сливочное мороженое"
    },

    24: {
        "name": "Шоколадный торт",
        "price": 250,
        "category": "Десерты",
        "description": "Шоколадный десерт"
    },

    25: {
        "name": "Чизкейк",
        "price": 300,
        "category": "Десерты",
        "description": "Классический чизкейк"
    },

    26: {
        "name": "Панкейки",
        "price": 280,
        "category": "Десерты",
        "description": "Панкейки с сиропом"
    },

    27: {
        "name": "Фруктовый салат",
        "price": 250,
        "category": "Десерты",
        "description": "Свежие фрукты"
    },

    28: {
        "name": "Стейк",
        "price": 950,
        "category": "Основные блюда",
        "description": "Мясной стейк"
    },

    29: {
        "name": "Курица с рисом",
        "price": 450,
        "category": "Основные блюда",
        "description": "Курица, рис, овощи"
    },

    30: {
        "name": "Паста Карбонара",
        "price": 500,
        "category": "Основные блюда",
        "description": "Паста с соусом"
    }

}


# ============================================================
#                 ГЛОБАЛЬНЫЕ ДАННЫЕ
# ============================================================

cart = []

orders = []

bookings = []

reviews = []

current_order_number = 1000


# ============================================================
#                 ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ============================================================

def line():

    print("=" * 65)


def title(text):

    line()

    print(text.center(65))

    line()


def pause():

    input("\nНажмите Enter, чтобы продолжить...")


def get_time():

    return datetime.datetime.now().strftime(
        "%d.%m.%Y %H:%M:%S"
    )


def money(value):

    return f"{value:.2f} {CURRENCY}"


# ============================================================
#                 ИНФОРМАЦИЯ О РЕСТОРАНЕ
# ============================================================

def show_restaurant_info():

    title("🍔 ИНФОРМАЦИЯ О РЕСТОРАНЕ 🍔")

    print(f"Название: {restaurant_info['name']}")

    print(f"Адрес: {restaurant_info['address']}")

    print(f"Телефон: {restaurant_info['phone']}")

    print(f"Время работы: {restaurant_info['working_hours']}")

    print(f"Количество столиков: {restaurant_info['tables']}")

    print(f"Рейтинг: {restaurant_info['rating']}")

    print(f"Заказов сегодня: {restaurant_info['orders_today']}")

    print(f"Выручка: {money(restaurant_info['revenue'])}")


# ============================================================
#                 ПОКАЗ МЕНЮ
# ============================================================

def show_menu():

    title("🍕 МЕНЮ РЕСТОРАНА 🍕")

    for number, product in menu.items():

        print(
            f"{number:02d}. "
            f"{product['name']:<25}"
            f"{money(product['price'])}"
        )

    line()


# ============================================================
#                 ПОДРОБНОЕ МЕНЮ
# ============================================================

def detailed_menu():

    title("📋 ПОДРОБНОЕ МЕНЮ")

    for number, product in menu.items():

        print(f"\nНомер: {number}")

        print(f"Название: {product['name']}")

        print(f"Категория: {product['category']}")

        print(f"Цена: {money(product['price'])}")

        print(f"Описание: {product['description']}")

        print("-" * 65)


# ============================================================
#                 ПОИСК БЛЮДА
# ============================================================

def search_food():

    title("🔎 ПОИСК БЛЮДА")

    search = input(
        "Введите название или категорию: "
    ).lower()

    found = False

    for number, product in menu.items():

        if (
            search in product["name"].lower()
            or search in product["category"].lower()
        ):

            print(
                f"{number}. "
                f"{product['name']} — "
                f"{money(product['price'])}"
            )

            found = True

    if not found:

        print("Ничего не найдено.")


# ============================================================
#                 ДОБАВЛЕНИЕ В КОРЗИНУ
# ============================================================

def add_to_cart():

    show_menu()

    try:

        number = int(
            input("Введите номер блюда: ")
        )

        if number not in menu:

            print("Такого блюда нет!")

            return

        quantity = int(
            input("Введите количество: ")
        )

        if quantity <= 0:

            print("Количество должно быть больше нуля!")

            return

        product = menu[number]

        item = {

            "id": number,

            "name": product["name"],

            "price": product["price"],

            "quantity": quantity

        }

        cart.append(item)

        print(
            f"\n✅ {product['name']} добавлено в корзину!"
        )

        print(
            f"Сумма: {money(product['price'] * quantity)}"
        )

    except ValueError:

        print("Ошибка! Введите число.")


# ============================================================
#                 ПРОСМОТР КОРЗИНЫ
# ============================================================

def show_cart():

    title("🛒 ВАША КОРЗИНА")

    if not cart:

        print("Корзина пустая.")

        return

    total = 0

    for index, item in enumerate(cart, start=1):

        item_total = (
            item["price"] * item["quantity"]
        )

        print(
            f"{index}. {item['name']}"
        )

        print(
            f"   Количество: {item['quantity']}"
        )

        print(
            f"   Цена: {money(item['price'])}"
        )

        print(
            f"   Сумма: {money(item_total)}"
        )

        print("-" * 65)

        total += item_total

    print(f"ИТОГО: {money(total)}")


# ============================================================
#                 УДАЛЕНИЕ ИЗ КОРЗИНЫ
# ============================================================

def remove_from_cart():

    if not cart:

        print("Корзина пустая!")

        return

    show_cart()

    try:

        number = int(
            input("Введите номер позиции: ")
        )

        if number < 1 or number > len(cart):

            print("Неверный номер!")

            return

        removed = cart.pop(number - 1)

        print(
            f"❌ {removed['name']} удалено."
        )

    except ValueError:

        print("Введите число!")


# ============================================================
#                 ОЧИСТКА КОРЗИНЫ
# ============================================================

def clear_cart():

    if not cart:

        print("Корзина уже пустая!")

        return

    confirm = input(
        "Очистить корзину? (да/нет): "
    ).lower()

    if confirm == "да":

        cart.clear()

        print("Корзина очищена.")

    else:

        print("Отмена.")


# ============================================================
#                 СКИДКА
# ============================================================

def calculate_discount(total):

    if total >= 3000:

        return total * 0.15

    elif total >= 2000:

        return total * 0.10

    elif total >= 1000:

        return total * 0.05

    return 0


# ============================================================
#                 ДОСТАВКА
# ============================================================

def choose_delivery():

    title("🚚 СПОСОБ ПОЛУЧЕНИЯ")

    print("1. Самовывоз")

    print("2. Доставка")

    choice = input("Выберите: ")

    if choice == "1":

        return "Самовывоз", 0

    elif choice == "2":

        address = input("Введите адрес: ")

        return f"Доставка: {address}", 150

    else:

        print("Неверный выбор!")

        return None, 0


# ============================================================
#                 ОФОРМЛЕНИЕ ЗАКАЗА
# ============================================================

def checkout():

    global current_order_number

    if not cart:

        print("Корзина пустая!")

        return

    title("🧾 ОФОРМЛЕНИЕ ЗАКАЗА")

    name = input("Ваше имя: ")

    phone = input("Ваш телефон: ")

    delivery_type, delivery_price = choose_delivery()

    if delivery_type is None:

        return

    total = sum(
        item["price"] * item["quantity"]
        for item in cart
    )

    discount = calculate_discount(total)

    final_total = (
        total - discount + delivery_price
    )

    print(f"\nСумма блюд: {money(total)}")

    print(f"Скидка: {money(discount)}")

    print(f"Доставка: {money(delivery_price)}")

    print(f"Итого: {money(final_total)}")

    print("\n1. Наличные")

    print("2. Банковская карта")

    payment_choice = input("Способ оплаты: ")

    if payment_choice == "1":

        payment = "Наличные"

    elif payment_choice == "2":

        payment = "Банковская карта"

    else:

        print("Неверный способ оплаты!")

        return

    current_order_number += 1

    order = {

        "number": current_order_number,

        "name": name,

        "phone": phone,

        "items": cart.copy(),

        "total": final_total,

        "date": get_time(),

        "delivery": delivery_type,

        "payment": payment,

        "status": "Принят"

    }

    orders.append(order)

    restaurant_info["orders_today"] += 1

    restaurant_info["revenue"] += final_total

    print("\n" + "=" * 65)

    print("              ✅ ЗАКАЗ ОФОРМЛЕН!")

    print("=" * 65)

    print(f"Номер заказа: #{order['number']}")

    print(f"Клиент: {name}")

    print(f"Сумма: {money(final_total)}")

    print(f"Статус: {order['status']}")

    print("=" * 65)

    cart.clear()


# ============================================================
#                 ИСТОРИЯ ЗАКАЗОВ
# ============================================================

def order_history():

    title("📦 ИСТОРИЯ ЗАКАЗОВ")

    if not orders:

        print("Заказов пока нет.")

        return

    for order in orders:

        print(f"\nЗаказ #{order['number']}")

        print(f"Клиент: {order['name']}")

        print(f"Дата: {order['date']}")

        print(f"Сумма: {money(order['total'])}")

        print(f"Получение: {order['delivery']}")

        print(f"Оплата: {order['payment']}")

        print(f"Статус: {order['status']}")

        print("-" * 65)


# ============================================================
#                 БРОНИРОВАНИЕ СТОЛИКА
# ============================================================

def book_table():

    title("🪑 БРОНИРОВАНИЕ СТОЛИКА")

    name = input("Введите ваше имя: ")

    phone = input("Введите телефон: ")

    date = input(
        "Введите дату (например 20.09.2026): "
    )

    time = input(
        "Введите время (например 19:30): "
    )

    try:

        people = int(
            input("Количество людей: ")
        )

        if people <= 0:

            print("Неверное количество!")

            return

    except ValueError:

        print("Введите число!")

        return

    # Проверка формата даты
    try:

        booking_date = datetime.datetime.strptime(
            date,
            "%d.%m.%Y"
        ).date()

        today = datetime.date.today()

        if booking_date < today:

            print("Нельзя бронировать прошедшую дату!")

            return

    except ValueError:

        print(
            "Неверный формат даты! "
            "Используйте ДД.ММ.ГГГГ"
        )

        return

    # Проверка времени
    try:

        booking_time = datetime.datetime.strptime(
            time,
            "%H:%M"
        ).time()

        if booking_time < datetime.time(10, 0) \
                or booking_time > datetime.time(22, 0):

            print(
                "Ресторан работает с 10:00 до 23:00."
            )

            return

    except ValueError:

        print(
            "Неверный формат времени! "
            "Используйте ЧЧ:ММ"
        )

        return

    # Проверка количества людей
    if people > 12:

        print(
            "Для компании больше 12 человек "
            "позвоните в ресторан."
        )

        return

    # Проверка занятых столиков
    occupied_tables = [

        booking["table"]

        for booking in bookings

        if booking["date"] == date
        and booking["time"] == time

    ]

    free_tables = [

        table

        for table in range(1, 21)

        if table not in occupied_tables

    ]

    if not free_tables:

        print(
            "На это время свободных столиков нет."
        )

        return

    table_number = free_tables[0]

    booking = {

        "number": random.randint(10000, 99999),

        "name": name,

        "phone": phone,

        "date": date,

        "time": time,

        "people": people,

        "table": table_number,

        "status": "Забронирован"

    }

    bookings.append(booking)

    print("\n" + "=" * 65)

    print("       ✅ СТОЛИК УСПЕШНО ЗАБРОНИРОВАН")

    print("=" * 65)

    print(f"Номер брони: #{booking['number']}")

    print(f"Имя: {name}")

    print(f"Телефон: {phone}")

    print(f"Дата: {date}")

    print(f"Время: {time}")

    print(f"Количество людей: {people}")

    print(f"Столик №: {table_number}")

    print(f"Статус: {booking['status']}")

    print("=" * 65)


# ============================================================
#                 ПРОСМОТР БРОНИРОВАНИЙ
# ============================================================

def show_bookings():

    title("📅 ВСЕ БРОНИРОВАНИЯ")

    if not bookings:

        print("Бронирований пока нет.")

        return

    for booking in bookings:

        print(
            f"\nБронь #{booking['number']}"
        )

        print(f"Имя: {booking['name']}")

        print(f"Телефон: {booking['phone']}")

        print(f"Дата: {booking['date']}")

        print(f"Время: {booking['time']}")

        print(f"Людей: {booking['people']}")

        print(f"Столик: №{booking['table']}")

        print(f"Статус: {booking['status']}")

        print("-" * 65)


# ============================================================
#                 ОТМЕНА БРОНИРОВАНИЯ
# ============================================================

def cancel_booking():

    if not bookings:

        print("Бронирований нет.")

        return

    show_bookings()

    try:

        number = int(
            input("Введите номер брони: ")
        )

        for booking in bookings:

            if booking["number"] == number:

                booking["status"] = "Отменён"

                print("Бронирование отменено!")

                return

        print("Бронь не найдена.")

    except ValueError:

        print("Введите число!")


# ============================================================
#                 ОЦЕНКА РЕСТОРАНА
# ============================================================

def rate_restaurant():

    title("⭐ ОЦЕНКА РЕСТОРАНА")

    name = input("Ваше имя: ")

    try:

        rating = int(
            input("Оценка от 1 до 5: ")
        )

        if rating < 1 or rating > 5:

            print("Оценка должна быть от 1 до 5!")

            return

    except ValueError:

        print("Введите число!")

        return

    comment = input("Ваш комментарий: ")

    review = {

        "name": name,

        "rating": rating,

        "comment": comment,

        "date": get_time()

    }

    reviews.append(review)

    print("\nСпасибо за вашу оценку!")

    print(f"Оценка: {rating}/5")

    print(f"Комментарий: {comment}")


# ============================================================
#                 ПРОСМОТР ОТЗЫВОВ
# ============================================================

def show_reviews():

    title("⭐ ОТЗЫВЫ КЛИЕНТОВ")

    if not reviews:

        print("Отзывов пока нет.")

        return

    for review in reviews:

        print(f"\nИмя: {review['name']}")

        print(f"Оценка: {review['rating']}/5")

        print(f"Комментарий: {review['comment']}")

        print(f"Дата: {review['date']}")

        print("-" * 65)


# ============================================================
#                 ГЛАВНОЕ МЕНЮ
# ============================================================

def main_menu():

    while True:

        title("🍔 TASTY FOOD RESTAURANT 🍔")

        print("1. Посмотреть меню")

        print("2. Подробное меню")

        print("3. Поиск блюда")

        print("4. Добавить блюдо")

        print("5. Посмотреть корзину")

        print("6. Удалить блюдо")

        print("7. Очистить корзину")

        print("8. Оформить заказ")

        print("9. История заказов")

        print("10. Забронировать столик")

        print("11. Посмотреть бронирования")

        print("12. Отменить бронирование")

        print("13. Оценить ресторан")

        print("14. Посмотреть отзывы")

        print("15. Информация о ресторане")

        print("16. Выход")

        line()

        choice = input("Выберите действие: ")

        if choice == "1":

            show_menu()

        elif choice == "2":

            detailed_menu()

        elif choice == "3":

            search_food()

        elif choice == "4":

            add_to_cart()

        elif choice == "5":

            show_cart()

        elif choice == "6":

            remove_from_cart()

        elif choice == "7":

            clear_cart()

        elif choice == "8":

            checkout()

        elif choice == "9":

            order_history()

        elif choice == "10":

            book_table()

        elif choice == "11":

            show_bookings()

        elif choice == "12":

            cancel_booking()

        elif choice == "13":

            rate_restaurant()

        elif choice == "14":

            show_reviews()

        elif choice == "15":

            show_restaurant_info()

        elif choice == "16":

            print("Спасибо за посещение!")

            break

        else:

            print("Неверный выбор!")


# ============================================================
#                 ЗАПУСК ПРОГРАММЫ
# ============================================================

def main():

    print("=" * 65)

    print("        🍔 ДОБРО ПОЖАЛОВАТЬ В TASTY FOOD 🍔")

    print("=" * 65)

    print("Режим: Ресторан")

    print("Регистрация отключена.")

    print("=" * 65)

    main_menu()


if __name__ == "__main__":

    main()

# ============================================================
#                  🍔 TASTY FOOD RESTAURANT 🍔
# ============================================================
#                 БОЛЬШОЙ ПРОЕКТ НА PYTHON
# ============================================================

import datetime
import random


# ============================================================
#                 НАСТРОЙКИ РЕСТОРАНА
# ============================================================

RESTAURANT_NAME = "TASTY FOOD"
RESTAURANT_ADDRESS = "Бишкек, Кыргызстан"
RESTAURANT_PHONE = "+996 555 123 456"
CURRENCY = "сом"


# ============================================================
#                 ДАННЫЕ РЕСТОРАНА
# ============================================================

restaurant_info = {

    "name": RESTAURANT_NAME,

    "address": RESTAURANT_ADDRESS,

    "phone": RESTAURANT_PHONE,

    "working_hours": "10:00 - 23:00",

    "tables": 20,

    "rating": 4.8,

    "orders_today": 0,

    "revenue": 0

}


# ============================================================
#                 МЕНЮ РЕСТОРАНА
# ============================================================

menu = {

    1: {
        "name": "Пицца Маргарита",
        "price": 450,
        "category": "Пицца",
        "description": "Томатный соус, сыр, базилик"
    },

    2: {
        "name": "Пицца Пепперони",
        "price": 550,
        "category": "Пицца",
        "description": "Сыр, пепперони, томатный соус"
    },

    3: {
        "name": "Пицца Четыре сыра",
        "price": 650,
        "category": "Пицца",
        "description": "Моцарелла, чеддер, пармезан"
    },

    4: {
        "name": "Пицца Грибная",
        "price": 500,
        "category": "Пицца",
        "description": "Грибы, сыр, соус"
    },

    5: {
        "name": "Пицца Мясная",
        "price": 700,
        "category": "Пицца",
        "description": "Мясо, сыр, овощи"
    },

    6: {
        "name": "Бургер Классический",
        "price": 300,
        "category": "Бургеры",
        "description": "Котлета, салат, соус"
    },

    7: {
        "name": "Чизбургер",
        "price": 350,
        "category": "Бургеры",
        "description": "Котлета, сыр, овощи"
    },

    8: {
        "name": "Двойной бургер",
        "price": 500,
        "category": "Бургеры",
        "description": "Две котлеты, двойной сыр"
    },

    9: {
        "name": "Чикенбургер",
        "price": 320,
        "category": "Бургеры",
        "description": "Курица, салат, соус"
    },

    10: {
        "name": "Бургер BBQ",
        "price": 450,
        "category": "Бургеры",
        "description": "Мясо, BBQ соус, сыр"
    },

    11: {
        "name": "Картошка Фри",
        "price": 150,
        "category": "Закуски",
        "description": "Хрустящая картошка"
    },

    12: {
        "name": "Наггетсы",
        "price": 250,
        "category": "Закуски",
        "description": "Куриные кусочки"
    },

    13: {
        "name": "Крылышки BBQ",
        "price": 400,
        "category": "Закуски",
        "description": "Куриные крылышки"
    },

    14: {
        "name": "Луковые кольца",
        "price": 180,
        "category": "Закуски",
        "description": "Хрустящие кольца"
    },

    15: {
        "name": "Сырные палочки",
        "price": 220,
        "category": "Закуски",
        "description": "Сыр в панировке"
    },

    16: {
        "name": "Кола",
        "price": 100,
        "category": "Напитки",
        "description": "Газированный напиток"
    },

    17: {
        "name": "Спрайт",
        "price": 100,
        "category": "Напитки",
        "description": "Лимонный напиток"
    },

    18: {
        "name": "Фанта",
        "price": 100,
        "category": "Напитки",
        "description": "Апельсиновый напиток"
    },

    19: {
        "name": "Сок Апельсиновый",
        "price": 120,
        "category": "Напитки",
        "description": "Натуральный сок"
    },

    20: {
        "name": "Лимонад",
        "price": 180,
        "category": "Напитки",
        "description": "Домашний лимонад"
    },

    21: {
        "name": "Кофе",
        "price": 150,
        "category": "Напитки",
        "description": "Горячий кофе"
    },

    22: {
        "name": "Капучино",
        "price": 220,
        "category": "Напитки",
        "description": "Кофе с молоком"
    },

    23: {
        "name": "Мороженое",
        "price": 180,
        "category": "Десерты",
        "description": "Сливочное мороженое"
    },

    24: {
        "name": "Шоколадный торт",
        "price": 250,
        "category": "Десерты",
        "description": "Шоколадный десерт"
    },

    25: {
        "name": "Чизкейк",
        "price": 300,
        "category": "Десерты",
        "description": "Классический чизкейк"
    },

    26: {
        "name": "Панкейки",
        "price": 280,
        "category": "Десерты",
        "description": "Панкейки с сиропом"
    },

    27: {
        "name": "Фруктовый салат",
        "price": 250,
        "category": "Десерты",
        "description": "Свежие фрукты"
    },

    28: {
        "name": "Стейк",
        "price": 950,
        "category": "Основные блюда",
        "description": "Мясной стейк"
    },

    29: {
        "name": "Курица с рисом",
        "price": 450,
        "category": "Основные блюда",
        "description": "Курица, рис, овощи"
    },

    30: {
        "name": "Паста Карбонара",
        "price": 500,
        "category": "Основные блюда",
        "description": "Паста с соусом"
    }

}


# ============================================================
#                 ГЛОБАЛЬНЫЕ ДАННЫЕ
# ============================================================

cart = []

orders = []

bookings = []

reviews = []

current_order_number = 1000


# ============================================================
#                 ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ============================================================

def line():

    print("=" * 65)


def title(text):

    line()

    print(text.center(65))

    line()


def pause():

    input("\nНажмите Enter, чтобы продолжить...")


def get_time():

    return datetime.datetime.now().strftime(
        "%d.%m.%Y %H:%M:%S"
    )


def money(value):

    return f"{value:.2f} {CURRENCY}"


# ============================================================
#                 ИНФОРМАЦИЯ О РЕСТОРАНЕ
# ============================================================

def show_restaurant_info():

    title("🍔 ИНФОРМАЦИЯ О РЕСТОРАНЕ 🍔")

    print(f"Название: {restaurant_info['name']}")

    print(f"Адрес: {restaurant_info['address']}")

    print(f"Телефон: {restaurant_info['phone']}")

    print(f"Время работы: {restaurant_info['working_hours']}")

    print(f"Количество столиков: {restaurant_info['tables']}")

    print(f"Рейтинг: {restaurant_info['rating']}")

    print(f"Заказов сегодня: {restaurant_info['orders_today']}")

    print(f"Выручка: {money(restaurant_info['revenue'])}")


# ============================================================
#                 ПОКАЗ МЕНЮ
# ============================================================

def show_menu():

    title("🍕 МЕНЮ РЕСТОРАНА 🍕")

    for number, product in menu.items():

        print(
            f"{number:02d}. "
            f"{product['name']:<25}"
            f"{money(product['price'])}"
        )

    line()


# ============================================================
#                 ПОДРОБНОЕ МЕНЮ
# ============================================================

def detailed_menu():

    title("📋 ПОДРОБНОЕ МЕНЮ")

    for number, product in menu.items():

        print(f"\nНомер: {number}")

        print(f"Название: {product['name']}")

        print(f"Категория: {product['category']}")

        print(f"Цена: {money(product['price'])}")

        print(f"Описание: {product['description']}")

        print("-" * 65)


# ============================================================
#                 ПОИСК БЛЮДА
# ============================================================

def search_food():

    title("🔎 ПОИСК БЛЮДА")

    search = input(
        "Введите название или категорию: "
    ).lower()

    found = False

    for number, product in menu.items():

        if (
            search in product["name"].lower()
            or search in product["category"].lower()
        ):

            print(
                f"{number}. "
                f"{product['name']} — "
                f"{money(product['price'])}"
            )

            found = True

    if not found:

        print("Ничего не найдено.")


# ============================================================
#                 ДОБАВЛЕНИЕ В КОРЗИНУ
# ============================================================

def add_to_cart():

    show_menu()

    try:

        number = int(
            input("Введите номер блюда: ")
        )

        if number not in menu:

            print("Такого блюда нет!")

            return

        quantity = int(
            input("Введите количество: ")
        )

        if quantity <= 0:

            print("Количество должно быть больше нуля!")

            return

        product = menu[number]

        item = {

            "id": number,

            "name": product["name"],

            "price": product["price"],

            "quantity": quantity

        }

        cart.append(item)

        print(
            f"\n✅ {product['name']} добавлено в корзину!"
        )

        print(
            f"Сумма: {money(product['price'] * quantity)}"
        )

    except ValueError:

        print("Ошибка! Введите число.")


# ============================================================
#                 ПРОСМОТР КОРЗИНЫ
# ============================================================

def show_cart():

    title("🛒 ВАША КОРЗИНА")

    if not cart:

        print("Корзина пустая.")

        return

    total = 0

    for index, item in enumerate(cart, start=1):

        item_total = (
            item["price"] * item["quantity"]
        )

        print(
            f"{index}. {item['name']}"
        )

        print(
            f"   Количество: {item['quantity']}"
        )

        print(
            f"   Цена: {money(item['price'])}"
        )

        print(
            f"   Сумма: {money(item_total)}"
        )

        print("-" * 65)

        total += item_total

    print(f"ИТОГО: {money(total)}")


# ============================================================
#                 УДАЛЕНИЕ ИЗ КОРЗИНЫ
# ============================================================

def remove_from_cart():

    if not cart:

        print("Корзина пустая!")

        return

    show_cart()

    try:

        number = int(
            input("Введите номер позиции: ")
        )

        if number < 1 or number > len(cart):

            print("Неверный номер!")

            return

        removed = cart.pop(number - 1)

        print(
            f"❌ {removed['name']} удалено."
        )

    except ValueError:

        print("Введите число!")


# ============================================================
#                 ОЧИСТКА КОРЗИНЫ
# ============================================================

def clear_cart():

    if not cart:

        print("Корзина уже пустая!")

        return

    confirm = input(
        "Очистить корзину? (да/нет): "
    ).lower()

    if confirm == "да":

        cart.clear()

        print("Корзина очищена.")

    else:

        print("Отмена.")


# ============================================================
#                 СКИДКА
# ============================================================

def calculate_discount(total):

    if total >= 3000:

        return total * 0.15

    elif total >= 2000:

        return total * 0.10

    elif total >= 1000:

        return total * 0.05

    return 0


# ============================================================
#                 ДОСТАВКА
# ============================================================

def choose_delivery():

    title("🚚 СПОСОБ ПОЛУЧЕНИЯ")

    print("1. Самовывоз")

    print("2. Доставка")

    choice = input("Выберите: ")

    if choice == "1":

        return "Самовывоз", 0

    elif choice == "2":

        address = input("Введите адрес: ")

        return f"Доставка: {address}", 150

    else:

        print("Неверный выбор!")

        return None, 0


# ============================================================
#                 ОФОРМЛЕНИЕ ЗАКАЗА
# ============================================================

def checkout():

    global current_order_number

    if not cart:

        print("Корзина пустая!")

        return

    title("🧾 ОФОРМЛЕНИЕ ЗАКАЗА")

    name = input("Ваше имя: ")

    phone = input("Ваш телефон: ")

    delivery_type, delivery_price = choose_delivery()

    if delivery_type is None:

        return

    total = sum(
        item["price"] * item["quantity"]
        for item in cart
    )

    discount = calculate_discount(total)

    final_total = (
        total - discount + delivery_price
    )

    print(f"\nСумма блюд: {money(total)}")

    print(f"Скидка: {money(discount)}")

    print(f"Доставка: {money(delivery_price)}")

    print(f"Итого: {money(final_total)}")

    print("\n1. Наличные")

    print("2. Банковская карта")

    payment_choice = input("Способ оплаты: ")

    if payment_choice == "1":

        payment = "Наличные"

    elif payment_choice == "2":

        payment = "Банковская карта"

    else:

        print("Неверный способ оплаты!")

        return

    current_order_number += 1

    order = {

        "number": current_order_number,

        "name": name,

        "phone": phone,

        "items": cart.copy(),

        "total": final_total,

        "date": get_time(),

        "delivery": delivery_type,

        "payment": payment,

        "status": "Принят"

    }

    orders.append(order)

    restaurant_info["orders_today"] += 1

    restaurant_info["revenue"] += final_total

    print("\n" + "=" * 65)

    print("              ✅ ЗАКАЗ ОФОРМЛЕН!")

    print("=" * 65)

    print(f"Номер заказа: #{order['number']}")

    print(f"Клиент: {name}")

    print(f"Сумма: {money(final_total)}")

    print(f"Статус: {order['status']}")

    print("=" * 65)

    cart.clear()


# ============================================================
#                 ИСТОРИЯ ЗАКАЗОВ
# ============================================================

def order_history():

    title("📦 ИСТОРИЯ ЗАКАЗОВ")

    if not orders:

        print("Заказов пока нет.")

        return

    for order in orders:

        print(f"\nЗаказ #{order['number']}")

        print(f"Клиент: {order['name']}")

        print(f"Дата: {order['date']}")

        print(f"Сумма: {money(order['total'])}")

        print(f"Получение: {order['delivery']}")

        print(f"Оплата: {order['payment']}")

        print(f"Статус: {order['status']}")

        print("-" * 65)


# ============================================================
#                 БРОНИРОВАНИЕ СТОЛИКА
# ============================================================

def book_table():

    title("🪑 БРОНИРОВАНИЕ СТОЛИКА")

    name = input("Введите ваше имя: ")

    phone = input("Введите телефон: ")

    date = input(
        "Введите дату (например 20.09.2026): "
    )

    time = input(
        "Введите время (например 19:30): "
    )

    try:

        people = int(
            input("Количество людей: ")
        )

        if people <= 0:

            print("Неверное количество!")

            return

    except ValueError:

        print("Введите число!")

        return

    # Проверка формата даты
    try:

        booking_date = datetime.datetime.strptime(
            date,
            "%d.%m.%Y"
        ).date()

        today = datetime.date.today()

        if booking_date < today:

            print("Нельзя бронировать прошедшую дату!")

            return

    except ValueError:

        print(
            "Неверный формат даты! "
            "Используйте ДД.ММ.ГГГГ"
        )

        return

    # Проверка времени
    try:

        booking_time = datetime.datetime.strptime(
            time,
            "%H:%M"
        ).time()

        if booking_time < datetime.time(10, 0) \
                or booking_time > datetime.time(22, 0):

            print(
                "Ресторан работает с 10:00 до 23:00."
            )

            return

    except ValueError:

        print(
            "Неверный формат времени! "
            "Используйте ЧЧ:ММ"
        )

        return

    # Проверка количества людей
    if people > 12:

        print(
            "Для компании больше 12 человек "
            "позвоните в ресторан."
        )

        return

    # Проверка занятых столиков
    occupied_tables = [

        booking["table"]

        for booking in bookings

        if booking["date"] == date
        and booking["time"] == time

    ]

    free_tables = [

        table

        for table in range(1, 21)

        if table not in occupied_tables

    ]

    if not free_tables:

        print(
            "На это время свободных столиков нет."
        )

        return

    table_number = free_tables[0]

    booking = {

        "number": random.randint(10000, 99999),

        "name": name,

        "phone": phone,

        "date": date,

        "time": time,

        "people": people,

        "table": table_number,

        "status": "Забронирован"

    }

    bookings.append(booking)

    print("\n" + "=" * 65)

    print("       ✅ СТОЛИК УСПЕШНО ЗАБРОНИРОВАН")

    print("=" * 65)

    print(f"Номер брони: #{booking['number']}")

    print(f"Имя: {name}")

    print(f"Телефон: {phone}")

    print(f"Дата: {date}")

    print(f"Время: {time}")

    print(f"Количество людей: {people}")

    print(f"Столик №: {table_number}")

    print(f"Статус: {booking['status']}")

    print("=" * 65)


# ============================================================
#                 ПРОСМОТР БРОНИРОВАНИЙ
# ============================================================

def show_bookings():

    title("📅 ВСЕ БРОНИРОВАНИЯ")

    if not bookings:

        print("Бронирований пока нет.")

        return

    for booking in bookings:

        print(
            f"\nБронь #{booking['number']}"
        )

        print(f"Имя: {booking['name']}")

        print(f"Телефон: {booking['phone']}")

        print(f"Дата: {booking['date']}")

        print(f"Время: {booking['time']}")

        print(f"Людей: {booking['people']}")

        print(f"Столик: №{booking['table']}")

        print(f"Статус: {booking['status']}")

        print("-" * 65)


# ============================================================
#                 ОТМЕНА БРОНИРОВАНИЯ
# ============================================================

def cancel_booking():

    if not bookings:

        print("Бронирований нет.")

        return

    show_bookings()

    try:

        number = int(
            input("Введите номер брони: ")
        )

        for booking in bookings:

            if booking["number"] == number:

                booking["status"] = "Отменён"

                print("Бронирование отменено!")

                return

        print("Бронь не найдена.")

    except ValueError:

        print("Введите число!")


# ============================================================
#                 ОЦЕНКА РЕСТОРАНА
# ============================================================

def rate_restaurant():

    title("⭐ ОЦЕНКА РЕСТОРАНА")

    name = input("Ваше имя: ")

    try:

        rating = int(
            input("Оценка от 1 до 5: ")
        )

        if rating < 1 or rating > 5:

            print("Оценка должна быть от 1 до 5!")

            return

    except ValueError:

        print("Введите число!")

        return

    comment = input("Ваш комментарий: ")

    review = {

        "name": name,

        "rating": rating,

        "comment": comment,

        "date": get_time()

    }

    reviews.append(review)

    print("\nСпасибо за вашу оценку!")

    print(f"Оценка: {rating}/5")

    print(f"Комментарий: {comment}")


# ============================================================
#                 ПРОСМОТР ОТЗЫВОВ
# ============================================================

def show_reviews():

    title("⭐ ОТЗЫВЫ КЛИЕНТОВ")

    if not reviews:

        print("Отзывов пока нет.")

        return

    for review in reviews:

        print(f"\nИмя: {review['name']}")

        print(f"Оценка: {review['rating']}/5")

        print(f"Комментарий: {review['comment']}")

        print(f"Дата: {review['date']}")

        print("-" * 65)


# ============================================================
#                 ГЛАВНОЕ МЕНЮ
# ============================================================

def main_menu():

    while True:

        title("🍔 TASTY FOOD RESTAURANT 🍔")

        print("1. Посмотреть меню")

        print("2. Подробное меню")

        print("3. Поиск блюда")

        print("4. Добавить блюдо")

        print("5. Посмотреть корзину")

        print("6. Удалить блюдо")

        print("7. Очистить корзину")

        print("8. Оформить заказ")

        print("9. История заказов")

        print("10. Забронировать столик")

        print("11. Посмотреть бронирования")

        print("12. Отменить бронирование")

        print("13. Оценить ресторан")

        print("14. Посмотреть отзывы")

        print("15. Информация о ресторане")

        print("16. Выход")

        line()

        choice = input("Выберите действие: ")

        if choice == "1":

            show_menu()

        elif choice == "2":

            detailed_menu()

        elif choice == "3":

            search_food()

        elif choice == "4":

            add_to_cart()

        elif choice == "5":

            show_cart()

        elif choice == "6":

            remove_from_cart()

        elif choice == "7":

            clear_cart()

        elif choice == "8":

            checkout()

        elif choice == "9":

            order_history()

        elif choice == "10":

            book_table()

        elif choice == "11":

            show_bookings()

        elif choice == "12":

            cancel_booking()

        elif choice == "13":

            rate_restaurant()

        elif choice == "14":

            show_reviews()

        elif choice == "15":

            show_restaurant_info()

        elif choice == "16":

            print("Спасибо за посещение!")

            break

        else:

            print("Неверный выбор!")


# ============================================================
#                 ЗАПУСК ПРОГРАММЫ
# ============================================================

def main():

    print("=" * 65)

    print("        🍔 ДОБРО ПОЖАЛОВАТЬ В TASTY FOOD 🍔")

    print("=" * 65)

    print("Режим: Ресторан")

    print("Регистрация отключена.")

    print("=" * 65)

    main_menu()


if __name__ == "__main__":

    main()


# ============================================================
#                  🍔 TASTY FOOD RESTAURANT 🍔
# ============================================================
#                 БОЛЬШОЙ ПРОЕКТ НА PYTHON
# ============================================================

import datetime
import random


# ============================================================
#                 НАСТРОЙКИ РЕСТОРАНА
# ============================================================

RESTAURANT_NAME = "TASTY FOOD"
RESTAURANT_ADDRESS = "Бишкек, Кыргызстан"
RESTAURANT_PHONE = "+996 555 123 456"
CURRENCY = "сом"


# ============================================================
#                 ДАННЫЕ РЕСТОРАНА
# ============================================================

restaurant_info = {

    "name": RESTAURANT_NAME,

    "address": RESTAURANT_ADDRESS,

    "phone": RESTAURANT_PHONE,

    "working_hours": "10:00 - 23:00",

    "tables": 20,

    "rating": 4.8,

    "orders_today": 0,

    "revenue": 0

}


# ============================================================
#                 МЕНЮ РЕСТОРАНА
# ============================================================

menu = {

    1: {
        "name": "Пицца Маргарита",
        "price": 450,
        "category": "Пицца",
        "description": "Томатный соус, сыр, базилик"
    },

    2: {
        "name": "Пицца Пепперони",
        "price": 550,
        "category": "Пицца",
        "description": "Сыр, пепперони, томатный соус"
    },

    3: {
        "name": "Пицца Четыре сыра",
        "price": 650,
        "category": "Пицца",
        "description": "Моцарелла, чеддер, пармезан"
    },

    4: {
        "name": "Пицца Грибная",
        "price": 500,
        "category": "Пицца",
        "description": "Грибы, сыр, соус"
    },

    5: {
        "name": "Пицца Мясная",
        "price": 700,
        "category": "Пицца",
        "description": "Мясо, сыр, овощи"
    },

    6: {
        "name": "Бургер Классический",
        "price": 300,
        "category": "Бургеры",
        "description": "Котлета, салат, соус"
    },

    7: {
        "name": "Чизбургер",
        "price": 350,
        "category": "Бургеры",
        "description": "Котлета, сыр, овощи"
    },

    8: {
        "name": "Двойной бургер",
        "price": 500,
        "category": "Бургеры",
        "description": "Две котлеты, двойной сыр"
    },

    9: {
        "name": "Чикенбургер",
        "price": 320,
        "category": "Бургеры",
        "description": "Курица, салат, соус"
    },

    10: {
        "name": "Бургер BBQ",
        "price": 450,
        "category": "Бургеры",
        "description": "Мясо, BBQ соус, сыр"
    },

    11: {
        "name": "Картошка Фри",
        "price": 150,
        "category": "Закуски",
        "description": "Хрустящая картошка"
    },

    12: {
        "name": "Наггетсы",
        "price": 250,
        "category": "Закуски",
        "description": "Куриные кусочки"
    },

    13: {
        "name": "Крылышки BBQ",
        "price": 400,
        "category": "Закуски",
        "description": "Куриные крылышки"
    },

    14: {
        "name": "Луковые кольца",
        "price": 180,
        "category": "Закуски",
        "description": "Хрустящие кольца"
    },

    15: {
        "name": "Сырные палочки",
        "price": 220,
        "category": "Закуски",
        "description": "Сыр в панировке"
    },

    16: {
        "name": "Кола",
        "price": 100,
        "category": "Напитки",
        "description": "Газированный напиток"
    },

    17: {
        "name": "Спрайт",
        "price": 100,
        "category": "Напитки",
        "description": "Лимонный напиток"
    },

    18: {
        "name": "Фанта",
        "price": 100,
        "category": "Напитки",
        "description": "Апельсиновый напиток"
    },

    19: {
        "name": "Сок Апельсиновый",
        "price": 120,
        "category": "Напитки",
        "description": "Натуральный сок"
    },

    20: {
        "name": "Лимонад",
        "price": 180,
        "category": "Напитки",
        "description": "Домашний лимонад"
    },

    21: {
        "name": "Кофе",
        "price": 150,
        "category": "Напитки",
        "description": "Горячий кофе"
    },

    22: {
        "name": "Капучино",
        "price": 220,
        "category": "Напитки",
        "description": "Кофе с молоком"
    },

    23: {
        "name": "Мороженое",
        "price": 180,
        "category": "Десерты",
        "description": "Сливочное мороженое"
    },

    24: {
        "name": "Шоколадный торт",
        "price": 250,
        "category": "Десерты",
        "description": "Шоколадный десерт"
    },

    25: {
        "name": "Чизкейк",
        "price": 300,
        "category": "Десерты",
        "description": "Классический чизкейк"
    },

    26: {
        "name": "Панкейки",
        "price": 280,
        "category": "Десерты",
        "description": "Панкейки с сиропом"
    },

    27: {
        "name": "Фруктовый салат",
        "price": 250,
        "category": "Десерты",
        "description": "Свежие фрукты"
    },

    28: {
        "name": "Стейк",
        "price": 950,
        "category": "Основные блюда",
        "description": "Мясной стейк"
    },

    29: {
        "name": "Курица с рисом",
        "price": 450,
        "category": "Основные блюда",
        "description": "Курица, рис, овощи"
    },

    30: {
        "name": "Паста Карбонара",
        "price": 500,
        "category": "Основные блюда",
        "description": "Паста с соусом"
    }

}


# ============================================================
#                 ГЛОБАЛЬНЫЕ ДАННЫЕ
# ============================================================

cart = []

orders = []

bookings = []

reviews = []

current_order_number = 1000


# ============================================================
#                 ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ============================================================

def line():

    print("=" * 65)


def title(text):

    line()

    print(text.center(65))

    line()


def pause():

    input("\nНажмите Enter, чтобы продолжить...")


def get_time():

    return datetime.datetime.now().strftime(
        "%d.%m.%Y %H:%M:%S"
    )


def money(value):

    return f"{value:.2f} {CURRENCY}"


# ============================================================
#                 ИНФОРМАЦИЯ О РЕСТОРАНЕ
# ============================================================

def show_restaurant_info():

    title("🍔 ИНФОРМАЦИЯ О РЕСТОРАНЕ 🍔")

    print(f"Название: {restaurant_info['name']}")

    print(f"Адрес: {restaurant_info['address']}")

    print(f"Телефон: {restaurant_info['phone']}")

    print(f"Время работы: {restaurant_info['working_hours']}")

    print(f"Количество столиков: {restaurant_info['tables']}")

    print(f"Рейтинг: {restaurant_info['rating']}")

    print(f"Заказов сегодня: {restaurant_info['orders_today']}")

    print(f"Выручка: {money(restaurant_info['revenue'])}")


# ============================================================
#                 ПОКАЗ МЕНЮ
# ============================================================

def show_menu():

    title("🍕 МЕНЮ РЕСТОРАНА 🍕")

    for number, product in menu.items():

        print(
            f"{number:02d}. "
            f"{product['name']:<25}"
            f"{money(product['price'])}"
        )

    line()


# ============================================================
#                 ПОДРОБНОЕ МЕНЮ
# ============================================================

def detailed_menu():

    title("📋 ПОДРОБНОЕ МЕНЮ")

    for number, product in menu.items():

        print(f"\nНомер: {number}")

        print(f"Название: {product['name']}")

        print(f"Категория: {product['category']}")

        print(f"Цена: {money(product['price'])}")

        print(f"Описание: {product['description']}")

        print("-" * 65)


# ============================================================
#                 ПОИСК БЛЮДА
# ============================================================

def search_food():

    title("🔎 ПОИСК БЛЮДА")

    search = input(
        "Введите название или категорию: "
    ).lower()

    found = False

    for number, product in menu.items():

        if (
            search in product["name"].lower()
            or search in product["category"].lower()
        ):

            print(
                f"{number}. "
                f"{product['name']} — "
                f"{money(product['price'])}"
            )

            found = True

    if not found:

        print("Ничего не найдено.")


# ============================================================
#                 ДОБАВЛЕНИЕ В КОРЗИНУ
# ============================================================

def add_to_cart():

    show_menu()

    try:

        number = int(
            input("Введите номер блюда: ")
        )

        if number not in menu:

            print("Такого блюда нет!")

            return

        quantity = int(
            input("Введите количество: ")
        )

        if quantity <= 0:

            print("Количество должно быть больше нуля!")

            return

        product = menu[number]

        item = {

            "id": number,

            "name": product["name"],

            "price": product["price"],

            "quantity": quantity

        }

        cart.append(item)

        print(
            f"\n✅ {product['name']} добавлено в корзину!"
        )

        print(
            f"Сумма: {money(product['price'] * quantity)}"
        )

    except ValueError:

        print("Ошибка! Введите число.")


# ============================================================
#                 ПРОСМОТР КОРЗИНЫ
# ============================================================

def show_cart():

    title("🛒 ВАША КОРЗИНА")

    if not cart:

        print("Корзина пустая.")

        return

    total = 0

    for index, item in enumerate(cart, start=1):

        item_total = (
            item["price"] * item["quantity"]
        )

        print(
            f"{index}. {item['name']}"
        )

        print(
            f"   Количество: {item['quantity']}"
        )

        print(
            f"   Цена: {money(item['price'])}"
        )

        print(
            f"   Сумма: {money(item_total)}"
        )

        print("-" * 65)

        total += item_total

    print(f"ИТОГО: {money(total)}")


# ============================================================
#                 УДАЛЕНИЕ ИЗ КОРЗИНЫ
# ============================================================

def remove_from_cart():

    if not cart:

        print("Корзина пустая!")

        return

    show_cart()

    try:

        number = int(
            input("Введите номер позиции: ")
        )

        if number < 1 or number > len(cart):

            print("Неверный номер!")

            return

        removed = cart.pop(number - 1)

        print(
            f"❌ {removed['name']} удалено."
        )

    except ValueError:

        print("Введите число!")


# ============================================================
#                 ОЧИСТКА КОРЗИНЫ
# ============================================================

def clear_cart():

    if not cart:

        print("Корзина уже пустая!")

        return

    confirm = input(
        "Очистить корзину? (да/нет): "
    ).lower()

    if confirm == "да":

        cart.clear()

        print("Корзина очищена.")

    else:

        print("Отмена.")


# ============================================================
#                 СКИДКА
# ============================================================

def calculate_discount(total):

    if total >= 3000:

        return total * 0.15

    elif total >= 2000:

        return total * 0.10

    elif total >= 1000:

        return total * 0.05

    return 0


# ============================================================
#                 ДОСТАВКА
# ============================================================

def choose_delivery():

    title("🚚 СПОСОБ ПОЛУЧЕНИЯ")

    print("1. Самовывоз")

    print("2. Доставка")

    choice = input("Выберите: ")

    if choice == "1":

        return "Самовывоз", 0

    elif choice == "2":

        address = input("Введите адрес: ")

        return f"Доставка: {address}", 150

    else:

        print("Неверный выбор!")

        return None, 0


# ============================================================
#                 ОФОРМЛЕНИЕ ЗАКАЗА
# ============================================================

def checkout():

    global current_order_number

    if not cart:

        print("Корзина пустая!")

        return

    title("🧾 ОФОРМЛЕНИЕ ЗАКАЗА")

    name = input("Ваше имя: ")

    phone = input("Ваш телефон: ")

    delivery_type, delivery_price = choose_delivery()

    if delivery_type is None:

        return

    total = sum(
        item["price"] * item["quantity"]
        for item in cart
    )

    discount = calculate_discount(total)

    final_total = (
        total - discount + delivery_price
    )

    print(f"\nСумма блюд: {money(total)}")

    print(f"Скидка: {money(discount)}")

    print(f"Доставка: {money(delivery_price)}")

    print(f"Итого: {money(final_total)}")

    print("\n1. Наличные")

    print("2. Банковская карта")

    payment_choice = input("Способ оплаты: ")

    if payment_choice == "1":

        payment = "Наличные"

    elif payment_choice == "2":

        payment = "Банковская карта"

    else:

        print("Неверный способ оплаты!")

        return

    current_order_number += 1

    order = {

        "number": current_order_number,

        "name": name,

        "phone": phone,

        "items": cart.copy(),

        "total": final_total,

        "date": get_time(),

        "delivery": delivery_type,

        "payment": payment,

        "status": "Принят"

    }

    orders.append(order)

    restaurant_info["orders_today"] += 1

    restaurant_info["revenue"] += final_total

    print("\n" + "=" * 65)

    print("              ✅ ЗАКАЗ ОФОРМЛЕН!")

    print("=" * 65)

    print(f"Номер заказа: #{order['number']}")

    print(f"Клиент: {name}")

    print(f"Сумма: {money(final_total)}")

    print(f"Статус: {order['status']}")

    print("=" * 65)

    cart.clear()


# ============================================================
#                 ИСТОРИЯ ЗАКАЗОВ
# ============================================================

def order_history():

    title("📦 ИСТОРИЯ ЗАКАЗОВ")

    if not orders:

        print("Заказов пока нет.")

        return

    for order in orders:

        print(f"\nЗаказ #{order['number']}")

        print(f"Клиент: {order['name']}")

        print(f"Дата: {order['date']}")

        print(f"Сумма: {money(order['total'])}")

        print(f"Получение: {order['delivery']}")

        print(f"Оплата: {order['payment']}")

        print(f"Статус: {order['status']}")

        print("-" * 65)


# ============================================================
#                 БРОНИРОВАНИЕ СТОЛИКА
# ============================================================

def book_table():

    title("🪑 БРОНИРОВАНИЕ СТОЛИКА")

    name = input("Введите ваше имя: ")

    phone = input("Введите телефон: ")

    date = input(
        "Введите дату (например 20.09.2026): "
    )

    time = input(
        "Введите время (например 19:30): "
    )

    try:

        people = int(
            input("Количество людей: ")
        )

        if people <= 0:

            print("Неверное количество!")

            return

    except ValueError:

        print("Введите число!")

        return

    # Проверка формата даты
    try:

        booking_date = datetime.datetime.strptime(
            date,
            "%d.%m.%Y"
        ).date()

        today = datetime.date.today()

        if booking_date < today:

            print("Нельзя бронировать прошедшую дату!")

            return

    except ValueError:

        print(
            "Неверный формат даты! "
            "Используйте ДД.ММ.ГГГГ"
        )

        return

    # Проверка времени
    try:

        booking_time = datetime.datetime.strptime(
            time,
            "%H:%M"
        ).time()

        if booking_time < datetime.time(10, 0) \
                or booking_time > datetime.time(22, 0):

            print(
                "Ресторан работает с 10:00 до 23:00."
            )

            return

    except ValueError:

        print(
            "Неверный формат времени! "
            "Используйте ЧЧ:ММ"
        )

        return

    # Проверка количества людей
    if people > 12:

        print(
            "Для компании больше 12 человек "
            "позвоните в ресторан."
        )

        return

    # Проверка занятых столиков
    occupied_tables = [

        booking["table"]

        for booking in bookings

        if booking["date"] == date
        and booking["time"] == time

    ]

    free_tables = [

        table

        for table in range(1, 21)

        if table not in occupied_tables

    ]

    if not free_tables:

        print(
            "На это время свободных столиков нет."
        )

        return

    table_number = free_tables[0]

    booking = {

        "number": random.randint(10000, 99999),

        "name": name,

        "phone": phone,

        "date": date,

        "time": time,

        "people": people,

        "table": table_number,

        "status": "Забронирован"

    }

    bookings.append(booking)

    print("\n" + "=" * 65)

    print("       ✅ СТОЛИК УСПЕШНО ЗАБРОНИРОВАН")

    print("=" * 65)

    print(f"Номер брони: #{booking['number']}")

    print(f"Имя: {name}")

    print(f"Телефон: {phone}")

    print(f"Дата: {date}")

    print(f"Время: {time}")

    print(f"Количество людей: {people}")

    print(f"Столик №: {table_number}")

    print(f"Статус: {booking['status']}")

    print("=" * 65)


# ============================================================
#                 ПРОСМОТР БРОНИРОВАНИЙ
# ============================================================

def show_bookings():

    title("📅 ВСЕ БРОНИРОВАНИЯ")

    if not bookings:

        print("Бронирований пока нет.")

        return

    for booking in bookings:

        print(
            f"\nБронь #{booking['number']}"
        )

        print(f"Имя: {booking['name']}")

        print(f"Телефон: {booking['phone']}")

        print(f"Дата: {booking['date']}")

        print(f"Время: {booking['time']}")

        print(f"Людей: {booking['people']}")

        print(f"Столик: №{booking['table']}")

        print(f"Статус: {booking['status']}")

        print("-" * 65)


# ============================================================
#                 ОТМЕНА БРОНИРОВАНИЯ
# ============================================================

def cancel_booking():

    if not bookings:

        print("Бронирований нет.")

        return

    show_bookings()

    try:

        number = int(
            input("Введите номер брони: ")
        )

        for booking in bookings:

            if booking["number"] == number:

                booking["status"] = "Отменён"

                print("Бронирование отменено!")

                return

        print("Бронь не найдена.")

    except ValueError:

        print("Введите число!")


# ============================================================
#                 ОЦЕНКА РЕСТОРАНА
# ============================================================

def rate_restaurant():

    title("⭐ ОЦЕНКА РЕСТОРАНА")

    name = input("Ваше имя: ")

    try:

        rating = int(
            input("Оценка от 1 до 5: ")
        )

        if rating < 1 or rating > 5:

            print("Оценка должна быть от 1 до 5!")

            return

    except ValueError:

        print("Введите число!")

        return

    comment = input("Ваш комментарий: ")

    review = {

        "name": name,

        "rating": rating,

        "comment": comment,

        "date": get_time()

    }

    reviews.append(review)

    print("\nСпасибо за вашу оценку!")

    print(f"Оценка: {rating}/5")

    print(f"Комментарий: {comment}")


# ============================================================
#                 ПРОСМОТР ОТЗЫВОВ
# ============================================================

def show_reviews():

    title("⭐ ОТЗЫВЫ КЛИЕНТОВ")

    if not reviews:

        print("Отзывов пока нет.")

        return

    for review in reviews:

        print(f"\nИмя: {review['name']}")

        print(f"Оценка: {review['rating']}/5")

        print(f"Комментарий: {review['comment']}")

        print(f"Дата: {review['date']}")

        print("-" * 65)


# ============================================================
#                 ГЛАВНОЕ МЕНЮ
# ============================================================

def main_menu():

    while True:

        title("🍔 TASTY FOOD RESTAURANT 🍔")

        print("1. Посмотреть меню")

        print("2. Подробное меню")

        print("3. Поиск блюда")

        print("4. Добавить блюдо")

        print("5. Посмотреть корзину")

        print("6. Удалить блюдо")

        print("7. Очистить корзину")

        print("8. Оформить заказ")

        print("9. История заказов")

        print("10. Забронировать столик")

        print("11. Посмотреть бронирования")

        print("12. Отменить бронирование")

        print("13. Оценить ресторан")

        print("14. Посмотреть отзывы")

        print("15. Информация о ресторане")

        print("16. Выход")

        line()

        choice = input("Выберите действие: ")

        if choice == "1":

            show_menu()

        elif choice == "2":

            detailed_menu()

        elif choice == "3":

            search_food()

        elif choice == "4":

            add_to_cart()

        elif choice == "5":

            show_cart()

        elif choice == "6":

            remove_from_cart()

        elif choice == "7":

            clear_cart()

        elif choice == "8":

            checkout()

        elif choice == "9":

            order_history()

        elif choice == "10":

            book_table()

        elif choice == "11":

            show_bookings()

        elif choice == "12":

            cancel_booking()

        elif choice == "13":

            rate_restaurant()

        elif choice == "14":

            show_reviews()

        elif choice == "15":

            show_restaurant_info()

        elif choice == "16":

            print("Спасибо за посещение!")

            break

        else:

            print("Неверный выбор!")


# ============================================================
#                 ЗАПУСК ПРОГРАММЫ
# ============================================================

def main():

    print("=" * 65)

    print("        🍔 ДОБРО ПОЖАЛОВАТЬ В TASTY FOOD 🍔")

    print("=" * 65)

    print("Режим: Ресторан")

    print("Регистрация отключена.")

    print("=" * 65)

    main_menu()


if __name__ == "__main__":

    main()

# ============================================================
#                  🍔 TASTY FOOD RESTAURANT 🍔
# ============================================================
#                 БОЛЬШОЙ ПРОЕКТ НА PYTHON
# ============================================================

import datetime
import random


# ============================================================
#                 НАСТРОЙКИ РЕСТОРАНА
# ============================================================

RESTAURANT_NAME = "TASTY FOOD"
RESTAURANT_ADDRESS = "Бишкек, Кыргызстан"
RESTAURANT_PHONE = "+996 555 123 456"
CURRENCY = "сом"


# ============================================================
#                 ДАННЫЕ РЕСТОРАНА
# ============================================================

restaurant_info = {

    "name": RESTAURANT_NAME,

    "address": RESTAURANT_ADDRESS,

    "phone": RESTAURANT_PHONE,

    "working_hours": "10:00 - 23:00",

    "tables": 20,

    "rating": 4.8,

    "orders_today": 0,

    "revenue": 0

}


# ============================================================
#                 МЕНЮ РЕСТОРАНА
# ============================================================

menu = {

    1: {
        "name": "Пицца Маргарита",
        "price": 450,
        "category": "Пицца",
        "description": "Томатный соус, сыр, базилик"
    },

    2: {
        "name": "Пицца Пепперони",
        "price": 550,
        "category": "Пицца",
        "description": "Сыр, пепперони, томатный соус"
    },

    3: {
        "name": "Пицца Четыре сыра",
        "price": 650,
        "category": "Пицца",
        "description": "Моцарелла, чеддер, пармезан"
    },

    4: {
        "name": "Пицца Грибная",
        "price": 500,
        "category": "Пицца",
        "description": "Грибы, сыр, соус"
    },

    5: {
        "name": "Пицца Мясная",
        "price": 700,
        "category": "Пицца",
        "description": "Мясо, сыр, овощи"
    },

    6: {
        "name": "Бургер Классический",
        "price": 300,
        "category": "Бургеры",
        "description": "Котлета, салат, соус"
    },

    7: {
        "name": "Чизбургер",
        "price": 350,
        "category": "Бургеры",
        "description": "Котлета, сыр, овощи"
    },

    8: {
        "name": "Двойной бургер",
        "price": 500,
        "category": "Бургеры",
        "description": "Две котлеты, двойной сыр"
    },

    9: {
        "name": "Чикенбургер",
        "price": 320,
        "category": "Бургеры",
        "description": "Курица, салат, соус"
    },

    10: {
        "name": "Бургер BBQ",
        "price": 450,
        "category": "Бургеры",
        "description": "Мясо, BBQ соус, сыр"
    },

    11: {
        "name": "Картошка Фри",
        "price": 150,
        "category": "Закуски",
        "description": "Хрустящая картошка"
    },

    12: {
        "name": "Наггетсы",
        "price": 250,
        "category": "Закуски",
        "description": "Куриные кусочки"
    },

    13: {
        "name": "Крылышки BBQ",
        "price": 400,
        "category": "Закуски",
        "description": "Куриные крылышки"
    },

    14: {
        "name": "Луковые кольца",
        "price": 180,
        "category": "Закуски",
        "description": "Хрустящие кольца"
    },

    15: {
        "name": "Сырные палочки",
        "price": 220,
        "category": "Закуски",
        "description": "Сыр в панировке"
    },

    16: {
        "name": "Кола",
        "price": 100,
        "category": "Напитки",
        "description": "Газированный напиток"
    },

    17: {
        "name": "Спрайт",
        "price": 100,
        "category": "Напитки",
        "description": "Лимонный напиток"
    },

    18: {
        "name": "Фанта",
        "price": 100,
        "category": "Напитки",
        "description": "Апельсиновый напиток"
    },

    19: {
        "name": "Сок Апельсиновый",
        "price": 120,
        "category": "Напитки",
        "description": "Натуральный сок"
    },

    20: {
        "name": "Лимонад",
        "price": 180,
        "category": "Напитки",
        "description": "Домашний лимонад"
    },

    21: {
        "name": "Кофе",
        "price": 150,
        "category": "Напитки",
        "description": "Горячий кофе"
    },

    22: {
        "name": "Капучино",
        "price": 220,
        "category": "Напитки",
        "description": "Кофе с молоком"
    },

    23: {
        "name": "Мороженое",
        "price": 180,
        "category": "Десерты",
        "description": "Сливочное мороженое"
    },

    24: {
        "name": "Шоколадный торт",
        "price": 250,
        "category": "Десерты",
        "description": "Шоколадный десерт"
    },

    25: {
        "name": "Чизкейк",
        "price": 300,
        "category": "Десерты",
        "description": "Классический чизкейк"
    },

    26: {
        "name": "Панкейки",
        "price": 280,
        "category": "Десерты",
        "description": "Панкейки с сиропом"
    },

    27: {
        "name": "Фруктовый салат",
        "price": 250,
        "category": "Десерты",
        "description": "Свежие фрукты"
    },

    28: {
        "name": "Стейк",
        "price": 950,
        "category": "Основные блюда",
        "description": "Мясной стейк"
    },

    29: {
        "name": "Курица с рисом",
        "price": 450,
        "category": "Основные блюда",
        "description": "Курица, рис, овощи"
    },

    30: {
        "name": "Паста Карбонара",
        "price": 500,
        "category": "Основные блюда",
        "description": "Паста с соусом"
    }

}


# ============================================================
#                 ГЛОБАЛЬНЫЕ ДАННЫЕ
# ============================================================

cart = []

orders = []

bookings = []

reviews = []

current_order_number = 1000


# ============================================================
#                 ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ============================================================

def line():

    print("=" * 65)


def title(text):

    line()

    print(text.center(65))

    line()


def pause():

    input("\nНажмите Enter, чтобы продолжить...")


def get_time():

    return datetime.datetime.now().strftime(
        "%d.%m.%Y %H:%M:%S"
    )


def money(value):

    return f"{value:.2f} {CURRENCY}"


# ============================================================
#                 ИНФОРМАЦИЯ О РЕСТОРАНЕ
# ============================================================

def show_restaurant_info():

    title("🍔 ИНФОРМАЦИЯ О РЕСТОРАНЕ 🍔")

    print(f"Название: {restaurant_info['name']}")

    print(f"Адрес: {restaurant_info['address']}")

    print(f"Телефон: {restaurant_info['phone']}")

    print(f"Время работы: {restaurant_info['working_hours']}")

    print(f"Количество столиков: {restaurant_info['tables']}")

    print(f"Рейтинг: {restaurant_info['rating']}")

    print(f"Заказов сегодня: {restaurant_info['orders_today']}")

    print(f"Выручка: {money(restaurant_info['revenue'])}")


# ============================================================
#                 ПОКАЗ МЕНЮ
# ============================================================

def show_menu():

    title("🍕 МЕНЮ РЕСТОРАНА 🍕")

    for number, product in menu.items():

        print(
            f"{number:02d}. "
            f"{product['name']:<25}"
            f"{money(product['price'])}"
        )

    line()


# ============================================================
#                 ПОДРОБНОЕ МЕНЮ
# ============================================================

def detailed_menu():

    title("📋 ПОДРОБНОЕ МЕНЮ")

    for number, product in menu.items():

        print(f"\nНомер: {number}")

        print(f"Название: {product['name']}")

        print(f"Категория: {product['category']}")

        print(f"Цена: {money(product['price'])}")

        print(f"Описание: {product['description']}")

        print("-" * 65)


# ============================================================
#                 ПОИСК БЛЮДА
# ============================================================

def search_food():

    title("🔎 ПОИСК БЛЮДА")

    search = input(
        "Введите название или категорию: "
    ).lower()

    found = False

    for number, product in menu.items():

        if (
            search in product["name"].lower()
            or search in product["category"].lower()
        ):

            print(
                f"{number}. "
                f"{product['name']} — "
                f"{money(product['price'])}"
            )

            found = True

    if not found:

        print("Ничего не найдено.")


# ============================================================
#                 ДОБАВЛЕНИЕ В КОРЗИНУ
# ============================================================

def add_to_cart():

    show_menu()

    try:

        number = int(
            input("Введите номер блюда: ")
        )

        if number not in menu:

            print("Такого блюда нет!")

            return

        quantity = int(
            input("Введите количество: ")
        )

        if quantity <= 0:

            print("Количество должно быть больше нуля!")

            return

        product = menu[number]

        item = {

            "id": number,

            "name": product["name"],

            "price": product["price"],

            "quantity": quantity

        }

        cart.append(item)

        print(
            f"\n✅ {product['name']} добавлено в корзину!"
        )

        print(
            f"Сумма: {money(product['price'] * quantity)}"
        )

    except ValueError:

        print("Ошибка! Введите число.")


# ============================================================
#                 ПРОСМОТР КОРЗИНЫ
# ============================================================

def show_cart():

    title("🛒 ВАША КОРЗИНА")

    if not cart:

        print("Корзина пустая.")

        return

    total = 0

    for index, item in enumerate(cart, start=1):

        item_total = (
            item["price"] * item["quantity"]
        )

        print(
            f"{index}. {item['name']}"
        )

        print(
            f"   Количество: {item['quantity']}"
        )

        print(
            f"   Цена: {money(item['price'])}"
        )

        print(
            f"   Сумма: {money(item_total)}"
        )

        print("-" * 65)

        total += item_total

    print(f"ИТОГО: {money(total)}")


# ============================================================
#                 УДАЛЕНИЕ ИЗ КОРЗИНЫ
# ============================================================

def remove_from_cart():

    if not cart:

        print("Корзина пустая!")

        return

    show_cart()

    try:

        number = int(
            input("Введите номер позиции: ")
        )

        if number < 1 or number > len(cart):

            print("Неверный номер!")

            return

        removed = cart.pop(number - 1)

        print(
            f"❌ {removed['name']} удалено."
        )

    except ValueError:

        print("Введите число!")


# ============================================================
#                 ОЧИСТКА КОРЗИНЫ
# ============================================================

def clear_cart():

    if not cart:

        print("Корзина уже пустая!")

        return

    confirm = input(
        "Очистить корзину? (да/нет): "
    ).lower()

    if confirm == "да":

        cart.clear()

        print("Корзина очищена.")

    else:

        print("Отмена.")


# ============================================================
#                 СКИДКА
# ============================================================

def calculate_discount(total):

    if total >= 3000:

        return total * 0.15

    elif total >= 2000:

        return total * 0.10

    elif total >= 1000:

        return total * 0.05

    return 0


# ============================================================
#                 ДОСТАВКА
# ============================================================

def choose_delivery():

    title("🚚 СПОСОБ ПОЛУЧЕНИЯ")

    print("1. Самовывоз")

    print("2. Доставка")

    choice = input("Выберите: ")

    if choice == "1":

        return "Самовывоз", 0

    elif choice == "2":

        address = input("Введите адрес: ")

        return f"Доставка: {address}", 150

    else:

        print("Неверный выбор!")

        return None, 0


# ============================================================
#                 ОФОРМЛЕНИЕ ЗАКАЗА
# ============================================================

def checkout():

    global current_order_number

    if not cart:

        print("Корзина пустая!")

        return

    title("🧾 ОФОРМЛЕНИЕ ЗАКАЗА")

    name = input("Ваше имя: ")

    phone = input("Ваш телефон: ")

    delivery_type, delivery_price = choose_delivery()

    if delivery_type is None:

        return

    total = sum(
        item["price"] * item["quantity"]
        for item in cart
    )

    discount = calculate_discount(total)

    final_total = (
        total - discount + delivery_price
    )

    print(f"\nСумма блюд: {money(total)}")

    print(f"Скидка: {money(discount)}")

    print(f"Доставка: {money(delivery_price)}")

    print(f"Итого: {money(final_total)}")

    print("\n1. Наличные")

    print("2. Банковская карта")

    payment_choice = input("Способ оплаты: ")

    if payment_choice == "1":

        payment = "Наличные"

    elif payment_choice == "2":

        payment = "Банковская карта"

    else:

        print("Неверный способ оплаты!")

        return

    current_order_number += 1

    order = {

        "number": current_order_number,

        "name": name,

        "phone": phone,

        "items": cart.copy(),

        "total": final_total,

        "date": get_time(),

        "delivery": delivery_type,

        "payment": payment,

        "status": "Принят"

    }

    orders.append(order)

    restaurant_info["orders_today"] += 1

    restaurant_info["revenue"] += final_total

    print("\n" + "=" * 65)

    print("              ✅ ЗАКАЗ ОФОРМЛЕН!")

    print("=" * 65)

    print(f"Номер заказа: #{order['number']}")

    print(f"Клиент: {name}")

    print(f"Сумма: {money(final_total)}")

    print(f"Статус: {order['status']}")

    print("=" * 65)

    cart.clear()


# ============================================================
#                 ИСТОРИЯ ЗАКАЗОВ
# ============================================================

def order_history():

    title("📦 ИСТОРИЯ ЗАКАЗОВ")

    if not orders:

        print("Заказов пока нет.")

        return

    for order in orders:

        print(f"\nЗаказ #{order['number']}")

        print(f"Клиент: {order['name']}")

        print(f"Дата: {order['date']}")

        print(f"Сумма: {money(order['total'])}")

        print(f"Получение: {order['delivery']}")

        print(f"Оплата: {order['payment']}")

        print(f"Статус: {order['status']}")

        print("-" * 65)


# ============================================================
#                 БРОНИРОВАНИЕ СТОЛИКА
# ============================================================

def book_table():

    title("🪑 БРОНИРОВАНИЕ СТОЛИКА")

    name = input("Введите ваше имя: ")

    phone = input("Введите телефон: ")

    date = input(
        "Введите дату (например 20.09.2026): "
    )

    time = input(
        "Введите время (например 19:30): "
    )

    try:

        people = int(
            input("Количество людей: ")
        )

        if people <= 0:

            print("Неверное количество!")

            return

    except ValueError:

        print("Введите число!")

        return

    # Проверка формата даты
    try:

        booking_date = datetime.datetime.strptime(
            date,
            "%d.%m.%Y"
        ).date()

        today = datetime.date.today()

        if booking_date < today:

            print("Нельзя бронировать прошедшую дату!")

            return

    except ValueError:

        print(
            "Неверный формат даты! "
            "Используйте ДД.ММ.ГГГГ"
        )

        return

    # Проверка времени
    try:

        booking_time = datetime.datetime.strptime(
            time,
            "%H:%M"
        ).time()

        if booking_time < datetime.time(10, 0) \
                or booking_time > datetime.time(22, 0):

            print(
                "Ресторан работает с 10:00 до 23:00."
            )

            return

    except ValueError:

        print(
            "Неверный формат времени! "
            "Используйте ЧЧ:ММ"
        )

        return

    # Проверка количества людей
    if people > 12:

        print(
            "Для компании больше 12 человек "
            "позвоните в ресторан."
        )

        return

    # Проверка занятых столиков
    occupied_tables = [

        booking["table"]

        for booking in bookings

        if booking["date"] == date
        and booking["time"] == time

    ]

    free_tables = [

        table

        for table in range(1, 21)

        if table not in occupied_tables

    ]

    if not free_tables:

        print(
            "На это время свободных столиков нет."
        )

        return

    table_number = free_tables[0]

    booking = {

        "number": random.randint(10000, 99999),

        "name": name,

        "phone": phone,

        "date": date,

        "time": time,

        "people": people,

        "table": table_number,

        "status": "Забронирован"

    }

    bookings.append(booking)

    print("\n" + "=" * 65)

    print("       ✅ СТОЛИК УСПЕШНО ЗАБРОНИРОВАН")

    print("=" * 65)

    print(f"Номер брони: #{booking['number']}")

    print(f"Имя: {name}")

    print(f"Телефон: {phone}")

    print(f"Дата: {date}")

    print(f"Время: {time}")

    print(f"Количество людей: {people}")

    print(f"Столик №: {table_number}")

    print(f"Статус: {booking['status']}")

    print("=" * 65)


# ============================================================
#                 ПРОСМОТР БРОНИРОВАНИЙ
# ============================================================

def show_bookings():

    title("📅 ВСЕ БРОНИРОВАНИЯ")

    if not bookings:

        print("Бронирований пока нет.")

        return

    for booking in bookings:

        print(
            f"\nБронь #{booking['number']}"
        )

        print(f"Имя: {booking['name']}")

        print(f"Телефон: {booking['phone']}")

        print(f"Дата: {booking['date']}")

        print(f"Время: {booking['time']}")

        print(f"Людей: {booking['people']}")

        print(f"Столик: №{booking['table']}")

        print(f"Статус: {booking['status']}")

        print("-" * 65)


# ============================================================
#                 ОТМЕНА БРОНИРОВАНИЯ
# ============================================================

def cancel_booking():

    if not bookings:

        print("Бронирований нет.")

        return

    show_bookings()

    try:

        number = int(
            input("Введите номер брони: ")
        )

        for booking in bookings:

            if booking["number"] == number:

                booking["status"] = "Отменён"

                print("Бронирование отменено!")

                return

        print("Бронь не найдена.")

    except ValueError:

        print("Введите число!")


# ============================================================
#                 ОЦЕНКА РЕСТОРАНА
# ============================================================

def rate_restaurant():

    title("⭐ ОЦЕНКА РЕСТОРАНА")

    name = input("Ваше имя: ")

    try:

        rating = int(
            input("Оценка от 1 до 5: ")
        )

        if rating < 1 or rating > 5:

            print("Оценка должна быть от 1 до 5!")

            return

    except ValueError:

        print("Введите число!")

        return

    comment = input("Ваш комментарий: ")

    review = {

        "name": name,

        "rating": rating,

        "comment": comment,

        "date": get_time()

    }

    reviews.append(review)

    print("\nСпасибо за вашу оценку!")

    print(f"Оценка: {rating}/5")

    print(f"Комментарий: {comment}")


# ============================================================
#                 ПРОСМОТР ОТЗЫВОВ
# ============================================================

def show_reviews():

    title("⭐ ОТЗЫВЫ КЛИЕНТОВ")

    if not reviews:

        print("Отзывов пока нет.")

        return

    for review in reviews:

        print(f"\nИмя: {review['name']}")

        print(f"Оценка: {review['rating']}/5")

        print(f"Комментарий: {review['comment']}")

        print(f"Дата: {review['date']}")

        print("-" * 65)


# ============================================================
#                 ГЛАВНОЕ МЕНЮ
# ============================================================

def main_menu():

    while True:

        title("🍔 TASTY FOOD RESTAURANT 🍔")

        print("1. Посмотреть меню")

        print("2. Подробное меню")

        print("3. Поиск блюда")

        print("4. Добавить блюдо")

        print("5. Посмотреть корзину")

        print("6. Удалить блюдо")

        print("7. Очистить корзину")

        print("8. Оформить заказ")

        print("9. История заказов")

        print("10. Забронировать столик")

        print("11. Посмотреть бронирования")

        print("12. Отменить бронирование")

        print("13. Оценить ресторан")

        print("14. Посмотреть отзывы")

        print("15. Информация о ресторане")

        print("16. Выход")

        line()

        choice = input("Выберите действие: ")

        if choice == "1":

            show_menu()

        elif choice == "2":

            detailed_menu()

        elif choice == "3":

            search_food()

        elif choice == "4":

            add_to_cart()

        elif choice == "5":

            show_cart()

        elif choice == "6":

            remove_from_cart()

        elif choice == "7":

            clear_cart()

        elif choice == "8":

            checkout()

        elif choice == "9":

            order_history()

        elif choice == "10":

            book_table()

        elif choice == "11":

            show_bookings()

        elif choice == "12":

            cancel_booking()

        elif choice == "13":

            rate_restaurant()

        elif choice == "14":

            show_reviews()

        elif choice == "15":

            show_restaurant_info()

        elif choice == "16":

            print("Спасибо за посещение!")

            break

        else:

            print("Неверный выбор!")


# ============================================================
#                 ЗАПУСК ПРОГРАММЫ
# ============================================================

def main():

    print("=" * 65)

    print("        🍔 ДОБРО ПОЖАЛОВАТЬ В TASTY FOOD 🍔")

    print("=" * 65)

    print("Режим: Ресторан")

    print("Регистрация отключена.")

    print("=" * 65)

    main_menu()


if __name__ == "__main__":

    main()

# ============================================================
#                  🍔 TASTY FOOD RESTAURANT 🍔
# ============================================================
#                 БОЛЬШОЙ ПРОЕКТ НА PYTHON
# ============================================================

import datetime
import random


# ============================================================
#                 НАСТРОЙКИ РЕСТОРАНА
# ============================================================

RESTAURANT_NAME = "TASTY FOOD"
RESTAURANT_ADDRESS = "Бишкек, Кыргызстан"
RESTAURANT_PHONE = "+996 555 123 456"
CURRENCY = "сом"


# ============================================================
#                 ДАННЫЕ РЕСТОРАНА
# ============================================================

restaurant_info = {

    "name": RESTAURANT_NAME,

    "address": RESTAURANT_ADDRESS,

    "phone": RESTAURANT_PHONE,

    "working_hours": "10:00 - 23:00",

    "tables": 20,

    "rating": 4.8,

    "orders_today": 0,

    "revenue": 0

}


# ============================================================
#                 МЕНЮ РЕСТОРАНА
# ============================================================

menu = {

    1: {
        "name": "Пицца Маргарита",
        "price": 450,
        "category": "Пицца",
        "description": "Томатный соус, сыр, базилик"
    },

    2: {
        "name": "Пицца Пепперони",
        "price": 550,
        "category": "Пицца",
        "description": "Сыр, пепперони, томатный соус"
    },

    3: {
        "name": "Пицца Четыре сыра",
        "price": 650,
        "category": "Пицца",
        "description": "Моцарелла, чеддер, пармезан"
    },

    4: {
        "name": "Пицца Грибная",
        "price": 500,
        "category": "Пицца",
        "description": "Грибы, сыр, соус"
    },

    5: {
        "name": "Пицца Мясная",
        "price": 700,
        "category": "Пицца",
        "description": "Мясо, сыр, овощи"
    },

    6: {
        "name": "Бургер Классический",
        "price": 300,
        "category": "Бургеры",
        "description": "Котлета, салат, соус"
    },

    7: {
        "name": "Чизбургер",
        "price": 350,
        "category": "Бургеры",
        "description": "Котлета, сыр, овощи"
    },

    8: {
        "name": "Двойной бургер",
        "price": 500,
        "category": "Бургеры",
        "description": "Две котлеты, двойной сыр"
    },

    9: {
        "name": "Чикенбургер",
        "price": 320,
        "category": "Бургеры",
        "description": "Курица, салат, соус"
    },

    10: {
        "name": "Бургер BBQ",
        "price": 450,
        "category": "Бургеры",
        "description": "Мясо, BBQ соус, сыр"
    },

    11: {
        "name": "Картошка Фри",
        "price": 150,
        "category": "Закуски",
        "description": "Хрустящая картошка"
    },

    12: {
        "name": "Наггетсы",
        "price": 250,
        "category": "Закуски",
        "description": "Куриные кусочки"
    },

    13: {
        "name": "Крылышки BBQ",
        "price": 400,
        "category": "Закуски",
        "description": "Куриные крылышки"
    },

    14: {
        "name": "Луковые кольца",
        "price": 180,
        "category": "Закуски",
        "description": "Хрустящие кольца"
    },

    15: {
        "name": "Сырные палочки",
        "price": 220,
        "category": "Закуски",
        "description": "Сыр в панировке"
    },

    16: {
        "name": "Кола",
        "price": 100,
        "category": "Напитки",
        "description": "Газированный напиток"
    },

    17: {
        "name": "Спрайт",
        "price": 100,
        "category": "Напитки",
        "description": "Лимонный напиток"
    },

    18: {
        "name": "Фанта",
        "price": 100,
        "category": "Напитки",
        "description": "Апельсиновый напиток"
    },

    19: {
        "name": "Сок Апельсиновый",
        "price": 120,
        "category": "Напитки",
        "description": "Натуральный сок"
    },

    20: {
        "name": "Лимонад",
        "price": 180,
        "category": "Напитки",
        "description": "Домашний лимонад"
    },

    21: {
        "name": "Кофе",
        "price": 150,
        "category": "Напитки",
        "description": "Горячий кофе"
    },

    22: {
        "name": "Капучино",
        "price": 220,
        "category": "Напитки",
        "description": "Кофе с молоком"
    },

    23: {
        "name": "Мороженое",
        "price": 180,
        "category": "Десерты",
        "description": "Сливочное мороженое"
    },

    24: {
        "name": "Шоколадный торт",
        "price": 250,
        "category": "Десерты",
        "description": "Шоколадный десерт"
    },

    25: {
        "name": "Чизкейк",
        "price": 300,
        "category": "Десерты",
        "description": "Классический чизкейк"
    },

    26: {
        "name": "Панкейки",
        "price": 280,
        "category": "Десерты",
        "description": "Панкейки с сиропом"
    },

    27: {
        "name": "Фруктовый салат",
        "price": 250,
        "category": "Десерты",
        "description": "Свежие фрукты"
    },

    28: {
        "name": "Стейк",
        "price": 950,
        "category": "Основные блюда",
        "description": "Мясной стейк"
    },

    29: {
        "name": "Курица с рисом",
        "price": 450,
        "category": "Основные блюда",
        "description": "Курица, рис, овощи"
    },

    30: {
        "name": "Паста Карбонара",
        "price": 500,
        "category": "Основные блюда",
        "description": "Паста с соусом"
    }

}


# ============================================================
#                 ГЛОБАЛЬНЫЕ ДАННЫЕ
# ============================================================

cart = []

orders = []

bookings = []

reviews = []

current_order_number = 1000


# ============================================================
#                 ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ============================================================

def line():

    print("=" * 65)


def title(text):

    line()

    print(text.center(65))

    line()


def pause():

    input("\nНажмите Enter, чтобы продолжить...")


def get_time():

    return datetime.datetime.now().strftime(
        "%d.%m.%Y %H:%M:%S"
    )


def money(value):

    return f"{value:.2f} {CURRENCY}"


# ============================================================
#                 ИНФОРМАЦИЯ О РЕСТОРАНЕ
# ============================================================

def show_restaurant_info():

    title("🍔 ИНФОРМАЦИЯ О РЕСТОРАНЕ 🍔")

    print(f"Название: {restaurant_info['name']}")

    print(f"Адрес: {restaurant_info['address']}")

    print(f"Телефон: {restaurant_info['phone']}")

    print(f"Время работы: {restaurant_info['working_hours']}")

    print(f"Количество столиков: {restaurant_info['tables']}")

    print(f"Рейтинг: {restaurant_info['rating']}")

    print(f"Заказов сегодня: {restaurant_info['orders_today']}")

    print(f"Выручка: {money(restaurant_info['revenue'])}")


# ============================================================
#                 ПОКАЗ МЕНЮ
# ============================================================

def show_menu():

    title("🍕 МЕНЮ РЕСТОРАНА 🍕")

    for number, product in menu.items():

        print(
            f"{number:02d}. "
            f"{product['name']:<25}"
            f"{money(product['price'])}"
        )

    line()


# ============================================================
#                 ПОДРОБНОЕ МЕНЮ
# ============================================================

def detailed_menu():

    title("📋 ПОДРОБНОЕ МЕНЮ")

    for number, product in menu.items():

        print(f"\nНомер: {number}")

        print(f"Название: {product['name']}")

        print(f"Категория: {product['category']}")

        print(f"Цена: {money(product['price'])}")

        print(f"Описание: {product['description']}")

        print("-" * 65)


# ============================================================
#                 ПОИСК БЛЮДА
# ============================================================

def search_food():

    title("🔎 ПОИСК БЛЮДА")

    search = input(
        "Введите название или категорию: "
    ).lower()

    found = False

    for number, product in menu.items():

        if (
            search in product["name"].lower()
            or search in product["category"].lower()
        ):

            print(
                f"{number}. "
                f"{product['name']} — "
                f"{money(product['price'])}"
            )

            found = True

    if not found:

        print("Ничего не найдено.")


# ============================================================
#                 ДОБАВЛЕНИЕ В КОРЗИНУ
# ============================================================

def add_to_cart():

    show_menu()

    try:

        number = int(
            input("Введите номер блюда: ")
        )

        if number not in menu:

            print("Такого блюда нет!")

            return

        quantity = int(
            input("Введите количество: ")
        )

        if quantity <= 0:

            print("Количество должно быть больше нуля!")

            return

        product = menu[number]

        item = {

            "id": number,

            "name": product["name"],

            "price": product["price"],

            "quantity": quantity

        }

        cart.append(item)

        print(
            f"\n✅ {product['name']} добавлено в корзину!"
        )

        print(
            f"Сумма: {money(product['price'] * quantity)}"
        )

    except ValueError:

        print("Ошибка! Введите число.")


# ============================================================
#                 ПРОСМОТР КОРЗИНЫ
# ============================================================

def show_cart():

    title("🛒 ВАША КОРЗИНА")

    if not cart:

        print("Корзина пустая.")

        return

    total = 0

    for index, item in enumerate(cart, start=1):

        item_total = (
            item["price"] * item["quantity"]
        )

        print(
            f"{index}. {item['name']}"
        )

        print(
            f"   Количество: {item['quantity']}"
        )

        print(
            f"   Цена: {money(item['price'])}"
        )

        print(
            f"   Сумма: {money(item_total)}"
        )

        print("-" * 65)

        total += item_total

    print(f"ИТОГО: {money(total)}")


# ============================================================
#                 УДАЛЕНИЕ ИЗ КОРЗИНЫ
# ============================================================

def remove_from_cart():

    if not cart:

        print("Корзина пустая!")

        return

    show_cart()

    try:

        number = int(
            input("Введите номер позиции: ")
        )

        if number < 1 or number > len(cart):

            print("Неверный номер!")

            return

        removed = cart.pop(number - 1)

        print(
            f"❌ {removed['name']} удалено."
        )

    except ValueError:

        print("Введите число!")


# ============================================================
#                 ОЧИСТКА КОРЗИНЫ
# ============================================================

def clear_cart():

    if not cart:

        print("Корзина уже пустая!")

        return

    confirm = input(
        "Очистить корзину? (да/нет): "
    ).lower()

    if confirm == "да":

        cart.clear()

        print("Корзина очищена.")

    else:

        print("Отмена.")


# ============================================================
#                 СКИДКА
# ============================================================

def calculate_discount(total):

    if total >= 3000:

        return total * 0.15

    elif total >= 2000:

        return total * 0.10

    elif total >= 1000:

        return total * 0.05

    return 0


# ============================================================
#                 ДОСТАВКА
# ============================================================

def choose_delivery():

    title("🚚 СПОСОБ ПОЛУЧЕНИЯ")

    print("1. Самовывоз")

    print("2. Доставка")

    choice = input("Выберите: ")

    if choice == "1":

        return "Самовывоз", 0

    elif choice == "2":

        address = input("Введите адрес: ")

        return f"Доставка: {address}", 150

    else:

        print("Неверный выбор!")

        return None, 0


# ============================================================
#                 ОФОРМЛЕНИЕ ЗАКАЗА
# ============================================================

def checkout():

    global current_order_number

    if not cart:

        print("Корзина пустая!")

        return

    title("🧾 ОФОРМЛЕНИЕ ЗАКАЗА")

    name = input("Ваше имя: ")

    phone = input("Ваш телефон: ")

    delivery_type, delivery_price = choose_delivery()

    if delivery_type is None:

        return

    total = sum(
        item["price"] * item["quantity"]
        for item in cart
    )

    discount = calculate_discount(total)

    final_total = (
        total - discount + delivery_price
    )

    print(f"\nСумма блюд: {money(total)}")

    print(f"Скидка: {money(discount)}")

    print(f"Доставка: {money(delivery_price)}")

    print(f"Итого: {money(final_total)}")

    print("\n1. Наличные")

    print("2. Банковская карта")

    payment_choice = input("Способ оплаты: ")

    if payment_choice == "1":

        payment = "Наличные"

    elif payment_choice == "2":

        payment = "Банковская карта"

    else:

        print("Неверный способ оплаты!")

        return

    current_order_number += 1

    order = {

        "number": current_order_number,

        "name": name,

        "phone": phone,

        "items": cart.copy(),

        "total": final_total,

        "date": get_time(),

        "delivery": delivery_type,

        "payment": payment,

        "status": "Принят"

    }

    orders.append(order)

    restaurant_info["orders_today"] += 1

    restaurant_info["revenue"] += final_total

    print("\n" + "=" * 65)

    print("              ✅ ЗАКАЗ ОФОРМЛЕН!")

    print("=" * 65)

    print(f"Номер заказа: #{order['number']}")

    print(f"Клиент: {name}")

    print(f"Сумма: {money(final_total)}")

    print(f"Статус: {order['status']}")

    print("=" * 65)

    cart.clear()


# ============================================================
#                 ИСТОРИЯ ЗАКАЗОВ
# ============================================================

def order_history():

    title("📦 ИСТОРИЯ ЗАКАЗОВ")

    if not orders:

        print("Заказов пока нет.")

        return

    for order in orders:

        print(f"\nЗаказ #{order['number']}")

        print(f"Клиент: {order['name']}")

        print(f"Дата: {order['date']}")

        print(f"Сумма: {money(order['total'])}")

        print(f"Получение: {order['delivery']}")

        print(f"Оплата: {order['payment']}")

        print(f"Статус: {order['status']}")

        print("-" * 65)


# ============================================================
#                 БРОНИРОВАНИЕ СТОЛИКА
# ============================================================

def book_table():

    title("🪑 БРОНИРОВАНИЕ СТОЛИКА")

    name = input("Введите ваше имя: ")

    phone = input("Введите телефон: ")

    date = input(
        "Введите дату (например 20.09.2026): "
    )

    time = input(
        "Введите время (например 19:30): "
    )

    try:

        people = int(
            input("Количество людей: ")
        )

        if people <= 0:

            print("Неверное количество!")

            return

    except ValueError:

        print("Введите число!")

        return

    # Проверка формата даты
    try:

        booking_date = datetime.datetime.strptime(
            date,
            "%d.%m.%Y"
        ).date()

        today = datetime.date.today()

        if booking_date < today:

            print("Нельзя бронировать прошедшую дату!")

            return

    except ValueError:

        print(
            "Неверный формат даты! "
            "Используйте ДД.ММ.ГГГГ"
        )

        return

    # Проверка времени
    try:

        booking_time = datetime.datetime.strptime(
            time,
            "%H:%M"
        ).time()

        if booking_time < datetime.time(10, 0) \
                or booking_time > datetime.time(22, 0):

            print(
                "Ресторан работает с 10:00 до 23:00."
            )

            return

    except ValueError:

        print(
            "Неверный формат времени! "
            "Используйте ЧЧ:ММ"
        )

        return

    # Проверка количества людей
    if people > 12:

        print(
            "Для компании больше 12 человек "
            "позвоните в ресторан."
        )

        return

    # Проверка занятых столиков
    occupied_tables = [

        booking["table"]

        for booking in bookings

        if booking["date"] == date
        and booking["time"] == time

    ]

    free_tables = [

        table

        for table in range(1, 21)

        if table not in occupied_tables

    ]

    if not free_tables:

        print(
            "На это время свободных столиков нет."
        )

        return

    table_number = free_tables[0]

    booking = {

        "number": random.randint(10000, 99999),

        "name": name,

        "phone": phone,

        "date": date,

        "time": time,

        "people": people,

        "table": table_number,

        "status": "Забронирован"

    }

    bookings.append(booking)

    print("\n" + "=" * 65)

    print("       ✅ СТОЛИК УСПЕШНО ЗАБРОНИРОВАН")

    print("=" * 65)

    print(f"Номер брони: #{booking['number']}")

    print(f"Имя: {name}")

    print(f"Телефон: {phone}")

    print(f"Дата: {date}")

    print(f"Время: {time}")

    print(f"Количество людей: {people}")

    print(f"Столик №: {table_number}")

    print(f"Статус: {booking['status']}")

    print("=" * 65)


# ============================================================
#                 ПРОСМОТР БРОНИРОВАНИЙ
# ============================================================

def show_bookings():

    title("📅 ВСЕ БРОНИРОВАНИЯ")

    if not bookings:

        print("Бронирований пока нет.")

        return

    for booking in bookings:

        print(
            f"\nБронь #{booking['number']}"
        )

        print(f"Имя: {booking['name']}")

        print(f"Телефон: {booking['phone']}")

        print(f"Дата: {booking['date']}")

        print(f"Время: {booking['time']}")

        print(f"Людей: {booking['people']}")

        print(f"Столик: №{booking['table']}")

        print(f"Статус: {booking['status']}")

        print("-" * 65)


# ============================================================
#                 ОТМЕНА БРОНИРОВАНИЯ
# ============================================================

def cancel_booking():

    if not bookings:

        print("Бронирований нет.")

        return

    show_bookings()

    try:

        number = int(
            input("Введите номер брони: ")
        )

        for booking in bookings:

            if booking["number"] == number:

                booking["status"] = "Отменён"

                print("Бронирование отменено!")

                return

        print("Бронь не найдена.")

    except ValueError:

        print("Введите число!")


# ============================================================
#                 ОЦЕНКА РЕСТОРАНА
# ============================================================

def rate_restaurant():

    title("⭐ ОЦЕНКА РЕСТОРАНА")

    name = input("Ваше имя: ")

    try:

        rating = int(
            input("Оценка от 1 до 5: ")
        )

        if rating < 1 or rating > 5:

            print("Оценка должна быть от 1 до 5!")

            return

    except ValueError:

        print("Введите число!")

        return

    comment = input("Ваш комментарий: ")

    review = {

        "name": name,

        "rating": rating,

        "comment": comment,

        "date": get_time()

    }

    reviews.append(review)

    print("\nСпасибо за вашу оценку!")

    print(f"Оценка: {rating}/5")

    print(f"Комментарий: {comment}")


# ============================================================
#                 ПРОСМОТР ОТЗЫВОВ
# ============================================================

def show_reviews():

    title("⭐ ОТЗЫВЫ КЛИЕНТОВ")

    if not reviews:

        print("Отзывов пока нет.")

        return

    for review in reviews:

        print(f"\nИмя: {review['name']}")

        print(f"Оценка: {review['rating']}/5")

        print(f"Комментарий: {review['comment']}")

        print(f"Дата: {review['date']}")

        print("-" * 65)


# ============================================================
#                 ГЛАВНОЕ МЕНЮ
# ============================================================

def main_menu():

    while True:

        title("🍔 TASTY FOOD RESTAURANT 🍔")

        print("1. Посмотреть меню")

        print("2. Подробное меню")

        print("3. Поиск блюда")

        print("4. Добавить блюдо")

        print("5. Посмотреть корзину")

        print("6. Удалить блюдо")

        print("7. Очистить корзину")

        print("8. Оформить заказ")

        print("9. История заказов")

        print("10. Забронировать столик")

        print("11. Посмотреть бронирования")

        print("12. Отменить бронирование")

        print("13. Оценить ресторан")

        print("14. Посмотреть отзывы")

        print("15. Информация о ресторане")

        print("16. Выход")

        line()

        choice = input("Выберите действие: ")

        if choice == "1":

            show_menu()

        elif choice == "2":

            detailed_menu()

        elif choice == "3":

            search_food()

        elif choice == "4":

            add_to_cart()

        elif choice == "5":

            show_cart()

        elif choice == "6":

            remove_from_cart()

        elif choice == "7":

            clear_cart()

        elif choice == "8":

            checkout()

        elif choice == "9":

            order_history()

        elif choice == "10":

            book_table()

        elif choice == "11":

            show_bookings()

        elif choice == "12":

            cancel_booking()

        elif choice == "13":

            rate_restaurant()

        elif choice == "14":

            show_reviews()

        elif choice == "15":

            show_restaurant_info()

        elif choice == "16":

            print("Спасибо за посещение!")

            break

        else:

            print("Неверный выбор!")


# ============================================================
#                 ЗАПУСК ПРОГРАММЫ
# ============================================================

def main():

    print("=" * 65)

    print("        🍔 ДОБРО ПОЖАЛОВАТЬ В TASTY FOOD 🍔")

    print("=" * 65)

    print("Режим: Ресторан")

    print("Регистрация отключена.")

    print("=" * 65)

    main_menu()


if __name__ == "__main__":

    main()

# ============================================================
#                  🍔 TASTY FOOD RESTAURANT 🍔
# ============================================================
#                 БОЛЬШОЙ ПРОЕКТ НА PYTHON
# ============================================================

import datetime
import random


# ============================================================
#                 НАСТРОЙКИ РЕСТОРАНА
# ============================================================

RESTAURANT_NAME = "TASTY FOOD"
RESTAURANT_ADDRESS = "Бишкек, Кыргызстан"
RESTAURANT_PHONE = "+996 555 123 456"
CURRENCY = "сом"


# ============================================================
#                 ДАННЫЕ РЕСТОРАНА
# ============================================================

restaurant_info = {

    "name": RESTAURANT_NAME,

    "address": RESTAURANT_ADDRESS,

    "phone": RESTAURANT_PHONE,

    "working_hours": "10:00 - 23:00",

    "tables": 20,

    "rating": 4.8,

    "orders_today": 0,

    "revenue": 0

}


# ============================================================
#                 МЕНЮ РЕСТОРАНА
# ============================================================

menu = {

    1: {
        "name": "Пицца Маргарита",
        "price": 450,
        "category": "Пицца",
        "description": "Томатный соус, сыр, базилик"
    },

    2: {
        "name": "Пицца Пепперони",
        "price": 550,
        "category": "Пицца",
        "description": "Сыр, пепперони, томатный соус"
    },

    3: {
        "name": "Пицца Четыре сыра",
        "price": 650,
        "category": "Пицца",
        "description": "Моцарелла, чеддер, пармезан"
    },

    4: {
        "name": "Пицца Грибная",
        "price": 500,
        "category": "Пицца",
        "description": "Грибы, сыр, соус"
    },

    5: {
        "name": "Пицца Мясная",
        "price": 700,
        "category": "Пицца",
        "description": "Мясо, сыр, овощи"
    },

    6: {
        "name": "Бургер Классический",
        "price": 300,
        "category": "Бургеры",
        "description": "Котлета, салат, соус"
    },

    7: {
        "name": "Чизбургер",
        "price": 350,
        "category": "Бургеры",
        "description": "Котлета, сыр, овощи"
    },

    8: {
        "name": "Двойной бургер",
        "price": 500,
        "category": "Бургеры",
        "description": "Две котлеты, двойной сыр"
    },

    9: {
        "name": "Чикенбургер",
        "price": 320,
        "category": "Бургеры",
        "description": "Курица, салат, соус"
    },

    10: {
        "name": "Бургер BBQ",
        "price": 450,
        "category": "Бургеры",
        "description": "Мясо, BBQ соус, сыр"
    },

    11: {
        "name": "Картошка Фри",
        "price": 150,
        "category": "Закуски",
        "description": "Хрустящая картошка"
    },

    12: {
        "name": "Наггетсы",
        "price": 250,
        "category": "Закуски",
        "description": "Куриные кусочки"
    },

    13: {
        "name": "Крылышки BBQ",
        "price": 400,
        "category": "Закуски",
        "description": "Куриные крылышки"
    },

    14: {
        "name": "Луковые кольца",
        "price": 180,
        "category": "Закуски",
        "description": "Хрустящие кольца"
    },

    15: {
        "name": "Сырные палочки",
        "price": 220,
        "category": "Закуски",
        "description": "Сыр в панировке"
    },

    16: {
        "name": "Кола",
        "price": 100,
        "category": "Напитки",
        "description": "Газированный напиток"
    },

    17: {
        "name": "Спрайт",
        "price": 100,
        "category": "Напитки",
        "description": "Лимонный напиток"
    },

    18: {
        "name": "Фанта",
        "price": 100,
        "category": "Напитки",
        "description": "Апельсиновый напиток"
    },

    19: {
        "name": "Сок Апельсиновый",
        "price": 120,
        "category": "Напитки",
        "description": "Натуральный сок"
    },

    20: {
        "name": "Лимонад",
        "price": 180,
        "category": "Напитки",
        "description": "Домашний лимонад"
    },

    21: {
        "name": "Кофе",
        "price": 150,
        "category": "Напитки",
        "description": "Горячий кофе"
    },

    22: {
        "name": "Капучино",
        "price": 220,
        "category": "Напитки",
        "description": "Кофе с молоком"
    },

    23: {
        "name": "Мороженое",
        "price": 180,
        "category": "Десерты",
        "description": "Сливочное мороженое"
    },

    24: {
        "name": "Шоколадный торт",
        "price": 250,
        "category": "Десерты",
        "description": "Шоколадный десерт"
    },

    25: {
        "name": "Чизкейк",
        "price": 300,
        "category": "Десерты",
        "description": "Классический чизкейк"
    },

    26: {
        "name": "Панкейки",
        "price": 280,
        "category": "Десерты",
        "description": "Панкейки с сиропом"
    },

    27: {
        "name": "Фруктовый салат",
        "price": 250,
        "category": "Десерты",
        "description": "Свежие фрукты"
    },

    28: {
        "name": "Стейк",
        "price": 950,
        "category": "Основные блюда",
        "description": "Мясной стейк"
    },

    29: {
        "name": "Курица с рисом",
        "price": 450,
        "category": "Основные блюда",
        "description": "Курица, рис, овощи"
    },

    30: {
        "name": "Паста Карбонара",
        "price": 500,
        "category": "Основные блюда",
        "description": "Паста с соусом"
    }

}


# ============================================================
#                 ГЛОБАЛЬНЫЕ ДАННЫЕ
# ============================================================

cart = []

orders = []

bookings = []

reviews = []

current_order_number = 1000


# ============================================================
#                 ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ============================================================

def line():

    print("=" * 65)


def title(text):

    line()

    print(text.center(65))

    line()


def pause():

    input("\nНажмите Enter, чтобы продолжить...")


def get_time():

    return datetime.datetime.now().strftime(
        "%d.%m.%Y %H:%M:%S"
    )


def money(value):

    return f"{value:.2f} {CURRENCY}"


# ============================================================
#                 ИНФОРМАЦИЯ О РЕСТОРАНЕ
# ============================================================

def show_restaurant_info():

    title("🍔 ИНФОРМАЦИЯ О РЕСТОРАНЕ 🍔")

    print(f"Название: {restaurant_info['name']}")

    print(f"Адрес: {restaurant_info['address']}")

    print(f"Телефон: {restaurant_info['phone']}")

    print(f"Время работы: {restaurant_info['working_hours']}")

    print(f"Количество столиков: {restaurant_info['tables']}")

    print(f"Рейтинг: {restaurant_info['rating']}")

    print(f"Заказов сегодня: {restaurant_info['orders_today']}")

    print(f"Выручка: {money(restaurant_info['revenue'])}")


# ============================================================
#                 ПОКАЗ МЕНЮ
# ============================================================

def show_menu():

    title("🍕 МЕНЮ РЕСТОРАНА 🍕")

    for number, product in menu.items():

        print(
            f"{number:02d}. "
            f"{product['name']:<25}"
            f"{money(product['price'])}"
        )

    line()


# ============================================================
#                 ПОДРОБНОЕ МЕНЮ
# ============================================================

def detailed_menu():

    title("📋 ПОДРОБНОЕ МЕНЮ")

    for number, product in menu.items():

        print(f"\nНомер: {number}")

        print(f"Название: {product['name']}")

        print(f"Категория: {product['category']}")

        print(f"Цена: {money(product['price'])}")

        print(f"Описание: {product['description']}")

        print("-" * 65)


# ============================================================
#                 ПОИСК БЛЮДА
# ============================================================

def search_food():

    title("🔎 ПОИСК БЛЮДА")

    search = input(
        "Введите название или категорию: "
    ).lower()

    found = False

    for number, product in menu.items():

        if (
            search in product["name"].lower()
            or search in product["category"].lower()
        ):

            print(
                f"{number}. "
                f"{product['name']} — "
                f"{money(product['price'])}"
            )

            found = True

    if not found:

        print("Ничего не найдено.")


# ============================================================
#                 ДОБАВЛЕНИЕ В КОРЗИНУ
# ============================================================

def add_to_cart():

    show_menu()

    try:

        number = int(
            input("Введите номер блюда: ")
        )

        if number not in menu:

            print("Такого блюда нет!")

            return

        quantity = int(
            input("Введите количество: ")
        )

        if quantity <= 0:

            print("Количество должно быть больше нуля!")

            return

        product = menu[number]

        item = {

            "id": number,

            "name": product["name"],

            "price": product["price"],

            "quantity": quantity

        }

        cart.append(item)

        print(
            f"\n✅ {product['name']} добавлено в корзину!"
        )

        print(
            f"Сумма: {money(product['price'] * quantity)}"
        )

    except ValueError:

        print("Ошибка! Введите число.")


# ============================================================
#                 ПРОСМОТР КОРЗИНЫ
# ============================================================

def show_cart():

    title("🛒 ВАША КОРЗИНА")

    if not cart:

        print("Корзина пустая.")

        return

    total = 0

    for index, item in enumerate(cart, start=1):

        item_total = (
            item["price"] * item["quantity"]
        )

        print(
            f"{index}. {item['name']}"
        )

        print(
            f"   Количество: {item['quantity']}"
        )

        print(
            f"   Цена: {money(item['price'])}"
        )

        print(
            f"   Сумма: {money(item_total)}"
        )

        print("-" * 65)

        total += item_total

    print(f"ИТОГО: {money(total)}")


# ============================================================
#                 УДАЛЕНИЕ ИЗ КОРЗИНЫ
# ============================================================

def remove_from_cart():

    if not cart:

        print("Корзина пустая!")

        return

    show_cart()

    try:

        number = int(
            input("Введите номер позиции: ")
        )

        if number < 1 or number > len(cart):

            print("Неверный номер!")

            return

        removed = cart.pop(number - 1)

        print(
            f"❌ {removed['name']} удалено."
        )

    except ValueError:

        print("Введите число!")


# ============================================================
#                 ОЧИСТКА КОРЗИНЫ
# ============================================================

def clear_cart():

    if not cart:

        print("Корзина уже пустая!")

        return

    confirm = input(
        "Очистить корзину? (да/нет): "
    ).lower()

    if confirm == "да":

        cart.clear()

        print("Корзина очищена.")

    else:

        print("Отмена.")


# ============================================================
#                 СКИДКА
# ============================================================

def calculate_discount(total):

    if total >= 3000:

        return total * 0.15

    elif total >= 2000:

        return total * 0.10

    elif total >= 1000:

        return total * 0.05

    return 0


# ============================================================
#                 ДОСТАВКА
# ============================================================

def choose_delivery():

    title("🚚 СПОСОБ ПОЛУЧЕНИЯ")

    print("1. Самовывоз")

    print("2. Доставка")

    choice = input("Выберите: ")

    if choice == "1":

        return "Самовывоз", 0

    elif choice == "2":

        address = input("Введите адрес: ")

        return f"Доставка: {address}", 150

    else:

        print("Неверный выбор!")

        return None, 0


# ============================================================
#                 ОФОРМЛЕНИЕ ЗАКАЗА
# ============================================================

def checkout():

    global current_order_number

    if not cart:

        print("Корзина пустая!")

        return

    title("🧾 ОФОРМЛЕНИЕ ЗАКАЗА")

    name = input("Ваше имя: ")

    phone = input("Ваш телефон: ")

    delivery_type, delivery_price = choose_delivery()

    if delivery_type is None:

        return

    total = sum(
        item["price"] * item["quantity"]
        for item in cart
    )

    discount = calculate_discount(total)

    final_total = (
        total - discount + delivery_price
    )

    print(f"\nСумма блюд: {money(total)}")

    print(f"Скидка: {money(discount)}")

    print(f"Доставка: {money(delivery_price)}")

    print(f"Итого: {money(final_total)}")

    print("\n1. Наличные")

    print("2. Банковская карта")

    payment_choice = input("Способ оплаты: ")

    if payment_choice == "1":

        payment = "Наличные"

    elif payment_choice == "2":

        payment = "Банковская карта"

    else:

        print("Неверный способ оплаты!")

        return

    current_order_number += 1

    order = {

        "number": current_order_number,

        "name": name,

        "phone": phone,

        "items": cart.copy(),

        "total": final_total,

        "date": get_time(),

        "delivery": delivery_type,

        "payment": payment,

        "status": "Принят"

    }

    orders.append(order)

    restaurant_info["orders_today"] += 1

    restaurant_info["revenue"] += final_total

    print("\n" + "=" * 65)

    print("              ✅ ЗАКАЗ ОФОРМЛЕН!")

    print("=" * 65)

    print(f"Номер заказа: #{order['number']}")

    print(f"Клиент: {name}")

    print(f"Сумма: {money(final_total)}")

    print(f"Статус: {order['status']}")

    print("=" * 65)

    cart.clear()


# ============================================================
#                 ИСТОРИЯ ЗАКАЗОВ
# ============================================================

def order_history():

    title("📦 ИСТОРИЯ ЗАКАЗОВ")

    if not orders:

        print("Заказов пока нет.")

        return

    for order in orders:

        print(f"\nЗаказ #{order['number']}")

        print(f"Клиент: {order['name']}")

        print(f"Дата: {order['date']}")

        print(f"Сумма: {money(order['total'])}")

        print(f"Получение: {order['delivery']}")

        print(f"Оплата: {order['payment']}")

        print(f"Статус: {order['status']}")

        print("-" * 65)


# ============================================================
#                 БРОНИРОВАНИЕ СТОЛИКА
# ============================================================

def book_table():

    title("🪑 БРОНИРОВАНИЕ СТОЛИКА")

    name = input("Введите ваше имя: ")

    phone = input("Введите телефон: ")

    date = input(
        "Введите дату (например 20.09.2026): "
    )

    time = input(
        "Введите время (например 19:30): "
    )

    try:

        people = int(
            input("Количество людей: ")
        )

        if people <= 0:

            print("Неверное количество!")

            return

    except ValueError:

        print("Введите число!")

        return

    # Проверка формата даты
    try:

        booking_date = datetime.datetime.strptime(
            date,
            "%d.%m.%Y"
        ).date()

        today = datetime.date.today()

        if booking_date < today:

            print("Нельзя бронировать прошедшую дату!")

            return

    except ValueError:

        print(
            "Неверный формат даты! "
            "Используйте ДД.ММ.ГГГГ"
        )

        return

    # Проверка времени
    try:

        booking_time = datetime.datetime.strptime(
            time,
            "%H:%M"
        ).time()

        if booking_time < datetime.time(10, 0) \
                or booking_time > datetime.time(22, 0):

            print(
                "Ресторан работает с 10:00 до 23:00."
            )

            return

    except ValueError:

        print(
            "Неверный формат времени! "
            "Используйте ЧЧ:ММ"
        )

        return

    # Проверка количества людей
    if people > 12:

        print(
            "Для компании больше 12 человек "
            "позвоните в ресторан."
        )

        return

    # Проверка занятых столиков
    occupied_tables = [

        booking["table"]

        for booking in bookings

        if booking["date"] == date
        and booking["time"] == time

    ]

    free_tables = [

        table

        for table in range(1, 21)

        if table not in occupied_tables

    ]

    if not free_tables:

        print(
            "На это время свободных столиков нет."
        )

        return

    table_number = free_tables[0]

    booking = {

        "number": random.randint(10000, 99999),

        "name": name,

        "phone": phone,

        "date": date,

        "time": time,

        "people": people,

        "table": table_number,

        "status": "Забронирован"

    }

    bookings.append(booking)

    print("\n" + "=" * 65)

    print("       ✅ СТОЛИК УСПЕШНО ЗАБРОНИРОВАН")

    print("=" * 65)

    print(f"Номер брони: #{booking['number']}")

    print(f"Имя: {name}")

    print(f"Телефон: {phone}")

    print(f"Дата: {date}")

    print(f"Время: {time}")

    print(f"Количество людей: {people}")

    print(f"Столик №: {table_number}")

    print(f"Статус: {booking['status']}")

    print("=" * 65)


# ============================================================
#                 ПРОСМОТР БРОНИРОВАНИЙ
# ============================================================

def show_bookings():

    title("📅 ВСЕ БРОНИРОВАНИЯ")

    if not bookings:

        print("Бронирований пока нет.")

        return

    for booking in bookings:

        print(
            f"\nБронь #{booking['number']}"
        )

        print(f"Имя: {booking['name']}")

        print(f"Телефон: {booking['phone']}")

        print(f"Дата: {booking['date']}")

        print(f"Время: {booking['time']}")

        print(f"Людей: {booking['people']}")

        print(f"Столик: №{booking['table']}")

        print(f"Статус: {booking['status']}")

        print("-" * 65)


# ============================================================
#                 ОТМЕНА БРОНИРОВАНИЯ
# ============================================================

def cancel_booking():

    if not bookings:

        print("Бронирований нет.")

        return

    show_bookings()

    try:

        number = int(
            input("Введите номер брони: ")
        )

        for booking in bookings:

            if booking["number"] == number:

                booking["status"] = "Отменён"

                print("Бронирование отменено!")

                return

        print("Бронь не найдена.")

    except ValueError:

        print("Введите число!")


# ============================================================
#                 ОЦЕНКА РЕСТОРАНА
# ============================================================

def rate_restaurant():

    title("⭐ ОЦЕНКА РЕСТОРАНА")

    name = input("Ваше имя: ")

    try:

        rating = int(
            input("Оценка от 1 до 5: ")
        )

        if rating < 1 or rating > 5:

            print("Оценка должна быть от 1 до 5!")

            return

    except ValueError:

        print("Введите число!")

        return

    comment = input("Ваш комментарий: ")

    review = {

        "name": name,

        "rating": rating,

        "comment": comment,

        "date": get_time()

    }

    reviews.append(review)

    print("\nСпасибо за вашу оценку!")

    print(f"Оценка: {rating}/5")

    print(f"Комментарий: {comment}")


# ============================================================
#                 ПРОСМОТР ОТЗЫВОВ
# ============================================================

def show_reviews():

    title("⭐ ОТЗЫВЫ КЛИЕНТОВ")

    if not reviews:

        print("Отзывов пока нет.")

        return

    for review in reviews:

        print(f"\nИмя: {review['name']}")

        print(f"Оценка: {review['rating']}/5")

        print(f"Комментарий: {review['comment']}")

        print(f"Дата: {review['date']}")

        print("-" * 65)


# ============================================================
#                 ГЛАВНОЕ МЕНЮ
# ============================================================

def main_menu():

    while True:

        title("🍔 TASTY FOOD RESTAURANT 🍔")

        print("1. Посмотреть меню")

        print("2. Подробное меню")

        print("3. Поиск блюда")

        print("4. Добавить блюдо")

        print("5. Посмотреть корзину")

        print("6. Удалить блюдо")

        print("7. Очистить корзину")

        print("8. Оформить заказ")

        print("9. История заказов")

        print("10. Забронировать столик")

        print("11. Посмотреть бронирования")

        print("12. Отменить бронирование")

        print("13. Оценить ресторан")

        print("14. Посмотреть отзывы")

        print("15. Информация о ресторане")

        print("16. Выход")

        line()

        choice = input("Выберите действие: ")

        if choice == "1":

            show_menu()

        elif choice == "2":

            detailed_menu()

        elif choice == "3":

            search_food()

        elif choice == "4":

            add_to_cart()

        elif choice == "5":

            show_cart()

        elif choice == "6":

            remove_from_cart()

        elif choice == "7":

            clear_cart()

        elif choice == "8":

            checkout()

        elif choice == "9":

            order_history()

        elif choice == "10":

            book_table()

        elif choice == "11":

            show_bookings()

        elif choice == "12":

            cancel_booking()

        elif choice == "13":

            rate_restaurant()

        elif choice == "14":

            show_reviews()

        elif choice == "15":

            show_restaurant_info()

        elif choice == "16":

            print("Спасибо за посещение!")

            break

        else:

            print("Неверный выбор!")


# ============================================================
#                 ЗАПУСК ПРОГРАММЫ
# ============================================================

def main():

    print("=" * 65)

    print("        🍔 ДОБРО ПОЖАЛОВАТЬ В TASTY FOOD 🍔")

    print("=" * 65)

    print("Режим: Ресторан")

    print("Регистрация отключена.")

    print("=" * 65)

    main_menu()


if __name__ == "__main__":

    main()

# ============================================================
#                  🍔 TASTY FOOD RESTAURANT 🍔
# ============================================================
#                 БОЛЬШОЙ ПРОЕКТ НА PYTHON
# ============================================================

import datetime
import random


# ============================================================
#                 НАСТРОЙКИ РЕСТОРАНА
# ============================================================

RESTAURANT_NAME = "TASTY FOOD"
RESTAURANT_ADDRESS = "Бишкек, Кыргызстан"
RESTAURANT_PHONE = "+996 555 123 456"
CURRENCY = "сом"


# ============================================================
#                 ДАННЫЕ РЕСТОРАНА
# ============================================================

restaurant_info = {

    "name": RESTAURANT_NAME,

    "address": RESTAURANT_ADDRESS,

    "phone": RESTAURANT_PHONE,

    "working_hours": "10:00 - 23:00",

    "tables": 20,

    "rating": 4.8,

    "orders_today": 0,

    "revenue": 0

}


# ============================================================
#                 МЕНЮ РЕСТОРАНА
# ============================================================

menu = {

    1: {
        "name": "Пицца Маргарита",
        "price": 450,
        "category": "Пицца",
        "description": "Томатный соус, сыр, базилик"
    },

    2: {
        "name": "Пицца Пепперони",
        "price": 550,
        "category": "Пицца",
        "description": "Сыр, пепперони, томатный соус"
    },

    3: {
        "name": "Пицца Четыре сыра",
        "price": 650,
        "category": "Пицца",
        "description": "Моцарелла, чеддер, пармезан"
    },

    4: {
        "name": "Пицца Грибная",
        "price": 500,
        "category": "Пицца",
        "description": "Грибы, сыр, соус"
    },

    5: {
        "name": "Пицца Мясная",
        "price": 700,
        "category": "Пицца",
        "description": "Мясо, сыр, овощи"
    },

    6: {
        "name": "Бургер Классический",
        "price": 300,
        "category": "Бургеры",
        "description": "Котлета, салат, соус"
    },

    7: {
        "name": "Чизбургер",
        "price": 350,
        "category": "Бургеры",
        "description": "Котлета, сыр, овощи"
    },

    8: {
        "name": "Двойной бургер",
        "price": 500,
        "category": "Бургеры",
        "description": "Две котлеты, двойной сыр"
    },

    9: {
        "name": "Чикенбургер",
        "price": 320,
        "category": "Бургеры",
        "description": "Курица, салат, соус"
    },

    10: {
        "name": "Бургер BBQ",
        "price": 450,
        "category": "Бургеры",
        "description": "Мясо, BBQ соус, сыр"
    },

    11: {
        "name": "Картошка Фри",
        "price": 150,
        "category": "Закуски",
        "description": "Хрустящая картошка"
    },

    12: {
        "name": "Наггетсы",
        "price": 250,
        "category": "Закуски",
        "description": "Куриные кусочки"
    },

    13: {
        "name": "Крылышки BBQ",
        "price": 400,
        "category": "Закуски",
        "description": "Куриные крылышки"
    },

    14: {
        "name": "Луковые кольца",
        "price": 180,
        "category": "Закуски",
        "description": "Хрустящие кольца"
    },

    15: {
        "name": "Сырные палочки",
        "price": 220,
        "category": "Закуски",
        "description": "Сыр в панировке"
    },

    16: {
        "name": "Кола",
        "price": 100,
        "category": "Напитки",
        "description": "Газированный напиток"
    },

    17: {
        "name": "Спрайт",
        "price": 100,
        "category": "Напитки",
        "description": "Лимонный напиток"
    },

    18: {
        "name": "Фанта",
        "price": 100,
        "category": "Напитки",
        "description": "Апельсиновый напиток"
    },

    19: {
        "name": "Сок Апельсиновый",
        "price": 120,
        "category": "Напитки",
        "description": "Натуральный сок"
    },

    20: {
        "name": "Лимонад",
        "price": 180,
        "category": "Напитки",
        "description": "Домашний лимонад"
    },

    21: {
        "name": "Кофе",
        "price": 150,
        "category": "Напитки",
        "description": "Горячий кофе"
    },

    22: {
        "name": "Капучино",
        "price": 220,
        "category": "Напитки",
        "description": "Кофе с молоком"
    },

    23: {
        "name": "Мороженое",
        "price": 180,
        "category": "Десерты",
        "description": "Сливочное мороженое"
    },

    24: {
        "name": "Шоколадный торт",
        "price": 250,
        "category": "Десерты",
        "description": "Шоколадный десерт"
    },

    25: {
        "name": "Чизкейк",
        "price": 300,
        "category": "Десерты",
        "description": "Классический чизкейк"
    },

    26: {
        "name": "Панкейки",
        "price": 280,
        "category": "Десерты",
        "description": "Панкейки с сиропом"
    },

    27: {
        "name": "Фруктовый салат",
        "price": 250,
        "category": "Десерты",
        "description": "Свежие фрукты"
    },

    28: {
        "name": "Стейк",
        "price": 950,
        "category": "Основные блюда",
        "description": "Мясной стейк"
    },

    29: {
        "name": "Курица с рисом",
        "price": 450,
        "category": "Основные блюда",
        "description": "Курица, рис, овощи"
    },

    30: {
        "name": "Паста Карбонара",
        "price": 500,
        "category": "Основные блюда",
        "description": "Паста с соусом"
    }

}


# ============================================================
#                 ГЛОБАЛЬНЫЕ ДАННЫЕ
# ============================================================

cart = []

orders = []

bookings = []

reviews = []

current_order_number = 1000


# ============================================================
#                 ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ============================================================

def line():

    print("=" * 65)


def title(text):

    line()

    print(text.center(65))

    line()


def pause():

    input("\nНажмите Enter, чтобы продолжить...")


def get_time():

    return datetime.datetime.now().strftime(
        "%d.%m.%Y %H:%M:%S"
    )


def money(value):

    return f"{value:.2f} {CURRENCY}"


# ============================================================
#                 ИНФОРМАЦИЯ О РЕСТОРАНЕ
# ============================================================

def show_restaurant_info():

    title("🍔 ИНФОРМАЦИЯ О РЕСТОРАНЕ 🍔")

    print(f"Название: {restaurant_info['name']}")

    print(f"Адрес: {restaurant_info['address']}")

    print(f"Телефон: {restaurant_info['phone']}")

    print(f"Время работы: {restaurant_info['working_hours']}")

    print(f"Количество столиков: {restaurant_info['tables']}")

    print(f"Рейтинг: {restaurant_info['rating']}")

    print(f"Заказов сегодня: {restaurant_info['orders_today']}")

    print(f"Выручка: {money(restaurant_info['revenue'])}")


# ============================================================
#                 ПОКАЗ МЕНЮ
# ============================================================

def show_menu():

    title("🍕 МЕНЮ РЕСТОРАНА 🍕")

    for number, product in menu.items():

        print(
            f"{number:02d}. "
            f"{product['name']:<25}"
            f"{money(product['price'])}"
        )

    line()


# ============================================================
#                 ПОДРОБНОЕ МЕНЮ
# ============================================================

def detailed_menu():

    title("📋 ПОДРОБНОЕ МЕНЮ")

    for number, product in menu.items():

        print(f"\nНомер: {number}")

        print(f"Название: {product['name']}")

        print(f"Категория: {product['category']}")

        print(f"Цена: {money(product['price'])}")

        print(f"Описание: {product['description']}")

        print("-" * 65)


# ============================================================
#                 ПОИСК БЛЮДА
# ============================================================

def search_food():

    title("🔎 ПОИСК БЛЮДА")

    search = input(
        "Введите название или категорию: "
    ).lower()

    found = False

    for number, product in menu.items():

        if (
            search in product["name"].lower()
            or search in product["category"].lower()
        ):

            print(
                f"{number}. "
                f"{product['name']} — "
                f"{money(product['price'])}"
            )

            found = True

    if not found:

        print("Ничего не найдено.")


# ============================================================
#                 ДОБАВЛЕНИЕ В КОРЗИНУ
# ============================================================

def add_to_cart():

    show_menu()

    try:

        number = int(
            input("Введите номер блюда: ")
        )

        if number not in menu:

            print("Такого блюда нет!")

            return

        quantity = int(
            input("Введите количество: ")
        )

        if quantity <= 0:

            print("Количество должно быть больше нуля!")

            return

        product = menu[number]

        item = {

            "id": number,

            "name": product["name"],

            "price": product["price"],

            "quantity": quantity

        }

        cart.append(item)

        print(
            f"\n✅ {product['name']} добавлено в корзину!"
        )

        print(
            f"Сумма: {money(product['price'] * quantity)}"
        )

    except ValueError:

        print("Ошибка! Введите число.")


# ============================================================
#                 ПРОСМОТР КОРЗИНЫ
# ============================================================

def show_cart():

    title("🛒 ВАША КОРЗИНА")

    if not cart:

        print("Корзина пустая.")

        return

    total = 0

    for index, item in enumerate(cart, start=1):

        item_total = (
            item["price"] * item["quantity"]
        )

        print(
            f"{index}. {item['name']}"
        )

        print(
            f"   Количество: {item['quantity']}"
        )

        print(
            f"   Цена: {money(item['price'])}"
        )

        print(
            f"   Сумма: {money(item_total)}"
        )

        print("-" * 65)

        total += item_total

    print(f"ИТОГО: {money(total)}")


# ============================================================
#                 УДАЛЕНИЕ ИЗ КОРЗИНЫ
# ============================================================

def remove_from_cart():

    if not cart:

        print("Корзина пустая!")

        return

    show_cart()

    try:

        number = int(
            input("Введите номер позиции: ")
        )

        if number < 1 or number > len(cart):

            print("Неверный номер!")

            return

        removed = cart.pop(number - 1)

        print(
            f"❌ {removed['name']} удалено."
        )

    except ValueError:

        print("Введите число!")


# ============================================================
#                 ОЧИСТКА КОРЗИНЫ
# ============================================================

def clear_cart():

    if not cart:

        print("Корзина уже пустая!")

        return

    confirm = input(
        "Очистить корзину? (да/нет): "
    ).lower()

    if confirm == "да":

        cart.clear()

        print("Корзина очищена.")

    else:

        print("Отмена.")


# ============================================================
#                 СКИДКА
# ============================================================

def calculate_discount(total):

    if total >= 3000:

        return total * 0.15

    elif total >= 2000:

        return total * 0.10

    elif total >= 1000:

        return total * 0.05

    return 0


# ============================================================
#                 ДОСТАВКА
# ============================================================

def choose_delivery():

    title("🚚 СПОСОБ ПОЛУЧЕНИЯ")

    print("1. Самовывоз")

    print("2. Доставка")

    choice = input("Выберите: ")

    if choice == "1":

        return "Самовывоз", 0

    elif choice == "2":

        address = input("Введите адрес: ")

        return f"Доставка: {address}", 150

    else:

        print("Неверный выбор!")

        return None, 0


# ============================================================
#                 ОФОРМЛЕНИЕ ЗАКАЗА
# ============================================================

def checkout():

    global current_order_number

    if not cart:

        print("Корзина пустая!")

        return

    title("🧾 ОФОРМЛЕНИЕ ЗАКАЗА")

    name = input("Ваше имя: ")

    phone = input("Ваш телефон: ")

    delivery_type, delivery_price = choose_delivery()

    if delivery_type is None:

        return

    total = sum(
        item["price"] * item["quantity"]
        for item in cart
    )

    discount = calculate_discount(total)

    final_total = (
        total - discount + delivery_price
    )

    print(f"\nСумма блюд: {money(total)}")

    print(f"Скидка: {money(discount)}")

    print(f"Доставка: {money(delivery_price)}")

    print(f"Итого: {money(final_total)}")

    print("\n1. Наличные")

    print("2. Банковская карта")

    payment_choice = input("Способ оплаты: ")

    if payment_choice == "1":

        payment = "Наличные"

    elif payment_choice == "2":

        payment = "Банковская карта"

    else:

        print("Неверный способ оплаты!")

        return

    current_order_number += 1

    order = {

        "number": current_order_number,

        "name": name,

        "phone": phone,

        "items": cart.copy(),

        "total": final_total,

        "date": get_time(),

        "delivery": delivery_type,

        "payment": payment,

        "status": "Принят"

    }

    orders.append(order)

    restaurant_info["orders_today"] += 1

    restaurant_info["revenue"] += final_total

    print("\n" + "=" * 65)

    print("              ✅ ЗАКАЗ ОФОРМЛЕН!")

    print("=" * 65)

    print(f"Номер заказа: #{order['number']}")

    print(f"Клиент: {name}")

    print(f"Сумма: {money(final_total)}")

    print(f"Статус: {order['status']}")

    print("=" * 65)

    cart.clear()


# ============================================================
#                 ИСТОРИЯ ЗАКАЗОВ
# ============================================================

def order_history():

    title("📦 ИСТОРИЯ ЗАКАЗОВ")

    if not orders:

        print("Заказов пока нет.")

        return

    for order in orders:

        print(f"\nЗаказ #{order['number']}")

        print(f"Клиент: {order['name']}")

        print(f"Дата: {order['date']}")

        print(f"Сумма: {money(order['total'])}")

        print(f"Получение: {order['delivery']}")

        print(f"Оплата: {order['payment']}")

        print(f"Статус: {order['status']}")

        print("-" * 65)


# ============================================================
#                 БРОНИРОВАНИЕ СТОЛИКА
# ============================================================

def book_table():

    title("🪑 БРОНИРОВАНИЕ СТОЛИКА")

    name = input("Введите ваше имя: ")

    phone = input("Введите телефон: ")

    date = input(
        "Введите дату (например 20.09.2026): "
    )

    time = input(
        "Введите время (например 19:30): "
    )

    try:

        people = int(
            input("Количество людей: ")
        )

        if people <= 0:

            print("Неверное количество!")

            return

    except ValueError:

        print("Введите число!")

        return

    # Проверка формата даты
    try:

        booking_date = datetime.datetime.strptime(
            date,
            "%d.%m.%Y"
        ).date()

        today = datetime.date.today()

        if booking_date < today:

            print("Нельзя бронировать прошедшую дату!")

            return

    except ValueError:

        print(
            "Неверный формат даты! "
            "Используйте ДД.ММ.ГГГГ"
        )

        return

    # Проверка времени
    try:

        booking_time = datetime.datetime.strptime(
            time,
            "%H:%M"
        ).time()

        if booking_time < datetime.time(10, 0) \
                or booking_time > datetime.time(22, 0):

            print(
                "Ресторан работает с 10:00 до 23:00."
            )

            return

    except ValueError:

        print(
            "Неверный формат времени! "
            "Используйте ЧЧ:ММ"
        )

        return

    # Проверка количества людей
    if people > 12:

        print(
            "Для компании больше 12 человек "
            "позвоните в ресторан."
        )

        return

    # Проверка занятых столиков
    occupied_tables = [

        booking["table"]

        for booking in bookings

        if booking["date"] == date
        and booking["time"] == time

    ]

    free_tables = [

        table

        for table in range(1, 21)

        if table not in occupied_tables

    ]

    if not free_tables:

        print(
            "На это время свободных столиков нет."
        )

        return

    table_number = free_tables[0]

    booking = {

        "number": random.randint(10000, 99999),

        "name": name,

        "phone": phone,

        "date": date,

        "time": time,

        "people": people,

        "table": table_number,

        "status": "Забронирован"

    }

    bookings.append(booking)

    print("\n" + "=" * 65)

    print("       ✅ СТОЛИК УСПЕШНО ЗАБРОНИРОВАН")

    print("=" * 65)

    print(f"Номер брони: #{booking['number']}")

    print(f"Имя: {name}")

    print(f"Телефон: {phone}")

    print(f"Дата: {date}")

    print(f"Время: {time}")

    print(f"Количество людей: {people}")

    print(f"Столик №: {table_number}")

    print(f"Статус: {booking['status']}")

    print("=" * 65)


# ============================================================
#                 ПРОСМОТР БРОНИРОВАНИЙ
# ============================================================

def show_bookings():

    title("📅 ВСЕ БРОНИРОВАНИЯ")

    if not bookings:

        print("Бронирований пока нет.")

        return

    for booking in bookings:

        print(
            f"\nБронь #{booking['number']}"
        )

        print(f"Имя: {booking['name']}")

        print(f"Телефон: {booking['phone']}")

        print(f"Дата: {booking['date']}")

        print(f"Время: {booking['time']}")

        print(f"Людей: {booking['people']}")

        print(f"Столик: №{booking['table']}")

        print(f"Статус: {booking['status']}")

        print("-" * 65)


# ============================================================
#                 ОТМЕНА БРОНИРОВАНИЯ
# ============================================================

def cancel_booking():

    if not bookings:

        print("Бронирований нет.")

        return

    show_bookings()

    try:

        number = int(
            input("Введите номер брони: ")
        )

        for booking in bookings:

            if booking["number"] == number:

                booking["status"] = "Отменён"

                print("Бронирование отменено!")

                return

        print("Бронь не найдена.")

    except ValueError:

        print("Введите число!")


# ============================================================
#                 ОЦЕНКА РЕСТОРАНА
# ============================================================

def rate_restaurant():

    title("⭐ ОЦЕНКА РЕСТОРАНА")

    name = input("Ваше имя: ")

    try:

        rating = int(
            input("Оценка от 1 до 5: ")
        )

        if rating < 1 or rating > 5:

            print("Оценка должна быть от 1 до 5!")

            return

    except ValueError:

        print("Введите число!")

        return

    comment = input("Ваш комментарий: ")

    review = {

        "name": name,

        "rating": rating,

        "comment": comment,

        "date": get_time()

    }

    reviews.append(review)

    print("\nСпасибо за вашу оценку!")

    print(f"Оценка: {rating}/5")

    print(f"Комментарий: {comment}")


# ============================================================
#                 ПРОСМОТР ОТЗЫВОВ
# ============================================================

def show_reviews():

    title("⭐ ОТЗЫВЫ КЛИЕНТОВ")

    if not reviews:

        print("Отзывов пока нет.")

        return

    for review in reviews:

        print(f"\nИмя: {review['name']}")

        print(f"Оценка: {review['rating']}/5")

        print(f"Комментарий: {review['comment']}")

        print(f"Дата: {review['date']}")

        print("-" * 65)


# ============================================================
#                 ГЛАВНОЕ МЕНЮ
# ============================================================

def main_menu():

    while True:

        title("🍔 TASTY FOOD RESTAURANT 🍔")

        print("1. Посмотреть меню")

        print("2. Подробное меню")

        print("3. Поиск блюда")

        print("4. Добавить блюдо")

        print("5. Посмотреть корзину")

        print("6. Удалить блюдо")

        print("7. Очистить корзину")

        print("8. Оформить заказ")

        print("9. История заказов")

        print("10. Забронировать столик")

        print("11. Посмотреть бронирования")

        print("12. Отменить бронирование")

        print("13. Оценить ресторан")

        print("14. Посмотреть отзывы")

        print("15. Информация о ресторане")

        print("16. Выход")

        line()

        choice = input("Выберите действие: ")

        if choice == "1":

            show_menu()

        elif choice == "2":

            detailed_menu()

        elif choice == "3":

            search_food()

        elif choice == "4":

            add_to_cart()

        elif choice == "5":

            show_cart()

        elif choice == "6":

            remove_from_cart()

        elif choice == "7":

            clear_cart()

        elif choice == "8":

            checkout()

        elif choice == "9":

            order_history()

        elif choice == "10":

            book_table()

        elif choice == "11":

            show_bookings()

        elif choice == "12":

            cancel_booking()

        elif choice == "13":

            rate_restaurant()

        elif choice == "14":

            show_reviews()

        elif choice == "15":

            show_restaurant_info()

        elif choice == "16":

            print("Спасибо за посещение!")

            break

        else:

            print("Неверный выбор!")


# ============================================================
#                 ЗАПУСК ПРОГРАММЫ
# ============================================================

def main():

    print("=" * 65)

    print("        🍔 ДОБРО ПОЖАЛОВАТЬ В TASTY FOOD 🍔")

    print("=" * 65)

    print("Режим: Ресторан")

    print("Регистрация отключена.")

    print("=" * 65)

    main_menu()


if __name__ == "__main__":

    main()