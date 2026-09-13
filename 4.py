import hashlib
import random
import string
import os


# ==============================
# ГЛАВНОЕ МЕНЮ
# ==============================

def show_menu():
    print("\n" + "=" * 40)
    print("       CAT SYSTEM")
    print("=" * 40)
    print("1. Вход")
    print("2. Регистрация")
    print("3. Забыл пароль?")
    print("4. Выход")
    print("=" * 40)


# ==============================
# ПРОВЕРКА ПАРОЛЯ
# ==============================

def check_password_strength(password: str) -> bool:
    if len(password) < 8:
        return False

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(
        c in "!@#$%^&*()_-+=" for c in password
    )

    return (
        has_upper
        and has_lower
        and has_digit
        and has_special
    )


# ==============================
# ХЕШИРОВАНИЕ ПАРОЛЯ
# ==============================

def hash_password(password: str) -> str:
    return hashlib.sha256(
        password.encode()
    ).hexdigest()


# ==============================
# ГЕНЕРАЦИЯ ID
# ==============================

def generate_random_id(length=10) -> str:
    chars = string.ascii_letters + string.digits

    return "".join(
        random.choice(chars)
        for _ in range(length)
    )


# ==============================
# РЕГИСТРАЦИЯ
# ==============================

def register(users: dict):
    print("\n" + "=" * 40)
    print("          РЕГИСТРАЦИЯ")
    print("=" * 40)

    username = input(
        "Введите имя пользователя: "
    ).strip()

    if not username:
        print("Имя не может быть пустым!")
        return

    if username in users:
        print("Такой пользователь уже существует!")
        return

    password = input("Введите пароль: ")

    if not check_password_strength(password):
        print("\nПароль слишком слабый!")
        print("Пароль должен содержать:")
        print("- Минимум 8 символов")
        print("- Заглавные буквы")
        print("- Строчные буквы")
        print("- Цифры")
        print("- Специальный символ")
        return

    confirm = input("Повторите пароль: ")

    if password != confirm:
        print("Пароли не совпадают!")
        return

    user_id = generate_random_id()

    users[username] = {
        "password": hash_password(password),
        "role": "user",
        "user_id": user_id,
        "attempts": 0,
        "blocked": False,
        "balance": 0,
        "level": 1
    }

    print("\nРегистрация успешна!")
    print("Ваш логин:", username)
    print("Ваш ID:", user_id)


# ==============================
# ВХОД
# ==============================

def login(users: dict):
    print("\n" + "=" * 40)
    print("             ВХОД")
    print("=" * 40)

    username = input("Введите логин: ")

    if username not in users:
        print("Пользователь не найден!")
        return None

    user = users[username]

    if user["blocked"]:
        print("Ваш аккаунт заблокирован!")
        return None

    password = input("Введите пароль: ")

    password_hash = hash_password(password)

    if password_hash == user["password"]:
        user["attempts"] = 0

        print("\nВы успешно вошли!")
        print("Добро пожаловать,", username)

        return username

    user["attempts"] += 1

    remaining = 3 - user["attempts"]

    print("Неверный пароль!")

    if remaining <= 0:
        user["blocked"] = True
        print("Ваш аккаунт заблокирован!")
    else:
        print("Осталось попыток:", remaining)

    return None


# ==============================
# ПРОФИЛЬ
# ==============================

def show_profile(users: dict, username: str):
    user = users[username]

    print("\n" + "=" * 40)
    print("             ПРОФИЛЬ")
    print("=" * 40)

    print("Логин:", username)
    print("ID:", user["user_id"])
    print("Роль:", user["role"])
    print("Уровень:", user["level"])
    print("Баланс:", user["balance"])
    print("Попытки:", user["attempts"])
    print("Заблокирован:", user["blocked"])

    print("=" * 40)


# ==============================
# МЕНЮ ПОЛЬЗОВАТЕЛЯ
# ==============================

def user_menu(users: dict, username: str):
    while True:
        print("\n" + "=" * 40)
        print("        МЕНЮ ПОЛЬЗОВАТЕЛЯ")
        print("=" * 40)

        print("Пользователь:", username)
        print("-" * 40)

        print("1. Мой профиль")
        print("2. Пополнить баланс")
        print("3. Игра с котом")
        print("4. Изменить пароль")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            show_profile(users, username)

        elif choice == "2":
            print("\nПополнение баланса")

            amount = input(
                "Введите сумму: "
            )

            if amount.isdigit():
                users[username]["balance"] += int(amount)

                print("Баланс пополнен!")
                print(
                    "Ваш баланс:",
                    users[username]["balance"]
                )
            else:
                print("Введите число!")

        elif choice == "3":
            print("\nИгра с котом!")

            number = random.randint(1, 5)

            answer = input(
                "Угадайте число от 1 до 5: "
            )

            if answer.isdigit() and int(answer) == number:
                print("Вы угадали!")

                users[username]["level"] += 1

                print("Ваш уровень повышен!")
            else:
                print("Вы не угадали!")
                print("Правильное число:", number)

        elif choice == "4":
            change_password(users, username)

        elif choice == "5":
            print("Вы вышли из аккаунта!")
            break

        else:
            print("Неверный выбор!")


