# ==================================================
#              🍔 TASTY FOOD RESTAURANT 🍔
#              БОЛЬШОЙ ПРОЕКТ НА PYTHON
# ==================================================

import datetime
import random

# ==================================================
# НАСТРОЙКИ РЕСТОРАНА
# ==================================================

restaurant_name = "Tasty Food"
restaurant_address = "Бишкек, Кыргызстан"
restaurant_phone = "+996 555 123 456"

currency = "сом"

# ==================================================
# ПОЛЬЗОВАТЕЛИ
# ==================================================

users = {
    "admin": {
        "password": "admin123",
        "name": "Администратор",
        "phone": "+996 700 000 000",
        "orders": []
    }
}

current_user = None

# ==================================================
# МЕНЮ РЕСТОРАНА
# ==================================================

menu = {

    1: {
        "name": "Пицца Маргарита",
        "price": 450,
        "category": "Пицца",
        "description": "Томатный соус, сыр и базилик",
        "available": True
    },

    2: {
        "name": "Пицца Пепперони",
        "price": 550,
        "category": "Пицца",
        "description": "Сыр, пепперони и томатный соус",
        "available": True
    },

    3: {
        "name": "Пицца Четыре сыра",
        "price": 650,
        "category": "Пицца",
        "description": "Четыре вида сыра",
        "available": True
    },

    4: {
        "name": "Бургер Классический",
        "price": 300,
        "category": "Бургеры",
        "description": "Котлета, сыр, салат и соус",
        "available": True
    },

    5: {
        "name": "Чизбургер",
        "price": 350,
        "category": "Бургеры",
        "description": "Бургер с сыром и овощами",
        "available": True
    },

    6: {
        "name": "Двойной бургер",
        "price": 500,
        "category": "Бургеры",
        "description": "Две котлеты и двойной сыр",
        "available": True
    },

    7: {
        "name": "Картошка Фри",
        "price": 150,
        "category": "Закуски",
        "description": "Хрустящая картошка",
        "available": True
    },

    8: {
        "name": "Куриные Наггетсы",
        "price": 250,
        "category": "Закуски",
        "description": "Куриные кусочки в панировке",
        "available": True
    },

    9: {
        "name": "Крылышки BBQ",
        "price": 400,
        "category": "Закуски",
        "description": "Куриные крылышки с соусом",
        "available": True
    },

    10: {
        "name": "Кола",
        "price": 100,
        "category": "Напитки",
        "description": "Газированный напиток",
        "available": True
    },

    11: {
        "name": "Сок Апельсиновый",
        "price": 120,
        "category": "Напитки",
        "description": "Апельсиновый сок",
        "available": True
    },

    12: {
        "name": "Лимонад",
        "price": 180,
        "category": "Напитки",
        "description": "Освежающий лимонад",
        "available": True
    },

    13: {
        "name": "Мороженое",
        "price": 180,
        "category": "Десерты",
        "description": "Сливочное мороженое",
        "available": True
    },

    14: {
        "name": "Шоколадный торт",
        "price": 250,
        "category": "Десерты",
        "description": "Нежный шоколадный десерт",
        "available": True
    },

    15: {
        "name": "Чизкейк",
        "price": 300,
        "category": "Десерты",
        "description": "Классический чизкейк",
        "available": True
    }
}

# ==================================================
# КОРЗИНА
# ==================================================

cart = []

# ==================================================
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ==================================================

def line():
    print("=" * 60)


def pause():
    input("\nНажмите Enter, чтобы продолжить...")


def get_total():
    total = 0

    for item in cart:
        total += item["price"] * item["quantity"]

    return total


def get_order_count():
    return len(cart)


def clear_screen():
    print("\n" * 2)


# ==================================================
# РЕГИСТРАЦИЯ
# ==================================================

def register():

    line()
    print("                 РЕГИСТРАЦИЯ")
    line()

    username = input("Придумайте логин: ").strip()

    if username == "":
        print("Логин не может быть пустым!")
        return

    if username in users:
        print("Такой пользователь уже существует!")
        return

    password = input("Придумайте пароль: ").strip()

    if len(password) < 4:
        print("Пароль должен содержать минимум 4 символа!")
        return

    name = input("Введите ваше имя: ")
    phone = input("Введите номер телефона: ")

    users[username] = {
        "password": password,
        "name": name,
        "phone": phone,
        "orders": []
    }

    print("\n✅ Регистрация успешно завершена!")
    print(f"Добро пожаловать, {name}!")


# ==================================================
# ВХОД
# ==================================================

def login():

    global current_user

    line()
    print("                    ВХОД")
    line()

    username = input("Логин: ")
    password = input("Пароль: ")

    if username in users:

        if users[username]["password"] == password:

            current_user = username

            print("\n✅ Вы успешно вошли!")
            print(
                f"Привет, {users[username]['name']}!"
            )

            return True

    print("\n❌ Неверный логин или пароль!")

    return False


# ==================================================
# ВЫХОД ИЗ АККАУНТА
# ==================================================

def logout():

    global current_user

    current_user = None
    cart.clear()

    print("\nВы вышли из аккаунта.")


# ==================================================
# ПОКАЗ МЕНЮ
# ==================================================

def show_menu():

    line()
    print("                 🍔 МЕНЮ РЕСТОРАНА")
    line()

    for number, product in menu.items():

        if product["available"]:

            print(
                f"{number}. "
                f"{product['name']:<25}"
                f"{product['price']} {currency}"
            )

    line()


# ==================================================
# ПОДРОБНОЕ МЕНЮ
# ==================================================

def detailed_menu():

    line()
    print("              ПОДРОБНОЕ МЕНЮ")
    line()

    for number, product in menu.items():

        if product["available"]:

            print(f"\nНомер: {number}")
            print(f"Название: {product['name']}")
            print(f"Категория: {product['category']}")
            print(f"Цена: {product['price']} {currency}")
            print(f"Описание: {product['description']}")

            print("-" * 60)


# ==================================================
# ПОИСК БЛЮДА
# ==================================================

def search_food():

    line()
    print("                 ПОИСК БЛЮДА")
    line()

    search = input("Введите название или категорию: ").lower()

    found = False

    for number, product in menu.items():

        if search in product["name"].lower() \
                or search in product["category"].lower():

            print(
                f"{number}. "
                f"{product['name']} — "
                f"{product['price']} {currency}"
            )

            found = True

    if not found:
        print("Ничего не найдено.")


# ==================================================
# ФИЛЬТР ПО КАТЕГОРИИ
# ==================================================

def category_menu():

    line()
    print("               КАТЕГОРИИ")
    line()

    print("1. Пицца")
    print("2. Бургеры")
    print("3. Закуски")
    print("4. Напитки")
    print("5. Десерты")

    choice = input("Выберите категорию: ")

    categories = {
        "1": "Пицца",
        "2": "Бургеры",
        "3": "Закуски",
        "4": "Напитки",
        "5": "Десерты"
    }

    if choice not in categories:
        print("Неверная категория!")
        return

    selected_category = categories[choice]

    line()
    print(f"КАТЕГОРИЯ: {selected_category}")
    line()

    for number, product in menu.items():

        if product["category"] == selected_category:

            print(
                f"{number}. "
                f"{product['name']} — "
                f"{product['price']} {currency}"
            )


# ==================================================
# ДОБАВЛЕНИЕ В КОРЗИНУ
# ==================================================

def add_to_cart():

    show_menu()

    try:

        choice = int(
            input("\nВведите номер блюда: ")
        )

        if choice not in menu:
            print("Такого блюда нет!")
            return

        product = menu[choice]

        if not product["available"]:
            print("Это блюдо сейчас недоступно!")
            return

        quantity = int(
            input("Введите количество: ")
        )

        if quantity <= 0:
            print("Количество должно быть больше нуля!")
            return

        item = {
            "id": choice,
            "name": product["name"],
            "price": product["price"],
            "quantity": quantity
        }

        cart.append(item)

        print(
            f"\n✅ {product['name']} добавлено!"
        )

        print(
            f"Сумма: "
            f"{product['price'] * quantity} {currency}"
        )

    except ValueError:

        print("Ошибка! Введите число.")


# ==================================================
# ПРОСМОТР КОРЗИНЫ
# ==================================================

def show_cart():

    line()
    print("                  🛒 КОРЗИНА")
    line()

    if not cart:

        print("Корзина пустая.")
        return

    for index, item in enumerate(cart, start=1):

        item_total = item["price"] * item["quantity"]

        print(
            f"{index}. {item['name']}"
        )

        print(
            f"   Цена: {item['price']} {currency}"
        )

        print(
            f"   Количество: {item['quantity']}"
        )

        print(
            f"   Сумма: {item_total} {currency}"
        )

        print("-" * 60)

    print(f"ВСЕГО: {get_total()} {currency}")


# ==================================================
# УДАЛЕНИЕ ИЗ КОРЗИНЫ
# ==================================================

