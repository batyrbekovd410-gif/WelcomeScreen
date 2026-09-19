# ==========================================
# 🐱 CAT SYSTEM — СИСТЕМА РЕГИСТРАЦИИ
# ==========================================

import hashlib
import random
import string
import os
import time


# ==========================================
# 1. КОТ
# ==========================================

def print_cat():
    cat = r"""
 /\_/\\
( o.o )
 > ^ <
    """
    print(cat)
    print("🐱 Мяу! Добро пожаловать!")


# ==========================================
# 2. ГЛАВНОЕ МЕНЮ
# ==========================================

def show_menu():
    print("\n" + "=" * 45)
    print("🐱 CAT SYSTEM 🐱")
    print("=" * 45)
    print("1. Вход")
    print("2. Регистрация")
    print("3. Забыли пароль?")
    print("4. Выход")
    print("=" * 45)


# ==========================================
# 3. ПРОВЕРКА ПАРОЛЯ
# ==========================================

def check_password_strength(password: str) -> bool:

    if len(password) < 8:
        return False

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(
        c in "!@#$%^&*()_+-="
        for c in password
    )

    return (
        has_upper
        and has_lower
        and has_digit
        and has_special
    )


# ==========================================
# 4. ХЕШИРОВАНИЕ ПАРОЛЯ
# ==========================================

def hash_password(password: str) -> str:
    return hashlib.sha256(
        password.encode()
    ).hexdigest()


# ==========================================
# 5. ГЕНЕРАЦИЯ ID
# ==========================================

def generate_random_id(length=8):

    chars = string.ascii_letters + string.digits

    return "".join(
        random.choice(chars)
        for _ in range(length)
    )


# ==========================================
# 6. РЕГИСТРАЦИЯ
# ==========================================

def register(users: dict):

    print("\n===== 📝 РЕГИСТРАЦИЯ =====")

    username = input(
        "Введите имя пользователя: "
    ).strip()

    if not username:
        print("❌ Имя не может быть пустым!")
        return

    if username in users:
        print("❌ Такой пользователь уже существует!")
        return

    password = input(
        "Введите пароль: "
    )

    if not check_password_strength(password):

        print("\n❌ Слабый пароль!")

        print("Пароль должен содержать:")
        print("• Минимум 8 символов")
        print("• Заглавную букву")
        print("• Строчную букву")
        print("• Цифру")
        print("• Специальный символ")

        return

    confirm = input(
        "Повторите пароль: "
    )

    if password != confirm:

        print("❌ Пароли не совпадают!")
        return

    user_id = generate_random_id()

    users[username] = {

        "id": user_id,

        "password": hash_password(password),

        "role": "user",

        "attempts": 0,

        "blocked": False,

        "balance": 0,

        "level": 1,

        "cat": "Мурзик"

    }

    print("\n✅ Регистрация успешна!")

    print(f"👤 Пользователь: {username}")

    print(f"🆔 Ваш ID: {user_id}")

    print("🐱 Ваш кот: Мурзик")


# ==========================================
# 7. ВХОД
# ==========================================

def login(users: dict):

    print("\n===== 🔐 ВХОД =====")

    username = input(
        "Введите имя пользователя: "
    ).strip()

    if username not in users:

        print("❌ Пользователь не найден!")

        return None

    user = users[username]

    if user["blocked"]:

        print("🔒 Аккаунт заблокирован!")

        return None

    password = input(
        "Введите пароль: "
    )

    password_hash = hash_password(password)

    if password_hash == user["password"]:

        user["attempts"] = 0

        print("\n✅ Вы успешно вошли!")

        print(f"Добро пожаловать, {username}!")

        return username

    else:

        user["attempts"] += 1

        remaining = 3 - user["attempts"]

        if remaining <= 0:

            user["blocked"] = True

            print("🔒 Слишком много попыток!")

            print("Аккаунт заблокирован!")

        else:

            print("❌ Неверный пароль!")

            print(
                f"Осталось попыток: {remaining}"
            )

        return None


# ==========================================
# 8. ПРОФИЛЬ
# ==========================================