# ==============================
# ИЗМЕНЕНИЕ ПАРОЛЯ
# ==============================

def change_password(users: dict, username: str):
    print("\n" + "=" * 40)
    print("         ИЗМЕНЕНИЕ ПАРОЛЯ")
    print("=" * 40)

    old_password = input("Старый пароль: ")

    if hash_password(old_password) != users[username]["password"]:
        print("Неверный старый пароль!")
        return

    new_password = input("Новый пароль: ")

    if not check_password_strength(new_password):
        print("Новый пароль слишком слабый!")
        return

    confirm = input("Повторите новый пароль: ")

    if new_password != confirm:
        print("Пароли не совпадают!")
        return

    users[username]["password"] = hash_password(
        new_password
    )

    print("Пароль успешно изменён!")


# ==============================
# ВОССТАНОВЛЕНИЕ ПАРОЛЯ
# ==============================

def reset_password(users: dict):
    print("\n" + "=" * 40)
    print("       ВОССТАНОВЛЕНИЕ ПАРОЛЯ")
    print("=" * 40)

    username = input(
        "Введите имя пользователя: "
    )

    if username not in users:
        print("Пользователь не найден!")
        return

    new_password = input("Введите новый пароль: ")

    if not check_password_strength(new_password):
        print("Пароль слишком слабый!")
        return

    users[username]["password"] = hash_password(
        new_password
    )

    users[username]["attempts"] = 0
    users[username]["blocked"] = False

    print("Пароль успешно восстановлен!")


# ==============================
# АДМИН-ПАНЕЛЬ
# ==============================

def admin_panel(users: dict):
    while True:
        print("\n" + "=" * 40)
        print("           ADMIN PANEL")
        print("=" * 40)

        print("1. Все пользователи")
        print("2. Удалить пользователя")
        print("3. Разблокировать пользователя")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            print("\nСПИСОК ПОЛЬЗОВАТЕЛЕЙ")

            if not users:
                print("Пользователей нет!")

            for name, data in users.items():
                print("-" * 30)
                print("Логин:", name)
                print("Роль:", data["role"])
                print("ID:", data["user_id"])
                print("Баланс:", data["balance"])
                print("Заблокирован:", data["blocked"])

        elif choice == "2":
            name = input(
                "Введите имя пользователя: "
            )

            if name in users and name != "admin":
                del users[name]
                print("Пользователь удалён!")
            else:
                print("Пользователь не найден!")

        elif choice == "3":
            name = input(
                "Введите имя для разблокировки: "
            )

            if name in users:
                users[name]["blocked"] = False
                users[name]["attempts"] = 0

                print("Пользователь разблокирован!")
            else:
                print("Пользователь не найден!")

        elif choice == "4":
            break

        else:
            print("Неверный выбор!")


# ==============================
# СОХРАНЕНИЕ ДАННЫХ
# ==============================

def save_data(users: dict):
    with open("users.txt", "w", encoding="utf-8") as file:

        for username, data in users.items():

            line = "|".join([
                username,
                data["password"],
                data["role"],
                data["user_id"],
                str(data["attempts"]),
                str(data["blocked"]),
                str(data["balance"]),
                str(data["level"])
            ])

            file.write(line + "\n")


# ==============================
# ЗАГРУЗКА ДАННЫХ
# ==============================

def load_data():
    users = {}

    if not os.path.exists("users.txt"):
        return users

    with open("users.txt", "r", encoding="utf-8") as file:

        for line in file:
            parts = line.strip().split("|")

            if len(parts) != 8:
                continue

            username = parts[0]

            users[username] = {
                "password": parts[1],
                "role": parts[2],
                "user_id": parts[3],
                "attempts": int(parts[4]),
                "blocked": parts[5] == "True",
                "balance": int(parts[6]),
                "level": int(parts[7])
            }

    return users


# ==============================
# ГЛАВНАЯ ФУНКЦИЯ
# ==============================

def main():

    users = load_data()

    # Создание администратора

    if "admin" not in users:
        users["admin"] = {
            "password": hash_password("Admin123!"),
            "role": "admin",
            "user_id": "ADMIN001",
            "attempts": 0,
            "blocked": False,
            "balance": 0,
            "level": 1
        }

    while True:

        show_menu()

        choice = input("Выберите действие: ")

        if choice == "1":

            username = login(users)

            if username:

                if users[username]["role"] == "admin":
                    admin_panel(users)
                else:
                    user_menu(users, username)

        elif choice == "2":
            register(users)

        elif choice == "3":
            reset_password(users)

        elif choice == "4":
            save_data(users)

            print("Данные сохранены!")
            print("До свидания!")

            break

        else:
            print("Неверный выбор!")


