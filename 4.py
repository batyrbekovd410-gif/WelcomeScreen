import hashlib
import random
import string
import os
import json
from datetime import datetime


# ==========================================
#              CAT SHOP
#          ГЛАВНАЯ ПРОГРАММА
# ==========================================


SHOP_NAME = "CAT SHOP"
VERSION = "2.0"


# ==========================================
#              ЦВЕТА И ОФОРМЛЕНИЕ
# ==========================================

def line():
    print("=" * 60)


def small_line():
    print("-" * 60)


def title(text):
    print()
    line()
    print(f"        {text}")
    line()


def pause():
    input("\nНажмите Enter, чтобы продолжить...")


def clear():
    os.system("clear")


# ==========================================
#              ХЕШИРОВАНИЕ
# ==========================================

def hash_password(password):
    return hashlib.sha256(
        password.encode()
    ).hexdigest()


def check_password(password):
    if len(password) < 8:
        return False

    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    special = any(
        c in "!@#$%^&*()_+-="
        for c in password
    )

    return upper and lower and digit and special


def generate_id():
    chars = string.ascii_uppercase + string.digits

    return "".join(
        random.choice(chars)
        for _ in range(8)
    )


# ==========================================
#              ДАННЫЕ МАГАЗИНА
# ==========================================

products = {

    1: {
        "name": "iPhone 15",
        "category": "Телефоны",
        "price": 75000,
        "stock": 10,
        "rating": 4.8,
        "description": "Современный смартфон Apple"
    },

    2: {
        "name": "Samsung Galaxy S24",
        "category": "Телефоны",
        "price": 68000,
        "stock": 15,
        "rating": 4.7,
        "description": "Мощный Android смартфон"
    },

    3: {
        "name": "Xiaomi Redmi Note",
        "category": "Телефоны",
        "price": 22000,
        "stock": 20,
        "rating": 4.5,
        "description": "Доступный смартфон"
    },

    4: {
        "name": "MacBook Air",
        "category": "Ноутбуки",
        "price": 120000,
        "stock": 5,
        "rating": 4.9,
        "description": "Лёгкий ноутбук Apple"
    },

    5: {
        "name": "ASUS VivoBook",
        "category": "Ноутбуки",
        "price": 65000,
        "stock": 8,
        "rating": 4.6,
        "description": "Ноутбук для учёбы"
    },

    6: {
        "name": "Lenovo IdeaPad",
        "category": "Ноутбуки",
        "price": 55000,
        "stock": 12,
        "rating": 4.4,
        "description": "Ноутбук для работы"
    },

    7: {
        "name": "AirPods Pro",
        "category": "Наушники",
        "price": 18000,
        "stock": 25,
        "rating": 4.8,
        "description": "Беспроводные наушники"
    },

    8: {
        "name": "JBL Headphones",
        "category": "Наушники",
        "price": 8500,
        "stock": 30,
        "rating": 4.6,
        "description": "Качественный звук"
    },

    9: {
        "name": "Gaming Mouse",
        "category": "Аксессуары",
        "price": 2500,
        "stock": 40,
        "rating": 4.5,
        "description": "Игровая мышь"
    },

    10: {
        "name": "Mechanical Keyboard",
        "category": "Аксессуары",
        "price": 5500,
        "stock": 18,
        "rating": 4.7,
        "description": "Механическая клавиатура"
    },

    11: {
        "name": "Power Bank",
        "category": "Аксессуары",
        "price": 3000,
        "stock": 35,
        "rating": 4.3,
        "description": "Портативная зарядка"
    },

    12: {
        "name": "Smart Watch",
        "category": "Гаджеты",
        "price": 12000,
        "stock": 14,
        "rating": 4.5,
        "description": "Умные часы"
    }

}


# ==========================================
#              ПОЛЬЗОВАТЕЛИ
# ==========================================

users = {}


# ==========================================
#              СОЗДАНИЕ ПОЛЬЗОВАТЕЛЯ
# ==========================================

def create_user(username, password, role="user"):

    users[username] = {

        "password": hash_password(password),

        "role": role,

        "id": generate_id(),

        "balance": 0,

        "level": 1,

        "experience": 0,

        "cart": {},

        "history": [],

        "blocked": False,

        "attempts": 0,

        "registration_date":
            datetime.now().strftime(
                "%d.%m.%Y"
            )

    }


# ==========================================
#              РЕГИСТРАЦИЯ
# ==========================================

def register():

    title("РЕГИСТРАЦИЯ")

    username = input(
        "Придумайте логин: "
    ).strip()

    if not username:

        print("Логин не может быть пустым!")

        pause()

        return

    if username in users:

        print("Такой пользователь уже существует!")

        pause()

        return

    if len(username) < 3:

        print("Логин должен быть длиннее 2 символов!")

        pause()

        return

    password = input(
        "Придумайте пароль: "
    )

    if not check_password(password):

        print("\nПароль слишком слабый!")

        print("Требования:")

        print("1. Минимум 8 символов")

        print("2. Заглавная буква")

        print("3. Строчная буква")

        print("4. Цифра")

        print("5. Специальный символ")

        pause()

        return

    confirm = input(
        "Повторите пароль: "
    )

    if password != confirm:

        print("Пароли не совпадают!")

        pause()

        return

    create_user(username, password)

    print("\nРегистрация успешна!")

    print("Ваш логин:", username)

    print(
        "Ваш ID:",
        users[username]["id"]
    )

    print("Добро пожаловать в CAT SHOP!")

    pause()


# ==========================================
#              ВХОД
# ==========================================

def login():

    title("ВХОД В CAT SHOP")

    username = input(
        "Введите логин: "
    )

    if username not in users:

        print("Пользователь не найден!")

        pause()

        return None

    user = users[username]

    if user["blocked"]:

        print("Ваш аккаунт заблокирован!")

        pause()

        return None

    password = input(
        "Введите пароль: "
    )

    if hash_password(password) == user["password"]:

        user["attempts"] = 0

        print("\nВы успешно вошли!")

        print(
            "Добро пожаловать,",
            username
        )

        pause()

        return username

    user["attempts"] += 1

    print("Неверный пароль!")

    if user["attempts"] >= 3:

        user["blocked"] = True

        print("Аккаунт заблокирован!")

    else:

        print(
            "Осталось попыток:",
            3 - user["attempts"]
        )

    pause()

    return None


# ==========================================
#              ПОКАЗ ТОВАРОВ
# ==========================================

def show_products():

    title("КАТАЛОГ ТОВАРОВ")

    for product_id, product in products.items():

        print(f"\nID товара: {product_id}")

        print("Название:", product["name"])

        print("Категория:", product["category"])

        print("Цена:", product["price"], "сом")

        print("На складе:", product["stock"])

        print("Рейтинг:", product["rating"])

        print("Описание:", product["description"])

        small_line()


# ==========================================
#              ПОИСК ТОВАРА
# ==========================================

def search_product():

    title("ПОИСК ТОВАРА")

    search = input(
        "Введите название товара: "
    ).lower()

    found = False

    for product_id, product in products.items():

        if search in product["name"].lower():

            print("\nID:", product_id)

            print("Название:", product["name"])

            print("Цена:", product["price"], "сом")

            print("Категория:", product["category"])

            print("Рейтинг:", product["rating"])

            found = True

    if not found:

        print("Товары не найдены!")

    pause()


# ==========================================
#              ФИЛЬТР ПО КАТЕГОРИИ
# ==========================================

def category_products():

    title("КАТЕГОРИИ")

    categories = set(
        product["category"]
        for product in products.values()
    )

    categories = list(categories)

    for i, category in enumerate(categories, 1):

        print(i, ".", category)

    choice = input(
        "\nВведите категорию: "
    )

    for product in products.values():

        if product["category"].lower() == choice.lower():

            print(
                product["name"],
                "-",
                product["price"],
                "сом"
            )

    pause()


# ==========================================
#              ДОБАВЛЕНИЕ В КОРЗИНУ
# ==========================================

def add_to_cart(username):

    title("ДОБАВЛЕНИЕ В КОРЗИНУ")

    show_products()

    try:

        product_id = int(
            input("Введите ID товара: ")
        )

        amount = int(
            input("Введите количество: ")
        )

    except ValueError:

        print("Введите правильное число!")

        pause()

        return

    if product_id not in products:

        print("Такого товара нет!")

        pause()

        return

    product = products[product_id]

    if amount <= 0:

        print("Количество должно быть больше 0!")

        pause()

        return

    if amount > product["stock"]:

        print("Недостаточно товара на складе!")

        pause()

        return

    cart = users[username]["cart"]

    if product_id in cart:

        cart[product_id] += amount

    else:

        cart[product_id] = amount

    print(
        product["name"],
        "добавлен в корзину!"
    )

    pause()


# ==========================================
#              КОРЗИНА
# ==========================================

def show_cart(username):

    title("МОЯ КОРЗИНА")

    cart = users[username]["cart"]

    if not cart:

        print("Корзина пустая!")

        pause()

        return

    total = 0

    for product_id, amount in cart.items():

        product = products[product_id]

        cost = product["price"] * amount

        print(
            product["name"],
            "x",
            amount,
            "=",
            cost,
            "сом"
        )

        total += cost

    small_line()

    print("ИТОГО:", total, "сом")

    pause()


# ==========================================
#              УДАЛЕНИЕ ИЗ КОРЗИНЫ
# ==========================================

def remove_from_cart(username):

    title("УДАЛЕНИЕ ИЗ КОРЗИНЫ")

    cart = users[username]["cart"]

    if not cart:

        print("Корзина пустая!")

        pause()

        return

    show_cart(username)

    try:

        product_id = int(
            input("ID товара для удаления: ")
        )

    except ValueError:

        print("Ошибка!")

        pause()

        return

    if product_id in cart:

        del cart[product_id]

        print("Товар удалён!")

    else:

        print("Такого товара нет в корзине!")

    pause()


# ==========================================
#              ПОКУПКА
# ==========================================

def buy_products(username):

    title("ОФОРМЛЕНИЕ ПОКУПКИ")

    user = users[username]

    cart = user["cart"]

    if not cart:

        print("Корзина пустая!")

        pause()

        return

    total = 0

    for product_id, amount in cart.items():

        product = products[product_id]

        total += product["price"] * amount

    print("Сумма заказа:", total, "сом")

    print("Ваш баланс:", user["balance"], "сом")

    if user["balance"] < total:

        print("\nНедостаточно средств!")

        print("Пополните баланс.")

        pause()

        return

    confirm = input(
        "Подтвердить покупку? (да/нет): "
    ).lower()

    if confirm != "да":

        print("Покупка отменена!")

        pause()

        return

    for product_id, amount in cart.items():

        products[product_id]["stock"] -= amount

    user["balance"] -= total

    user["experience"] += 10

    if user["experience"] >= 100:

        user["level"] += 1

        user["experience"] = 0

        print("Поздравляем! Новый уровень!")

    purchase = {

        "date": datetime.now().strftime(
            "%d.%m.%Y %H:%M"
        ),

        "total": total,

        "items": dict(cart)

    }

    user["history"].append(purchase)

    user["cart"] = {}

    print("\nПокупка успешно оформлена!")

    print("Спасибо за покупку в CAT SHOP!")

    pause()


# ==========================================
#              ПОПОЛНЕНИЕ БАЛАНСА
# ==========================================