def show_profile(users: dict, username: str):

    user = users[username]

    print("\n===== 👤 ПРОФИЛЬ =====")

    print(f"Имя: {username}")

    print(f"ID: {user['id']}")

    print(f"Роль: {user['role']}")

    print(f"Кот: {user['cat']}")

    print(f"Уровень: {user['level']}")

    print(f"Баланс: {user['balance']} сом")

    print(f"Попытки входа: {user['attempts']}")

    print(
        "Заблокирован:",
        "Да" if user["blocked"] else "Нет"
    )


# ==========================================
# 9. МЕНЮ ПОЛЬЗОВАТЕЛЯ
# ==========================================

def user_menu(users: dict, username: str):

    while True:

        print("\n" + "=" * 40)

        print(f"🐱 Личный кабинет: {username}")

        print("=" * 40)

        print("1. Мой профиль")
        print("2. Покормить кота")
        print("3. Играть с котом")
        print("4. Изменить пароль")
        print("5. Выйти из аккаунта")

        choice = input(
            "Выберите действие: "
        )

        if choice == "1":

            show_profile(users, username)

        elif choice == "2":

            print("\n🐟 Вы покормили кота!")

            print("Мурзик: Ням-ням! 😺")

            users[username]["balance"] += 10

            print("💰 Вы получили 10 сом!")

        elif choice == "3":

            print("\n🎮 Игра с котом!")

            number = random.randint(1, 5)

            answer = input(
                "Угадайте число от 1 до 5: "
            )

            if answer.isdigit():

                if int(answer) == number:

                    print("🎉 Вы выиграли!")

                    users[username]["level"] += 1

                else:

                    print(
                        f"Не угадали! Было число {number}"
                    )

            else:

                print("Введите число!")

        elif choice == "4":

            change_password(users, username)

        elif choice == "5":

            print("👋 Вы вышли из аккаунта!")

            break

        else:

            print("❌ Неверный выбор!")


# ==========================================
# 10. ИЗМЕНЕНИЕ ПАРОЛЯ
# ==========================================

def change_password(users: dict, username: str):

    print("\n===== 🔑 НОВЫЙ ПАРОЛЬ =====")

    old_password = input(
        "Старый пароль: "
    )

    if hash_password(old_password) != users[username]["password"]:

        print("❌ Неверный старый пароль!")

        return

    new_password = input(
        "Новый пароль: "
    )

    if not check_password_strength(new_password):

        print("❌ Пароль слишком слабый!")

        return

    confirm = input(
        "Повторите новый пароль: "
    )

    if new_password != confirm:

        print("❌ Пароли не совпадают!")

        return

    users[username]["password"] = hash_password(
        new_password
    )

    print("✅ Пароль успешно изменён!")


# ==========================================
# 11. ВОССТАНОВЛЕНИЕ ПАРОЛЯ
# ==========================================

def reset_password(users: dict):

    print("\n===== 🔄 ВОССТАНОВЛЕНИЕ =====")

    username = input(
        "Введите имя пользователя: "
    ).strip()

    if username not in users:

        print("❌ Пользователь не найден!")

        return

    new_password = input(
        "Введите новый пароль: "
    )

    if not check_password_strength(new_password):

        print("❌ Пароль слишком слабый!")

        return

    users[username]["password"] = hash_password(
        new_password
    )

    users[username]["attempts"] = 0

    users[username]["blocked"] = False

    print("✅ Пароль восстановлен!")


# ==========================================
# 12. АДМИНИСТРАТОР
# ==========================================

def admin_panel(users: dict):

    while True:

        print("\n===== 👑 ADMIN PANEL =====")

        print("1. Все пользователи")
        print("2. Удалить пользователя")
        print("3. Разблокировать пользователя")
        print("4. Выйти")

        choice = input(
            "Выберите действие: "
        )

        if choice == "1":

            print("\n===== 👥 ПОЛЬЗОВАТЕЛИ =====")

            if not users:

                print("Пользователей нет!")

            for name, data in users.items():

                print(
                    f"👤 {name} | "
                    f"Роль: {data['role']} | "
                    f"ID: {data['id']}"
                )

        elif choice == "2":

            name = input(
                "Введите имя для удаления: "
            )

            if name in users and name != "admin":

                del users[name]

                print("✅ Пользователь удалён!")

            else:

                print("❌ Пользователь не найден!")

        elif choice == "3":

            name = input(
                "Введите имя для разблокировки: "
            )

            if name in users:

                users[name]["blocked"] = False

                users[name]["attempts"] = 0

                print("✅ Пользователь разблокирован!")

            else:

                print("❌ Пользователь не найден!")

        elif choice == "4":

            break

        else:

            print("❌ Неверный выбор!")