if __name__ == "__main__":
    main()

import hashlib
import random
import string
import os


# ==============================
# ГЛАВНОЕ МЕНЮ
# ==============================

def show_menu():
    print("\n" + "=" * 40)
    print("       CAT SYSTEM")
    print("=" * 40)
    print("1. Вход")
    print("2. Регистрация")
    print("3. Забыл пароль?")
    print("4. Выход")
    print("=" * 40)


# ==============================
# ПРОВЕРКА ПАРОЛЯ
# ==============================

def check_password_strength(password: str) -> bool:
    if len(password) < 8:
        return False

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(
        c in "!@#$%^&*()_-+=" for c in password
    )

    return (
        has_upper
        and has_lower
        and has_digit
        and has_special
    )


# ==============================
# ХЕШИРОВАНИЕ ПАРОЛЯ
# ==============================

def hash_password(password: str) -> str:
    return hashlib.sha256(
        password.encode()
    ).hexdigest()


# ==============================
# ГЕНЕРАЦИЯ ID
# ==============================

def generate_random_id(length=10) -> str:
    chars = string.ascii_letters + string.digits

    return "".join(
        random.choice(chars)
        for _ in range(length)
    )


# ==============================
# РЕГИСТРАЦИЯ
# ==============================

def register(users: dict):
    print("\n" + "=" * 40)
    print("          РЕГИСТРАЦИЯ")
    print("=" * 40)

    username = input(
        "Введите имя пользователя: "
    ).strip()

    if not username:
        print("Имя не может быть пустым!")
        return

    if username in users:
        print("Такой пользователь уже существует!")
        return

    password = input("Введите пароль: ")

    if not check_password_strength(password):
        print("\nПароль слишком слабый!")
        print("Пароль должен содержать:")
        print("- Минимум 8 символов")
        print("- Заглавные буквы")
        print("- Строчные буквы")
        print("- Цифры")
        print("- Специальный символ")
        return

    confirm = input("Повторите пароль: ")

    if password != confirm:
        print("Пароли не совпадают!")
        return

    user_id = generate_random_id()

    users[username] = {
        "password": hash_password(password),
        "role": "user",
        "user_id": user_id,
        "attempts": 0,
        "blocked": False,
        "balance": 0,
        "level": 1
    }

    print("\nРегистрация успешна!")
    print("Ваш логин:", username)
    print("Ваш ID:", user_id)


# ==============================
# ВХОД
# ==============================

def login(users: dict):
    print("\n" + "=" * 40)
    print("             ВХОД")
    print("=" * 40)

    username = input("Введите логин: ")

    if username not in users:
        print("Пользователь не найден!")
        return None

    user = users[username]

    if user["blocked"]:
        print("Ваш аккаунт заблокирован!")
        return None

    password = input("Введите пароль: ")

    password_hash = hash_password(password)

    if password_hash == user["password"]:
        user["attempts"] = 0

        print("\nВы успешно вошли!")
        print("Добро пожаловать,", username)

        return username

    user["attempts"] += 1

    remaining = 3 - user["attempts"]

    print("Неверный пароль!")

    if remaining <= 0:
        user["blocked"] = True
        print("Ваш аккаунт заблокирован!")
    else:
        print("Осталось попыток:", remaining)

    return None


# ==============================
# ПРОФИЛЬ
# ==============================

def show_profile(users: dict, username: str):
    user = users[username]

    print("\n" + "=" * 40)
    print("             ПРОФИЛЬ")
    print("=" * 40)

    print("Логин:", username)
    print("ID:", user["user_id"])
    print("Роль:", user["role"])
    print("Уровень:", user["level"])
    print("Баланс:", user["balance"])
    print("Попытки:", user["attempts"])
    print("Заблокирован:", user["blocked"])

    print("=" * 40)


# ==============================
# МЕНЮ ПОЛЬЗОВАТЕЛЯ
# ==============================

def user_menu(users: dict, username: str):
    while True:
        print("\n" + "=" * 40)
        print("        МЕНЮ ПОЛЬЗОВАТЕЛЯ")
        print("=" * 40)

        print("Пользователь:", username)
        print("-" * 40)

        print("1. Мой профиль")
        print("2. Пополнить баланс")
        print("3. Игра с котом")
        print("4. Изменить пароль")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            show_profile(users, username)

        elif choice == "2":
            print("\nПополнение баланса")

            amount = input(
                "Введите сумму: "
            )

            if amount.isdigit():
                users[username]["balance"] += int(amount)

                print("Баланс пополнен!")
                print(
                    "Ваш баланс:",
                    users[username]["balance"]
                )
            else:
                print("Введите число!")

        elif choice == "3":
            print("\nИгра с котом!")

            number = random.randint(1, 5)

            answer = input(
                "Угадайте число от 1 до 5: "
            )

            if answer.isdigit() and int(answer) == number:
                print("Вы угадали!")

                users[username]["level"] += 1

                print("Ваш уровень повышен!")
            else:
                print("Вы не угадали!")
                print("Правильное число:", number)

        elif choice == "4":
            change_password(users, username)

        elif choice == "5":
            print("Вы вышли из аккаунта!")
            break

        else:
            print("Неверный выбор!")


