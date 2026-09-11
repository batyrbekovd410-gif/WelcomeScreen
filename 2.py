
correct_login = "admin"
correct_password = "12345"

print("=" * 40)
print("        🔐 СИСТЕМА ВХОДА")
print("=" * 40)

login = input("Введите логин: ")
password = input("Введите пароль: ")

if login == correct_login and password == correct_password:
    print("\n✅ Вход выполнен!")
    print("Добро пожаловать,", login)

elif login != correct_login:
    print("\n❌ Неправильный логин!")

else:
    print("\n❌ Неправильный пароль!")

