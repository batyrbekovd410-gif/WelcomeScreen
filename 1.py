age = int(input("Жашыңызды киргизиңиз: "))
login = input("Логинди киргизиңиз: ")
password = input("Паролду киргизиңиз: ")
student = input("Сиз студентсизби: ")

if (age >= 18 and login == "admin" and password == "12345" )or (age >= 16 and student == "ooba"):
    print("сизге кирууго уруксат")
else:
    print("сизге ктрууго уруксат жок")