# ==========================================
# 13. СОХРАНЕНИЕ ДАННЫХ
# ==========================================

def save_data(users: dict):

    with open(
        "users.txt",
        "w",
        encoding="utf-8"
    ) as file:

        for username, data in users.items():

            file.write(
                f"{username}|"
                f"{data['password']}|"
                f"{data['role']}|"
                f"{data['id']}|"
                f"{data['attempts']}|"
                f"{data['blocked']}|"
                f"{data['balance']}|"
                f"{data['level']}|"
                f"{data['cat']}\n"
            )


# ==========================================
# 14. ЗАГРУЗКА ДАННЫХ
# ==========================================

def load_data():

    users = {}

    if not os.path.exists("users.txt"):

        return users

    with open(
        "users.txt",
        "r",
        encoding="utf-8"
    ) as file:

        for line in file:

            parts = line.strip().split("|")

            if len(parts) != 9:

                continue

            username = parts[0]

            users[username] = {

                "password": parts[1],

                "role": parts[2],

                "id": parts[3],

                "attempts": int(parts[4]),

                "blocked": parts[5] == "True",

                "balance": int(parts[6]),

                "level": int(parts[7]),

                "cat": parts[8]

            }

    return users


# ==========================================
# 15. ГЛАВНАЯ ФУНКЦИЯ
# ==========================================

def main():

    users = load_data()

    # Создание администратора

    if "admin" not in users:

        users["admin"] = {

            "password": hash_password("Admin123!"),

            "role": "admin",

            "id": "ADMIN001",

            "attempts": 0,

            "blocked": False,

            "balance": 0,

            "level": 99,

            "cat": "Босс"

        }

    while True:

        print_cat()

        show_menu()

        choice = input(
            "Выберите действие: "
        )

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

            print("\n🐱 До свидания!")

            print("Программа завершена.")

            break

        else:

            print("❌ Неверный выбор!")

        save_data(users)


# ==========================================
# ЗАПУСК
# ==========================================

if __name__ == "__main__":

    main()
# ==========================================
# 🐱 CAT SYSTEM — СИСТЕМА РЕГИСТРАЦИИ
# ==========================================

import hashlib
import random
import string
import os
import time


# ==========================================
# 1. КОТ
# ==========================================

def print_cat():
    cat = r"""
 /\_/\\
( o.o )
 > ^ <
    """
    print(cat)
    print("🐱 Мяу! Добро пожаловать!")


# ==========================================
# 2. ГЛАВНОЕ МЕНЮ
# ==========================================

def show_menu():
    print("\n" + "=" * 45)
    print("🐱 CAT SYSTEM 🐱")
    print("=" * 45)
    print("1. Вход")
    print("2. Регистрация")
    print("3. Забыли пароль?")
    print("4. Выход")
    print("=" * 45)


# ==========================================
# 3. ПРОВЕРКА ПАРОЛЯ
# ==========================================

def check_password_strength(password: str) -> bool:

    if len(password) < 8:
        return False

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(
        c in "!@#$%^&*()_+-="
        for c in password
    )

    return (
        has_upper
        and has_lower
        and has_digit
        and has_special
    )


# ==========================================
# 4. ХЕШИРОВАНИЕ ПАРОЛЯ
# ==========================================

def hash_password(password: str) -> str:
    return hashlib.sha256(
        password.encode()
    ).hexdigest()


# ==========================================
# 5. ГЕНЕРАЦИЯ ID
# ==========================================

def generate_random_id(length=8):

    chars = string.ascii_letters + string.digits

    return "".join(
        random.choice(chars)
        for _ in range(length)
    )


# ==========================================
# 6. РЕГИСТРАЦИЯ
# ==========================================