# ==============================
# ИЗМЕНЕНИЕ ПАРОЛЯ
# ==============================

def change_password(users: dict, username: str):
    print("\n" + "=" * 40)
    print("         ИЗМЕНЕНИЕ ПАРОЛЯ")
    print("=" * 40)

    old_password = input("Старый пароль: ")

    if hash_password(old_password) != users[username]["password"]:
        print("Неверный старый пароль!")
        return

    new_password = input("Новый пароль: ")

    if not check_password_strength(new_password):
        print("Новый пароль слишком слабый!")
        return

    confirm = input("Повторите новый пароль: ")

    if new_password != confirm:
        print("Пароли не совпадают!")
        return

    users[username]["password"] = hash_password(
        new_password
    )

    print("Пароль успешно изменён!")


# ==============================
# ВОССТАНОВЛЕНИЕ ПАРОЛЯ
# ==============================

def reset_password(users: dict):
    print("\n" + "=" * 40)
    print("       ВОССТАНОВЛЕНИЕ ПАРОЛЯ")
    print("=" * 40)

    username = input(
        "Введите имя пользователя: "
    )

    if username not in users:
        print("Пользователь не найден!")
        return

    new_password = input("Введите новый пароль: ")

    if not check_password_strength(new_password):
        print("Пароль слишком слабый!")
        return

    users[username]["password"] = hash_password(
        new_password
    )

    users[username]["attempts"] = 0
    users[username]["blocked"] = False

    print("Пароль успешно восстановлен!")


# ==============================
# АДМИН-ПАНЕЛЬ
# ==============================

def admin_panel(users: dict):
    while True:
        print("\n" + "=" * 40)
        print("           ADMIN PANEL")
        print("=" * 40)

        print("1. Все пользователи")
        print("2. Удалить пользователя")
        print("3. Разблокировать пользователя")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            print("\nСПИСОК ПОЛЬЗОВАТЕЛЕЙ")

            if not users:
                print("Пользователей нет!")

            for name, data in users.items():
                print("-" * 30)
                print("Логин:", name)
                print("Роль:", data["role"])
                print("ID:", data["user_id"])
                print("Баланс:", data["balance"])
                print("Заблокирован:", data["blocked"])

        elif choice == "2":
            name = input(
                "Введите имя пользователя: "
            )

            if name in users and name != "admin":
                del users[name]
                print("Пользователь удалён!")
            else:
                print("Пользователь не найден!")

        elif choice == "3":
            name = input(
                "Введите имя для разблокировки: "
            )

            if name in users:
                users[name]["blocked"] = False
                users[name]["attempts"] = 0

                print("Пользователь разблокирован!")
            else:
                print("Пользователь не найден!")

        elif choice == "4":
            break

        else:
            print("Неверный выбор!")


# ==============================
# СОХРАНЕНИЕ ДАННЫХ
# ==============================

def save_data(users: dict):
    with open("users.txt", "w", encoding="utf-8") as file:

        for username, data in users.items():

            line = "|".join([
                username,
                data["password"],
                data["role"],
                data["user_id"],
                str(data["attempts"]),
                str(data["blocked"]),
                str(data["balance"]),
                str(data["level"])
            ])

            file.write(line + "\n")


# ==============================
# ЗАГРУЗКА ДАННЫХ
# ==============================

def load_data():
    users = {}

    if not os.path.exists("users.txt"):
        return users

    with open("users.txt", "r", encoding="utf-8") as file:

        for line in file:
            parts = line.strip().split("|")

            if len(parts) != 8:
                continue

            username = parts[0]

            users[username] = {
                "password": parts[1],
                "role": parts[2],
                "user_id": parts[3],
                "attempts": int(parts[4]),
                "blocked": parts[5] == "True",
                "balance": int(parts[6]),
                "level": int(parts[7])
            }

    return users


# ==============================
# ГЛАВНАЯ ФУНКЦИЯ
# ==============================

def main():

    users = load_data()

    # Создание администратора

    if "admin" not in users:
        users["admin"] = {
            "password": hash_password("Admin123!"),
            "role": "admin",
            "user_id": "ADMIN001",
            "attempts": 0,
            "blocked": False,
            "balance": 0,
            "level": 1
        }

    while True:

        show_menu()

        choice = input("Выберите действие: ")

        if choice == "1":

            username = login(users)

            if username:

                if users[username]["role"] == "admin":
                    admin_panel(users)
                else:
                    user_menu(users, username)

        elif choice == "2":
            register(users)

        elif choice == "3":
            reset_password(users)

        elif choice == "4":
            save_data(users)

            print("Данные сохранены!")
            print("До свидания!")

            break

        else:
            print("Неверный выбор!")


