from statistics import mean
from traceback import print_tb


def info():
    print("name : Daniel")
    print("surname : Baturbekov")
    print("age : 15")
    print("phone : 0226003498")

def calkulate (a = 7, b = 89, operator ="*"):
    if operator == "+":
        print(f"{a} + {b} = {a + b}")
    elif operator == "-":
        print(f"{a} - {b} = {a - b}")
    elif operator == "*":
        print(f"{a} * {b} = {a * b}")
    elif operator == "/":
        print(f"{a} / {b} = {a / b}")
    elif operator == "//":
        print(f"{a} // {b} = {a // b}")
    else:
        print(f">>{operator}<< бул оператор жок")
#
# calkulate(6,8,"+")
# calkulate(6,8,"-")
# calkulate(7,8,"$")
# calkulate()

# def age(a=int):
#     if a < 18:
#         print("не совиршенна летний")
#     elif a  > 60:
#         print("вы уже пенсианер")
#     else:
#         print("ок")
#
# while True: age(int(input("Ведите число: ")))

def check_password(user):
    password = user['password'].lower()
    name = user['first_name'].lower()
    surname = user['last_name'].lower()

    validate = True

    if len(password) < 8:
        print("Пароль с символом меньше 8 символов")
        validate = False

    if name in password:
        print("Нельзя использовать имя пользователя в пароле")
        validate = False

    if surname in password:
        print("Нельзя использовать фамилию пользователя в пароле")
        validate = False

    if validate:
        return "Пароль подходит для аккаунта"
    else:
        return "Пароль не подходит"

#
# data = {
#     'first_name': 'даниэль',
#     'last_name': 'Батырбеков',
#     'password': 'киборк007'
# }
#
# result = check_password(data)
# print(result)
#
# print()

# def full_name(first_name, last_name,middle_name= ""):
#     print(
#         f"{last_name} {first_name}"
#         if len(middle_name) == 0
#         else f"{last_name} {first_name} {middle_name} "
#     )
#
# full_name("Daniel",last_name="Baturbekov")
# full_name(middle_name="Mederbekovih",last_name="Baturbekov",first_name="Daniel")

#
# def say_hello(): print("Hello")
#
#
# def say_goodbye(): print("Good Bye")
#
#
# message = say_hello
# message()  # Hello
# message()
# message = say_goodbye
# message()  # Good Bye
# message()

# def main(x, z, name):
#     goin = name(z, x)
#     print(f"goin : {goin}")
#
# def name(z, x):
#     return z + x
# a = main(7 , 8, name)

def sum(a, b): return a + b

def subtract(a, b): return a - b

def multiply(a, b): return a * b

def divide(a, b): return a // b

def select_operation(choice):
    if choice == 1:
        return sum
    elif choice == 2:
        return subtract
    elif choice == 3:
        return divide
    else:
        return multiply


kill= select_operation(1)
print(kill(435, 435))

kill = select_operation(2)
print(kill(10, 9))

kill = select_operation(3)
print(kill(1740, 2))

kill = select_operation(4)
print(kill(145, 6))


kill= select_operation(1)
print(kill(435, 435))

kill = select_operation(2)
print(kill(10, 9))

kill = select_operation(3)
print(kill(1740, 2))

kill = select_operation(4)
print(kill(145, 6))