def register(users: dict):

    print("\n===== 📝 РЕГИСТРАЦИЯ =====")

    username = input(
        "Введите имя пользователя: "
    ).strip()

    if not username:
        print("❌ Имя не может быть пустым!")
        return

    if username in users:
        print("❌ Такой пользователь уже существует!")
        return

    password = input(
        "Введите пароль: "
    )

    if not check_password_strength(password):

        print("\n❌ Слабый пароль!")

        print("Пароль должен содержать:")
        print("• Минимум 8 символов")
        print("• Заглавную букву")
        print("• Строчную букву")
        print("• Цифру")
        print("• Специальный символ")

        return

    confirm = input(
        "Повторите пароль: "
    )

    if password != confirm:

        print("❌ Пароли не совпадают!")
        return

    user_id = generate_random_id()

    users[username] = {

        "id": user_id,

        "password": hash_password(password),

        "role": "user",

        "attempts": 0,

        "blocked": False,

        "balance": 0,

        "level": 1,

        "cat": "Мурзик"

    }

    print("\n✅ Регистрация успешна!")

    print(f"👤 Пользователь: {username}")

    print(f"🆔 Ваш ID: {user_id}")

    print("🐱 Ваш кот: Мурзик")


# ==========================================
# 7. ВХОД
# ==========================================

def login(users: dict):

    print("\n===== 🔐 ВХОД =====")

    username = input(
        "Введите имя пользователя: "
    ).strip()

    if username not in users:

        print("❌ Пользователь не найден!")

        return None

    user = users[username]

    if user["blocked"]:

        print("🔒 Аккаунт заблокирован!")

        return None

    password = input(
        "Введите пароль: "
    )

    password_hash = hash_password(password)

    if password_hash == user["password"]:

        user["attempts"] = 0

        print("\n✅ Вы успешно вошли!")

        print(f"Добро пожаловать, {username}!")

        return username

    else:

        user["attempts"] += 1

        remaining = 3 - user["attempts"]

        if remaining <= 0:

            user["blocked"] = True

            print("🔒 Слишком много попыток!")

            print("Аккаунт заблокирован!")

        else:

            print("❌ Неверный пароль!")

            print(
                f"Осталось попыток: {remaining}"
            )

        return None


# ==========================================
# 8. ПРОФИЛЬ
# ==========================================

def show_profile(users: dict, username: str):

    user = users[username]

    print("\n===== 👤 ПРОФИЛЬ =====")

    print(f"Имя: {username}")

    print(f"ID: {user['id']}")

    print(f"Роль: {user['role']}")

    print(f"Кот: {user['cat']}")

    print(f"Уровень: {user['level']}")

    print(f"Баланс: {user['balance']} сом")

    print(f"Попытки входа: {user['attempts']}")

    print(
        "Заблокирован:",
        "Да" if user["blocked"] else "Нет"
    )


# ==========================================
# 9. МЕНЮ ПОЛЬЗОВАТЕЛЯ
# ==========================================

def user_menu(users: dict, username: str):

    while True:

        print("\n" + "=" * 40)

        print(f"🐱 Личный кабинет: {username}")

        print("=" * 40)

        print("1. Мой профиль")
        print("2. Покормить кота")
        print("3. Играть с котом")
        print("4. Изменить пароль")
        print("5. Выйти из аккаунта")

        choice = input(
            "Выберите действие: "
        )

        if choice == "1":

            show_profile(users, username)

        elif choice == "2":

            print("\n🐟 Вы покормили кота!")

            print("Мурзик: Ням-ням! 😺")

            users[username]["balance"] += 10

            print("💰 Вы получили 10 сом!")

        elif choice == "3":

            print("\n🎮 Игра с котом!")

            number = random.randint(1, 5)

            answer = input(
                "Угадайте число от 1 до 5: "
            )

            if answer.isdigit():

                if int(answer) == number:

                    print("🎉 Вы выиграли!")

                    users[username]["level"] += 1

                else:

                    print(
                        f"Не угадали! Было число {number}"
                    )

            else:

                print("Введите число!")

        elif choice == "4":

            change_password(users, username)

        elif choice == "5":

            print("👋 Вы вышли из аккаунта!")

            break

        else:

            print("❌ Неверный выбор!")


# ==========================================
# 10. ИЗМЕНЕНИЕ ПАРОЛЯ
# ==========================================

def change_password(users: dict, username: str):

    print("\n===== 🔑 НОВЫЙ ПАРОЛЬ =====")

    old_password = input(
        "Старый пароль: "
    )

    if hash_password(old_password) != users[username]["password"]:

        print("❌ Неверный старый пароль!")

        return

    new_password = input(
        "Новый пароль: "
    )

    if not check_password_strength(new_password):

        print("❌ Пароль слишком слабый!")

        return

    confirm = input(
        "Повторите новый пароль: "
    )

    if new_password != confirm:

        print("❌ Пароли не совпадают!")

        return

    users[username]["password"] = hash_password(
        new_password
    )

    print("✅ Пароль успешно изменён!")