if __name__ == "__main__":
    main()

import hashlib
import random
import string
import os


# ==============================
# ГЛАВНОЕ МЕНЮ
# ==============================

def show_menu():
    print("\n" + "=" * 40)
    print("       CAT SYSTEM")
    print("=" * 40)
    print("1. Вход")
    print("2. Регистрация")
    print("3. Забыл пароль?")
    print("4. Выход")
    print("=" * 40)


# ==============================
# ПРОВЕРКА ПАРОЛЯ
# ==============================

def check_password_strength(password: str) -> bool:
    if len(password) < 8:
        return False

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(
        c in "!@#$%^&*()_-+=" for c in password
    )

    return (
        has_upper
        and has_lower
        and has_digit
        and has_special
    )


# ==============================
# ХЕШИРОВАНИЕ ПАРОЛЯ
# ==============================

def hash_password(password: str) -> str:
    return hashlib.sha256(
        password.encode()
    ).hexdigest()


# ==============================
# ГЕНЕРАЦИЯ ID
# ==============================

def generate_random_id(length=10) -> str:
    chars = string.ascii_letters + string.digits

    return "".join(
        random.choice(chars)
        for _ in range(length)
    )


# ==============================
# РЕГИСТРАЦИЯ
# ==============================

def register(users: dict):
    print("\n" + "=" * 40)
    print("          РЕГИСТРАЦИЯ")
    print("=" * 40)

    username = input(
        "Введите имя пользователя: "
    ).strip()

    if not username:
        print("Имя не может быть пустым!")
        return

    if username in users:
        print("Такой пользователь уже существует!")
        return

    password = input("Введите пароль: ")

    if not check_password_strength(password):
        print("\nПароль слишком слабый!")
        print("Пароль должен содержать:")
        print("- Минимум 8 символов")
        print("- Заглавные буквы")
        print("- Строчные буквы")
        print("- Цифры")
        print("- Специальный символ")
        return

    confirm = input("Повторите пароль: ")

    if password != confirm:
        print("Пароли не совпадают!")
        return

    user_id = generate_random_id()

    users[username] = {
        "password": hash_password(password),
        "role": "user",
        "user_id": user_id,
        "attempts": 0,
        "blocked": False,
        "balance": 0,
        "level": 1
    }

    print("\nРегистрация успешна!")
    print("Ваш логин:", username)
    print("Ваш ID:", user_id)


# ==============================
# ВХОД
# ==============================

def login(users: dict):
    print("\n" + "=" * 40)
    print("             ВХОД")
    print("=" * 40)

    username = input("Введите логин: ")

    if username not in users:
        print("Пользователь не найден!")
        return None

    user = users[username]

    if user["blocked"]:
        print("Ваш аккаунт заблокирован!")
        return None

    password = input("Введите пароль: ")

    password_hash = hash_password(password)

    if password_hash == user["password"]:
        user["attempts"] = 0

        print("\nВы успешно вошли!")
        print("Добро пожаловать,", username)

        return username

    user["attempts"] += 1

    remaining = 3 - user["attempts"]

    print("Неверный пароль!")

    if remaining <= 0:
        user["blocked"] = True
        print("Ваш аккаунт заблокирован!")
    else:
        print("Осталось попыток:", remaining)

    return None


# ==============================
# ПРОФИЛЬ
# ==============================

def show_profile(users: dict, username: str):
    user = users[username]

    print("\n" + "=" * 40)
    print("             ПРОФИЛЬ")
    print("=" * 40)

    print("Логин:", username)
    print("ID:", user["user_id"])
    print("Роль:", user["role"])
    print("Уровень:", user["level"])
    print("Баланс:", user["balance"])
    print("Попытки:", user["attempts"])
    print("Заблокирован:", user["blocked"])

    print("=" * 40)


# ==============================
# МЕНЮ ПОЛЬЗОВАТЕЛЯ
# ==============================

def user_menu(users: dict, username: str):
    while True:
        print("\n" + "=" * 40)
        print("        МЕНЮ ПОЛЬЗОВАТЕЛЯ")
        print("=" * 40)

        print("Пользователь:", username)
        print("-" * 40)

        print("1. Мой профиль")
        print("2. Пополнить баланс")
        print("3. Игра с котом")
        print("4. Изменить пароль")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            show_profile(users, username)

        elif choice == "2":
            print("\nПополнение баланса")

            amount = input(
                "Введите сумму: "
            )

            if amount.isdigit():
                users[username]["balance"] += int(amount)

                print("Баланс пополнен!")
                print(
                    "Ваш баланс:",
                    users[username]["balance"]
                )
            else:
                print("Введите число!")

        elif choice == "3":
            print("\nИгра с котом!")

            number = random.randint(1, 5)

            answer = input(
                "Угадайте число от 1 до 5: "
            )

            if answer.isdigit() and int(answer) == number:
                print("Вы угадали!")

                users[username]["level"] += 1

                print("Ваш уровень повышен!")
            else:
                print("Вы не угадали!")
                print("Правильное число:", number)

        elif choice == "4":
            change_password(users, username)

        elif choice == "5":
            print("Вы вышли из аккаунта!")
            break

        else:
            print("Неверный выбор!")