def add_balance(username):

    title("ПОПОЛНЕНИЕ БАЛАНСА")

    try:

        amount = int(
            input("Введите сумму: ")
        )

    except ValueError:

        print("Введите число!")

        pause()

        return

    if amount <= 0:

        print("Сумма должна быть больше 0!")

        pause()

        return

    users[username]["balance"] += amount

    print(
        "Баланс пополнен на",
        amount,
        "сом"
    )

    print(
        "Новый баланс:",
        users[username]["balance"]
    )

    pause()


# ==========================================
#              ИСТОРИЯ ПОКУПОК
# ==========================================

def purchase_history(username):

    title("ИСТОРИЯ ПОКУПОК")

    history = users[username]["history"]

    if not history:

        print("Покупок ещё не было!")

        pause()

        return

    for i, purchase in enumerate(history, 1):

        print("\nПокупка №", i)

        print("Дата:", purchase["date"])

        print("Сумма:", purchase["total"], "сом")

        print("Товары:")

        for product_id, amount in purchase["items"].items():

            print(
                "-",
                products[product_id]["name"],
                "x",
                amount
            )

        small_line()

    pause()


# ==========================================
#              ПРОФИЛЬ
# ==========================================

def profile(username):

    title("МОЙ ПРОФИЛЬ")

    user = users[username]

    print("Логин:", username)

    print("ID:", user["id"])

    print("Роль:", user["role"])

    print("Баланс:", user["balance"], "сом")

    print("Уровень:", user["level"])

    print("Опыт:", user["experience"], "/ 100")

    print("Дата регистрации:", user["registration_date"])

    print("Товаров в корзине:", len(user["cart"]))

    print("Количество покупок:", len(user["history"]))

    pause()


# ==========================================
#              ИЗМЕНЕНИЕ ПАРОЛЯ
# ==========================================

def change_password(username):

    title("ИЗМЕНЕНИЕ ПАРОЛЯ")

    old_password = input(
        "Старый пароль: "
    )

    if hash_password(old_password) != users[username]["password"]:

        print("Старый пароль неправильный!")

        pause()

        return

    new_password = input(
        "Новый пароль: "
    )

    if not check_password(new_password):

        print("Новый пароль слишком слабый!")

        pause()

        return

    confirm = input(
        "Повторите новый пароль: "
    )

    if new_password != confirm:

        print("Пароли не совпадают!")

        pause()

        return

    users[username]["password"] = hash_password(
        new_password
    )

    print("Пароль успешно изменён!")

    pause()


# ==========================================
#              МЕНЮ ПОЛЬЗОВАТЕЛЯ
# ==========================================

def user_menu(username):

    while True:

        title("CAT SHOP | USER MENU")

        print("Пользователь:", username)

        print("Баланс:", users[username]["balance"], "сом")

        print()

        print("1. Каталог товаров")

        print("2. Поиск товара")

        print("3. Категории")

        print("4. Добавить товар в корзину")

        print("5. Моя корзина")

        print("6. Удалить товар из корзины")

        print("7. Купить товары")

        print("8. Пополнить баланс")

        print("9. История покупок")

        print("10. Мой профиль")

        print("11. Изменить пароль")

        print("12. Выйти из аккаунта")

        choice = input(
            "\nВыберите действие: "
        )

        if choice == "1":

            show_products()

            pause()

        elif choice == "2":

            search_product()

        elif choice == "3":

            category_products()

        elif choice == "4":

            add_to_cart(username)

        elif choice == "5":

            show_cart(username)

        elif choice == "6":

            remove_from_cart(username)

        elif choice == "7":

            buy_products(username)

        elif choice == "8":

            add_balance(username)

        elif choice == "9":

            purchase_history(username)

        elif choice == "10":

            profile(username)

        elif choice == "11":

            change_password(username)

        elif choice == "12":

            print("Вы вышли из аккаунта!")

            break

        else:

            print("Неверный выбор!")

            pause()


# ==========================================
#              АДМИН-ПАНЕЛЬ
# ==========================================

def admin_panel():

    while True:

        title("ADMIN PANEL")

        print("1. Все пользователи")

        print("2. Все товары")

        print("3. Добавить товар")

        print("4. Удалить товар")

        print("5. Изменить цену")

        print("6. Пополнить склад")

        print("7. Разблокировать пользователя")

        print("8. Удалить пользователя")

        print("9. Выход")

        choice = input(
            "\nВыберите действие: "
        )

        if choice == "1":

            show_all_users()

        elif choice == "2":

            show_products()

            pause()

        elif choice == "3":

            add_product()

        elif choice == "4":

            delete_product()

        elif choice == "5":

            change_price()

        elif choice == "6":

            add_stock()

        elif choice == "7":

            unblock_user()

        elif choice == "8":

            delete_user()

        elif choice == "9":

            break

        else:

            print("Неверный выбор!")

            pause()


# ==========================================
#              ВСЕ ПОЛЬЗОВАТЕЛИ
# ==========================================

def show_all_users():

    title("ВСЕ ПОЛЬЗОВАТЕЛИ")

    for username, user in users.items():

        print("\nЛогин:", username)

        print("ID:", user["id"])

        print("Роль:", user["role"])

        print("Баланс:", user["balance"])

        print("Уровень:", user["level"])

        print("Заблокирован:", user["blocked"])

        small_line()

    pause()


# ==========================================
#              ДОБАВЛЕНИЕ ТОВАРА
# ==========================================

def add_product():

    title("ДОБАВЛЕНИЕ ТОВАРА")

    name = input(
        "Название товара: "
    )

    category = input(
        "Категория: "
    )

    try:

        price = int(
            input("Цена: ")
        )

        stock = int(
            input("Количество: ")
        )

    except ValueError:

        print("Ошибка! Введите числа.")

        pause()

        return

    description = input(
        "Описание: "
    )

    new_id = max(products.keys()) + 1

    products[new_id] = {

        "name": name,

        "category": category,

        "price": price,

        "stock": stock,

        "rating": 5.0,

        "description": description

    }

    print("Товар добавлен!")

    print("ID нового товара:", new_id)

    pause()


# ==========================================
#              УДАЛЕНИЕ ТОВАРА
# ==========================================

def delete_product():

    title("УДАЛЕНИЕ ТОВАРА")

    show_products()

    try:

        product_id = int(
            input("ID товара: ")
        )

    except ValueError:

        print("Ошибка!")

        pause()

        return

    if product_id in products:

        deleted = products.pop(product_id)

        print(
            "Удалён товар:",
            deleted["name"]
        )

    else:

        print("Товар не найден!")

    pause()


# ==========================================
#              ИЗМЕНЕНИЕ ЦЕНЫ
# ==========================================

def change_price():

    title("ИЗМЕНЕНИЕ ЦЕНЫ")

    show_products()

    try:

        product_id = int(
            input("ID товара: ")
        )

        new_price = int(
            input("Новая цена: ")
        )

    except ValueError:

        print("Ошибка!")

        pause()

        return

    if product_id not in products:

        print("Товар не найден!")

        pause()

        return

    if new_price <= 0:

        print("Цена должна быть больше 0!")

        pause()

        return

    products[product_id]["price"] = new_price

    print("Цена изменена!")

    pause()


# ==========================================
#              ПОПОЛНЕНИЕ СКЛАДА
# ==========================================

def add_stock():

    title("ПОПОЛНЕНИЕ СКЛАДА")

    show_products()

    try:

        product_id = int(
            input("ID товара: ")
        )

        amount = int(
            input("Количество: ")
        )

    except ValueError:

        print("Ошибка!")

        pause()

        return

    if product_id not in products:

        print("Товар не найден!")

        pause()

        return

    if amount <= 0:

        print("Количество должно быть больше 0!")

        pause()

        return

    products[product_id]["stock"] += amount

    print("Склад пополнен!")

    pause()


# ==========================================
#              РАЗБЛОКИРОВКА
# ==========================================

def unblock_user():

    title("РАЗБЛОКИРОВКА ПОЛЬЗОВАТЕЛЯ")

    username = input(
        "Введите логин: "
    )

    if username in users:

        users[username]["blocked"] = False

        users[username]["attempts"] = 0

        print("Пользователь разблокирован!")

    else:

        print("Пользователь не найден!")

    pause()


# ==========================================
#              УДАЛЕНИЕ ПОЛЬЗОВАТЕЛЯ
# ==========================================

def delete_user():

    title("УДАЛЕНИЕ ПОЛЬЗОВАТЕЛЯ")

    username = input(
        "Введите логин: "
    )

    if username == "admin":

        print("Нельзя удалить администратора!")

        pause()

        return

    if username in users:

        del users[username]

        print("Пользователь удалён!")

    else:

        print("Пользователь не найден!")

    pause()


# ==========================================
#              СОХРАНЕНИЕ ДАННЫХ
# ==========================================