def remove_from_cart():

    if not cart:

        print("Корзина пустая!")
        return

    show_cart()

    try:

        number = int(
            input("\nВведите номер позиции: ")
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


# ==================================================
# ОЧИСТКА КОРЗИНЫ
# ==================================================

def clear_cart():

    if not cart:

        print("Корзина уже пустая!")
        return

    confirm = input(
        "Вы точно хотите очистить корзину? (да/нет): "
    ).lower()

    if confirm == "да":

        cart.clear()

        print("Корзина очищена.")

    else:

        print("Отмена.")


# ==================================================
# СКИДКА
# ==================================================

def calculate_discount(total):

    if total >= 3000:

        discount = total * 0.15

    elif total >= 2000:

        discount = total * 0.10

    elif total >= 1000:

        discount = total * 0.05

    else:

        discount = 0

    return discount


# ==================================================
# ДОСТАВКА
# ==================================================

def delivery():

    line()
    print("                 🚚 ДОСТАВКА")
    line()

    print("1. Самовывоз")
    print("2. Доставка по Бишкеку")

    choice = input("Выберите способ получения: ")

    if choice == "1":

        print("Вы выбрали самовывоз.")
        return "Самовывоз", 0

    elif choice == "2":

        address = input("Введите адрес доставки: ")

        print(f"Адрес: {address}")

        return "Доставка", 150

    else:

        print("Неверный выбор!")

        return None, 0


# ==================================================
# ОФОРМЛЕНИЕ ЗАКАЗА
# ==================================================

def checkout():

    if not cart:

        print("\nКорзина пустая!")
        return

    line()
    print("                ОФОРМЛЕНИЕ ЗАКАЗА")
    line()

    total = get_total()

    discount = calculate_discount(total)

    delivery_type, delivery_price = delivery()

    if delivery_type is None:

        return

    final_total = total - discount + delivery_price

    print("\n" + "=" * 60)

    print("                    ЧЕК")

    print("=" * 60)

    print(f"Ресторан: {restaurant_name}")
    print(f"Адрес: {restaurant_address}")
    print(f"Телефон: {restaurant_phone}")

    print("-" * 60)

    print(f"Клиент: {users[current_user]['name']}")

    print("-" * 60)

    for item in cart:

        print(
            f"{item['name']} "
            f"x{item['quantity']} — "
            f"{item['price'] * item['quantity']} {currency}"
        )

    print("-" * 60)

    print(f"Сумма блюд: {total} {currency}")
    print(f"Скидка: {discount} {currency}")
    print(f"Доставка: {delivery_price} {currency}")

    print("-" * 60)

    print(
        f"ИТОГО: {final_total} {currency}"
    )

    print("=" * 60)

    print("1. Наличные")
    print("2. Банковская карта")

    payment = input("Способ оплаты: ")

    if payment == "1":

        payment_name = "Наличные"

    elif payment == "2":

        payment_name = "Банковская карта"

    else:

        print("Неверный способ оплаты!")

        return

    order = {

        "number": random.randint(10000, 99999),

        "items": cart.copy(),

        "total": final_total,

        "date": datetime.datetime.now().strftime(
            "%d.%m.%Y %H:%M"
        ),

        "delivery": delivery_type,

        "payment": payment_name

    }

    users[current_user]["orders"].append(order)

    print("\n✅ Заказ успешно оформлен!")

    print(
        f"Номер заказа: #{order['number']}"
    )

    print(
        f"Статус: Принят"
    )

    cart.clear()


# ==================================================
# ИСТОРИЯ ЗАКАЗОВ
# ==================================================

def order_history():

    line()
    print("                ИСТОРИЯ ЗАКАЗОВ")
    line()

    orders = users[current_user]["orders"]

    if not orders:

        print("У вас пока нет заказов.")
        return

    for order in orders:

        print(
            f"\nЗаказ #{order['number']}"
        )

        print(
            f"Дата: {order['date']}"
        )

        print(
            f"Сумма: {order['total']} {currency}"
        )

        print(
            f"Получение: {order['delivery']}"
        )

        print(
            f"Оплата: {order['payment']}"
        )

        print(
            "Статус: Завершён"
        )

        print("-" * 60)


# ==================================================
# ЛИЧНЫЙ КАБИНЕТ
# ==================================================

def profile():

    line()
    print("                 ЛИЧНЫЙ КАБИНЕТ")
    line()

    user = users[current_user]

    print(f"Логин: {current_user}")
    print(f"Имя: {user['name']}")
    print(f"Телефон: {user['phone']}")

    print(
        f"Количество заказов: {len(user['orders'])}"
    )


# ==================================================
# БРОНИРОВАНИЕ СТОЛИКА
# ==================================================

def book_table():

    line()
    print("                 БРОНИРОВАНИЕ СТОЛИКА")
    line()

    name = input("Введите имя: ")

    date = input(
        "Введите дату бронирования: "
    )

    time = input(
        "Введите время: "
    )

    try:

        people = int(
            input("Количество людей: ")
        )

        if people <= 0:

            print("Количество людей должно быть больше нуля!")
            return

    except ValueError:

        print("Введите число!")
        return

    table_number = random.randint(1, 20)

    print("\n✅ Столик забронирован!")

    print(f"Имя: {name}")
    print(f"Дата: {date}")
    print(f"Время: {time}")
    print(f"Людей: {people}")
    print(f"Номер столика: {table_number}")


# ==================================================
# ОЦЕНКА РЕСТОРАНА
# ==================================================

def rate_restaurant():

    line()
    print("                 ОЦЕНКА РЕСТОРАНА")
    line()

    try:

        rating = int(
            input("Оцените ресторан от 1 до 5: ")
        )

        if rating < 1 or rating > 5:

            print("Оценка должна быть от 1 до 5!")
            return

        comment = input(
            "Оставьте комментарий: "
        )

        print("\nСпасибо за вашу оценку!")

        print(f"Оценка: {rating}/5")
        print(f"Комментарий: {comment}")

    except ValueError:

        print("Введите число!")


# ==================================================
# АДМИН-ПАНЕЛЬ
# ==================================================

def admin_panel():

    if current_user != "admin":

        print("Доступ запрещён!")
        return

    while True:

        line()
        print("                 АДМИН-ПАНЕЛЬ")
        line()

        print("1. Посмотреть все блюда")
        print("2. Добавить блюдо")
        print("3. Изменить цену")
        print("4. Изменить доступность")
        print("5. Посмотреть пользователей")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":

            detailed_menu()

        elif choice == "2":

            add_food()

        elif choice == "3":

            change_price()

        elif choice == "4":

            change_availability()

        elif choice == "5":

            show_users()

        elif choice == "6":

            break

        else:

            print("Неверный выбор!")


# ==================================================
# ДОБАВЛЕНИЕ НОВОГО БЛЮДА
# ==================================================

def add_food():

    line()
    print("                 ДОБАВИТЬ БЛЮДО")
    line()

    try:

        number = max(menu.keys()) + 1

        name = input("Название блюда: ")

        price = int(
            input("Цена: ")
        )

        category = input("Категория: ")

        description = input("Описание: ")

        menu[number] = {

            "name": name,

            "price": price,

            "category": category,

            "description": description,

            "available": True

        }

        print("Блюдо добавлено!")

    except ValueError:

        print("Цена должна быть числом!")


# ==================================================
# ИЗМЕНЕНИЕ ЦЕНЫ
# ==================================================

def change_price():

    show_menu()

    try:

        number = int(
            input("Номер блюда: ")
        )

        if number not in menu:

            print("Блюдо не найдено!")
            return

        new_price = int(
            input("Новая цена: ")
        )

        menu[number]["price"] = new_price

        print("Цена изменена!")

    except ValueError:

        print("Ошибка!")


# ==================================================
# ДОСТУПНОСТЬ БЛЮДА
# ==================================================

def change_availability():

    show_menu()

    try:

        number = int(
            input("Номер блюда: ")
        )

        if number not in menu:

            print("Блюдо не найдено!")
            return

        menu[number]["available"] = not menu[number]["available"]

        print("Доступность изменена!")

    except ValueError:

        print("Ошибка!")


# ==================================================
# ПРОСМОТР ПОЛЬЗОВАТЕЛЕЙ
# ==================================================

def show_users():

    line()
    print("                 ПОЛЬЗОВАТЕЛИ")
    line()

    for username, user in users.items():

        print(f"\nЛогин: {username}")
        print(f"Имя: {user['name']}")
        print(f"Телефон: {user['phone']}")
        print(f"Заказов: {len(user['orders'])}")


# ==================================================
# ГЛАВНОЕ МЕНЮ
# ==================================================

def main_menu():

    while current_user is not None:

        line()

        print(
            f"        ДОБРО ПОЖАЛОВАТЬ, "
            f"{users[current_user]['name']}!"
        )

        line()

        print("1. Посмотреть меню")
        print("2. Подробное меню")
        print("3. Поиск блюда")
        print("4. Категории")
        print("5. Добавить в корзину")
        print("6. Посмотреть корзину")
        print("7. Удалить из корзины")
        print("8. Очистить корзину")
        print("9. Оформить заказ")
        print("10. История заказов")
        print("11. Личный кабинет")
        print("12. Забронировать столик")
        print("13. Оценить ресторан")
        print("14. Админ-панель")
        print("15. Выйти из аккаунта")

        line()

        choice = input("Выберите действие: ")

        if choice == "1":

            show_menu()

        elif choice == "2":

            detailed_menu()

        elif choice == "3":

            search_food()

        elif choice == "4":

            category_menu()

        elif choice == "5":

            add_to_cart()

        elif choice == "6":

            show_cart()

        elif choice == "7":

            remove_from_cart()

        elif choice == "8":

            clear_cart()

        elif choice == "9":

            checkout()

        elif choice == "10":

            order_history()

        elif choice == "11":

            profile()

        elif choice == "12":

            book_table()

        elif choice == "13":

            rate_restaurant()

        elif choice == "14":

            admin_panel()

        elif choice == "15":

            logout()

        else:

            print("Неверный выбор!")


# ==================================================
# ЗАПУСК ПРОГРАММЫ
# ==================================================

def main():

    while True:

        line()

        print("          🍔 TASTY FOOD RESTAURANT 🍔")

        line()

        print("1. Регистрация")
        print("2. Вход")
        print("3. Выход")

        line()

        choice = input("Выберите действие: ")

        if choice == "1":

            register()

        elif choice == "2":

            if login():

                main_menu()

        elif choice == "3":

            print("Спасибо за посещение!")
            break

        else:

            print("Неверный выбор!")


# ==================================================
# ЗАПУСК
# ==================================================

if __name__ == "__main__":

    main()



# ==================================================
#              🍔 TASTY FOOD RESTAURANT 🍔
#              БОЛЬШОЙ ПРОЕКТ НА PYTHON
# ==================================================

import datetime
import random

# ==================================================
# НАСТРОЙКИ РЕСТОРАНА
# ==================================================

restaurant_name = "Tasty Food"
restaurant_address = "Бишкек, Кыргызстан"
restaurant_phone = "+996 555 123 456"

currency = "сом"

# ==================================================
# ПОЛЬЗОВАТЕЛИ
# ==================================================

users = {
    "admin": {
        "password": "admin123",
        "name": "Администратор",
        "phone": "+996 700 000 000",
        "orders": []
    }
}

current_user = None

# ==================================================
# МЕНЮ РЕСТОРАНА
# ==================================================

menu = {

    1: {
        "name": "Пицца Маргарита",
        "price": 450,
        "category": "Пицца",
        "description": "Томатный соус, сыр и базилик",
        "available": True
    },

    2: {
        "name": "Пицца Пепперони",
        "price": 550,
        "category": "Пицца",
        "description": "Сыр, пепперони и томатный соус",
        "available": True
    },

    3: {
        "name": "Пицца Четыре сыра",
        "price": 650,
        "category": "Пицца",
        "description": "Четыре вида сыра",
        "available": True
    },

    4: {
        "name": "Бургер Классический",
        "price": 300,
        "category": "Бургеры",
        "description": "Котлета, сыр, салат и соус",
        "available": True
    },

    5: {
        "name": "Чизбургер",
        "price": 350,
        "category": "Бургеры",
        "description": "Бургер с сыром и овощами",
        "available": True
    },

    6: {
        "name": "Двойной бургер",
        "price": 500,
        "category": "Бургеры",
        "description": "Две котлеты и двойной сыр",
        "available": True
    },

    7: {
        "name": "Картошка Фри",
        "price": 150,
        "category": "Закуски",
        "description": "Хрустящая картошка",
        "available": True
    },

    8: {
        "name": "Куриные Наггетсы",
        "price": 250,
        "category": "Закуски",
        "description": "Куриные кусочки в панировке",
        "available": True
    },

    9: {
        "name": "Крылышки BBQ",
        "price": 400,
        "category": "Закуски",
        "description": "Куриные крылышки с соусом",
        "available": True
    },

    10: {
        "name": "Кола",
        "price": 100,
        "category": "Напитки",
        "description": "Газированный напиток",
        "available": True
    },

    11: {
        "name": "Сок Апельсиновый",
        "price": 120,
        "category": "Напитки",
        "description": "Апельсиновый сок",
        "available": True
    },

    12: {
        "name": "Лимонад",
        "price": 180,
        "category": "Напитки",
        "description": "Освежающий лимонад",
        "available": True
    },

    13: {
        "name": "Мороженое",
        "price": 180,
        "category": "Десерты",
        "description": "Сливочное мороженое",
        "available": True
    },

    14: {
        "name": "Шоколадный торт",
        "price": 250,
        "category": "Десерты",
        "description": "Нежный шоколадный десерт",
        "available": True
    },

    15: {
        "name": "Чизкейк",
        "price": 300,
        "category": "Десерты",
        "description": "Классический чизкейк",
        "available": True
    }
}

# ==================================================
# КОРЗИНА
# ==================================================

cart = []

# ==================================================
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ==================================================

def line():
    print("=" * 60)


def pause():
    input("\nНажмите Enter, чтобы продолжить...")


def get_total():
    total = 0

    for item in cart:
        total += item["price"] * item["quantity"]

    return total


def get_order_count():
    return len(cart)


def clear_screen():
    print("\n" * 2)


# ==================================================
# РЕГИСТРАЦИЯ
# ==================================================

def register():

    line()
    print("                 РЕГИСТРАЦИЯ")
    line()

    username = input("Придумайте логин: ").strip()

    if username == "":
        print("Логин не может быть пустым!")
        return

    if username in users:
        print("Такой пользователь уже существует!")
        return

    password = input("Придумайте пароль: ").strip()

    if len(password) < 4:
        print("Пароль должен содержать минимум 4 символа!")
        return

    name = input("Введите ваше имя: ")
    phone = input("Введите номер телефона: ")

    users[username] = {
        "password": password,
        "name": name,
        "phone": phone,
        "orders": []
    }

    print("\n✅ Регистрация успешно завершена!")
    print(f"Добро пожаловать, {name}!")


# ==================================================
# ВХОД
# ==================================================

def login():

    global current_user

    line()
    print("                    ВХОД")
    line()

    username = input("Логин: ")
    password = input("Пароль: ")

    if username in users:

        if users[username]["password"] == password:

            current_user = username

            print("\n✅ Вы успешно вошли!")
            print(
                f"Привет, {users[username]['name']}!"
            )

            return True

    print("\n❌ Неверный логин или пароль!")

    return False


# ==================================================
# ВЫХОД ИЗ АККАУНТА
# ==================================================

def logout():

    global current_user

    current_user = None
    cart.clear()

    print("\nВы вышли из аккаунта.")


# ==================================================
# ПОКАЗ МЕНЮ
# ==================================================

def show_menu():

    line()
    print("                 🍔 МЕНЮ РЕСТОРАНА")
    line()

    for number, product in menu.items():

        if product["available"]:

            print(
                f"{number}. "
                f"{product['name']:<25}"
                f"{product['price']} {currency}"
            )

    line()


# ==================================================
# ПОДРОБНОЕ МЕНЮ
# ==================================================

def detailed_menu():

    line()
    print("              ПОДРОБНОЕ МЕНЮ")
    line()

    for number, product in menu.items():

        if product["available"]:

            print(f"\nНомер: {number}")
            print(f"Название: {product['name']}")
            print(f"Категория: {product['category']}")
            print(f"Цена: {product['price']} {currency}")
            print(f"Описание: {product['description']}")

            print("-" * 60)


# ==================================================
# ПОИСК БЛЮДА
# ==================================================

def search_food():

    line()
    print("                 ПОИСК БЛЮДА")
    line()

    search = input("Введите название или категорию: ").lower()

    found = False

    for number, product in menu.items():

        if search in product["name"].lower() \
                or search in product["category"].lower():

            print(
                f"{number}. "
                f"{product['name']} — "
                f"{product['price']} {currency}"
            )

            found = True

    if not found:
        print("Ничего не найдено.")


# ==================================================
# ФИЛЬТР ПО КАТЕГОРИИ
# ==================================================

def category_menu():

    line()
    print("               КАТЕГОРИИ")
    line()

    print("1. Пицца")
    print("2. Бургеры")
    print("3. Закуски")
    print("4. Напитки")
    print("5. Десерты")

    choice = input("Выберите категорию: ")

    categories = {
        "1": "Пицца",
        "2": "Бургеры",
        "3": "Закуски",
        "4": "Напитки",
        "5": "Десерты"
    }

    if choice not in categories:
        print("Неверная категория!")
        return

    selected_category = categories[choice]

    line()
    print(f"КАТЕГОРИЯ: {selected_category}")
    line()

    for number, product in menu.items():

        if product["category"] == selected_category:

            print(
                f"{number}. "
                f"{product['name']} — "
                f"{product['price']} {currency}"
            )


# ==================================================
# ДОБАВЛЕНИЕ В КОРЗИНУ
# ==================================================

def add_to_cart():

    show_menu()

    try:

        choice = int(
            input("\nВведите номер блюда: ")
        )

        if choice not in menu:
            print("Такого блюда нет!")
            return

        product = menu[choice]

        if not product["available"]:
            print("Это блюдо сейчас недоступно!")
            return

        quantity = int(
            input("Введите количество: ")
        )

        if quantity <= 0:
            print("Количество должно быть больше нуля!")
            return

        item = {
            "id": choice,
            "name": product["name"],
            "price": product["price"],
            "quantity": quantity
        }

        cart.append(item)

        print(
            f"\n✅ {product['name']} добавлено!"
        )

        print(
            f"Сумма: "
            f"{product['price'] * quantity} {currency}"
        )

    except ValueError:

        print("Ошибка! Введите число.")


# ==================================================
# ПРОСМОТР КОРЗИНЫ
# ==================================================

def show_cart():

    line()
    print("                  🛒 КОРЗИНА")
    line()

    if not cart:

        print("Корзина пустая.")
        return

    for index, item in enumerate(cart, start=1):

        item_total = item["price"] * item["quantity"]

        print(
            f"{index}. {item['name']}"
        )

        print(
            f"   Цена: {item['price']} {currency}"
        )

        print(
            f"   Количество: {item['quantity']}"
        )

        print(
            f"   Сумма: {item_total} {currency}"
        )

        print("-" * 60)

    print(f"ВСЕГО: {get_total()} {currency}")


# ==================================================
# УДАЛЕНИЕ ИЗ КОРЗИНЫ
# ==================================================

def remove_from_cart():

    if not cart:

        print("Корзина пустая!")
        return

    show_cart()

    try:

        number = int(
            input("\nВведите номер позиции: ")
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


# ==================================================
# ОЧИСТКА КОРЗИНЫ
# ==================================================

def clear_cart():

    if not cart:

        print("Корзина уже пустая!")
        return

    confirm = input(
        "Вы точно хотите очистить корзину? (да/нет): "
    ).lower()

    if confirm == "да":

        cart.clear()

        print("Корзина очищена.")

    else:

        print("Отмена.")


# ==================================================
# СКИДКА
# ==================================================

def calculate_discount(total):

    if total >= 3000:

        discount = total * 0.15

    elif total >= 2000:

        discount = total * 0.10

    elif total >= 1000:

        discount = total * 0.05

    else:

        discount = 0

    return discount


# ==================================================
# ДОСТАВКА
# ==================================================

def delivery():

    line()
    print("                 🚚 ДОСТАВКА")
    line()

    print("1. Самовывоз")
    print("2. Доставка по Бишкеку")

    choice = input("Выберите способ получения: ")

    if choice == "1":

        print("Вы выбрали самовывоз.")
        return "Самовывоз", 0

    elif choice == "2":

        address = input("Введите адрес доставки: ")

        print(f"Адрес: {address}")

        return "Доставка", 150

    else:

        print("Неверный выбор!")

        return None, 0


# ==================================================
# ОФОРМЛЕНИЕ ЗАКАЗА
# ==================================================

def checkout():

    if not cart:

        print("\nКорзина пустая!")
        return

    line()
    print("                ОФОРМЛЕНИЕ ЗАКАЗА")
    line()

    total = get_total()

    discount = calculate_discount(total)

    delivery_type, delivery_price = delivery()

    if delivery_type is None:

        return

    final_total = total - discount + delivery_price

    print("\n" + "=" * 60)

    print("                    ЧЕК")

    print("=" * 60)

    print(f"Ресторан: {restaurant_name}")
    print(f"Адрес: {restaurant_address}")
    print(f"Телефон: {restaurant_phone}")

    print("-" * 60)

    print(f"Клиент: {users[current_user]['name']}")

    print("-" * 60)

    for item in cart:

        print(
            f"{item['name']} "
            f"x{item['quantity']} — "
            f"{item['price'] * item['quantity']} {currency}"
        )

    print("-" * 60)

    print(f"Сумма блюд: {total} {currency}")
    print(f"Скидка: {discount} {currency}")
    print(f"Доставка: {delivery_price} {currency}")

    print("-" * 60)

    print(
        f"ИТОГО: {final_total} {currency}"
    )

    print("=" * 60)

    print("1. Наличные")
    print("2. Банковская карта")

    payment = input("Способ оплаты: ")

    if payment == "1":

        payment_name = "Наличные"

    elif payment == "2":

        payment_name = "Банковская карта"

    else:

        print("Неверный способ оплаты!")

        return

    order = {

        "number": random.randint(10000, 99999),

        "items": cart.copy(),

        "total": final_total,

        "date": datetime.datetime.now().strftime(
            "%d.%m.%Y %H:%M"
        ),

        "delivery": delivery_type,

        "payment": payment_name

    }

    users[current_user]["orders"].append(order)

    print("\n✅ Заказ успешно оформлен!")

    print(
        f"Номер заказа: #{order['number']}"
    )

    print(
        f"Статус: Принят"
    )

    cart.clear()


# ==================================================
# ИСТОРИЯ ЗАКАЗОВ
# ==================================================

def order_history():

    line()
    print("                ИСТОРИЯ ЗАКАЗОВ")
    line()

    orders = users[current_user]["orders"]

    if not orders:

        print("У вас пока нет заказов.")
        return

    for order in orders:

        print(
            f"\nЗаказ #{order['number']}"
        )

        print(
            f"Дата: {order['date']}"
        )

        print(
            f"Сумма: {order['total']} {currency}"
        )

        print(
            f"Получение: {order['delivery']}"
        )

        print(
            f"Оплата: {order['payment']}"
        )

        print(
            "Статус: Завершён"
        )

        print("-" * 60)


# ==================================================
# ЛИЧНЫЙ КАБИНЕТ
# ==================================================

def profile():

    line()
    print("                 ЛИЧНЫЙ КАБИНЕТ")
    line()

    user = users[current_user]

    print(f"Логин: {current_user}")
    print(f"Имя: {user['name']}")
    print(f"Телефон: {user['phone']}")

    print(
        f"Количество заказов: {len(user['orders'])}"
    )


# ==================================================
# БРОНИРОВАНИЕ СТОЛИКА
# ==================================================

def book_table():

    line()
    print("                 БРОНИРОВАНИЕ СТОЛИКА")
    line()

    name = input("Введите имя: ")

    date = input(
        "Введите дату бронирования: "
    )

    time = input(
        "Введите время: "
    )

    try:

        people = int(
            input("Количество людей: ")
        )

        if people <= 0:

            print("Количество людей должно быть больше нуля!")
            return

    except ValueError:

        print("Введите число!")
        return

    table_number = random.randint(1, 20)

    print("\n✅ Столик забронирован!")

    print(f"Имя: {name}")
    print(f"Дата: {date}")
    print(f"Время: {time}")
    print(f"Людей: {people}")
    print(f"Номер столика: {table_number}")


# ==================================================
# ОЦЕНКА РЕСТОРАНА
# ==================================================

def rate_restaurant():

    line()
    print("                 ОЦЕНКА РЕСТОРАНА")
    line()

    try:

        rating = int(
            input("Оцените ресторан от 1 до 5: ")
        )

        if rating < 1 or rating > 5:

            print("Оценка должна быть от 1 до 5!")
            return

        comment = input(
            "Оставьте комментарий: "
        )

        print("\nСпасибо за вашу оценку!")

        print(f"Оценка: {rating}/5")
        print(f"Комментарий: {comment}")

    except ValueError:

        print("Введите число!")


# ==================================================
# АДМИН-ПАНЕЛЬ
# ==================================================

def admin_panel():

    if current_user != "admin":

        print("Доступ запрещён!")
        return

    while True:

        line()
        print("                 АДМИН-ПАНЕЛЬ")
        line()

        print("1. Посмотреть все блюда")
        print("2. Добавить блюдо")
        print("3. Изменить цену")
        print("4. Изменить доступность")
        print("5. Посмотреть пользователей")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":

            detailed_menu()

        elif choice == "2":

            add_food()

        elif choice == "3":

            change_price()

        elif choice == "4":

            change_availability()

        elif choice == "5":

            show_users()

        elif choice == "6":

            break

        else:

            print("Неверный выбор!")


# ==================================================
# ДОБАВЛЕНИЕ НОВОГО БЛЮДА
# ==================================================

def add_food():

    line()
    print("                 ДОБАВИТЬ БЛЮДО")
    line()

    try:

        number = max(menu.keys()) + 1

        name = input("Название блюда: ")

        price = int(
            input("Цена: ")
        )

        category = input("Категория: ")

        description = input("Описание: ")

        menu[number] = {

            "name": name,

            "price": price,

            "category": category,

            "description": description,

            "available": True

        }

        print("Блюдо добавлено!")

    except ValueError:

        print("Цена должна быть числом!")


# ==================================================
# ИЗМЕНЕНИЕ ЦЕНЫ
# ==================================================

def change_price():

    show_menu()

    try:

        number = int(
            input("Номер блюда: ")
        )

        if number not in menu:

            print("Блюдо не найдено!")
            return

        new_price = int(
            input("Новая цена: ")
        )

        menu[number]["price"] = new_price

        print("Цена изменена!")

    except ValueError:

        print("Ошибка!")


# ==================================================
# ДОСТУПНОСТЬ БЛЮДА
# ==================================================

def change_availability():

    show_menu()

    try:

        number = int(
            input("Номер блюда: ")
        )

        if number not in menu:

            print("Блюдо не найдено!")
            return

        menu[number]["available"] = not menu[number]["available"]

        print("Доступность изменена!")

    except ValueError:

        print("Ошибка!")


# ==================================================
# ПРОСМОТР ПОЛЬЗОВАТЕЛЕЙ
# ==================================================

def show_users():

    line()
    print("                 ПОЛЬЗОВАТЕЛИ")
    line()

    for username, user in users.items():

        print(f"\nЛогин: {username}")
        print(f"Имя: {user['name']}")
        print(f"Телефон: {user['phone']}")
        print(f"Заказов: {len(user['orders'])}")


# ==================================================
# ГЛАВНОЕ МЕНЮ
# ==================================================

def main_menu():

    while current_user is not None:

        line()

        print(
            f"        ДОБРО ПОЖАЛОВАТЬ, "
            f"{users[current_user]['name']}!"
        )

        line()

        print("1. Посмотреть меню")
        print("2. Подробное меню")
        print("3. Поиск блюда")
        print("4. Категории")
        print("5. Добавить в корзину")
        print("6. Посмотреть корзину")
        print("7. Удалить из корзины")
        print("8. Очистить корзину")
        print("9. Оформить заказ")
        print("10. История заказов")
        print("11. Личный кабинет")
        print("12. Забронировать столик")
        print("13. Оценить ресторан")
        print("14. Админ-панель")
        print("15. Выйти из аккаунта")

        line()

        choice = input("Выберите действие: ")

        if choice == "1":

            show_menu()

        elif choice == "2":

            detailed_menu()

        elif choice == "3":

            search_food()

        elif choice == "4":

            category_menu()

        elif choice == "5":

            add_to_cart()

        elif choice == "6":

            show_cart()

        elif choice == "7":

            remove_from_cart()

        elif choice == "8":

            clear_cart()

        elif choice == "9":

            checkout()

        elif choice == "10":

            order_history()

        elif choice == "11":

            profile()

        elif choice == "12":

            book_table()

        elif choice == "13":

            rate_restaurant()

        elif choice == "14":

            admin_panel()

        elif choice == "15":

            logout()

        else:

            print("Неверный выбор!")


# ==================================================
# ЗАПУСК ПРОГРАММЫ
# ==================================================

def main():

    while True:

        line()

        print("          🍔 TASTY FOOD RESTAURANT 🍔")

        line()

        print("1. Регистрация")
        print("2. Вход")
        print("3. Выход")

        line()

        choice = input("Выберите действие: ")

        if choice == "1":

            register()

        elif choice == "2":

            if login():

                main_menu()

        elif choice == "3":

            print("Спасибо за посещение!")
            break

        else:

            print("Неверный выбор!")


# ==================================================
# ЗАПУСК
# ==================================================

if __name__ == "__main__":

    main()


# ==================================================
#              🍔 TASTY FOOD RESTAURANT 🍔
#              БОЛЬШОЙ ПРОЕКТ НА PYTHON
# ==================================================

import datetime
import random

# ==================================================
# НАСТРОЙКИ РЕСТОРАНА
# ==================================================

restaurant_name = "Tasty Food"
restaurant_address = "Бишкек, Кыргызстан"
restaurant_phone = "+996 555 123 456"

currency = "сом"

# ==================================================
# ПОЛЬЗОВАТЕЛИ
# ==================================================

users = {
    "admin": {
        "password": "admin123",
        "name": "Администратор",
        "phone": "+996 700 000 000",
        "orders": []
    }
}

current_user = None

# ==================================================
# МЕНЮ РЕСТОРАНА
# ==================================================

menu = {

    1: {
        "name": "Пицца Маргарита",
        "price": 450,
        "category": "Пицца",
        "description": "Томатный соус, сыр и базилик",
        "available": True
    },

    2: {
        "name": "Пицца Пепперони",
        "price": 550,
        "category": "Пицца",
        "description": "Сыр, пепперони и томатный соус",
        "available": True
    },

    3: {
        "name": "Пицца Четыре сыра",
        "price": 650,
        "category": "Пицца",
        "description": "Четыре вида сыра",
        "available": True
    },

    4: {
        "name": "Бургер Классический",
        "price": 300,
        "category": "Бургеры",
        "description": "Котлета, сыр, салат и соус",
        "available": True
    },

    5: {
        "name": "Чизбургер",
        "price": 350,
        "category": "Бургеры",
        "description": "Бургер с сыром и овощами",
        "available": True
    },

    6: {
        "name": "Двойной бургер",
        "price": 500,
        "category": "Бургеры",
        "description": "Две котлеты и двойной сыр",
        "available": True
    },

    7: {
        "name": "Картошка Фри",
        "price": 150,
        "category": "Закуски",
        "description": "Хрустящая картошка",
        "available": True
    },

    8: {
        "name": "Куриные Наггетсы",
        "price": 250,
        "category": "Закуски",
        "description": "Куриные кусочки в панировке",
        "available": True
    },

    9: {
        "name": "Крылышки BBQ",
        "price": 400,
        "category": "Закуски",
        "description": "Куриные крылышки с соусом",
        "available": True
    },

    10: {
        "name": "Кола",
        "price": 100,
        "category": "Напитки",
        "description": "Газированный напиток",
        "available": True
    },

    11: {
        "name": "Сок Апельсиновый",
        "price": 120,
        "category": "Напитки",
        "description": "Апельсиновый сок",
        "available": True
    },

    12: {
        "name": "Лимонад",
        "price": 180,
        "category": "Напитки",
        "description": "Освежающий лимонад",
        "available": True
    },

    13: {
        "name": "Мороженое",
        "price": 180,
        "category": "Десерты",
        "description": "Сливочное мороженое",
        "available": True
    },

    14: {
        "name": "Шоколадный торт",
        "price": 250,
        "category": "Десерты",
        "description": "Нежный шоколадный десерт",
        "available": True
    },

    15: {
        "name": "Чизкейк",
        "price": 300,
        "category": "Десерты",
        "description": "Классический чизкейк",
        "available": True
    }
}

# ==================================================
# КОРЗИНА
# ==================================================

cart = []

# ==================================================
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ==================================================

def line():
    print("=" * 60)


def pause():
    input("\nНажмите Enter, чтобы продолжить...")


def get_total():
    total = 0

    for item in cart:
        total += item["price"] * item["quantity"]

    return total


def get_order_count():
    return len(cart)


def clear_screen():
    print("\n" * 2)


# ==================================================
# РЕГИСТРАЦИЯ
# ==================================================

def register():

    line()
    print("                 РЕГИСТРАЦИЯ")
    line()

    username = input("Придумайте логин: ").strip()

    if username == "":
        print("Логин не может быть пустым!")
        return

    if username in users:
        print("Такой пользователь уже существует!")
        return

    password = input("Придумайте пароль: ").strip()

    if len(password) < 4:
        print("Пароль должен содержать минимум 4 символа!")
        return

    name = input("Введите ваше имя: ")
    phone = input("Введите номер телефона: ")

    users[username] = {
        "password": password,
        "name": name,
        "phone": phone,
        "orders": []
    }

    print("\n✅ Регистрация успешно завершена!")
    print(f"Добро пожаловать, {name}!")


# ==================================================
# ВХОД
# ==================================================

def login():

    global current_user

    line()
    print("                    ВХОД")
    line()

    username = input("Логин: ")
    password = input("Пароль: ")

    if username in users:

        if users[username]["password"] == password:

            current_user = username

            print("\n✅ Вы успешно вошли!")
            print(
                f"Привет, {users[username]['name']}!"
            )

            return True

    print("\n❌ Неверный логин или пароль!")

    return False


# ==================================================
# ВЫХОД ИЗ АККАУНТА
# ==================================================

def logout():

    global current_user

    current_user = None
    cart.clear()

    print("\nВы вышли из аккаунта.")


# ==================================================
# ПОКАЗ МЕНЮ
# ==================================================

def show_menu():

    line()
    print("                 🍔 МЕНЮ РЕСТОРАНА")
    line()

    for number, product in menu.items():

        if product["available"]:

            print(
                f"{number}. "
                f"{product['name']:<25}"
                f"{product['price']} {currency}"
            )

    line()


# ==================================================
# ПОДРОБНОЕ МЕНЮ
# ==================================================

def detailed_menu():

    line()
    print("              ПОДРОБНОЕ МЕНЮ")
    line()

    for number, product in menu.items():

        if product["available"]:

            print(f"\nНомер: {number}")
            print(f"Название: {product['name']}")
            print(f"Категория: {product['category']}")
            print(f"Цена: {product['price']} {currency}")
            print(f"Описание: {product['description']}")

            print("-" * 60)


# ==================================================
# ПОИСК БЛЮДА
# ==================================================

def search_food():

    line()
    print("                 ПОИСК БЛЮДА")
    line()

    search = input("Введите название или категорию: ").lower()

    found = False

    for number, product in menu.items():

        if search in product["name"].lower() \
                or search in product["category"].lower():

            print(
                f"{number}. "
                f"{product['name']} — "
                f"{product['price']} {currency}"
            )

            found = True

    if not found:
        print("Ничего не найдено.")


# ==================================================
# ФИЛЬТР ПО КАТЕГОРИИ
# ==================================================

def category_menu():

    line()
    print("               КАТЕГОРИИ")
    line()

    print("1. Пицца")
    print("2. Бургеры")
    print("3. Закуски")
    print("4. Напитки")
    print("5. Десерты")

    choice = input("Выберите категорию: ")

    categories = {
        "1": "Пицца",
        "2": "Бургеры",
        "3": "Закуски",
        "4": "Напитки",
        "5": "Десерты"
    }

    if choice not in categories:
        print("Неверная категория!")
        return

    selected_category = categories[choice]

    line()
    print(f"КАТЕГОРИЯ: {selected_category}")
    line()

    for number, product in menu.items():

        if product["category"] == selected_category:

            print(
                f"{number}. "
                f"{product['name']} — "
                f"{product['price']} {currency}"
            )


# ==================================================
# ДОБАВЛЕНИЕ В КОРЗИНУ
# ==================================================

def add_to_cart():

    show_menu()

    try:

        choice = int(
            input("\nВведите номер блюда: ")
        )

        if choice not in menu:
            print("Такого блюда нет!")
            return

        product = menu[choice]

        if not product["available"]:
            print("Это блюдо сейчас недоступно!")
            return

        quantity = int(
            input("Введите количество: ")
        )

        if quantity <= 0:
            print("Количество должно быть больше нуля!")
            return

        item = {
            "id": choice,
            "name": product["name"],
            "price": product["price"],
            "quantity": quantity
        }

        cart.append(item)

        print(
            f"\n✅ {product['name']} добавлено!"
        )

        print(
            f"Сумма: "
            f"{product['price'] * quantity} {currency}"
        )

    except ValueError:

        print("Ошибка! Введите число.")


# ==================================================
# ПРОСМОТР КОРЗИНЫ
# ==================================================

def show_cart():

    line()
    print("                  🛒 КОРЗИНА")
    line()

    if not cart:

        print("Корзина пустая.")
        return

    for index, item in enumerate(cart, start=1):

        item_total = item["price"] * item["quantity"]

        print(
            f"{index}. {item['name']}"
        )

        print(
            f"   Цена: {item['price']} {currency}"
        )

        print(
            f"   Количество: {item['quantity']}"
        )

        print(
            f"   Сумма: {item_total} {currency}"
        )

        print("-" * 60)

    print(f"ВСЕГО: {get_total()} {currency}")


# ==================================================
# УДАЛЕНИЕ ИЗ КОРЗИНЫ
# ==================================================

def remove_from_cart():

    if not cart:

        print("Корзина пустая!")
        return

    show_cart()

    try:

        number = int(
            input("\nВведите номер позиции: ")
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


# ==================================================
# ОЧИСТКА КОРЗИНЫ
# ==================================================

def clear_cart():

    if not cart:

        print("Корзина уже пустая!")
        return

    confirm = input(
        "Вы точно хотите очистить корзину? (да/нет): "
    ).lower()

    if confirm == "да":

        cart.clear()

        print("Корзина очищена.")

    else:

        print("Отмена.")


# ==================================================
# СКИДКА
# ==================================================

def calculate_discount(total):

    if total >= 3000:

        discount = total * 0.15

    elif total >= 2000:

        discount = total * 0.10

    elif total >= 1000:

        discount = total * 0.05

    else:

        discount = 0

    return discount


# ==================================================
# ДОСТАВКА
# ==================================================

def delivery():

    line()
    print("                 🚚 ДОСТАВКА")
    line()

    print("1. Самовывоз")
    print("2. Доставка по Бишкеку")

    choice = input("Выберите способ получения: ")

    if choice == "1":

        print("Вы выбрали самовывоз.")
        return "Самовывоз", 0

    elif choice == "2":

        address = input("Введите адрес доставки: ")

        print(f"Адрес: {address}")

        return "Доставка", 150

    else:

        print("Неверный выбор!")

        return None, 0


# ==================================================
# ОФОРМЛЕНИЕ ЗАКАЗА
# ==================================================

def checkout():

    if not cart:

        print("\nКорзина пустая!")
        return

    line()
    print("                ОФОРМЛЕНИЕ ЗАКАЗА")
    line()

    total = get_total()

    discount = calculate_discount(total)

    delivery_type, delivery_price = delivery()

    if delivery_type is None:

        return

    final_total = total - discount + delivery_price

    print("\n" + "=" * 60)

    print("                    ЧЕК")

    print("=" * 60)

    print(f"Ресторан: {restaurant_name}")
    print(f"Адрес: {restaurant_address}")
    print(f"Телефон: {restaurant_phone}")

    print("-" * 60)

    print(f"Клиент: {users[current_user]['name']}")

    print("-" * 60)

    for item in cart:

        print(
            f"{item['name']} "
            f"x{item['quantity']} — "
            f"{item['price'] * item['quantity']} {currency}"
        )

    print("-" * 60)

    print(f"Сумма блюд: {total} {currency}")
    print(f"Скидка: {discount} {currency}")
    print(f"Доставка: {delivery_price} {currency}")

    print("-" * 60)

    print(
        f"ИТОГО: {final_total} {currency}"
    )

    print("=" * 60)

    print("1. Наличные")
    print("2. Банковская карта")

    payment = input("Способ оплаты: ")

    if payment == "1":

        payment_name = "Наличные"

    elif payment == "2":

        payment_name = "Банковская карта"

    else:

        print("Неверный способ оплаты!")

        return

    order = {

        "number": random.randint(10000, 99999),

        "items": cart.copy(),

        "total": final_total,

        "date": datetime.datetime.now().strftime(
            "%d.%m.%Y %H:%M"
        ),

        "delivery": delivery_type,

        "payment": payment_name

    }

    users[current_user]["orders"].append(order)

    print("\n✅ Заказ успешно оформлен!")

    print(
        f"Номер заказа: #{order['number']}"
    )

    print(
        f"Статус: Принят"
    )

    cart.clear()


# ==================================================
# ИСТОРИЯ ЗАКАЗОВ
# ==================================================

def order_history():

    line()
    print("                ИСТОРИЯ ЗАКАЗОВ")
    line()

    orders = users[current_user]["orders"]

    if not orders:

        print("У вас пока нет заказов.")
        return

    for order in orders:

        print(
            f"\nЗаказ #{order['number']}"
        )

        print(
            f"Дата: {order['date']}"
        )

        print(
            f"Сумма: {order['total']} {currency}"
        )

        print(
            f"Получение: {order['delivery']}"
        )

        print(
            f"Оплата: {order['payment']}"
        )

        print(
            "Статус: Завершён"
        )

        print("-" * 60)


# ==================================================
# ЛИЧНЫЙ КАБИНЕТ
# ==================================================

def profile():

    line()
    print("                 ЛИЧНЫЙ КАБИНЕТ")
    line()

    user = users[current_user]

    print(f"Логин: {current_user}")
    print(f"Имя: {user['name']}")
    print(f"Телефон: {user['phone']}")

    print(
        f"Количество заказов: {len(user['orders'])}"
    )


# ==================================================
# БРОНИРОВАНИЕ СТОЛИКА
# ==================================================

def book_table():

    line()
    print("                 БРОНИРОВАНИЕ СТОЛИКА")
    line()

    name = input("Введите имя: ")

    date = input(
        "Введите дату бронирования: "
    )

    time = input(
        "Введите время: "
    )

    try:

        people = int(
            input("Количество людей: ")
        )

        if people <= 0:

            print("Количество людей должно быть больше нуля!")
            return

    except ValueError:

        print("Введите число!")
        return

    table_number = random.randint(1, 20)

    print("\n✅ Столик забронирован!")

    print(f"Имя: {name}")
    print(f"Дата: {date}")
    print(f"Время: {time}")
    print(f"Людей: {people}")
    print(f"Номер столика: {table_number}")


# ==================================================
# ОЦЕНКА РЕСТОРАНА
# ==================================================

def rate_restaurant():

    line()
    print("                 ОЦЕНКА РЕСТОРАНА")
    line()

    try:

        rating = int(
            input("Оцените ресторан от 1 до 5: ")
        )

        if rating < 1 or rating > 5:

            print("Оценка должна быть от 1 до 5!")
            return

        comment = input(
            "Оставьте комментарий: "
        )

        print("\nСпасибо за вашу оценку!")

        print(f"Оценка: {rating}/5")
        print(f"Комментарий: {comment}")

    except ValueError:

        print("Введите число!")


# ==================================================
# АДМИН-ПАНЕЛЬ
# ==================================================

def admin_panel():

    if current_user != "admin":

        print("Доступ запрещён!")
        return

    while True:

        line()
        print("                 АДМИН-ПАНЕЛЬ")
        line()

        print("1. Посмотреть все блюда")
        print("2. Добавить блюдо")
        print("3. Изменить цену")
        print("4. Изменить доступность")
        print("5. Посмотреть пользователей")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":

            detailed_menu()

        elif choice == "2":

            add_food()

        elif choice == "3":

            change_price()

        elif choice == "4":

            change_availability()

        elif choice == "5":

            show_users()

        elif choice == "6":

            break

        else:

            print("Неверный выбор!")


# ==================================================
# ДОБАВЛЕНИЕ НОВОГО БЛЮДА
# ==================================================

def add_food():

    line()
    print("                 ДОБАВИТЬ БЛЮДО")
    line()

    try:

        number = max(menu.keys()) + 1

        name = input("Название блюда: ")

        price = int(
            input("Цена: ")
        )

        category = input("Категория: ")

        description = input("Описание: ")

        menu[number] = {

            "name": name,

            "price": price,

            "category": category,

            "description": description,

            "available": True

        }

        print("Блюдо добавлено!")

    except ValueError:

        print("Цена должна быть числом!")


# ==================================================
# ИЗМЕНЕНИЕ ЦЕНЫ
# ==================================================

def change_price():

    show_menu()

    try:

        number = int(
            input("Номер блюда: ")
        )

        if number not in menu:

            print("Блюдо не найдено!")
            return

        new_price = int(
            input("Новая цена: ")
        )

        menu[number]["price"] = new_price

        print("Цена изменена!")

    except ValueError:

        print("Ошибка!")


# ==================================================
# ДОСТУПНОСТЬ БЛЮДА
# ==================================================

def change_availability():

    show_menu()

    try:

        number = int(
            input("Номер блюда: ")
        )

        if number not in menu:

            print("Блюдо не найдено!")
            return

        menu[number]["available"] = not menu[number]["available"]

        print("Доступность изменена!")

    except ValueError:

        print("Ошибка!")


# ==================================================
# ПРОСМОТР ПОЛЬЗОВАТЕЛЕЙ
# ==================================================

def show_users():

    line()
    print("                 ПОЛЬЗОВАТЕЛИ")
    line()

    for username, user in users.items():

        print(f"\nЛогин: {username}")
        print(f"Имя: {user['name']}")
        print(f"Телефон: {user['phone']}")
        print(f"Заказов: {len(user['orders'])}")


# ==================================================
# ГЛАВНОЕ МЕНЮ
# ==================================================

def main_menu():

    while current_user is not None:

        line()

        print(
            f"        ДОБРО ПОЖАЛОВАТЬ, "
            f"{users[current_user]['name']}!"
        )

        line()

        print("1. Посмотреть меню")
        print("2. Подробное меню")
        print("3. Поиск блюда")
        print("4. Категории")
        print("5. Добавить в корзину")
        print("6. Посмотреть корзину")
        print("7. Удалить из корзины")
        print("8. Очистить корзину")
        print("9. Оформить заказ")
        print("10. История заказов")
        print("11. Личный кабинет")
        print("12. Забронировать столик")
        print("13. Оценить ресторан")
        print("14. Админ-панель")
        print("15. Выйти из аккаунта")

        line()

        choice = input("Выберите действие: ")

        if choice == "1":

            show_menu()

        elif choice == "2":

            detailed_menu()

        elif choice == "3":

            search_food()

        elif choice == "4":

            category_menu()

        elif choice == "5":

            add_to_cart()

        elif choice == "6":

            show_cart()

        elif choice == "7":

            remove_from_cart()

        elif choice == "8":

            clear_cart()

        elif choice == "9":

            checkout()

        elif choice == "10":

            order_history()

        elif choice == "11":

            profile()

        elif choice == "12":

            book_table()

        elif choice == "13":

            rate_restaurant()

        elif choice == "14":

            admin_panel()

        elif choice == "15":

            logout()

        else:

            print("Неверный выбор!")


# ==================================================
# ЗАПУСК ПРОГРАММЫ
# ==================================================

def main():

    while True:

        line()

        print("          🍔 TASTY FOOD RESTAURANT 🍔")

        line()

        print("1. Регистрация")
        print("2. Вход")
        print("3. Выход")

        line()

        choice = input("Выберите действие: ")

        if choice == "1":

            register()

        elif choice == "2":

            if login():

                main_menu()

        elif choice == "3":

            print("Спасибо за посещение!")
            break

        else:

            print("Неверный выбор!")


# ==================================================
# ЗАПУСК
# ==================================================

if __name__ == "__main__":

    main()



# ==================================================
#              🍔 TASTY FOOD RESTAURANT 🍔
#              БОЛЬШОЙ ПРОЕКТ НА PYTHON
# ==================================================

import datetime
import random

# ==================================================
# НАСТРОЙКИ РЕСТОРАНА
# ==================================================

restaurant_name = "Tasty Food"
restaurant_address = "Бишкек, Кыргызстан"
restaurant_phone = "+996 555 123 456"

currency = "сом"

# ==================================================
# ПОЛЬЗОВАТЕЛИ
# ==================================================

users = {
    "admin": {
        "password": "admin123",
        "name": "Администратор",
        "phone": "+996 700 000 000",
        "orders": []
    }
}

current_user = None

# ==================================================
# МЕНЮ РЕСТОРАНА
# ==================================================

menu = {

    1: {
        "name": "Пицца Маргарита",
        "price": 450,
        "category": "Пицца",
        "description": "Томатный соус, сыр и базилик",
        "available": True
    },

    2: {
        "name": "Пицца Пепперони",
        "price": 550,
        "category": "Пицца",
        "description": "Сыр, пепперони и томатный соус",
        "available": True
    },

    3: {
        "name": "Пицца Четыре сыра",
        "price": 650,
        "category": "Пицца",
        "description": "Четыре вида сыра",
        "available": True
    },

    4: {
        "name": "Бургер Классический",
        "price": 300,
        "category": "Бургеры",
        "description": "Котлета, сыр, салат и соус",
        "available": True
    },

    5: {
        "name": "Чизбургер",
        "price": 350,
        "category": "Бургеры",
        "description": "Бургер с сыром и овощами",
        "available": True
    },

    6: {
        "name": "Двойной бургер",
        "price": 500,
        "category": "Бургеры",
        "description": "Две котлеты и двойной сыр",
        "available": True
    },

    7: {
        "name": "Картошка Фри",
        "price": 150,
        "category": "Закуски",
        "description": "Хрустящая картошка",
        "available": True
    },

    8: {
        "name": "Куриные Наггетсы",
        "price": 250,
        "category": "Закуски",
        "description": "Куриные кусочки в панировке",
        "available": True
    },

    9: {
        "name": "Крылышки BBQ",
        "price": 400,
        "category": "Закуски",
        "description": "Куриные крылышки с соусом",
        "available": True
    },

    10: {
        "name": "Кола",
        "price": 100,
        "category": "Напитки",
        "description": "Газированный напиток",
        "available": True
    },

    11: {
        "name": "Сок Апельсиновый",
        "price": 120,
        "category": "Напитки",
        "description": "Апельсиновый сок",
        "available": True
    },

    12: {
        "name": "Лимонад",
        "price": 180,
        "category": "Напитки",
        "description": "Освежающий лимонад",
        "available": True
    },

    13: {
        "name": "Мороженое",
        "price": 180,
        "category": "Десерты",
        "description": "Сливочное мороженое",
        "available": True
    },

    14: {
        "name": "Шоколадный торт",
        "price": 250,
        "category": "Десерты",
        "description": "Нежный шоколадный десерт",
        "available": True
    },

    15: {
        "name": "Чизкейк",
        "price": 300,
        "category": "Десерты",
        "description": "Классический чизкейк",
        "available": True
    }
}

# ==================================================
# КОРЗИНА
# ==================================================

cart = []

# ==================================================
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ==================================================

def line():
    print("=" * 60)


def pause():
    input("\nНажмите Enter, чтобы продолжить...")


def get_total():
    total = 0

    for item in cart:
        total += item["price"] * item["quantity"]

    return total


def get_order_count():
    return len(cart)


def clear_screen():
    print("\n" * 2)


# ==================================================
# РЕГИСТРАЦИЯ
# ==================================================

def register():

    line()
    print("                 РЕГИСТРАЦИЯ")
    line()

    username = input("Придумайте логин: ").strip()

    if username == "":
        print("Логин не может быть пустым!")
        return

    if username in users:
        print("Такой пользователь уже существует!")
        return

    password = input("Придумайте пароль: ").strip()

    if len(password) < 4:
        print("Пароль должен содержать минимум 4 символа!")
        return

    name = input("Введите ваше имя: ")
    phone = input("Введите номер телефона: ")

    users[username] = {
        "password": password,
        "name": name,
        "phone": phone,
        "orders": []
    }

    print("\n✅ Регистрация успешно завершена!")
    print(f"Добро пожаловать, {name}!")


# ==================================================
# ВХОД
# ==================================================

def login():

    global current_user

    line()
    print("                    ВХОД")
    line()

    username = input("Логин: ")
    password = input("Пароль: ")

    if username in users:

        if users[username]["password"] == password:

            current_user = username

            print("\n✅ Вы успешно вошли!")
            print(
                f"Привет, {users[username]['name']}!"
            )

            return True

    print("\n❌ Неверный логин или пароль!")

    return False


# ==================================================
# ВЫХОД ИЗ АККАУНТА
# ==================================================

def logout():

    global current_user

    current_user = None
    cart.clear()

    print("\nВы вышли из аккаунта.")


# ==================================================
# ПОКАЗ МЕНЮ
# ==================================================

def show_menu():

    line()
    print("                 🍔 МЕНЮ РЕСТОРАНА")
    line()

    for number, product in menu.items():

        if product["available"]:

            print(
                f"{number}. "
                f"{product['name']:<25}"
                f"{product['price']} {currency}"
            )

    line()


# ==================================================
# ПОДРОБНОЕ МЕНЮ
# ==================================================

def detailed_menu():

    line()
    print("              ПОДРОБНОЕ МЕНЮ")
    line()

    for number, product in menu.items():

        if product["available"]:

            print(f"\nНомер: {number}")
            print(f"Название: {product['name']}")
            print(f"Категория: {product['category']}")
            print(f"Цена: {product['price']} {currency}")
            print(f"Описание: {product['description']}")

            print("-" * 60)


# ==================================================
# ПОИСК БЛЮДА
# ==================================================

def search_food():

    line()
    print("                 ПОИСК БЛЮДА")
    line()

    search = input("Введите название или категорию: ").lower()

    found = False

    for number, product in menu.items():

        if search in product["name"].lower() \
                or search in product["category"].lower():

            print(
                f"{number}. "
                f"{product['name']} — "
                f"{product['price']} {currency}"
            )

            found = True

    if not found:
        print("Ничего не найдено.")


# ==================================================
# ФИЛЬТР ПО КАТЕГОРИИ
# ==================================================

def category_menu():

    line()
    print("               КАТЕГОРИИ")
    line()

    print("1. Пицца")
    print("2. Бургеры")
    print("3. Закуски")
    print("4. Напитки")
    print("5. Десерты")

    choice = input("Выберите категорию: ")

    categories = {
        "1": "Пицца",
        "2": "Бургеры",
        "3": "Закуски",
        "4": "Напитки",
        "5": "Десерты"
    }

    if choice not in categories:
        print("Неверная категория!")
        return

    selected_category = categories[choice]

    line()
    print(f"КАТЕГОРИЯ: {selected_category}")
    line()

    for number, product in menu.items():

        if product["category"] == selected_category:

            print(
                f"{number}. "
                f"{product['name']} — "
                f"{product['price']} {currency}"
            )


# ==================================================
# ДОБАВЛЕНИЕ В КОРЗИНУ
# ==================================================

def add_to_cart():

    show_menu()

    try:

        choice = int(
            input("\nВведите номер блюда: ")
        )

        if choice not in menu:
            print("Такого блюда нет!")
            return

        product = menu[choice]

        if not product["available"]:
            print("Это блюдо сейчас недоступно!")
            return

        quantity = int(
            input("Введите количество: ")
        )

        if quantity <= 0:
            print("Количество должно быть больше нуля!")
            return

        item = {
            "id": choice,
            "name": product["name"],
            "price": product["price"],
            "quantity": quantity
        }

        cart.append(item)

        print(
            f"\n✅ {product['name']} добавлено!"
        )

        print(
            f"Сумма: "
            f"{product['price'] * quantity} {currency}"
        )

    except ValueError:

        print("Ошибка! Введите число.")


# ==================================================
# ПРОСМОТР КОРЗИНЫ
# ==================================================

def show_cart():

    line()
    print("                  🛒 КОРЗИНА")
    line()

    if not cart:

        print("Корзина пустая.")
        return

    for index, item in enumerate(cart, start=1):

        item_total = item["price"] * item["quantity"]

        print(
            f"{index}. {item['name']}"
        )

        print(
            f"   Цена: {item['price']} {currency}"
        )

        print(
            f"   Количество: {item['quantity']}"
        )

        print(
            f"   Сумма: {item_total} {currency}"
        )

        print("-" * 60)

    print(f"ВСЕГО: {get_total()} {currency}")


# ==================================================
# УДАЛЕНИЕ ИЗ КОРЗИНЫ
# ==================================================

def remove_from_cart():

    if not cart:

        print("Корзина пустая!")
        return

    show_cart()

    try:

        number = int(
            input("\nВведите номер позиции: ")
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


# ==================================================
# ОЧИСТКА КОРЗИНЫ
# ==================================================

def clear_cart():

    if not cart:

        print("Корзина уже пустая!")
        return

    confirm = input(
        "Вы точно хотите очистить корзину? (да/нет): "
    ).lower()

    if confirm == "да":

        cart.clear()

        print("Корзина очищена.")

    else:

        print("Отмена.")


# ==================================================
# СКИДКА
# ==================================================

def calculate_discount(total):

    if total >= 3000:

        discount = total * 0.15

    elif total >= 2000:

        discount = total * 0.10

    elif total >= 1000:

        discount = total * 0.05

    else:

        discount = 0

    return discount


# ==================================================
# ДОСТАВКА
# ==================================================

def delivery():

    line()
    print("                 🚚 ДОСТАВКА")
    line()

    print("1. Самовывоз")
    print("2. Доставка по Бишкеку")

    choice = input("Выберите способ получения: ")

    if choice == "1":

        print("Вы выбрали самовывоз.")
        return "Самовывоз", 0

    elif choice == "2":

        address = input("Введите адрес доставки: ")

        print(f"Адрес: {address}")

        return "Доставка", 150

    else:

        print("Неверный выбор!")

        return None, 0


# ==================================================
# ОФОРМЛЕНИЕ ЗАКАЗА
# ==================================================

def checkout():

    if not cart:

        print("\nКорзина пустая!")
        return

    line()
    print("                ОФОРМЛЕНИЕ ЗАКАЗА")
    line()

    total = get_total()

    discount = calculate_discount(total)

    delivery_type, delivery_price = delivery()

    if delivery_type is None:

        return

    final_total = total - discount + delivery_price

    print("\n" + "=" * 60)

    print("                    ЧЕК")

    print("=" * 60)

    print(f"Ресторан: {restaurant_name}")
    print(f"Адрес: {restaurant_address}")
    print(f"Телефон: {restaurant_phone}")

    print("-" * 60)

    print(f"Клиент: {users[current_user]['name']}")

    print("-" * 60)

    for item in cart:

        print(
            f"{item['name']} "
            f"x{item['quantity']} — "
            f"{item['price'] * item['quantity']} {currency}"
        )

    print("-" * 60)

    print(f"Сумма блюд: {total} {currency}")
    print(f"Скидка: {discount} {currency}")
    print(f"Доставка: {delivery_price} {currency}")

    print("-" * 60)

    print(
        f"ИТОГО: {final_total} {currency}"
    )

    print("=" * 60)

    print("1. Наличные")
    print("2. Банковская карта")

    payment = input("Способ оплаты: ")

    if payment == "1":

        payment_name = "Наличные"

    elif payment == "2":

        payment_name = "Банковская карта"

    else:

        print("Неверный способ оплаты!")

        return

    order = {

        "number": random.randint(10000, 99999),

        "items": cart.copy(),

        "total": final_total,

        "date": datetime.datetime.now().strftime(
            "%d.%m.%Y %H:%M"
        ),

        "delivery": delivery_type,

        "payment": payment_name

    }

    users[current_user]["orders"].append(order)

    print("\n✅ Заказ успешно оформлен!")

    print(
        f"Номер заказа: #{order['number']}"
    )

    print(
        f"Статус: Принят"
    )

    cart.clear()


# ==================================================
# ИСТОРИЯ ЗАКАЗОВ
# ==================================================

def order_history():

    line()
    print("                ИСТОРИЯ ЗАКАЗОВ")
    line()

    orders = users[current_user]["orders"]

    if not orders:

        print("У вас пока нет заказов.")
        return

    for order in orders:

        print(
            f"\nЗаказ #{order['number']}"
        )

        print(
            f"Дата: {order['date']}"
        )

        print(
            f"Сумма: {order['total']} {currency}"
        )

        print(
            f"Получение: {order['delivery']}"
        )

        print(
            f"Оплата: {order['payment']}"
        )

        print(
            "Статус: Завершён"
        )

        print("-" * 60)


# ==================================================
# ЛИЧНЫЙ КАБИНЕТ
# ==================================================

def profile():

    line()
    print("                 ЛИЧНЫЙ КАБИНЕТ")
    line()

    user = users[current_user]

    print(f"Логин: {current_user}")
    print(f"Имя: {user['name']}")
    print(f"Телефон: {user['phone']}")

    print(
        f"Количество заказов: {len(user['orders'])}"
    )


# ==================================================
# БРОНИРОВАНИЕ СТОЛИКА
# ==================================================

def book_table():

    line()
    print("                 БРОНИРОВАНИЕ СТОЛИКА")
    line()

    name = input("Введите имя: ")

    date = input(
        "Введите дату бронирования: "
    )

    time = input(
        "Введите время: "
    )

    try:

        people = int(
            input("Количество людей: ")
        )

        if people <= 0:

            print("Количество людей должно быть больше нуля!")
            return

    except ValueError:

        print("Введите число!")
        return

    table_number = random.randint(1, 20)

    print("\n✅ Столик забронирован!")

    print(f"Имя: {name}")
    print(f"Дата: {date}")
    print(f"Время: {time}")
    print(f"Людей: {people}")
    print(f"Номер столика: {table_number}")


# ==================================================
# ОЦЕНКА РЕСТОРАНА
# ==================================================

def rate_restaurant():

    line()
    print("                 ОЦЕНКА РЕСТОРАНА")
    line()

    try:

        rating = int(
            input("Оцените ресторан от 1 до 5: ")
        )

        if rating < 1 or rating > 5:

            print("Оценка должна быть от 1 до 5!")
            return

        comment = input(
            "Оставьте комментарий: "
        )

        print("\nСпасибо за вашу оценку!")

        print(f"Оценка: {rating}/5")
        print(f"Комментарий: {comment}")

    except ValueError:

        print("Введите число!")


# ==================================================
# АДМИН-ПАНЕЛЬ
# ==================================================

def admin_panel():

    if current_user != "admin":

        print("Доступ запрещён!")
        return

    while True:

        line()
        print("                 АДМИН-ПАНЕЛЬ")
        line()

        print("1. Посмотреть все блюда")
        print("2. Добавить блюдо")
        print("3. Изменить цену")
        print("4. Изменить доступность")
        print("5. Посмотреть пользователей")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":

            detailed_menu()

        elif choice == "2":

            add_food()

        elif choice == "3":

            change_price()

        elif choice == "4":

            change_availability()

        elif choice == "5":

            show_users()

        elif choice == "6":

            break

        else:

            print("Неверный выбор!")


# ==================================================
# ДОБАВЛЕНИЕ НОВОГО БЛЮДА
# ==================================================

def add_food():

    line()
    print("                 ДОБАВИТЬ БЛЮДО")
    line()

    try:

        number = max(menu.keys()) + 1

        name = input("Название блюда: ")

        price = int(
            input("Цена: ")
        )

        category = input("Категория: ")

        description = input("Описание: ")

        menu[number] = {

            "name": name,

            "price": price,

            "category": category,

            "description": description,

            "available": True

        }

        print("Блюдо добавлено!")

    except ValueError:

        print("Цена должна быть числом!")


# ==================================================
# ИЗМЕНЕНИЕ ЦЕНЫ
# ==================================================

def change_price():

    show_menu()

    try:

        number = int(
            input("Номер блюда: ")
        )

        if number not in menu:

            print("Блюдо не найдено!")
            return

        new_price = int(
            input("Новая цена: ")
        )

        menu[number]["price"] = new_price

        print("Цена изменена!")

    except ValueError:

        print("Ошибка!")


# ==================================================
# ДОСТУПНОСТЬ БЛЮДА
# ==================================================

def change_availability():

    show_menu()

    try:

        number = int(
            input("Номер блюда: ")
        )

        if number not in menu:

            print("Блюдо не найдено!")
            return

        menu[number]["available"] = not menu[number]["available"]

        print("Доступность изменена!")

    except ValueError:

        print("Ошибка!")


# ==================================================
# ПРОСМОТР ПОЛЬЗОВАТЕЛЕЙ
# ==================================================

def show_users():

    line()
    print("                 ПОЛЬЗОВАТЕЛИ")
    line()

    for username, user in users.items():

        print(f"\nЛогин: {username}")
        print(f"Имя: {user['name']}")
        print(f"Телефон: {user['phone']}")
        print(f"Заказов: {len(user['orders'])}")


# ==================================================
# ГЛАВНОЕ МЕНЮ
# ==================================================

def main_menu():

    while current_user is not None:

        line()

        print(
            f"        ДОБРО ПОЖАЛОВАТЬ, "
            f"{users[current_user]['name']}!"
        )

        line()

        print("1. Посмотреть меню")
        print("2. Подробное меню")
        print("3. Поиск блюда")
        print("4. Категории")
        print("5. Добавить в корзину")
        print("6. Посмотреть корзину")
        print("7. Удалить из корзины")
        print("8. Очистить корзину")
        print("9. Оформить заказ")
        print("10. История заказов")
        print("11. Личный кабинет")
        print("12. Забронировать столик")
        print("13. Оценить ресторан")
        print("14. Админ-панель")
        print("15. Выйти из аккаунта")

        line()

        choice = input("Выберите действие: ")

        if choice == "1":

            show_menu()

        elif choice == "2":

            detailed_menu()

        elif choice == "3":

            search_food()

        elif choice == "4":

            category_menu()

        elif choice == "5":

            add_to_cart()

        elif choice == "6":

            show_cart()

        elif choice == "7":

            remove_from_cart()

        elif choice == "8":

            clear_cart()

        elif choice == "9":

            checkout()

        elif choice == "10":

            order_history()

        elif choice == "11":

            profile()

        elif choice == "12":

            book_table()

        elif choice == "13":

            rate_restaurant()

        elif choice == "14":

            admin_panel()

        elif choice == "15":

            logout()

        else:

            print("Неверный выбор!")


# ==================================================
# ЗАПУСК ПРОГРАММЫ
# ==================================================

def main():

    while True:

        line()

        print("          🍔 TASTY FOOD RESTAURANT 🍔")

        line()

        print("1. Регистрация")
        print("2. Вход")
        print("3. Выход")

        line()

        choice = input("Выберите действие: ")

        if choice == "1":

            register()

        elif choice == "2":

            if login():

                main_menu()

        elif choice == "3":

            print("Спасибо за посещение!")
            break

        else:

            print("Неверный выбор!")


# ==================================================
# ЗАПУСК
# ==================================================

if __name__ == "__main__":

    main()