# ==============================
# ИЗМЕНЕНИЕ ПАРОЛЯ
# ==============================

def change_password(users: dict, username: str):
    print("\n" + "=" * 40)
    print("         ИЗМЕНЕНИЕ ПАРОЛЯ")
    print("=" * 40)

    old_password = input("Старый пароль: ")

    if hash_password(old_password) != users[username]["password"]:
        print("Неверный старый пароль!")
        return

    new_password = input("Новый пароль: ")

    if not check_password_strength(new_password):
        print("Новый пароль слишком слабый!")
        return

    confirm = input("Повторите новый пароль: ")

    if new_password != confirm:
        print("Пароли не совпадают!")
        return

    users[username]["password"] = hash_password(
        new_password
    )

    print("Пароль успешно изменён!")


# ==============================
# ВОССТАНОВЛЕНИЕ ПАРОЛЯ
# ==============================

def reset_password(users: dict):
    print("\n" + "=" * 40)
    print("       ВОССТАНОВЛЕНИЕ ПАРОЛЯ")
    print("=" * 40)

    username = input(
        "Введите имя пользователя: "
    )

    if username not in users:
        print("Пользователь не найден!")
        return

    new_password = input("Введите новый пароль: ")

    if not check_password_strength(new_password):
        print("Пароль слишком слабый!")
        return

    users[username]["password"] = hash_password(
        new_password
    )

    users[username]["attempts"] = 0
    users[username]["blocked"] = False

    print("Пароль успешно восстановлен!")


# ==============================
# АДМИН-ПАНЕЛЬ
# ==============================

def admin_panel(users: dict):
    while True:
        print("\n" + "=" * 40)
        print("           ADMIN PANEL")
        print("=" * 40)

        print("1. Все пользователи")
        print("2. Удалить пользователя")
        print("3. Разблокировать пользователя")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            print("\nСПИСОК ПОЛЬЗОВАТЕЛЕЙ")

            if not users:
                print("Пользователей нет!")

            for name, data in users.items():
                print("-" * 30)
                print("Логин:", name)
                print("Роль:", data["role"])
                print("ID:", data["user_id"])
                print("Баланс:", data["balance"])
                print("Заблокирован:", data["blocked"])

        elif choice == "2":
            name = input(
                "Введите имя пользователя: "
            )

            if name in users and name != "admin":
                del users[name]
                print("Пользователь удалён!")
            else:
                print("Пользователь не найден!")

        elif choice == "3":
            name = input(
                "Введите имя для разблокировки: "
            )

            if name in users:
                users[name]["blocked"] = False
                users[name]["attempts"] = 0

                print("Пользователь разблокирован!")
            else:
                print("Пользователь не найден!")

        elif choice == "4":
            break

        else:
            print("Неверный выбор!")


# ==============================
# СОХРАНЕНИЕ ДАННЫХ
# ==============================

def save_data(users: dict):
    with open("users.txt", "w", encoding="utf-8") as file:

        for username, data in users.items():

            line = "|".join([
                username,
                data["password"],
                data["role"],
                data["user_id"],
                str(data["attempts"]),
                str(data["blocked"]),
                str(data["balance"]),
                str(data["level"])
            ])

            file.write(line + "\n")


# ==============================
# ЗАГРУЗКА ДАННЫХ
# ==============================

def load_data():
    users = {}

    if not os.path.exists("users.txt"):
        return users

    with open("users.txt", "r", encoding="utf-8") as file:

        for line in file:
            parts = line.strip().split("|")

            if len(parts) != 8:
                continue

            username = parts[0]

            users[username] = {
                "password": parts[1],
                "role": parts[2],
                "user_id": parts[3],
                "attempts": int(parts[4]),
                "blocked": parts[5] == "True",
                "balance": int(parts[6]),
                "level": int(parts[7])
            }

    return users


# ==============================
# ГЛАВНАЯ ФУНКЦИЯ
# ==============================

def main():

    users = load_data()

    # Создание администратора

    if "admin" not in users:
        users["admin"] = {
            "password": hash_password("Admin123!"),
            "role": "admin",
            "user_id": "ADMIN001",
            "attempts": 0,
            "blocked": False,
            "balance": 0,
            "level": 1
        }

    while True:

        show_menu()

        choice = input("Выберите действие: ")

        if choice == "1":

            username = login(users)

            if username:

                if users[username]["role"] == "admin":
                    admin_panel(users)
                else:
                    user_menu(users, username)

        elif choice == "2":
            register(users)

        elif choice == "3":
            reset_password(users)

        elif choice == "4":
            save_data(users)

            print("Данные сохранены!")
            print("До свидания!")

            break

        else:
            print("Неверный выбор!")


if __name__ == "__main__":
    main()