def save_data():

    data = {

        "users": users,

        "products": products

    }

    with open(
        "cat_shop_data.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )


# ==========================================
#              ЗАГРУЗКА ДАННЫХ
# ==========================================

def load_data():

    global users
    global products

    if not os.path.exists("cat_shop_data.json"):

        return

    try:

        with open(
            "cat_shop_data.json",
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

            users = data.get("users", {})

            products = {
                int(k): v
                for k, v in data.get(
                    "products",
                    {}
                ).items()
            }

    except Exception:

        print("Не удалось загрузить данные!")


# ==========================================
#              СОЗДАНИЕ АДМИНА
# ==========================================

def create_admin():

    if "admin" not in users:

        create_user(
            "admin",
            "Admin123!",
            "admin"
        )


# ==========================================
#              ГЛАВНОЕ МЕНЮ
# ==========================================

def main_menu():

    while True:

        title(
            f"{SHOP_NAME} | VERSION {VERSION}"
        )

        print("Добро пожаловать в магазин гаджетов!")

        print()

        print("1. Войти")

        print("2. Регистрация")

        print("3. Забыл пароль")

        print("4. О программе")

        print("5. Выход")

        choice = input(
            "\nВыберите действие: "
        )

        if choice == "1":

            username = login()

            if username:

                if users[username]["role"] == "admin":

                    admin_panel()

                else:

                    user_menu(username)

        elif choice == "2":

            register()

        elif choice == "3":

            reset_password()

        elif choice == "4":

            about_program()

        elif choice == "5":

            save_data()

            print("Данные сохранены!")

            print("До свидания!")

            break

        else:

            print("Неверный выбор!")

            pause()


# ==========================================
#              ВОССТАНОВЛЕНИЕ ПАРОЛЯ
# ==========================================

def reset_password():

    title("ВОССТАНОВЛЕНИЕ ПАРОЛЯ")

    username = input(
        "Введите логин: "
    )

    if username not in users:

        print("Пользователь не найден!")

        pause()

        return

    new_password = input(
        "Введите новый пароль: "
    )

    if not check_password(new_password):

        print("Пароль слишком слабый!")

        pause()

        return

    users[username]["password"] = hash_password(
        new_password
    )

    users[username]["attempts"] = 0

    users[username]["blocked"] = False

    print("Пароль изменён!")

    pause()


# ==========================================
#              О ПРОГРАММЕ
# ==========================================

def about_program():

    title("О ПРОГРАММЕ")

    print("Название:", SHOP_NAME)

    print("Версия:", VERSION)

    print("Язык: Python")

    print("Среда: PyCharm")

    print("Тип: Магазин гаджетов")

    print()

    print("Возможности:")

    print("- Регистрация")

    print("- Вход")

    print("- Каталог")

    print("- Корзина")

    print("- Покупки")

    print("- Баланс")

    print("- Админ-панель")

    print("- Сохранение данных")

    pause()


# ==========================================
#              ЗАПУСК
# ==========================================

if __name__ == "__main__":

    load_data()

    create_admin()

    main_menu()


import hashlib
import random
import string
import os
import json
from datetime import datetime


# ==========================================
#              CAT SHOP
#          ГЛАВНАЯ ПРОГРАММА
# ==========================================


SHOP_NAME = "CAT SHOP"
VERSION = "2.0"


# ==========================================
#              ЦВЕТА И ОФОРМЛЕНИЕ
# ==========================================

def line():
    print("=" * 60)


def small_line():
    print("-" * 60)


def title(text):
    print()
    line()
    print(f"        {text}")
    line()


def pause():
    input("\nНажмите Enter, чтобы продолжить...")


def clear():
    os.system("clear")


# ==========================================
#              ХЕШИРОВАНИЕ
# ==========================================

def hash_password(password):
    return hashlib.sha256(
        password.encode()
    ).hexdigest()


def check_password(password):
    if len(password) < 8:
        return False

    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    special = any(
        c in "!@#$%^&*()_+-="
        for c in password
    )

    return upper and lower and digit and special


def generate_id():
    chars = string.ascii_uppercase + string.digits

    return "".join(
        random.choice(chars)
        for _ in range(8)
    )


# ==========================================
#              ДАННЫЕ МАГАЗИНА
# ==========================================

products = {

    1: {
        "name": "iPhone 15",
        "category": "Телефоны",
        "price": 75000,
        "stock": 10,
        "rating": 4.8,
        "description": "Современный смартфон Apple"
    },

    2: {
        "name": "Samsung Galaxy S24",
        "category": "Телефоны",
        "price": 68000,
        "stock": 15,
        "rating": 4.7,
        "description": "Мощный Android смартфон"
    },

    3: {
        "name": "Xiaomi Redmi Note",
        "category": "Телефоны",
        "price": 22000,
        "stock": 20,
        "rating": 4.5,
        "description": "Доступный смартфон"
    },

    4: {
        "name": "MacBook Air",
        "category": "Ноутбуки",
        "price": 120000,
        "stock": 5,
        "rating": 4.9,
        "description": "Лёгкий ноутбук Apple"
    },

    5: {
        "name": "ASUS VivoBook",
        "category": "Ноутбуки",
        "price": 65000,
        "stock": 8,
        "rating": 4.6,
        "description": "Ноутбук для учёбы"
    },

    6: {
        "name": "Lenovo IdeaPad",
        "category": "Ноутбуки",
        "price": 55000,
        "stock": 12,
        "rating": 4.4,
        "description": "Ноутбук для работы"
    },

    7: {
        "name": "AirPods Pro",
        "category": "Наушники",
        "price": 18000,
        "stock": 25,
        "rating": 4.8,
        "description": "Беспроводные наушники"
    },

    8: {
        "name": "JBL Headphones",
        "category": "Наушники",
        "price": 8500,
        "stock": 30,
        "rating": 4.6,
        "description": "Качественный звук"
    },

    9: {
        "name": "Gaming Mouse",
        "category": "Аксессуары",
        "price": 2500,
        "stock": 40,
        "rating": 4.5,
        "description": "Игровая мышь"
    },

    10: {
        "name": "Mechanical Keyboard",
        "category": "Аксессуары",
        "price": 5500,
        "stock": 18,
        "rating": 4.7,
        "description": "Механическая клавиатура"
    },

    11: {
        "name": "Power Bank",
        "category": "Аксессуары",
        "price": 3000,
        "stock": 35,
        "rating": 4.3,
        "description": "Портативная зарядка"
    },

    12: {
        "name": "Smart Watch",
        "category": "Гаджеты",
        "price": 12000,
        "stock": 14,
        "rating": 4.5,
        "description": "Умные часы"
    }

}


# ==========================================
#              ПОЛЬЗОВАТЕЛИ
# ==========================================

users = {}


# ==========================================
#              СОЗДАНИЕ ПОЛЬЗОВАТЕЛЯ
# ==========================================

def create_user(username, password, role="user"):

    users[username] = {

        "password": hash_password(password),

        "role": role,

        "id": generate_id(),

        "balance": 0,

        "level": 1,

        "experience": 0,

        "cart": {},

        "history": [],

        "blocked": False,

        "attempts": 0,

        "registration_date":
            datetime.now().strftime(
                "%d.%m.%Y"
            )

    }


# ==========================================
#              РЕГИСТРАЦИЯ
# ==========================================

def register():

    title("РЕГИСТРАЦИЯ")

    username = input(
        "Придумайте логин: "
    ).strip()

    if not username:

        print("Логин не может быть пустым!")

        pause()

        return

    if username in users:

        print("Такой пользователь уже существует!")

        pause()

        return

    if len(username) < 3:

        print("Логин должен быть длиннее 2 символов!")

        pause()

        return

    password = input(
        "Придумайте пароль: "
    )

    if not check_password(password):

        print("\nПароль слишком слабый!")

        print("Требования:")

        print("1. Минимум 8 символов")

        print("2. Заглавная буква")

        print("3. Строчная буква")

        print("4. Цифра")

        print("5. Специальный символ")

        pause()

        return

    confirm = input(
        "Повторите пароль: "
    )

    if password != confirm:

        print("Пароли не совпадают!")

        pause()

        return

    create_user(username, password)

    print("\nРегистрация успешна!")

    print("Ваш логин:", username)

    print(
        "Ваш ID:",
        users[username]["id"]
    )

    print("Добро пожаловать в CAT SHOP!")

    pause()


# ==========================================
#              ВХОД
# ==========================================

def login():

    title("ВХОД В CAT SHOP")

    username = input(
        "Введите логин: "
    )

    if username not in users:

        print("Пользователь не найден!")

        pause()

        return None

    user = users[username]

    if user["blocked"]:

        print("Ваш аккаунт заблокирован!")

        pause()

        return None

    password = input(
        "Введите пароль: "
    )

    if hash_password(password) == user["password"]:

        user["attempts"] = 0

        print("\nВы успешно вошли!")

        print(
            "Добро пожаловать,",
            username
        )

        pause()

        return username

    user["attempts"] += 1

    print("Неверный пароль!")

    if user["attempts"] >= 3:

        user["blocked"] = True

        print("Аккаунт заблокирован!")

    else:

        print(
            "Осталось попыток:",
            3 - user["attempts"]
        )

    pause()

    return None


# ==========================================
#              ПОКАЗ ТОВАРОВ
# ==========================================

def show_products():

    title("КАТАЛОГ ТОВАРОВ")

    for product_id, product in products.items():

        print(f"\nID товара: {product_id}")

        print("Название:", product["name"])

        print("Категория:", product["category"])

        print("Цена:", product["price"], "сом")

        print("На складе:", product["stock"])

        print("Рейтинг:", product["rating"])

        print("Описание:", product["description"])

        small_line()


# ==========================================
#              ПОИСК ТОВАРА
# ==========================================

def search_product():

    title("ПОИСК ТОВАРА")

    search = input(
        "Введите название товара: "
    ).lower()

    found = False

    for product_id, product in products.items():

        if search in product["name"].lower():

            print("\nID:", product_id)

            print("Название:", product["name"])

            print("Цена:", product["price"], "сом")

            print("Категория:", product["category"])

            print("Рейтинг:", product["rating"])

            found = True

    if not found:

        print("Товары не найдены!")

    pause()


# ==========================================
#              ФИЛЬТР ПО КАТЕГОРИИ
# ==========================================

def category_products():

    title("КАТЕГОРИИ")

    categories = set(
        product["category"]
        for product in products.values()
    )

    categories = list(categories)

    for i, category in enumerate(categories, 1):

        print(i, ".", category)

    choice = input(
        "\nВведите категорию: "
    )

    for product in products.values():

        if product["category"].lower() == choice.lower():

            print(
                product["name"],
                "-",
                product["price"],
                "сом"
            )

    pause()


# ==========================================
#              ДОБАВЛЕНИЕ В КОРЗИНУ
# ==========================================

def add_to_cart(username):

    title("ДОБАВЛЕНИЕ В КОРЗИНУ")

    show_products()

    try:

        product_id = int(
            input("Введите ID товара: ")
        )

        amount = int(
            input("Введите количество: ")
        )

    except ValueError:

        print("Введите правильное число!")

        pause()

        return

    if product_id not in products:

        print("Такого товара нет!")

        pause()

        return

    product = products[product_id]

    if amount <= 0:

        print("Количество должно быть больше 0!")

        pause()

        return

    if amount > product["stock"]:

        print("Недостаточно товара на складе!")

        pause()

        return

    cart = users[username]["cart"]

    if product_id in cart:

        cart[product_id] += amount

    else:

        cart[product_id] = amount

    print(
        product["name"],
        "добавлен в корзину!"
    )

    pause()


# ==========================================
#              КОРЗИНА
# ==========================================

def show_cart(username):

    title("МОЯ КОРЗИНА")

    cart = users[username]["cart"]

    if not cart:

        print("Корзина пустая!")

        pause()

        return

    total = 0

    for product_id, amount in cart.items():

        product = products[product_id]

        cost = product["price"] * amount

        print(
            product["name"],
            "x",
            amount,
            "=",
            cost,
            "сом"
        )

        total += cost

    small_line()

    print("ИТОГО:", total, "сом")

    pause()


# ==========================================
#              УДАЛЕНИЕ ИЗ КОРЗИНЫ
# ==========================================

def remove_from_cart(username):

    title("УДАЛЕНИЕ ИЗ КОРЗИНЫ")

    cart = users[username]["cart"]

    if not cart:

        print("Корзина пустая!")

        pause()

        return

    show_cart(username)

    try:

        product_id = int(
            input("ID товара для удаления: ")
        )

    except ValueError:

        print("Ошибка!")

        pause()

        return

    if product_id in cart:

        del cart[product_id]

        print("Товар удалён!")

    else:

        print("Такого товара нет в корзине!")

    pause()


# ==========================================
#              ПОКУПКА
# ==========================================

def buy_products(username):

    title("ОФОРМЛЕНИЕ ПОКУПКИ")

    user = users[username]

    cart = user["cart"]

    if not cart:

        print("Корзина пустая!")

        pause()

        return

    total = 0

    for product_id, amount in cart.items():

        product = products[product_id]

        total += product["price"] * amount

    print("Сумма заказа:", total, "сом")

    print("Ваш баланс:", user["balance"], "сом")

    if user["balance"] < total:

        print("\nНедостаточно средств!")

        print("Пополните баланс.")

        pause()

        return

    confirm = input(
        "Подтвердить покупку? (да/нет): "
    ).lower()

    if confirm != "да":

        print("Покупка отменена!")

        pause()

        return

    for product_id, amount in cart.items():

        products[product_id]["stock"] -= amount

    user["balance"] -= total

    user["experience"] += 10

    if user["experience"] >= 100:

        user["level"] += 1

        user["experience"] = 0

        print("Поздравляем! Новый уровень!")

    purchase = {

        "date": datetime.now().strftime(
            "%d.%m.%Y %H:%M"
        ),

        "total": total,

        "items": dict(cart)

    }

    user["history"].append(purchase)

    user["cart"] = {}

    print("\nПокупка успешно оформлена!")

    print("Спасибо за покупку в CAT SHOP!")

    pause()


# ==========================================
#              ПОПОЛНЕНИЕ БАЛАНСА
# ==========================================

def add_balance(username):

    title("ПОПОЛНЕНИЕ БАЛАНСА")

    try:

        amount = int(
            input("Введите сумму: ")
        )

    except ValueError:

        print("Введите число!")

        pause()

        return

    if amount <= 0:

        print("Сумма должна быть больше 0!")

        pause()

        return

    users[username]["balance"] += amount

    print(
        "Баланс пополнен на",
        amount,
        "сом"
    )

    print(
        "Новый баланс:",
        users[username]["balance"]
    )

    pause()


# ==========================================
#              ИСТОРИЯ ПОКУПОК
# ==========================================

def purchase_history(username):

    title("ИСТОРИЯ ПОКУПОК")

    history = users[username]["history"]

    if not history:

        print("Покупок ещё не было!")

        pause()

        return

    for i, purchase in enumerate(history, 1):

        print("\nПокупка №", i)

        print("Дата:", purchase["date"])

        print("Сумма:", purchase["total"], "сом")

        print("Товары:")

        for product_id, amount in purchase["items"].items():

            print(
                "-",
                products[product_id]["name"],
                "x",
                amount
            )

        small_line()

    pause()


# ==========================================
#              ПРОФИЛЬ
# ==========================================

def profile(username):

    title("МОЙ ПРОФИЛЬ")

    user = users[username]

    print("Логин:", username)

    print("ID:", user["id"])

    print("Роль:", user["role"])

    print("Баланс:", user["balance"], "сом")

    print("Уровень:", user["level"])

    print("Опыт:", user["experience"], "/ 100")

    print("Дата регистрации:", user["registration_date"])

    print("Товаров в корзине:", len(user["cart"]))

    print("Количество покупок:", len(user["history"]))

    pause()


# ==========================================
#              ИЗМЕНЕНИЕ ПАРОЛЯ
# ==========================================

def change_password(username):

    title("ИЗМЕНЕНИЕ ПАРОЛЯ")

    old_password = input(
        "Старый пароль: "
    )

    if hash_password(old_password) != users[username]["password"]:

        print("Старый пароль неправильный!")

        pause()

        return

    new_password = input(
        "Новый пароль: "
    )

    if not check_password(new_password):

        print("Новый пароль слишком слабый!")

        pause()

        return

    confirm = input(
        "Повторите новый пароль: "
    )

    if new_password != confirm:

        print("Пароли не совпадают!")

        pause()

        return

    users[username]["password"] = hash_password(
        new_password
    )

    print("Пароль успешно изменён!")

    pause()


# ==========================================
#              МЕНЮ ПОЛЬЗОВАТЕЛЯ
# ==========================================

def user_menu(username):

    while True:

        title("CAT SHOP | USER MENU")

        print("Пользователь:", username)

        print("Баланс:", users[username]["balance"], "сом")

        print()

        print("1. Каталог товаров")

        print("2. Поиск товара")

        print("3. Категории")

        print("4. Добавить товар в корзину")

        print("5. Моя корзина")

        print("6. Удалить товар из корзины")

        print("7. Купить товары")

        print("8. Пополнить баланс")

        print("9. История покупок")

        print("10. Мой профиль")

        print("11. Изменить пароль")

        print("12. Выйти из аккаунта")

        choice = input(
            "\nВыберите действие: "
        )

        if choice == "1":

            show_products()

            pause()

        elif choice == "2":

            search_product()

        elif choice == "3":

            category_products()

        elif choice == "4":

            add_to_cart(username)

        elif choice == "5":

            show_cart(username)

        elif choice == "6":

            remove_from_cart(username)

        elif choice == "7":

            buy_products(username)

        elif choice == "8":

            add_balance(username)

        elif choice == "9":

            purchase_history(username)

        elif choice == "10":

            profile(username)

        elif choice == "11":

            change_password(username)

        elif choice == "12":

            print("Вы вышли из аккаунта!")

            break

        else:

            print("Неверный выбор!")

            pause()


# ==========================================
#              АДМИН-ПАНЕЛЬ
# ==========================================

def admin_panel():

    while True:

        title("ADMIN PANEL")

        print("1. Все пользователи")

        print("2. Все товары")

        print("3. Добавить товар")

        print("4. Удалить товар")

        print("5. Изменить цену")

        print("6. Пополнить склад")

        print("7. Разблокировать пользователя")

        print("8. Удалить пользователя")

        print("9. Выход")

        choice = input(
            "\nВыберите действие: "
        )

        if choice == "1":

            show_all_users()

        elif choice == "2":

            show_products()

            pause()

        elif choice == "3":

            add_product()

        elif choice == "4":

            delete_product()

        elif choice == "5":

            change_price()

        elif choice == "6":

            add_stock()

        elif choice == "7":

            unblock_user()

        elif choice == "8":

            delete_user()

        elif choice == "9":

            break

        else:

            print("Неверный выбор!")

            pause()


# ==========================================
#              ВСЕ ПОЛЬЗОВАТЕЛИ
# ==========================================

def show_all_users():

    title("ВСЕ ПОЛЬЗОВАТЕЛИ")

    for username, user in users.items():

        print("\nЛогин:", username)

        print("ID:", user["id"])

        print("Роль:", user["role"])

        print("Баланс:", user["balance"])

        print("Уровень:", user["level"])

        print("Заблокирован:", user["blocked"])

        small_line()

    pause()


# ==========================================
#              ДОБАВЛЕНИЕ ТОВАРА
# ==========================================

def add_product():

    title("ДОБАВЛЕНИЕ ТОВАРА")

    name = input(
        "Название товара: "
    )

    category = input(
        "Категория: "
    )

    try:

        price = int(
            input("Цена: ")
        )

        stock = int(
            input("Количество: ")
        )

    except ValueError:

        print("Ошибка! Введите числа.")

        pause()

        return

    description = input(
        "Описание: "
    )

    new_id = max(products.keys()) + 1

    products[new_id] = {

        "name": name,

        "category": category,

        "price": price,

        "stock": stock,

        "rating": 5.0,

        "description": description

    }

    print("Товар добавлен!")

    print("ID нового товара:", new_id)

    pause()


# ==========================================
#              УДАЛЕНИЕ ТОВАРА
# ==========================================

def delete_product():

    title("УДАЛЕНИЕ ТОВАРА")

    show_products()

    try:

        product_id = int(
            input("ID товара: ")
        )

    except ValueError:

        print("Ошибка!")

        pause()

        return

    if product_id in products:

        deleted = products.pop(product_id)

        print(
            "Удалён товар:",
            deleted["name"]
        )

    else:

        print("Товар не найден!")

    pause()


# ==========================================
#              ИЗМЕНЕНИЕ ЦЕНЫ
# ==========================================

def change_price():

    title("ИЗМЕНЕНИЕ ЦЕНЫ")

    show_products()

    try:

        product_id = int(
            input("ID товара: ")
        )

        new_price = int(
            input("Новая цена: ")
        )

    except ValueError:

        print("Ошибка!")

        pause()

        return

    if product_id not in products:

        print("Товар не найден!")

        pause()

        return

    if new_price <= 0:

        print("Цена должна быть больше 0!")

        pause()

        return

    products[product_id]["price"] = new_price

    print("Цена изменена!")

    pause()


# ==========================================
#              ПОПОЛНЕНИЕ СКЛАДА
# ==========================================

def add_stock():

    title("ПОПОЛНЕНИЕ СКЛАДА")

    show_products()

    try:

        product_id = int(
            input("ID товара: ")
        )

        amount = int(
            input("Количество: ")
        )

    except ValueError:

        print("Ошибка!")

        pause()

        return

    if product_id not in products:

        print("Товар не найден!")

        pause()

        return

    if amount <= 0:

        print("Количество должно быть больше 0!")

        pause()

        return

    products[product_id]["stock"] += amount

    print("Склад пополнен!")

    pause()


# ==========================================
#              РАЗБЛОКИРОВКА
# ==========================================

def unblock_user():

    title("РАЗБЛОКИРОВКА ПОЛЬЗОВАТЕЛЯ")

    username = input(
        "Введите логин: "
    )

    if username in users:

        users[username]["blocked"] = False

        users[username]["attempts"] = 0

        print("Пользователь разблокирован!")

    else:

        print("Пользователь не найден!")

    pause()


# ==========================================
#              УДАЛЕНИЕ ПОЛЬЗОВАТЕЛЯ
# ==========================================

def delete_user():

    title("УДАЛЕНИЕ ПОЛЬЗОВАТЕЛЯ")

    username = input(
        "Введите логин: "
    )

    if username == "admin":

        print("Нельзя удалить администратора!")

        pause()

        return

    if username in users:

        del users[username]

        print("Пользователь удалён!")

    else:

        print("Пользователь не найден!")

    pause()


# ==========================================
#              СОХРАНЕНИЕ ДАННЫХ
# ==========================================

def save_data():

    data = {

        "users": users,

        "products": products

    }

    with open(
        "cat_shop_data.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )


# ==========================================
#              ЗАГРУЗКА ДАННЫХ
# ==========================================

def load_data():

    global users
    global products

    if not os.path.exists("cat_shop_data.json"):

        return

    try:

        with open(
            "cat_shop_data.json",
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

            users = data.get("users", {})

            products = {
                int(k): v
                for k, v in data.get(
                    "products",
                    {}
                ).items()
            }

    except Exception:

        print("Не удалось загрузить данные!")


# ==========================================
#              СОЗДАНИЕ АДМИНА
# ==========================================

def create_admin():

    if "admin" not in users:

        create_user(
            "admin",
            "Admin123!",
            "admin"
        )


# ==========================================
#              ГЛАВНОЕ МЕНЮ
# ==========================================

def main_menu():

    while True:

        title(
            f"{SHOP_NAME} | VERSION {VERSION}"
        )

        print("Добро пожаловать в магазин гаджетов!")

        print()

        print("1. Войти")

        print("2. Регистрация")

        print("3. Забыл пароль")

        print("4. О программе")

        print("5. Выход")

        choice = input(
            "\nВыберите действие: "
        )

        if choice == "1":

            username = login()

            if username:

                if users[username]["role"] == "admin":

                    admin_panel()

                else:

                    user_menu(username)

        elif choice == "2":

            register()

        elif choice == "3":

            reset_password()

        elif choice == "4":

            about_program()

        elif choice == "5":

            save_data()

            print("Данные сохранены!")

            print("До свидания!")

            break

        else:

            print("Неверный выбор!")

            pause()


# ==========================================
#              ВОССТАНОВЛЕНИЕ ПАРОЛЯ
# ==========================================

def reset_password():

    title("ВОССТАНОВЛЕНИЕ ПАРОЛЯ")

    username = input(
        "Введите логин: "
    )

    if username not in users:

        print("Пользователь не найден!")

        pause()

        return

    new_password = input(
        "Введите новый пароль: "
    )

    if not check_password(new_password):

        print("Пароль слишком слабый!")

        pause()

        return

    users[username]["password"] = hash_password(
        new_password
    )

    users[username]["attempts"] = 0

    users[username]["blocked"] = False

    print("Пароль изменён!")

    pause()


# ==========================================
#              О ПРОГРАММЕ
# ==========================================

def about_program():

    title("О ПРОГРАММЕ")

    print("Название:", SHOP_NAME)

    print("Версия:", VERSION)

    print("Язык: Python")

    print("Среда: PyCharm")

    print("Тип: Магазин гаджетов")

    print()

    print("Возможности:")

    print("- Регистрация")

    print("- Вход")

    print("- Каталог")

    print("- Корзина")

    print("- Покупки")

    print("- Баланс")

    print("- Админ-панель")

    print("- Сохранение данных")

    pause()


# ==========================================
#              ЗАПУСК
# ==========================================

if __name__ == "__main__":

    load_data()

    create_admin()

    main_menu()

import hashlib
import random
import string
import os
import json
from datetime import datetime


# ==========================================
#              CAT SHOP
#          ГЛАВНАЯ ПРОГРАММА
# ==========================================


SHOP_NAME = "CAT SHOP"
VERSION = "2.0"


# ==========================================
#              ЦВЕТА И ОФОРМЛЕНИЕ
# ==========================================

def line():
    print("=" * 60)


def small_line():
    print("-" * 60)


def title(text):
    print()
    line()
    print(f"        {text}")
    line()


def pause():
    input("\nНажмите Enter, чтобы продолжить...")


def clear():
    os.system("clear")


# ==========================================
#              ХЕШИРОВАНИЕ
# ==========================================

def hash_password(password):
    return hashlib.sha256(
        password.encode()
    ).hexdigest()


def check_password(password):
    if len(password) < 8:
        return False

    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    special = any(
        c in "!@#$%^&*()_+-="
        for c in password
    )

    return upper and lower and digit and special


def generate_id():
    chars = string.ascii_uppercase + string.digits

    return "".join(
        random.choice(chars)
        for _ in range(8)
    )


# ==========================================
#              ДАННЫЕ МАГАЗИНА
# ==========================================

products = {

    1: {
        "name": "iPhone 15",
        "category": "Телефоны",
        "price": 75000,
        "stock": 10,
        "rating": 4.8,
        "description": "Современный смартфон Apple"
    },

    2: {
        "name": "Samsung Galaxy S24",
        "category": "Телефоны",
        "price": 68000,
        "stock": 15,
        "rating": 4.7,
        "description": "Мощный Android смартфон"
    },

    3: {
        "name": "Xiaomi Redmi Note",
        "category": "Телефоны",
        "price": 22000,
        "stock": 20,
        "rating": 4.5,
        "description": "Доступный смартфон"
    },

    4: {
        "name": "MacBook Air",
        "category": "Ноутбуки",
        "price": 120000,
        "stock": 5,
        "rating": 4.9,
        "description": "Лёгкий ноутбук Apple"
    },

    5: {
        "name": "ASUS VivoBook",
        "category": "Ноутбуки",
        "price": 65000,
        "stock": 8,
        "rating": 4.6,
        "description": "Ноутбук для учёбы"
    },

    6: {
        "name": "Lenovo IdeaPad",
        "category": "Ноутбуки",
        "price": 55000,
        "stock": 12,
        "rating": 4.4,
        "description": "Ноутбук для работы"
    },

    7: {
        "name": "AirPods Pro",
        "category": "Наушники",
        "price": 18000,
        "stock": 25,
        "rating": 4.8,
        "description": "Беспроводные наушники"
    },

    8: {
        "name": "JBL Headphones",
        "category": "Наушники",
        "price": 8500,
        "stock": 30,
        "rating": 4.6,
        "description": "Качественный звук"
    },

    9: {
        "name": "Gaming Mouse",
        "category": "Аксессуары",
        "price": 2500,
        "stock": 40,
        "rating": 4.5,
        "description": "Игровая мышь"
    },

    10: {
        "name": "Mechanical Keyboard",
        "category": "Аксессуары",
        "price": 5500,
        "stock": 18,
        "rating": 4.7,
        "description": "Механическая клавиатура"
    },

    11: {
        "name": "Power Bank",
        "category": "Аксессуары",
        "price": 3000,
        "stock": 35,
        "rating": 4.3,
        "description": "Портативная зарядка"
    },

    12: {
        "name": "Smart Watch",
        "category": "Гаджеты",
        "price": 12000,
        "stock": 14,
        "rating": 4.5,
        "description": "Умные часы"
    }

}


# ==========================================
#              ПОЛЬЗОВАТЕЛИ
# ==========================================

users = {}


# ==========================================
#              СОЗДАНИЕ ПОЛЬЗОВАТЕЛЯ
# ==========================================

def create_user(username, password, role="user"):

    users[username] = {

        "password": hash_password(password),

        "role": role,

        "id": generate_id(),

        "balance": 0,

        "level": 1,

        "experience": 0,

        "cart": {},

        "history": [],

        "blocked": False,

        "attempts": 0,

        "registration_date":
            datetime.now().strftime(
                "%d.%m.%Y"
            )

    }


# ==========================================
#              РЕГИСТРАЦИЯ
# ==========================================

def register():

    title("РЕГИСТРАЦИЯ")

    username = input(
        "Придумайте логин: "
    ).strip()

    if not username:

        print("Логин не может быть пустым!")

        pause()

        return

    if username in users:

        print("Такой пользователь уже существует!")

        pause()

        return

    if len(username) < 3:

        print("Логин должен быть длиннее 2 символов!")

        pause()

        return

    password = input(
        "Придумайте пароль: "
    )

    if not check_password(password):

        print("\nПароль слишком слабый!")

        print("Требования:")

        print("1. Минимум 8 символов")

        print("2. Заглавная буква")

        print("3. Строчная буква")

        print("4. Цифра")

        print("5. Специальный символ")

        pause()

        return

    confirm = input(
        "Повторите пароль: "
    )

    if password != confirm:

        print("Пароли не совпадают!")

        pause()

        return

    create_user(username, password)

    print("\nРегистрация успешна!")

    print("Ваш логин:", username)

    print(
        "Ваш ID:",
        users[username]["id"]
    )

    print("Добро пожаловать в CAT SHOP!")

    pause()


# ==========================================
#              ВХОД
# ==========================================

def login():

    title("ВХОД В CAT SHOP")

    username = input(
        "Введите логин: "
    )

    if username not in users:

        print("Пользователь не найден!")

        pause()

        return None

    user = users[username]

    if user["blocked"]:

        print("Ваш аккаунт заблокирован!")

        pause()

        return None

    password = input(
        "Введите пароль: "
    )

    if hash_password(password) == user["password"]:

        user["attempts"] = 0

        print("\nВы успешно вошли!")

        print(
            "Добро пожаловать,",
            username
        )

        pause()

        return username

    user["attempts"] += 1

    print("Неверный пароль!")

    if user["attempts"] >= 3:

        user["blocked"] = True

        print("Аккаунт заблокирован!")

    else:

        print(
            "Осталось попыток:",
            3 - user["attempts"]
        )

    pause()

    return None


# ==========================================
#              ПОКАЗ ТОВАРОВ
# ==========================================

def show_products():

    title("КАТАЛОГ ТОВАРОВ")

    for product_id, product in products.items():

        print(f"\nID товара: {product_id}")

        print("Название:", product["name"])

        print("Категория:", product["category"])

        print("Цена:", product["price"], "сом")

        print("На складе:", product["stock"])

        print("Рейтинг:", product["rating"])

        print("Описание:", product["description"])

        small_line()


# ==========================================
#              ПОИСК ТОВАРА
# ==========================================

def search_product():

    title("ПОИСК ТОВАРА")

    search = input(
        "Введите название товара: "
    ).lower()

    found = False

    for product_id, product in products.items():

        if search in product["name"].lower():

            print("\nID:", product_id)

            print("Название:", product["name"])

            print("Цена:", product["price"], "сом")

            print("Категория:", product["category"])

            print("Рейтинг:", product["rating"])

            found = True

    if not found:

        print("Товары не найдены!")

    pause()


# ==========================================
#              ФИЛЬТР ПО КАТЕГОРИИ
# ==========================================

def category_products():

    title("КАТЕГОРИИ")

    categories = set(
        product["category"]
        for product in products.values()
    )

    categories = list(categories)

    for i, category in enumerate(categories, 1):

        print(i, ".", category)

    choice = input(
        "\nВведите категорию: "
    )

    for product in products.values():

        if product["category"].lower() == choice.lower():

            print(
                product["name"],
                "-",
                product["price"],
                "сом"
            )

    pause()


# ==========================================
#              ДОБАВЛЕНИЕ В КОРЗИНУ
# ==========================================

def add_to_cart(username):

    title("ДОБАВЛЕНИЕ В КОРЗИНУ")

    show_products()

    try:

        product_id = int(
            input("Введите ID товара: ")
        )

        amount = int(
            input("Введите количество: ")
        )

    except ValueError:

        print("Введите правильное число!")

        pause()

        return

    if product_id not in products:

        print("Такого товара нет!")

        pause()

        return

    product = products[product_id]

    if amount <= 0:

        print("Количество должно быть больше 0!")

        pause()

        return

    if amount > product["stock"]:

        print("Недостаточно товара на складе!")

        pause()

        return

    cart = users[username]["cart"]

    if product_id in cart:

        cart[product_id] += amount

    else:

        cart[product_id] = amount

    print(
        product["name"],
        "добавлен в корзину!"
    )

    pause()


# ==========================================
#              КОРЗИНА
# ==========================================

def show_cart(username):

    title("МОЯ КОРЗИНА")

    cart = users[username]["cart"]

    if not cart:

        print("Корзина пустая!")

        pause()

        return

    total = 0

    for product_id, amount in cart.items():

        product = products[product_id]

        cost = product["price"] * amount

        print(
            product["name"],
            "x",
            amount,
            "=",
            cost,
            "сом"
        )

        total += cost

    small_line()

    print("ИТОГО:", total, "сом")

    pause()


# ==========================================
#              УДАЛЕНИЕ ИЗ КОРЗИНЫ
# ==========================================

def remove_from_cart(username):

    title("УДАЛЕНИЕ ИЗ КОРЗИНЫ")

    cart = users[username]["cart"]

    if not cart:

        print("Корзина пустая!")

        pause()

        return

    show_cart(username)

    try:

        product_id = int(
            input("ID товара для удаления: ")
        )

    except ValueError:

        print("Ошибка!")

        pause()

        return

    if product_id in cart:

        del cart[product_id]

        print("Товар удалён!")

    else:

        print("Такого товара нет в корзине!")

    pause()


# ==========================================
#              ПОКУПКА
# ==========================================

def buy_products(username):

    title("ОФОРМЛЕНИЕ ПОКУПКИ")

    user = users[username]

    cart = user["cart"]

    if not cart:

        print("Корзина пустая!")

        pause()

        return

    total = 0

    for product_id, amount in cart.items():

        product = products[product_id]

        total += product["price"] * amount

    print("Сумма заказа:", total, "сом")

    print("Ваш баланс:", user["balance"], "сом")

    if user["balance"] < total:

        print("\nНедостаточно средств!")

        print("Пополните баланс.")

        pause()

        return

    confirm = input(
        "Подтвердить покупку? (да/нет): "
    ).lower()

    if confirm != "да":

        print("Покупка отменена!")

        pause()

        return

    for product_id, amount in cart.items():

        products[product_id]["stock"] -= amount

    user["balance"] -= total

    user["experience"] += 10

    if user["experience"] >= 100:

        user["level"] += 1

        user["experience"] = 0

        print("Поздравляем! Новый уровень!")

    purchase = {

        "date": datetime.now().strftime(
            "%d.%m.%Y %H:%M"
        ),

        "total": total,

        "items": dict(cart)

    }

    user["history"].append(purchase)

    user["cart"] = {}

    print("\nПокупка успешно оформлена!")

    print("Спасибо за покупку в CAT SHOP!")

    pause()


# ==========================================
#              ПОПОЛНЕНИЕ БАЛАНСА
# ==========================================

def add_balance(username):

    title("ПОПОЛНЕНИЕ БАЛАНСА")

    try:

        amount = int(
            input("Введите сумму: ")
        )

    except ValueError:

        print("Введите число!")

        pause()

        return

    if amount <= 0:

        print("Сумма должна быть больше 0!")

        pause()

        return

    users[username]["balance"] += amount

    print(
        "Баланс пополнен на",
        amount,
        "сом"
    )

    print(
        "Новый баланс:",
        users[username]["balance"]
    )

    pause()


# ==========================================
#              ИСТОРИЯ ПОКУПОК
# ==========================================

def purchase_history(username):

    title("ИСТОРИЯ ПОКУПОК")

    history = users[username]["history"]

    if not history:

        print("Покупок ещё не было!")

        pause()

        return

    for i, purchase in enumerate(history, 1):

        print("\nПокупка №", i)

        print("Дата:", purchase["date"])

        print("Сумма:", purchase["total"], "сом")

        print("Товары:")

        for product_id, amount in purchase["items"].items():

            print(
                "-",
                products[product_id]["name"],
                "x",
                amount
            )

        small_line()

    pause()


# ==========================================
#              ПРОФИЛЬ
# ==========================================

def profile(username):

    title("МОЙ ПРОФИЛЬ")

    user = users[username]

    print("Логин:", username)

    print("ID:", user["id"])

    print("Роль:", user["role"])

    print("Баланс:", user["balance"], "сом")

    print("Уровень:", user["level"])

    print("Опыт:", user["experience"], "/ 100")

    print("Дата регистрации:", user["registration_date"])

    print("Товаров в корзине:", len(user["cart"]))

    print("Количество покупок:", len(user["history"]))

    pause()


# ==========================================
#              ИЗМЕНЕНИЕ ПАРОЛЯ
# ==========================================

def change_password(username):

    title("ИЗМЕНЕНИЕ ПАРОЛЯ")

    old_password = input(
        "Старый пароль: "
    )

    if hash_password(old_password) != users[username]["password"]:

        print("Старый пароль неправильный!")

        pause()

        return

    new_password = input(
        "Новый пароль: "
    )

    if not check_password(new_password):

        print("Новый пароль слишком слабый!")

        pause()

        return

    confirm = input(
        "Повторите новый пароль: "
    )

    if new_password != confirm:

        print("Пароли не совпадают!")

        pause()

        return

    users[username]["password"] = hash_password(
        new_password
    )

    print("Пароль успешно изменён!")

    pause()


# ==========================================
#              МЕНЮ ПОЛЬЗОВАТЕЛЯ
# ==========================================

def user_menu(username):

    while True:

        title("CAT SHOP | USER MENU")

        print("Пользователь:", username)

        print("Баланс:", users[username]["balance"], "сом")

        print()

        print("1. Каталог товаров")

        print("2. Поиск товара")

        print("3. Категории")

        print("4. Добавить товар в корзину")

        print("5. Моя корзина")

        print("6. Удалить товар из корзины")

        print("7. Купить товары")

        print("8. Пополнить баланс")

        print("9. История покупок")

        print("10. Мой профиль")

        print("11. Изменить пароль")

        print("12. Выйти из аккаунта")

        choice = input(
            "\nВыберите действие: "
        )

        if choice == "1":

            show_products()

            pause()

        elif choice == "2":

            search_product()

        elif choice == "3":

            category_products()

        elif choice == "4":

            add_to_cart(username)

        elif choice == "5":

            show_cart(username)

        elif choice == "6":

            remove_from_cart(username)

        elif choice == "7":

            buy_products(username)

        elif choice == "8":

            add_balance(username)

        elif choice == "9":

            purchase_history(username)

        elif choice == "10":

            profile(username)

        elif choice == "11":

            change_password(username)

        elif choice == "12":

            print("Вы вышли из аккаунта!")

            break

        else:

            print("Неверный выбор!")

            pause()


# ==========================================
#              АДМИН-ПАНЕЛЬ
# ==========================================

def admin_panel():

    while True:

        title("ADMIN PANEL")

        print("1. Все пользователи")

        print("2. Все товары")

        print("3. Добавить товар")

        print("4. Удалить товар")

        print("5. Изменить цену")

        print("6. Пополнить склад")

        print("7. Разблокировать пользователя")

        print("8. Удалить пользователя")

        print("9. Выход")

        choice = input(
            "\nВыберите действие: "
        )

        if choice == "1":

            show_all_users()

        elif choice == "2":

            show_products()

            pause()

        elif choice == "3":

            add_product()

        elif choice == "4":

            delete_product()

        elif choice == "5":

            change_price()

        elif choice == "6":

            add_stock()

        elif choice == "7":

            unblock_user()

        elif choice == "8":

            delete_user()

        elif choice == "9":

            break

        else:

            print("Неверный выбор!")

            pause()


# ==========================================
#              ВСЕ ПОЛЬЗОВАТЕЛИ
# ==========================================

def show_all_users():

    title("ВСЕ ПОЛЬЗОВАТЕЛИ")

    for username, user in users.items():

        print("\nЛогин:", username)

        print("ID:", user["id"])

        print("Роль:", user["role"])

        print("Баланс:", user["balance"])

        print("Уровень:", user["level"])

        print("Заблокирован:", user["blocked"])

        small_line()

    pause()


# ==========================================
#              ДОБАВЛЕНИЕ ТОВАРА
# ==========================================

def add_product():

    title("ДОБАВЛЕНИЕ ТОВАРА")

    name = input(
        "Название товара: "
    )

    category = input(
        "Категория: "
    )

    try:

        price = int(
            input("Цена: ")
        )

        stock = int(
            input("Количество: ")
        )

    except ValueError:

        print("Ошибка! Введите числа.")

        pause()

        return

    description = input(
        "Описание: "
    )

    new_id = max(products.keys()) + 1

    products[new_id] = {

        "name": name,

        "category": category,

        "price": price,

        "stock": stock,

        "rating": 5.0,

        "description": description

    }

    print("Товар добавлен!")

    print("ID нового товара:", new_id)

    pause()


# ==========================================
#              УДАЛЕНИЕ ТОВАРА
# ==========================================

def delete_product():

    title("УДАЛЕНИЕ ТОВАРА")

    show_products()

    try:

        product_id = int(
            input("ID товара: ")
        )

    except ValueError:

        print("Ошибка!")

        pause()

        return

    if product_id in products:

        deleted = products.pop(product_id)

        print(
            "Удалён товар:",
            deleted["name"]
        )

    else:

        print("Товар не найден!")

    pause()


# ==========================================
#              ИЗМЕНЕНИЕ ЦЕНЫ
# ==========================================

def change_price():

    title("ИЗМЕНЕНИЕ ЦЕНЫ")

    show_products()

    try:

        product_id = int(
            input("ID товара: ")
        )

        new_price = int(
            input("Новая цена: ")
        )

    except ValueError:

        print("Ошибка!")

        pause()

        return

    if product_id not in products:

        print("Товар не найден!")

        pause()

        return

    if new_price <= 0:

        print("Цена должна быть больше 0!")

        pause()

        return

    products[product_id]["price"] = new_price

    print("Цена изменена!")

    pause()


# ==========================================
#              ПОПОЛНЕНИЕ СКЛАДА
# ==========================================

def add_stock():

    title("ПОПОЛНЕНИЕ СКЛАДА")

    show_products()

    try:

        product_id = int(
            input("ID товара: ")
        )

        amount = int(
            input("Количество: ")
        )

    except ValueError:

        print("Ошибка!")

        pause()

        return

    if product_id not in products:

        print("Товар не найден!")

        pause()

        return

    if amount <= 0:

        print("Количество должно быть больше 0!")

        pause()

        return

    products[product_id]["stock"] += amount

    print("Склад пополнен!")

    pause()


# ==========================================
#              РАЗБЛОКИРОВКА
# ==========================================

def unblock_user():

    title("РАЗБЛОКИРОВКА ПОЛЬЗОВАТЕЛЯ")

    username = input(
        "Введите логин: "
    )

    if username in users:

        users[username]["blocked"] = False

        users[username]["attempts"] = 0

        print("Пользователь разблокирован!")

    else:

        print("Пользователь не найден!")

    pause()


# ==========================================
#              УДАЛЕНИЕ ПОЛЬЗОВАТЕЛЯ
# ==========================================

def delete_user():

    title("УДАЛЕНИЕ ПОЛЬЗОВАТЕЛЯ")

    username = input(
        "Введите логин: "
    )

    if username == "admin":

        print("Нельзя удалить администратора!")

        pause()

        return

    if username in users:

        del users[username]

        print("Пользователь удалён!")

    else:

        print("Пользователь не найден!")

    pause()


# ==========================================
#              СОХРАНЕНИЕ ДАННЫХ
# ==========================================

def save_data():

    data = {

        "users": users,

        "products": products

    }

    with open(
        "cat_shop_data.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )


# ==========================================
#              ЗАГРУЗКА ДАННЫХ
# ==========================================

def load_data():

    global users
    global products

    if not os.path.exists("cat_shop_data.json"):

        return

    try:

        with open(
            "cat_shop_data.json",
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

            users = data.get("users", {})

            products = {
                int(k): v
                for k, v in data.get(
                    "products",
                    {}
                ).items()
            }

    except Exception:

        print("Не удалось загрузить данные!")


# ==========================================
#              СОЗДАНИЕ АДМИНА
# ==========================================

def create_admin():

    if "admin" not in users:

        create_user(
            "admin",
            "Admin123!",
            "admin"
        )


# ==========================================
#              ГЛАВНОЕ МЕНЮ
# ==========================================

def main_menu():

    while True:

        title(
            f"{SHOP_NAME} | VERSION {VERSION}"
        )

        print("Добро пожаловать в магазин гаджетов!")

        print()

        print("1. Войти")

        print("2. Регистрация")

        print("3. Забыл пароль")

        print("4. О программе")

        print("5. Выход")

        choice = input(
            "\nВыберите действие: "
        )

        if choice == "1":

            username = login()

            if username:

                if users[username]["role"] == "admin":

                    admin_panel()

                else:

                    user_menu(username)

        elif choice == "2":

            register()

        elif choice == "3":

            reset_password()

        elif choice == "4":

            about_program()

        elif choice == "5":

            save_data()

            print("Данные сохранены!")

            print("До свидания!")

            break

        else:

            print("Неверный выбор!")

            pause()


# ==========================================
#              ВОССТАНОВЛЕНИЕ ПАРОЛЯ
# ==========================================

def reset_password():

    title("ВОССТАНОВЛЕНИЕ ПАРОЛЯ")

    username = input(
        "Введите логин: "
    )

    if username not in users:

        print("Пользователь не найден!")

        pause()

        return

    new_password = input(
        "Введите новый пароль: "
    )

    if not check_password(new_password):

        print("Пароль слишком слабый!")

        pause()

        return

    users[username]["password"] = hash_password(
        new_password
    )

    users[username]["attempts"] = 0

    users[username]["blocked"] = False

    print("Пароль изменён!")

    pause()


# ==========================================
#              О ПРОГРАММЕ
# ==========================================

def about_program():

    title("О ПРОГРАММЕ")

    print("Название:", SHOP_NAME)

    print("Версия:", VERSION)

    print("Язык: Python")

    print("Среда: PyCharm")

    print("Тип: Магазин гаджетов")

    print()

    print("Возможности:")

    print("- Регистрация")

    print("- Вход")

    print("- Каталог")

    print("- Корзина")

    print("- Покупки")

    print("- Баланс")

    print("- Админ-панель")

    print("- Сохранение данных")

    pause()


# ==========================================
#              ЗАПУСК
# ==========================================

if __name__ == "__main__":

    load_data()

    create_admin()

    main_menu()

import hashlib
import random
import string
import os
import json
from datetime import datetime


# ==========================================
#              CAT SHOP
#          ГЛАВНАЯ ПРОГРАММА
# ==========================================


SHOP_NAME = "CAT SHOP"
VERSION = "2.0"


# ==========================================
#              ЦВЕТА И ОФОРМЛЕНИЕ
# ==========================================

def line():
    print("=" * 60)


def small_line():
    print("-" * 60)


def title(text):
    print()
    line()
    print(f"        {text}")
    line()


def pause():
    input("\nНажмите Enter, чтобы продолжить...")


def clear():
    os.system("clear")


# ==========================================
#              ХЕШИРОВАНИЕ
# ==========================================

def hash_password(password):
    return hashlib.sha256(
        password.encode()
    ).hexdigest()


def check_password(password):
    if len(password) < 8:
        return False

    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    special = any(
        c in "!@#$%^&*()_+-="
        for c in password
    )

    return upper and lower and digit and special


def generate_id():
    chars = string.ascii_uppercase + string.digits

    return "".join(
        random.choice(chars)
        for _ in range(8)
    )


# ==========================================
#              ДАННЫЕ МАГАЗИНА
# ==========================================

products = {

    1: {
        "name": "iPhone 15",
        "category": "Телефоны",
        "price": 75000,
        "stock": 10,
        "rating": 4.8,
        "description": "Современный смартфон Apple"
    },

    2: {
        "name": "Samsung Galaxy S24",
        "category": "Телефоны",
        "price": 68000,
        "stock": 15,
        "rating": 4.7,
        "description": "Мощный Android смартфон"
    },

    3: {
        "name": "Xiaomi Redmi Note",
        "category": "Телефоны",
        "price": 22000,
        "stock": 20,
        "rating": 4.5,
        "description": "Доступный смартфон"
    },

    4: {
        "name": "MacBook Air",
        "category": "Ноутбуки",
        "price": 120000,
        "stock": 5,
        "rating": 4.9,
        "description": "Лёгкий ноутбук Apple"
    },

    5: {
        "name": "ASUS VivoBook",
        "category": "Ноутбуки",
        "price": 65000,
        "stock": 8,
        "rating": 4.6,
        "description": "Ноутбук для учёбы"
    },

    6: {
        "name": "Lenovo IdeaPad",
        "category": "Ноутбуки",
        "price": 55000,
        "stock": 12,
        "rating": 4.4,
        "description": "Ноутбук для работы"
    },

    7: {
        "name": "AirPods Pro",
        "category": "Наушники",
        "price": 18000,
        "stock": 25,
        "rating": 4.8,
        "description": "Беспроводные наушники"
    },

    8: {
        "name": "JBL Headphones",
        "category": "Наушники",
        "price": 8500,
        "stock": 30,
        "rating": 4.6,
        "description": "Качественный звук"
    },

    9: {
        "name": "Gaming Mouse",
        "category": "Аксессуары",
        "price": 2500,
        "stock": 40,
        "rating": 4.5,
        "description": "Игровая мышь"
    },

    10: {
        "name": "Mechanical Keyboard",
        "category": "Аксессуары",
        "price": 5500,
        "stock": 18,
        "rating": 4.7,
        "description": "Механическая клавиатура"
    },

    11: {
        "name": "Power Bank",
        "category": "Аксессуары",
        "price": 3000,
        "stock": 35,
        "rating": 4.3,
        "description": "Портативная зарядка"
    },

    12: {
        "name": "Smart Watch",
        "category": "Гаджеты",
        "price": 12000,
        "stock": 14,
        "rating": 4.5,
        "description": "Умные часы"
    }

}


# ==========================================
#              ПОЛЬЗОВАТЕЛИ
# ==========================================

users = {}


# ==========================================
#              СОЗДАНИЕ ПОЛЬЗОВАТЕЛЯ
# ==========================================

def create_user(username, password, role="user"):

    users[username] = {

        "password": hash_password(password),

        "role": role,

        "id": generate_id(),

        "balance": 0,

        "level": 1,

        "experience": 0,

        "cart": {},

        "history": [],

        "blocked": False,

        "attempts": 0,

        "registration_date":
            datetime.now().strftime(
                "%d.%m.%Y"
            )

    }


# ==========================================
#              РЕГИСТРАЦИЯ
# ==========================================

def register():

    title("РЕГИСТРАЦИЯ")

    username = input(
        "Придумайте логин: "
    ).strip()

    if not username:

        print("Логин не может быть пустым!")

        pause()

        return

    if username in users:

        print("Такой пользователь уже существует!")

        pause()

        return

    if len(username) < 3:

        print("Логин должен быть длиннее 2 символов!")

        pause()

        return

    password = input(
        "Придумайте пароль: "
    )

    if not check_password(password):

        print("\nПароль слишком слабый!")

        print("Требования:")

        print("1. Минимум 8 символов")

        print("2. Заглавная буква")

        print("3. Строчная буква")

        print("4. Цифра")

        print("5. Специальный символ")

        pause()

        return

    confirm = input(
        "Повторите пароль: "
    )

    if password != confirm:

        print("Пароли не совпадают!")

        pause()

        return

    create_user(username, password)

    print("\nРегистрация успешна!")

    print("Ваш логин:", username)

    print(
        "Ваш ID:",
        users[username]["id"]
    )

    print("Добро пожаловать в CAT SHOP!")

    pause()


# ==========================================
#              ВХОД
# ==========================================

def login():

    title("ВХОД В CAT SHOP")

    username = input(
        "Введите логин: "
    )

    if username not in users:

        print("Пользователь не найден!")

        pause()

        return None

    user = users[username]

    if user["blocked"]:

        print("Ваш аккаунт заблокирован!")

        pause()

        return None

    password = input(
        "Введите пароль: "
    )

    if hash_password(password) == user["password"]:

        user["attempts"] = 0

        print("\nВы успешно вошли!")

        print(
            "Добро пожаловать,",
            username
        )

        pause()

        return username

    user["attempts"] += 1

    print("Неверный пароль!")

    if user["attempts"] >= 3:

        user["blocked"] = True

        print("Аккаунт заблокирован!")

    else:

        print(
            "Осталось попыток:",
            3 - user["attempts"]
        )

    pause()

    return None


# ==========================================
#              ПОКАЗ ТОВАРОВ
# ==========================================

def show_products():

    title("КАТАЛОГ ТОВАРОВ")

    for product_id, product in products.items():

        print(f"\nID товара: {product_id}")

        print("Название:", product["name"])

        print("Категория:", product["category"])

        print("Цена:", product["price"], "сом")

        print("На складе:", product["stock"])

        print("Рейтинг:", product["rating"])

        print("Описание:", product["description"])

        small_line()


# ==========================================
#              ПОИСК ТОВАРА
# ==========================================

def search_product():

    title("ПОИСК ТОВАРА")

    search = input(
        "Введите название товара: "
    ).lower()

    found = False

    for product_id, product in products.items():

        if search in product["name"].lower():

            print("\nID:", product_id)

            print("Название:", product["name"])

            print("Цена:", product["price"], "сом")

            print("Категория:", product["category"])

            print("Рейтинг:", product["rating"])

            found = True

    if not found:

        print("Товары не найдены!")

    pause()


# ==========================================
#              ФИЛЬТР ПО КАТЕГОРИИ
# ==========================================

def category_products():

    title("КАТЕГОРИИ")

    categories = set(
        product["category"]
        for product in products.values()
    )

    categories = list(categories)

    for i, category in enumerate(categories, 1):

        print(i, ".", category)

    choice = input(
        "\nВведите категорию: "
    )

    for product in products.values():

        if product["category"].lower() == choice.lower():

            print(
                product["name"],
                "-",
                product["price"],
                "сом"
            )

    pause()


# ==========================================
#              ДОБАВЛЕНИЕ В КОРЗИНУ
# ==========================================

def add_to_cart(username):

    title("ДОБАВЛЕНИЕ В КОРЗИНУ")

    show_products()

    try:

        product_id = int(
            input("Введите ID товара: ")
        )

        amount = int(
            input("Введите количество: ")
        )

    except ValueError:

        print("Введите правильное число!")

        pause()

        return

    if product_id not in products:

        print("Такого товара нет!")

        pause()

        return

    product = products[product_id]

    if amount <= 0:

        print("Количество должно быть больше 0!")

        pause()

        return

    if amount > product["stock"]:

        print("Недостаточно товара на складе!")

        pause()

        return

    cart = users[username]["cart"]

    if product_id in cart:

        cart[product_id] += amount

    else:

        cart[product_id] = amount

    print(
        product["name"],
        "добавлен в корзину!"
    )

    pause()


# ==========================================
#              КОРЗИНА
# ==========================================

def show_cart(username):

    title("МОЯ КОРЗИНА")

    cart = users[username]["cart"]

    if not cart:

        print("Корзина пустая!")

        pause()

        return

    total = 0

    for product_id, amount in cart.items():

        product = products[product_id]

        cost = product["price"] * amount

        print(
            product["name"],
            "x",
            amount,
            "=",
            cost,
            "сом"
        )

        total += cost

    small_line()

    print("ИТОГО:", total, "сом")

    pause()


# ==========================================
#              УДАЛЕНИЕ ИЗ КОРЗИНЫ
# ==========================================

def remove_from_cart(username):

    title("УДАЛЕНИЕ ИЗ КОРЗИНЫ")

    cart = users[username]["cart"]

    if not cart:

        print("Корзина пустая!")

        pause()

        return

    show_cart(username)

    try:

        product_id = int(
            input("ID товара для удаления: ")
        )

    except ValueError:

        print("Ошибка!")

        pause()

        return

    if product_id in cart:

        del cart[product_id]

        print("Товар удалён!")

    else:

        print("Такого товара нет в корзине!")

    pause()


# ==========================================
#              ПОКУПКА
# ==========================================

def buy_products(username):

    title("ОФОРМЛЕНИЕ ПОКУПКИ")

    user = users[username]

    cart = user["cart"]

    if not cart:

        print("Корзина пустая!")

        pause()

        return

    total = 0

    for product_id, amount in cart.items():

        product = products[product_id]

        total += product["price"] * amount

    print("Сумма заказа:", total, "сом")

    print("Ваш баланс:", user["balance"], "сом")

    if user["balance"] < total:

        print("\nНедостаточно средств!")

        print("Пополните баланс.")

        pause()

        return

    confirm = input(
        "Подтвердить покупку? (да/нет): "
    ).lower()

    if confirm != "да":

        print("Покупка отменена!")

        pause()

        return

    for product_id, amount in cart.items():

        products[product_id]["stock"] -= amount

    user["balance"] -= total

    user["experience"] += 10

    if user["experience"] >= 100:

        user["level"] += 1

        user["experience"] = 0

        print("Поздравляем! Новый уровень!")

    purchase = {

        "date": datetime.now().strftime(
            "%d.%m.%Y %H:%M"
        ),

        "total": total,

        "items": dict(cart)

    }

    user["history"].append(purchase)

    user["cart"] = {}

    print("\nПокупка успешно оформлена!")

    print("Спасибо за покупку в CAT SHOP!")

    pause()


# ==========================================
#              ПОПОЛНЕНИЕ БАЛАНСА
# ==========================================

def add_balance(username):

    title("ПОПОЛНЕНИЕ БАЛАНСА")

    try:

        amount = int(
            input("Введите сумму: ")
        )

    except ValueError:

        print("Введите число!")

        pause()

        return

    if amount <= 0:

        print("Сумма должна быть больше 0!")

        pause()

        return

    users[username]["balance"] += amount

    print(
        "Баланс пополнен на",
        amount,
        "сом"
    )

    print(
        "Новый баланс:",
        users[username]["balance"]
    )

    pause()


# ==========================================
#              ИСТОРИЯ ПОКУПОК
# ==========================================

def purchase_history(username):

    title("ИСТОРИЯ ПОКУПОК")

    history = users[username]["history"]

    if not history:

        print("Покупок ещё не было!")

        pause()

        return

    for i, purchase in enumerate(history, 1):

        print("\nПокупка №", i)

        print("Дата:", purchase["date"])

        print("Сумма:", purchase["total"], "сом")

        print("Товары:")

        for product_id, amount in purchase["items"].items():

            print(
                "-",
                products[product_id]["name"],
                "x",
                amount
            )

        small_line()

    pause()


# ==========================================
#              ПРОФИЛЬ
# ==========================================

def profile(username):

    title("МОЙ ПРОФИЛЬ")

    user = users[username]

    print("Логин:", username)

    print("ID:", user["id"])

    print("Роль:", user["role"])

    print("Баланс:", user["balance"], "сом")

    print("Уровень:", user["level"])

    print("Опыт:", user["experience"], "/ 100")

    print("Дата регистрации:", user["registration_date"])

    print("Товаров в корзине:", len(user["cart"]))

    print("Количество покупок:", len(user["history"]))

    pause()


# ==========================================
#              ИЗМЕНЕНИЕ ПАРОЛЯ
# ==========================================

def change_password(username):

    title("ИЗМЕНЕНИЕ ПАРОЛЯ")

    old_password = input(
        "Старый пароль: "
    )

    if hash_password(old_password) != users[username]["password"]:

        print("Старый пароль неправильный!")

        pause()

        return

    new_password = input(
        "Новый пароль: "
    )

    if not check_password(new_password):

        print("Новый пароль слишком слабый!")

        pause()

        return

    confirm = input(
        "Повторите новый пароль: "
    )

    if new_password != confirm:

        print("Пароли не совпадают!")

        pause()

        return

    users[username]["password"] = hash_password(
        new_password
    )

    print("Пароль успешно изменён!")

    pause()


# ==========================================
#              МЕНЮ ПОЛЬЗОВАТЕЛЯ
# ==========================================

def user_menu(username):

    while True:

        title("CAT SHOP | USER MENU")

        print("Пользователь:", username)

        print("Баланс:", users[username]["balance"], "сом")

        print()

        print("1. Каталог товаров")

        print("2. Поиск товара")

        print("3. Категории")

        print("4. Добавить товар в корзину")

        print("5. Моя корзина")

        print("6. Удалить товар из корзины")

        print("7. Купить товары")

        print("8. Пополнить баланс")

        print("9. История покупок")

        print("10. Мой профиль")

        print("11. Изменить пароль")

        print("12. Выйти из аккаунта")

        choice = input(
            "\nВыберите действие: "
        )

        if choice == "1":

            show_products()

            pause()

        elif choice == "2":

            search_product()

        elif choice == "3":

            category_products()

        elif choice == "4":

            add_to_cart(username)

        elif choice == "5":

            show_cart(username)

        elif choice == "6":

            remove_from_cart(username)

        elif choice == "7":

            buy_products(username)

        elif choice == "8":

            add_balance(username)

        elif choice == "9":

            purchase_history(username)

        elif choice == "10":

            profile(username)

        elif choice == "11":

            change_password(username)

        elif choice == "12":

            print("Вы вышли из аккаунта!")

            break

        else:

            print("Неверный выбор!")

            pause()


# ==========================================
#              АДМИН-ПАНЕЛЬ
# ==========================================

def admin_panel():

    while True:

        title("ADMIN PANEL")

        print("1. Все пользователи")

        print("2. Все товары")

        print("3. Добавить товар")

        print("4. Удалить товар")

        print("5. Изменить цену")

        print("6. Пополнить склад")

        print("7. Разблокировать пользователя")

        print("8. Удалить пользователя")

        print("9. Выход")

        choice = input(
            "\nВыберите действие: "
        )

        if choice == "1":

            show_all_users()

        elif choice == "2":

            show_products()

            pause()

        elif choice == "3":

            add_product()

        elif choice == "4":

            delete_product()

        elif choice == "5":

            change_price()

        elif choice == "6":

            add_stock()

        elif choice == "7":

            unblock_user()

        elif choice == "8":

            delete_user()

        elif choice == "9":

            break

        else:

            print("Неверный выбор!")

            pause()


# ==========================================
#              ВСЕ ПОЛЬЗОВАТЕЛИ
# ==========================================

def show_all_users():

    title("ВСЕ ПОЛЬЗОВАТЕЛИ")

    for username, user in users.items():

        print("\nЛогин:", username)

        print("ID:", user["id"])

        print("Роль:", user["role"])

        print("Баланс:", user["balance"])

        print("Уровень:", user["level"])

        print("Заблокирован:", user["blocked"])

        small_line()

    pause()


# ==========================================
#              ДОБАВЛЕНИЕ ТОВАРА
# ==========================================

def add_product():

    title("ДОБАВЛЕНИЕ ТОВАРА")

    name = input(
        "Название товара: "
    )

    category = input(
        "Категория: "
    )

    try:

        price = int(
            input("Цена: ")
        )

        stock = int(
            input("Количество: ")
        )

    except ValueError:

        print("Ошибка! Введите числа.")

        pause()

        return

    description = input(
        "Описание: "
    )

    new_id = max(products.keys()) + 1

    products[new_id] = {

        "name": name,

        "category": category,

        "price": price,

        "stock": stock,

        "rating": 5.0,

        "description": description

    }

    print("Товар добавлен!")

    print("ID нового товара:", new_id)

    pause()


# ==========================================
#              УДАЛЕНИЕ ТОВАРА
# ==========================================

def delete_product():

    title("УДАЛЕНИЕ ТОВАРА")

    show_products()

    try:

        product_id = int(
            input("ID товара: ")
        )

    except ValueError:

        print("Ошибка!")

        pause()

        return

    if product_id in products:

        deleted = products.pop(product_id)

        print(
            "Удалён товар:",
            deleted["name"]
        )

    else:

        print("Товар не найден!")

    pause()


# ==========================================
#              ИЗМЕНЕНИЕ ЦЕНЫ
# ==========================================

def change_price():

    title("ИЗМЕНЕНИЕ ЦЕНЫ")

    show_products()

    try:

        product_id = int(
            input("ID товара: ")
        )

        new_price = int(
            input("Новая цена: ")
        )

    except ValueError:

        print("Ошибка!")

        pause()

        return

    if product_id not in products:

        print("Товар не найден!")

        pause()

        return

    if new_price <= 0:

        print("Цена должна быть больше 0!")

        pause()

        return

    products[product_id]["price"] = new_price

    print("Цена изменена!")

    pause()


# ==========================================
#              ПОПОЛНЕНИЕ СКЛАДА
# ==========================================

def add_stock():

    title("ПОПОЛНЕНИЕ СКЛАДА")

    show_products()

    try:

        product_id = int(
            input("ID товара: ")
        )

        amount = int(
            input("Количество: ")
        )

    except ValueError:

        print("Ошибка!")

        pause()

        return

    if product_id not in products:

        print("Товар не найден!")

        pause()

        return

    if amount <= 0:

        print("Количество должно быть больше 0!")

        pause()

        return

    products[product_id]["stock"] += amount

    print("Склад пополнен!")

    pause()


# ==========================================
#              РАЗБЛОКИРОВКА
# ==========================================

def unblock_user():

    title("РАЗБЛОКИРОВКА ПОЛЬЗОВАТЕЛЯ")

    username = input(
        "Введите логин: "
    )

    if username in users:

        users[username]["blocked"] = False

        users[username]["attempts"] = 0

        print("Пользователь разблокирован!")

    else:

        print("Пользователь не найден!")

    pause()


# ==========================================
#              УДАЛЕНИЕ ПОЛЬЗОВАТЕЛЯ
# ==========================================

def delete_user():

    title("УДАЛЕНИЕ ПОЛЬЗОВАТЕЛЯ")

    username = input(
        "Введите логин: "
    )

    if username == "admin":

        print("Нельзя удалить администратора!")

        pause()

        return

    if username in users:

        del users[username]

        print("Пользователь удалён!")

    else:

        print("Пользователь не найден!")

    pause()


# ==========================================
#              СОХРАНЕНИЕ ДАННЫХ
# ==========================================

def save_data():

    data = {

        "users": users,

        "products": products

    }

    with open(
        "cat_shop_data.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )


# ==========================================
#              ЗАГРУЗКА ДАННЫХ
# ==========================================

def load_data():

    global users
    global products

    if not os.path.exists("cat_shop_data.json"):

        return

    try:

        with open(
            "cat_shop_data.json",
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

            users = data.get("users", {})

            products = {
                int(k): v
                for k, v in data.get(
                    "products",
                    {}
                ).items()
            }

    except Exception:

        print("Не удалось загрузить данные!")


# ==========================================
#              СОЗДАНИЕ АДМИНА
# ==========================================

def create_admin():

    if "admin" not in users:

        create_user(
            "admin",
            "Admin123!",
            "admin"
        )


# ==========================================
#              ГЛАВНОЕ МЕНЮ
# ==========================================

def main_menu():

    while True:

        title(
            f"{SHOP_NAME} | VERSION {VERSION}"
        )

        print("Добро пожаловать в магазин гаджетов!")

        print()

        print("1. Войти")

        print("2. Регистрация")

        print("3. Забыл пароль")

        print("4. О программе")

        print("5. Выход")

        choice = input(
            "\nВыберите действие: "
        )

        if choice == "1":

            username = login()

            if username:

                if users[username]["role"] == "admin":

                    admin_panel()

                else:

                    user_menu(username)

        elif choice == "2":

            register()

        elif choice == "3":

            reset_password()

        elif choice == "4":

            about_program()

        elif choice == "5":

            save_data()

            print("Данные сохранены!")

            print("До свидания!")

            break

        else:

            print("Неверный выбор!")

            pause()


# ==========================================
#              ВОССТАНОВЛЕНИЕ ПАРОЛЯ
# ==========================================

def reset_password():

    title("ВОССТАНОВЛЕНИЕ ПАРОЛЯ")

    username = input(
        "Введите логин: "
    )

    if username not in users:

        print("Пользователь не найден!")

        pause()

        return

    new_password = input(
        "Введите новый пароль: "
    )

    if not check_password(new_password):

        print("Пароль слишком слабый!")

        pause()

        return

    users[username]["password"] = hash_password(
        new_password
    )

    users[username]["attempts"] = 0

    users[username]["blocked"] = False

    print("Пароль изменён!")

    pause()


# ==========================================
#              О ПРОГРАММЕ
# ==========================================

def about_program():

    title("О ПРОГРАММЕ")

    print("Название:", SHOP_NAME)

    print("Версия:", VERSION)

    print("Язык: Python")

    print("Среда: PyCharm")

    print("Тип: Магазин гаджетов")

    print()

    print("Возможности:")

    print("- Регистрация")

    print("- Вход")

    print("- Каталог")

    print("- Корзина")

    print("- Покупки")

    print("- Баланс")

    print("- Админ-панель")

    print("- Сохранение данных")

    pause()


# ==========================================
#              ЗАПУСК
# ==========================================

if __name__ == "__main__":

    load_data()

    create_admin()

    main_menu()