# ==========================================
# 11. ВОССТАНОВЛЕНИЕ ПАРОЛЯ
# ==========================================

def reset_password(users: dict):

    print("\n===== 🔄 ВОССТАНОВЛЕНИЕ =====")

    username = input(
        "Введите имя пользователя: "
    ).strip()

    if username not in users:

        print("❌ Пользователь не найден!")

        return

    new_password = input(
        "Введите новый пароль: "
    )

    if not check_password_strength(new_password):

        print("❌ Пароль слишком слабый!")

        return

    users[username]["password"] = hash_password(
        new_password
    )

    users[username]["attempts"] = 0

    users[username]["blocked"] = False

    print("✅ Пароль восстановлен!")


# ==========================================
# 12. АДМИНИСТРАТОР
# ==========================================

def admin_panel(users: dict):

    while True:

        print("\n===== 👑 ADMIN PANEL =====")

        print("1. Все пользователи")
        print("2. Удалить пользователя")
        print("3. Разблокировать пользователя")
        print("4. Выйти")

        choice = input(
            "Выберите действие: "
        )

        if choice == "1":

            print("\n===== 👥 ПОЛЬЗОВАТЕЛИ =====")

            if not users:

                print("Пользователей нет!")

            for name, data in users.items():

                print(
                    f"👤 {name} | "
                    f"Роль: {data['role']} | "
                    f"ID: {data['id']}"
                )

        elif choice == "2":

            name = input(
                "Введите имя для удаления: "
            )

            if name in users and name != "admin":

                del users[name]

                print("✅ Пользователь удалён!")

            else:

                print("❌ Пользователь не найден!")

        elif choice == "3":

            name = input(
                "Введите имя для разблокировки: "
            )

            if name in users:

                users[name]["blocked"] = False

                users[name]["attempts"] = 0

                print("✅ Пользователь разблокирован!")

            else:

                print("❌ Пользователь не найден!")

        elif choice == "4":

            break

        else:

            print("❌ Неверный выбор!")


# ==========================================
# 13. СОХРАНЕНИЕ ДАННЫХ
# ==========================================

def save_data(users: dict):

    with open(
        "users.txt",
        "w",
        encoding="utf-8"
    ) as file:

        for username, data in users.items():

            file.write(
                f"{username}|"
                f"{data['password']}|"
                f"{data['role']}|"
                f"{data['id']}|"
                f"{data['attempts']}|"
                f"{data['blocked']}|"
                f"{data['balance']}|"
                f"{data['level']}|"
                f"{data['cat']}\n"
            )


# ==========================================
# 14. ЗАГРУЗКА ДАННЫХ
# ==========================================

def load_data():

    users = {}

    if not os.path.exists("users.txt"):

        return users

    with open(
        "users.txt",
        "r",
        encoding="utf-8"
    ) as file:

        for line in file:

            parts = line.strip().split("|")

            if len(parts) != 9:

                continue

            username = parts[0]

            users[username] = {

                "password": parts[1],

                "role": parts[2],

                "id": parts[3],

                "attempts": int(parts[4]),

                "blocked": parts[5] == "True",

                "balance": int(parts[6]),

                "level": int(parts[7]),

                "cat": parts[8]

            }

    return users


# ==========================================
# 15. ГЛАВНАЯ ФУНКЦИЯ
# ==========================================

def main():

    users = load_data()

    # Создание администратора

    if "admin" not in users:

        users["admin"] = {

            "password": hash_password("Admin123!"),

            "role": "admin",

            "id": "ADMIN001",

            "attempts": 0,

            "blocked": False,

            "balance": 0,

            "level": 99,

            "cat": "Босс"

        }

    while True:

        print_cat()

        show_menu()

        choice = input(
            "Выберите действие: "
        )

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

            print("\n🐱 До свидания!")

            print("Программа завершена.")

            break

        else:


            print("❌ Неверный выбор!")

        save_data(users)


# ==========================================
# ЗАПУСК
# ==========================================

if __name__ == "__main__":

    main()