import hashlib
import random
import string
import os


# ==============================
# ГЛАВНОЕ МЕНЮ
# ==============================

def show_menu():
    print("\n" + "=" * 40)
    print("       CAT SYSTEM")
    print("=" * 40)
    print("1. Вход")
    print("2. Регистрация")
    print("3. Забыл пароль?")
    print("4. Выход")
    print("=" * 40)


# ==============================
# ПРОВЕРКА ПАРОЛЯ
# ==============================

def check_password_strength(password: str) -> bool:
    if len(password) < 8:
        return False

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(
        c in "!@#$%^&*()_-+=" for c in password
    )

    return (
        has_upper
        and has_lower
        and has_digit
        and has_special
    )


# ==============================
# ХЕШИРОВАНИЕ ПАРОЛЯ
# ==============================

def hash_password(password: str) -> str:
    return hashlib.sha256(
        password.encode()
    ).hexdigest()


# ==============================
# ГЕНЕРАЦИЯ ID
# ==============================

def generate_random_id(length=10) -> str:
    chars = string.ascii_letters + string.digits

    return "".join(
        random.choice(chars)
        for _ in range(length)
    )


# ==============================
# РЕГИСТРАЦИЯ
# ==============================

def register(users: dict):
    print("\n" + "=" * 40)
    print("          РЕГИСТРАЦИЯ")
    print("=" * 40)

    username = input(
        "Введите имя пользователя: "
    ).strip()

    if not username:
        print("Имя не может быть пустым!")
        return

    if username in users:
        print("Такой пользователь уже существует!")
        return

    password = input("Введите пароль: ")

    if not check_password_strength(password):
        print("\nПароль слишком слабый!")
        print("Пароль должен содержать:")
        print("- Минимум 8 символов")
        print("- Заглавные буквы")
        print("- Строчные буквы")
        print("- Цифры")
        print("- Специальный символ")
        return

    confirm = input("Повторите пароль: ")

    if password != confirm:
        print("Пароли не совпадают!")
        return

    user_id = generate_random_id()

    users[username] = {
        "password": hash_password(password),
        "role": "user",
        "user_id": user_id,
        "attempts": 0,
        "blocked": False,
        "balance": 0,
        "level": 1
    }

    print("\nРегистрация успешна!")
    print("Ваш логин:", username)
    print("Ваш ID:", user_id)


# ==============================
# ВХОД
# ==============================

def login(users: dict):
    print("\n" + "=" * 40)
    print("             ВХОД")
    print("=" * 40)

    username = input("Введите логин: ")

    if username not in users:
        print("Пользователь не найден!")
        return None

    user = users[username]

    if user["blocked"]:
        print("Ваш аккаунт заблокирован!")
        return None

    password = input("Введите пароль: ")

    password_hash = hash_password(password)

    if password_hash == user["password"]:
        user["attempts"] = 0

        print("\nВы успешно вошли!")
        print("Добро пожаловать,", username)

        return username

    user["attempts"] += 1

    remaining = 3 - user["attempts"]

    print("Неверный пароль!")

    if remaining <= 0:
        user["blocked"] = True
        print("Ваш аккаунт заблокирован!")
    else:
        print("Осталось попыток:", remaining)

    return None


# ==============================
# ПРОФИЛЬ
# ==============================

def show_profile(users: dict, username: str):
    user = users[username]

    print("\n" + "=" * 40)
    print("             ПРОФИЛЬ")
    print("=" * 40)

    print("Логин:", username)
    print("ID:", user["user_id"])
    print("Роль:", user["role"])
    print("Уровень:", user["level"])
    print("Баланс:", user["balance"])
    print("Попытки:", user["attempts"])
    print("Заблокирован:", user["blocked"])

    print("=" * 40)


# ==============================
# МЕНЮ ПОЛЬЗОВАТЕЛЯ
# ==============================

def user_menu(users: dict, username: str):
    while True:
        print("\n" + "=" * 40)
        print("        МЕНЮ ПОЛЬЗОВАТЕЛЯ")
        print("=" * 40)

        print("Пользователь:", username)
        print("-" * 40)

        print("1. Мой профиль")
        print("2. Пополнить баланс")
        print("3. Игра с котом")
        print("4. Изменить пароль")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            show_profile(users, username)

        elif choice == "2":
            print("\nПополнение баланса")

            amount = input(
                "Введите сумму: "
            )

            if amount.isdigit():
                users[username]["balance"] += int(amount)

                print("Баланс пополнен!")
                print(
                    "Ваш баланс:",
                    users[username]["balance"]
                )
            else:
                print("Введите число!")

        elif choice == "3":
            print("\nИгра с котом!")

            number = random.randint(1, 5)

            answer = input(
                "Угадайте число от 1 до 5: "
            )

            if answer.isdigit() and int(answer) == number:
                print("Вы угадали!")

                users[username]["level"] += 1

                print("Ваш уровень повышен!")
            else:
                print("Вы не угадали!")
                print("Правильное число:", number)

        elif choice == "4":
            change_password(users, username)

        elif choice == "5":
            print("Вы вышли из аккаунта!")
            break

        else:
            print("Неверный выбор!")


