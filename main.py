#1
x = int(input("видите число: "))

if x <= 9:
    print("бул цифра")
elif x <= 99:
    print("бул сан")
else:
    print("бул узун сан")
#2
age = int(input("Введите возраст: "))

print(age >= 18 and age < 60)

#3
age = int(input("Введите возраст: "))
print(age >= 10 and age < 50)
#4
dey = input("видите ден нидели: ")
print(dey == "васкрисения" or dey =="субота")


#5


age = int(input("Введите ваш возраст: "))
student = input("Вы студент? : ")

if age > 18 and student == "да":
    print("Вход разрешён")
else:
     print("вхот запришиён")

#6
password = int(input("видите пароль: "))
login = input("видите логин: ")
if password == 1234 and login == "admin":
    print("киррууго уруксат")
else:
    print("кирууго болбойт")

#7

ball =  int(input("видите бал: "))
if ball >= 50 and ball <= 100:
    print("Упай туура")
else:
    print("Туура эмес упай")
#8
weather = float(input("аба ырайын жаз: "))
if weather <= 0 or weather >=35:
    print("Аба ырайы экстрималдуу ")
else:
    print("аба ырайы нормалдуу")


student = input("Вы студент: ")

if not student == "да":
    print("Сиз студент эмессиз")


#9

age = int(input("Жашыңызды киргизиңиз: "))
money = float(input("Акчаңызды киргизиңиз: "))

if age > 18 and money >= 1000:
    print("Акцияга катыша аласыз")
else:
    print("Акцияга катыша албайсыз")



#10
age = int(input("Жашыңызды киргизиңиз: "))
login = input("Логинди киргизиңиз: ")
password = input("Паролду киргизиңиз: ")
student = input("Сиз студентсизби: ")

if (age > 18 and login == "admin" and password == "12345") or (student == "ооба" and age > 16):
    print("Системага кирүүгө уруксат берилди")
else:
    print("Системага кирүүгө уруксат жок")