# ==============================
# ИЗМЕНЕНИЕ ПАРОЛЯ
# ==============================

def change_password(users: dict, username: str):
    print("\n" + "=" * 40)
    print("         ИЗМЕНЕНИЕ ПАРОЛЯ")
    print("=" * 40)

    old_password = input("Старый пароль: ")

    if hash_password(old_password) != users[username]["password"]:
        print("Неверный старый пароль!")
        return

    new_password = input("Новый пароль: ")

    if not check_password_strength(new_password):
        print("Новый пароль слишком слабый!")
        return

    confirm = input("Повторите новый пароль: ")

    if new_password != confirm:
        print("Пароли не совпадают!")
        return

    users[username]["password"] = hash_password(
        new_password
    )

    print("Пароль успешно изменён!")


# ==============================
# ВОССТАНОВЛЕНИЕ ПАРОЛЯ
# ==============================

def reset_password(users: dict):
    print("\n" + "=" * 40)
    print("       ВОССТАНОВЛЕНИЕ ПАРОЛЯ")
    print("=" * 40)

    username = input(
        "Введите имя пользователя: "
    )

    if username not in users:
        print("Пользователь не найден!")
        return

    new_password = input("Введите новый пароль: ")

    if not check_password_strength(new_password):
        print("Пароль слишком слабый!")
        return

    users[username]["password"] = hash_password(
        new_password
    )

    users[username]["attempts"] = 0
    users[username]["blocked"] = False

    print("Пароль успешно восстановлен!")


# ==============================
# АДМИН-ПАНЕЛЬ
# ==============================

def admin_panel(users: dict):
    while True:
        print("\n" + "=" * 40)
        print("           ADMIN PANEL")
        print("=" * 40)

        print("1. Все пользователи")
        print("2. Удалить пользователя")
        print("3. Разблокировать пользователя")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            print("\nСПИСОК ПОЛЬЗОВАТЕЛЕЙ")

            if not users:
                print("Пользователей нет!")

            for name, data in users.items():
                print("-" * 30)
                print("Логин:", name)
                print("Роль:", data["role"])
                print("ID:", data["user_id"])
                print("Баланс:", data["balance"])
                print("Заблокирован:", data["blocked"])

        elif choice == "2":
            name = input(
                "Введите имя пользователя: "
            )

            if name in users and name != "admin":
                del users[name]
                print("Пользователь удалён!")
            else:
                print("Пользователь не найден!")

        elif choice == "3":
            name = input(
                "Введите имя для разблокировки: "
            )

            if name in users:
                users[name]["blocked"] = False
                users[name]["attempts"] = 0

                print("Пользователь разблокирован!")
            else:
                print("Пользователь не найден!")

        elif choice == "4":
            break

        else:
            print("Неверный выбор!")


# ==============================
# СОХРАНЕНИЕ ДАННЫХ
# ==============================

def save_data(users: dict):
    with open("users.txt", "w", encoding="utf-8") as file:

        for username, data in users.items():

            line = "|".join([
                username,
                data["password"],
                data["role"],
                data["user_id"],
                str(data["attempts"]),
                str(data["blocked"]),
                str(data["balance"]),
                str(data["level"])
            ])

            file.write(line + "\n")


# ==============================
# ЗАГРУЗКА ДАННЫХ
# ==============================

def load_data():
    users = {}

    if not os.path.exists("users.txt"):
        return users

    with open("users.txt", "r", encoding="utf-8") as file:

        for line in file:
            parts = line.strip().split("|")

            if len(parts) != 8:
                continue

            username = parts[0]

            users[username] = {
                "password": parts[1],
                "role": parts[2],
                "user_id": parts[3],
                "attempts": int(parts[4]),
                "blocked": parts[5] == "True",
                "balance": int(parts[6]),
                "level": int(parts[7])
            }

    return users


# ==============================
# ГЛАВНАЯ ФУНКЦИЯ
# ==============================

def main():

    users = load_data()

    # Создание администратора

    if "admin" not in users:
        users["admin"] = {
            "password": hash_password("Admin123!"),
            "role": "admin",
            "user_id": "ADMIN001",
            "attempts": 0,
            "blocked": False,
            "balance": 0,
            "level": 1
        }

    while True:

        show_menu()

        choice = input("Выберите действие: ")

        if choice == "1":

            username = login(users)

            if username:

                if users[username]["role"] == "admin":
                    admin_panel(users)
                else:
                    user_menu(users, username)

        elif choice == "2":
            register(users)

        elif choice == "3":
            reset_password(users)

        elif choice == "4":
            save_data(users)

            print("Данные сохранены!")
            print("До свидания!")

            break

        else:
            print("Неверный выбор!")


if __name__ == "__main__":
    main()