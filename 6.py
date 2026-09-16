import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import random


# ==========================================
# 🏦 БАНКОВСКАЯ СИСТЕМА
# Графический интерфейс Tkinter
# ==========================================


class BankApp:

    def __init__(self, root):

        self.root = root

        self.root.title("DANIEL BANK")
        self.root.geometry("900x650")
        self.root.resizable(False, False)

        # Цвета интерфейса
        self.bg_color = "#101827"
        self.card_color = "#1D2A3A"
        self.button_color = "#2563EB"
        self.text_color = "#FFFFFF"
        self.green_color = "#22C55E"
        self.red_color = "#EF4444"

        self.root.configure(
            bg=self.bg_color
        )

        self.users = {}

        self.current_user = None

        self.start_screen()



    def clear_window(self):

        for widget in self.root.winfo_children():

            widget.destroy()


    def create_button(
        self,
        parent,
        text,
        command,
        color=None
    ):

        if color is None:

            color = self.button_color

        return tk.Button(
            parent,
            text=text,
            command=command,
            bg=color,
            fg="white",
            font=("Arial", 12, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=10
        )


    def create_entry(
        self,
        parent,
        show=None
    ):

        return tk.Entry(
            parent,
            font=("Arial", 13),
            bg="#273449",
            fg="white",
            insertbackground="white",
            relief="flat",
            show=show
        )


    def title_label(
        self,
        parent,
        text,
        size=25
    ):

        return tk.Label(
            parent,
            text=text,
            bg=self.bg_color,
            fg=self.text_color,
            font=("Arial", size, "bold")
        )


    # ======================================
    # СТАРТОВОЕ ОКНО
    # ======================================

    def start_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        tk.Label(
            frame,
            text="🏦",
            font=("Arial", 55),
            bg=self.bg_color,
            fg="white"
        ).pack(pady=10)

        self.title_label(
            frame,
            "DANIEL BANK",
            32
        ).pack(pady=5)

        tk.Label(
            frame,
            text="Ваш учебный цифровой банк",
            bg=self.bg_color,
            fg="#94A3B8",
            font=("Arial", 13)
        ).pack(pady=5)

        self.create_button(
            frame,
            "🔐 Войти в банк",
            self.login_screen
        ).pack(
            pady=15,
            fill="x"
        )

        self.create_button(
            frame,
            "👤 Регистрация",
            self.register_screen
        ).pack(
            pady=5,
            fill="x"
        )

        tk.Label(
            frame,
            text="Учебный проект на Python",
            bg=self.bg_color,
            fg="#64748B",
            font=("Arial", 10)
        ).pack(pady=30)


    # ======================================
    # РЕГИСТРАЦИЯ
    # ======================================

    def register_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "👤 Регистрация",
            26
        ).pack(pady=20)

        tk.Label(
            frame,
            text="Имя пользователя",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        name_entry = self.create_entry(frame)

        name_entry.pack(
            pady=8,
            ipady=8
        )

        tk.Label(
            frame,
            text="Придумайте логин",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        login_entry = self.create_entry(frame)

        login_entry.pack(
            pady=8,
            ipady=8
        )

        tk.Label(
            frame,
            text="Придумайте пароль",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        password_entry = self.create_entry(
            frame,
            show="*"
        )

        password_entry.pack(
            pady=8,
            ipady=8
        )

        def register():

            name = name_entry.get().strip()
            login = login_entry.get().strip()
            password = password_entry.get()

            if not name or not login or not password:

                messagebox.showwarning(
                    "Ошибка",
                    "Заполните все поля!"
                )

                return

            if login in self.users:

                messagebox.showerror(
                    "Ошибка",
                    "Такой логин уже существует!"
                )

                return

            if len(password) < 4:

                messagebox.showwarning(
                    "Пароль",
                    "Пароль должен содержать минимум 4 символа."
                )

                return

            self.users[login] = {

                "name": name,

                "password": password,

                "balance": 1000.0,

                "card": self.generate_card(),

                "pin": str(
                    random.randint(1000, 9999)
                ),

                "history": [

                    "Счёт открыт. Начальный баланс: 1000 сом"

                ],

                "blocked": False

            }

            messagebox.showinfo(
                "Успешно",
                "Регистрация завершена!\n"
                "На счёт начислено 1000 сом."
            )

            self.login_screen()

        self.create_button(
            frame,
            "Зарегистрироваться",
            register
        ).pack(
            pady=15,
            fill="x"
        )

        self.create_button(
            frame,
            "Назад",
            self.start_screen,
            "#475569"
        ).pack(
            fill="x"
        )


    def generate_card(self):

        return " ".join(

            str(
                random.randint(1000, 9999)
            )

            for _ in range(4)

        )


    # ======================================
    # ВХОД
    # ======================================

    def login_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "🔐 Вход в банк",
            27
        ).pack(pady=20)

        tk.Label(
            frame,
            text="Логин",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        login_entry = self.create_entry(frame)

        login_entry.pack(
            pady=8,
            ipady=8
        )

        tk.Label(
            frame,
            text="Пароль",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        password_entry = self.create_entry(
            frame,
            show="*"
        )

        password_entry.pack(
            pady=8,
            ipady=8
        )

        def login():

            login = login_entry.get().strip()
            password = password_entry.get()

            if login not in self.users:

                messagebox.showerror(
                    "Ошибка",
                    "Пользователь не найден!"
                )

                return

            user = self.users[login]

            if user["password"] != password:

                messagebox.showerror(
                    "Ошибка",
                    "Неверный пароль!"
                )

                return

            if user["blocked"]:

                messagebox.showerror(
                    "Карта заблокирована",
                    "Обратитесь в банк."
                )

                return

            self.current_user = login

            self.dashboard()

        self.create_button(
            frame,
            "Войти",
            login
        ).pack(
            pady=15,
            fill="x"
        )

        self.create_button(
            frame,
            "Назад",
            self.start_screen,
            "#475569"
        ).pack(
            fill="x"
        )


    # ======================================
    # ГЛАВНОЕ МЕНЮ
    # ======================================

    def dashboard(self):

        self.clear_window()

        user = self.users[
            self.current_user
        ]

        # Верхняя панель
        top = tk.Frame(
            self.root,
            bg="#172235",
            height=75
        )

        top.pack(
            fill="x"
        )

        tk.Label(
            top,
            text="🏦 DANIEL BANK",
            bg="#172235",
            fg="white",
            font=("Arial", 22, "bold")
        ).pack(
            side="left",
            padx=25,
            pady=20
        )

        tk.Label(
            top,
            text=f"👤 {user['name']}",
            bg="#172235",
            fg="#CBD5E1",
            font=("Arial", 12)
        ).pack(
            side="right",
            padx=25
        )

        # Основная область
        main = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        main.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=25
        )

        tk.Label(
            main,
            text="Главная страница",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 24, "bold")
        ).pack(
            anchor="w"
        )

        # Карточка баланса
        balance_card = tk.Frame(
            main,
            bg=self.card_color,
            height=150
        )

        balance_card.pack(
            fill="x",
            pady=20
        )

        tk.Label(
            balance_card,
            text="Текущий баланс",
            bg=self.card_color,
            fg="#94A3B8",
            font=("Arial", 12)
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 5)
        )

        balance_label = tk.Label(
            balance_card,
            text=f"{user['balance']:,.2f} сом",
            bg=self.card_color,
            fg=self.green_color,
            font=("Arial", 30, "bold")
        )

        balance_label.pack(
            anchor="w",
            padx=25
        )

        # Кнопки меню
        buttons = tk.Frame(
            main,
            bg=self.bg_color
        )

        buttons.pack(
            fill="both",
            expand=True
        )

        menu_items = [

            ("💰 Баланс", self.balance_screen),

            ("➕ Пополнить", self.deposit_screen),

            ("➖ Снять деньги", self.withdraw_screen),

            ("🔄 Перевод", self.transfer_screen),

            ("💳 Моя карта", self.card_screen),

            ("📜 История", self.history_screen),

            ("⚙️ Настройки", self.settings_screen),

            ("🚪 Выйти", self.logout)

        ]

        for index, (text, command) in enumerate(
            menu_items
        ):

            row = index // 2
            col = index % 2

            button = self.create_button(
                buttons,
                text,
                command
            )

            button.grid(
                row=row,
                column=col,
                padx=8,
                pady=8,
                sticky="nsew"
            )

        for i in range(4):

            buttons.rowconfigure(
                i,
                weight=1
            )

        buttons.columnconfigure(
            0,
            weight=1
        )

        buttons.columnconfigure(
            1,
            weight=1
        )


    # ======================================
    # БАЛАНС
    # ======================================

    def balance_screen(self):

        self.clear_window()

        user = self.users[
            self.current_user
        ]

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "💰 Ваш баланс",
            28
        ).pack(pady=25)

        tk.Label(
            frame,
            text=f"{user['balance']:,.2f} сом",
            bg=self.bg_color,
            fg=self.green_color,
            font=("Arial", 38, "bold")
        ).pack(pady=20)

        tk.Label(
            frame,
            text="Доступные средства",
            bg=self.bg_color,
            fg="#94A3B8",
            font=("Arial", 13)
        ).pack()

        self.create_button(
            frame,
            "Назад в меню",
            self.dashboard
        ).pack(
            pady=40
        )


    # ======================================
    # ПОПОЛНЕНИЕ
    # ======================================

    def deposit_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "➕ Пополнение счёта",
            26
        ).pack(pady=25)

        tk.Label(
            frame,
            text="Введите сумму в сомах",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 13)
        ).pack()

        amount_entry = self.create_entry(frame)

        amount_entry.pack(
            pady=15,
            ipady=10
        )

        def deposit():

            try:

                amount = float(
                    amount_entry.get()
                )

                if amount <= 0:

                    raise ValueError

                user = self.users[
                    self.current_user
                ]

                user["balance"] += amount

                user["history"].append(

                    f"Пополнение: +{amount:.2f} сом"

                )

                messagebox.showinfo(
                    "Успешно",
                    f"Пополнено на {amount:.2f} сом"
                )

                self.dashboard()

            except ValueError:

                messagebox.showerror(
                    "Ошибка",
                    "Введите правильную сумму!"
                )

        self.create_button(
            frame,
            "Пополнить",
            deposit
        ).pack(
            pady=15
        )

        self.create_button(
            frame,
            "Назад",
            self.dashboard,
            "#475569"
        ).pack()


    # ======================================
    # СНЯТИЕ
    # ======================================

    def withdraw_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "➖ Снятие денег",
            26
        ).pack(pady=25)

        tk.Label(
            frame,
            text="Введите сумму",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 13)
        ).pack()

        amount_entry = self.create_entry(frame)

        amount_entry.pack(
            pady=15,
            ipady=10
        )

        def withdraw():

            try:

                amount = float(
                    amount_entry.get()
                )

                user = self.users[
                    self.current_user
                ]

                if amount <= 0:

                    raise ValueError

                if amount > user["balance"]:

                    messagebox.showerror(
                        "Ошибка",
                        "Недостаточно средств!"
                    )

                    return

                user["balance"] -= amount

                user["history"].append(

                    f"Снятие: -{amount:.2f} сом"

                )

                messagebox.showinfo(
                    "Успешно",
                    "Деньги сняты!"
                )

                self.dashboard()

            except ValueError:

                messagebox.showerror(
                    "Ошибка",
                    "Введите правильную сумму!"
                )

        self.create_button(
            frame,
            "Снять деньги",
            withdraw
        ).pack(
            pady=15
        )

        self.create_button(
            frame,
            "Назад",
            self.dashboard,
            "#475569"
        ).pack()


    # ======================================
    # ПЕРЕВОД
    # ======================================

    def transfer_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "🔄 Перевод денег",
            26
        ).pack(pady=25)

        tk.Label(
            frame,
            text="Логин получателя",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        recipient_entry = self.create_entry(frame)

        recipient_entry.pack(
            pady=10,
            ipady=8
        )

        tk.Label(
            frame,
            text="Сумма перевода",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        amount_entry = self.create_entry(frame)

        amount_entry.pack(
            pady=10,
            ipady=8
        )

        def transfer():

            recipient = recipient_entry.get().strip()

            try:

                amount = float(
                    amount_entry.get()
                )

                if amount <= 0:

                    raise ValueError

                if recipient not in self.users:

                    messagebox.showerror(
                        "Ошибка",
                        "Получатель не найден!"
                    )

                    return

                if recipient == self.current_user:

                    messagebox.showerror(
                        "Ошибка",
                        "Нельзя переводить самому себе!"
                    )

                    return

                sender = self.users[
                    self.current_user
                ]

                receiver = self.users[
                    recipient
                ]

                if amount > sender["balance"]:

                    messagebox.showerror(
                        "Ошибка",
                        "Недостаточно средств!"
                    )

                    return

                sender["balance"] -= amount

                receiver["balance"] += amount

                sender["history"].append(

                    f"Перевод пользователю {recipient}: "
                    f"-{amount:.2f} сом"

                )

                receiver["history"].append(

                    f"Получен перевод от "
                    f"{self.current_user}: "
                    f"+{amount:.2f} сом"

                )

                messagebox.showinfo(
                    "Успешно",
                    "Перевод выполнен!"
                )

                self.dashboard()

            except ValueError:

                messagebox.showerror(
                    "Ошибка",
                    "Введите правильную сумму!"
                )

        self.create_button(
            frame,
            "Отправить перевод",
            transfer
        ).pack(
            pady=15
        )

        self.create_button(
            frame,
            "Назад",
            self.dashboard,
            "#475569"
        ).pack()


    # ======================================
    # БАНКОВСКАЯ КАРТА
    # ======================================

    def card_screen(self):

        self.clear_window()

        user = self.users[
            self.current_user
        ]

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "💳 Моя банковская карта",
            25
        ).pack(pady=25)

        card = tk.Frame(
            frame,
            bg="#1E40AF",
            width=500,
            height=240
        )

        card.pack(
            pady=15
        )

        card.pack_propagate(False)

        tk.Label(
            card,
            text="DANIEL BANK",
            bg="#1E40AF",
            fg="white",
            font=("Arial", 20, "bold")
        ).pack(
            anchor="w",
            padx=25,
            pady=20
        )

        tk.Label(
            card,
            text=user["card"],
            bg="#1E40AF",
            fg="white",
            font=("Arial", 20)
        ).pack(
            pady=20
        )

        tk.Label(
            card,
            text=user["name"],
            bg="#1E40AF",
            fg="white",
            font=("Arial", 12)
        ).pack(
            anchor="w",
            padx=25
        )

        tk.Label(
            frame,
            text="PIN-код: " + user["pin"],
            bg=self.bg_color,
            fg="#CBD5E1",
            font=("Arial", 13)
        ).pack(pady=10)

        self.create_button(
            frame,
            "Назад",
            self.dashboard
        ).pack(pady=20)


    # ======================================
    # ИСТОРИЯ ОПЕРАЦИЙ
    # ======================================

    def history_screen(self):

        self.clear_window()

        user = self.users[
            self.current_user
        ]

        self.title_label(
            self.root,
            "📜 История операций",
            25
        ).pack(pady=20)

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            fill="both",
            expand=True,
            padx=30
        )

        scrollbar = tk.Scrollbar(frame)

        scrollbar.pack(
            side="right",
            fill="y"
        )

        history_list = tk.Listbox(
            frame,
            bg="#273449",
            fg="white",
            font=("Arial", 12),
            yscrollcommand=scrollbar.set
        )

        history_list.pack(
            fill="both",
            expand=True
        )

        scrollbar.config(
            command=history_list.yview
        )

        for operation in user["history"]:

            history_list.insert(
                tk.END,
                operation
            )

        self.create_button(
            self.root,
            "Назад",
            self.dashboard
        ).pack(pady=15)


    # ======================================
    # НАСТРОЙКИ
    # ======================================

    def settings_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "⚙️ Настройки",
            27
        ).pack(pady=25)

        self.create_button(
            frame,
            "🔑 Изменить пароль",
            self.change_password
        ).pack(
            pady=10,
            fill="x"
        )

        self.create_button(
            frame,
            "🚫 Заблокировать карту",
            self.block_card,
            self.red_color
        ).pack(
            pady=10,
            fill="x"
        )

        self.create_button(
            frame,
            "Назад",
            self.dashboard,
            "#475569"
        ).pack(
            pady=20,
            fill="x"
        )


    # ======================================
    # ИЗМЕНЕНИЕ ПАРОЛЯ
    # ======================================

    def change_password(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "🔑 Новый пароль",
            26
        ).pack(pady=25)

        tk.Label(
            frame,
            text="Введите новый пароль",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        password_entry = self.create_entry(
            frame,
            show="*"
        )

        password_entry.pack(
            pady=15,
            ipady=8
        )

        def save_password():

            password = password_entry.get()

            if len(password) < 4:

                messagebox.showwarning(
                    "Ошибка",
                    "Минимум 4 символа!"
                )

                return

            self.users[
                self.current_user
            ]["password"] = password

            messagebox.showinfo(
                "Успешно",
                "Пароль изменён!"
            )

            self.dashboard()

        self.create_button(
            frame,
            "Сохранить пароль",
            save_password
        ).pack(pady=15)

        self.create_button(
            frame,
            "Назад",
            self.settings_screen,
            "#475569"
        ).pack()


    # ======================================
    # БЛОКИРОВКА КАРТЫ
    # ======================================

    def block_card(self):

        answer = messagebox.askyesno(
            "Блокировка",
            "Вы действительно хотите заблокировать карту?"
        )

        if answer:

            self.users[
                self.current_user
            ]["blocked"] = True

            messagebox.showinfo(
                "Карта заблокирована",
                "Карта заблокирована."
            )

            self.logout()


    # ======================================
    # ВЫХОД
    # ======================================

    def logout(self):

        self.current_user = None

        self.start_screen()


# ==========================================
# ЗАПУСК ПРОГРАММЫ
# ==========================================

if __name__ == "__main__":

    root = tk.Tk()

    app = BankApp(root)

    root.mainloop()


import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import random


# ==========================================
# 🏦 БАНКОВСКАЯ СИСТЕМА
# Графический интерфейс Tkinter
# ==========================================


class BankApp:

    def __init__(self, root):

        self.root = root

        self.root.title("DANIEL BANK")
        self.root.geometry("900x650")
        self.root.resizable(False, False)

        # Цвета интерфейса
        self.bg_color = "#101827"
        self.card_color = "#1D2A3A"
        self.button_color = "#2563EB"
        self.text_color = "#FFFFFF"
        self.green_color = "#22C55E"
        self.red_color = "#EF4444"

        self.root.configure(
            bg=self.bg_color
        )

        # Данные клиентов
        self.users = {}

        # Текущий пользователь
        self.current_user = None

        # Запуск стартового окна
        self.start_screen()


    # ======================================
    # ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
    # ======================================

    def clear_window(self):

        for widget in self.root.winfo_children():

            widget.destroy()


    def create_button(
        self,
        parent,
        text,
        command,
        color=None
    ):

        if color is None:

            color = self.button_color

        return tk.Button(
            parent,
            text=text,
            command=command,
            bg=color,
            fg="white",
            font=("Arial", 12, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=10
        )


    def create_entry(
        self,
        parent,
        show=None
    ):

        return tk.Entry(
            parent,
            font=("Arial", 13),
            bg="#273449",
            fg="white",
            insertbackground="white",
            relief="flat",
            show=show
        )


    def title_label(
        self,
        parent,
        text,
        size=25
    ):

        return tk.Label(
            parent,
            text=text,
            bg=self.bg_color,
            fg=self.text_color,
            font=("Arial", size, "bold")
        )


    # ======================================
    # СТАРТОВОЕ ОКНО
    # ======================================

    def start_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        tk.Label(
            frame,
            text="🏦",
            font=("Arial", 55),
            bg=self.bg_color,
            fg="white"
        ).pack(pady=10)

        self.title_label(
            frame,
            "DANIEL BANK",
            32
        ).pack(pady=5)

        tk.Label(
            frame,
            text="Ваш учебный цифровой банк",
            bg=self.bg_color,
            fg="#94A3B8",
            font=("Arial", 13)
        ).pack(pady=5)

        self.create_button(
            frame,
            "🔐 Войти в банк",
            self.login_screen
        ).pack(
            pady=15,
            fill="x"
        )

        self.create_button(
            frame,
            "👤 Регистрация",
            self.register_screen
        ).pack(
            pady=5,
            fill="x"
        )

        tk.Label(
            frame,
            text="Учебный проект на Python",
            bg=self.bg_color,
            fg="#64748B",
            font=("Arial", 10)
        ).pack(pady=30)


    # ======================================
    # РЕГИСТРАЦИЯ
    # ======================================

    def register_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "👤 Регистрация",
            26
        ).pack(pady=20)

        tk.Label(
            frame,
            text="Имя пользователя",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        name_entry = self.create_entry(frame)

        name_entry.pack(
            pady=8,
            ipady=8
        )

        tk.Label(
            frame,
            text="Придумайте логин",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        login_entry = self.create_entry(frame)

        login_entry.pack(
            pady=8,
            ipady=8
        )

        tk.Label(
            frame,
            text="Придумайте пароль",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        password_entry = self.create_entry(
            frame,
            show="*"
        )

        password_entry.pack(
            pady=8,
            ipady=8
        )

        def register():

            name = name_entry.get().strip()
            login = login_entry.get().strip()
            password = password_entry.get()

            if not name or not login or not password:

                messagebox.showwarning(
                    "Ошибка",
                    "Заполните все поля!"
                )

                return

            if login in self.users:

                messagebox.showerror(
                    "Ошибка",
                    "Такой логин уже существует!"
                )

                return

            if len(password) < 4:

                messagebox.showwarning(
                    "Пароль",
                    "Пароль должен содержать минимум 4 символа."
                )

                return

            self.users[login] = {

                "name": name,

                "password": password,

                "balance": 1000.0,

                "card": self.generate_card(),

                "pin": str(
                    random.randint(1000, 9999)
                ),

                "history": [

                    "Счёт открыт. Начальный баланс: 1000 сом"

                ],

                "blocked": False

            }

            messagebox.showinfo(
                "Успешно",
                "Регистрация завершена!\n"
                "На счёт начислено 1000 сом."
            )

            self.login_screen()

        self.create_button(
            frame,
            "Зарегистрироваться",
            register
        ).pack(
            pady=15,
            fill="x"
        )

        self.create_button(
            frame,
            "Назад",
            self.start_screen,
            "#475569"
        ).pack(
            fill="x"
        )


    def generate_card(self):

        return " ".join(

            str(
                random.randint(1000, 9999)
            )

            for _ in range(4)

        )


    # ======================================
    # ВХОД
    # ======================================

    def login_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "🔐 Вход в банк",
            27
        ).pack(pady=20)

        tk.Label(
            frame,
            text="Логин",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        login_entry = self.create_entry(frame)

        login_entry.pack(
            pady=8,
            ipady=8
        )

        tk.Label(
            frame,
            text="Пароль",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        password_entry = self.create_entry(
            frame,
            show="*"
        )

        password_entry.pack(
            pady=8,
            ipady=8
        )

        def login():

            login = login_entry.get().strip()
            password = password_entry.get()

            if login not in self.users:

                messagebox.showerror(
                    "Ошибка",
                    "Пользователь не найден!"
                )

                return

            user = self.users[login]

            if user["password"] != password:

                messagebox.showerror(
                    "Ошибка",
                    "Неверный пароль!"
                )

                return

            if user["blocked"]:

                messagebox.showerror(
                    "Карта заблокирована",
                    "Обратитесь в банк."
                )

                return

            self.current_user = login

            self.dashboard()

        self.create_button(
            frame,
            "Войти",
            login
        ).pack(
            pady=15,
            fill="x"
        )

        self.create_button(
            frame,
            "Назад",
            self.start_screen,
            "#475569"
        ).pack(
            fill="x"
        )


    # ======================================
    # ГЛАВНОЕ МЕНЮ
    # ======================================

    def dashboard(self):

        self.clear_window()

        user = self.users[
            self.current_user
        ]

        # Верхняя панель
        top = tk.Frame(
            self.root,
            bg="#172235",
            height=75
        )

        top.pack(
            fill="x"
        )

        tk.Label(
            top,
            text="🏦 DANIEL BANK",
            bg="#172235",
            fg="white",
            font=("Arial", 22, "bold")
        ).pack(
            side="left",
            padx=25,
            pady=20
        )

        tk.Label(
            top,
            text=f"👤 {user['name']}",
            bg="#172235",
            fg="#CBD5E1",
            font=("Arial", 12)
        ).pack(
            side="right",
            padx=25
        )

        # Основная область
        main = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        main.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=25
        )

        tk.Label(
            main,
            text="Главная страница",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 24, "bold")
        ).pack(
            anchor="w"
        )

        # Карточка баланса
        balance_card = tk.Frame(
            main,
            bg=self.card_color,
            height=150
        )

        balance_card.pack(
            fill="x",
            pady=20
        )

        tk.Label(
            balance_card,
            text="Текущий баланс",
            bg=self.card_color,
            fg="#94A3B8",
            font=("Arial", 12)
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 5)
        )

        balance_label = tk.Label(
            balance_card,
            text=f"{user['balance']:,.2f} сом",
            bg=self.card_color,
            fg=self.green_color,
            font=("Arial", 30, "bold")
        )

        balance_label.pack(
            anchor="w",
            padx=25
        )

        # Кнопки меню
        buttons = tk.Frame(
            main,
            bg=self.bg_color
        )

        buttons.pack(
            fill="both",
            expand=True
        )

        menu_items = [

            ("💰 Баланс", self.balance_screen),

            ("➕ Пополнить", self.deposit_screen),

            ("➖ Снять деньги", self.withdraw_screen),

            ("🔄 Перевод", self.transfer_screen),

            ("💳 Моя карта", self.card_screen),

            ("📜 История", self.history_screen),

            ("⚙️ Настройки", self.settings_screen),

            ("🚪 Выйти", self.logout)

        ]

        for index, (text, command) in enumerate(
            menu_items
        ):

            row = index // 2
            col = index % 2

            button = self.create_button(
                buttons,
                text,
                command
            )

            button.grid(
                row=row,
                column=col,
                padx=8,
                pady=8,
                sticky="nsew"
            )

        for i in range(4):

            buttons.rowconfigure(
                i,
                weight=1
            )

        buttons.columnconfigure(
            0,
            weight=1
        )

        buttons.columnconfigure(
            1,
            weight=1
        )


    # ======================================
    # БАЛАНС
    # ======================================

    def balance_screen(self):

        self.clear_window()

        user = self.users[
            self.current_user
        ]

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "💰 Ваш баланс",
            28
        ).pack(pady=25)

        tk.Label(
            frame,
            text=f"{user['balance']:,.2f} сом",
            bg=self.bg_color,
            fg=self.green_color,
            font=("Arial", 38, "bold")
        ).pack(pady=20)

        tk.Label(
            frame,
            text="Доступные средства",
            bg=self.bg_color,
            fg="#94A3B8",
            font=("Arial", 13)
        ).pack()

        self.create_button(
            frame,
            "Назад в меню",
            self.dashboard
        ).pack(
            pady=40
        )


    # ======================================
    # ПОПОЛНЕНИЕ
    # ======================================

    def deposit_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "➕ Пополнение счёта",
            26
        ).pack(pady=25)

        tk.Label(
            frame,
            text="Введите сумму в сомах",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 13)
        ).pack()

        amount_entry = self.create_entry(frame)

        amount_entry.pack(
            pady=15,
            ipady=10
        )

        def deposit():

            try:

                amount = float(
                    amount_entry.get()
                )

                if amount <= 0:

                    raise ValueError

                user = self.users[
                    self.current_user
                ]

                user["balance"] += amount

                user["history"].append(

                    f"Пополнение: +{amount:.2f} сом"

                )

                messagebox.showinfo(
                    "Успешно",
                    f"Пополнено на {amount:.2f} сом"
                )

                self.dashboard()

            except ValueError:

                messagebox.showerror(
                    "Ошибка",
                    "Введите правильную сумму!"
                )

        self.create_button(
            frame,
            "Пополнить",
            deposit
        ).pack(
            pady=15
        )

        self.create_button(
            frame,
            "Назад",
            self.dashboard,
            "#475569"
        ).pack()


    # ======================================
    # СНЯТИЕ
    # ======================================

    def withdraw_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "➖ Снятие денег",
            26
        ).pack(pady=25)

        tk.Label(
            frame,
            text="Введите сумму",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 13)
        ).pack()

        amount_entry = self.create_entry(frame)

        amount_entry.pack(
            pady=15,
            ipady=10
        )

        def withdraw():

            try:

                amount = float(
                    amount_entry.get()
                )

                user = self.users[
                    self.current_user
                ]

                if amount <= 0:

                    raise ValueError

                if amount > user["balance"]:

                    messagebox.showerror(
                        "Ошибка",
                        "Недостаточно средств!"
                    )

                    return

                user["balance"] -= amount

                user["history"].append(

                    f"Снятие: -{amount:.2f} сом"

                )

                messagebox.showinfo(
                    "Успешно",
                    "Деньги сняты!"
                )

                self.dashboard()

            except ValueError:

                messagebox.showerror(
                    "Ошибка",
                    "Введите правильную сумму!"
                )

        self.create_button(
            frame,
            "Снять деньги",
            withdraw
        ).pack(
            pady=15
        )

        self.create_button(
            frame,
            "Назад",
            self.dashboard,
            "#475569"
        ).pack()


    # ======================================
    # ПЕРЕВОД
    # ======================================

    def transfer_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "🔄 Перевод денег",
            26
        ).pack(pady=25)

        tk.Label(
            frame,
            text="Логин получателя",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        recipient_entry = self.create_entry(frame)

        recipient_entry.pack(
            pady=10,
            ipady=8
        )

        tk.Label(
            frame,
            text="Сумма перевода",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        amount_entry = self.create_entry(frame)

        amount_entry.pack(
            pady=10,
            ipady=8
        )

        def transfer():

            recipient = recipient_entry.get().strip()

            try:

                amount = float(
                    amount_entry.get()
                )

                if amount <= 0:

                    raise ValueError

                if recipient not in self.users:

                    messagebox.showerror(
                        "Ошибка",
                        "Получатель не найден!"
                    )

                    return

                if recipient == self.current_user:

                    messagebox.showerror(
                        "Ошибка",
                        "Нельзя переводить самому себе!"
                    )

                    return

                sender = self.users[
                    self.current_user
                ]

                receiver = self.users[
                    recipient
                ]

                if amount > sender["balance"]:

                    messagebox.showerror(
                        "Ошибка",
                        "Недостаточно средств!"
                    )

                    return

                sender["balance"] -= amount

                receiver["balance"] += amount

                sender["history"].append(

                    f"Перевод пользователю {recipient}: "
                    f"-{amount:.2f} сом"

                )

                receiver["history"].append(

                    f"Получен перевод от "
                    f"{self.current_user}: "
                    f"+{amount:.2f} сом"

                )

                messagebox.showinfo(
                    "Успешно",
                    "Перевод выполнен!"
                )

                self.dashboard()

            except ValueError:

                messagebox.showerror(
                    "Ошибка",
                    "Введите правильную сумму!"
                )

        self.create_button(
            frame,
            "Отправить перевод",
            transfer
        ).pack(
            pady=15
        )

        self.create_button(
            frame,
            "Назад",
            self.dashboard,
            "#475569"
        ).pack()


    # ======================================
    # БАНКОВСКАЯ КАРТА
    # ======================================

    def card_screen(self):

        self.clear_window()

        user = self.users[
            self.current_user
        ]

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "💳 Моя банковская карта",
            25
        ).pack(pady=25)

        card = tk.Frame(
            frame,
            bg="#1E40AF",
            width=500,
            height=240
        )

        card.pack(
            pady=15
        )

        card.pack_propagate(False)

        tk.Label(
            card,
            text="DANIEL BANK",
            bg="#1E40AF",
            fg="white",
            font=("Arial", 20, "bold")
        ).pack(
            anchor="w",
            padx=25,
            pady=20
        )

        tk.Label(
            card,
            text=user["card"],
            bg="#1E40AF",
            fg="white",
            font=("Arial", 20)
        ).pack(
            pady=20
        )

        tk.Label(
            card,
            text=user["name"],
            bg="#1E40AF",
            fg="white",
            font=("Arial", 12)
        ).pack(
            anchor="w",
            padx=25
        )

        tk.Label(
            frame,
            text="PIN-код: " + user["pin"],
            bg=self.bg_color,
            fg="#CBD5E1",
            font=("Arial", 13)
        ).pack(pady=10)

        self.create_button(
            frame,
            "Назад",
            self.dashboard
        ).pack(pady=20)


    # ======================================
    # ИСТОРИЯ ОПЕРАЦИЙ
    # ======================================

    def history_screen(self):

        self.clear_window()

        user = self.users[
            self.current_user
        ]

        self.title_label(
            self.root,
            "📜 История операций",
            25
        ).pack(pady=20)

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            fill="both",
            expand=True,
            padx=30
        )

        scrollbar = tk.Scrollbar(frame)

        scrollbar.pack(
            side="right",
            fill="y"
        )

        history_list = tk.Listbox(
            frame,
            bg="#273449",
            fg="white",
            font=("Arial", 12),
            yscrollcommand=scrollbar.set
        )

        history_list.pack(
            fill="both",
            expand=True
        )

        scrollbar.config(
            command=history_list.yview
        )

        for operation in user["history"]:

            history_list.insert(
                tk.END,
                operation
            )

        self.create_button(
            self.root,
            "Назад",
            self.dashboard
        ).pack(pady=15)


    # ======================================
    # НАСТРОЙКИ
    # ======================================

    def settings_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "⚙️ Настройки",
            27
        ).pack(pady=25)

        self.create_button(
            frame,
            "🔑 Изменить пароль",
            self.change_password
        ).pack(
            pady=10,
            fill="x"
        )

        self.create_button(
            frame,
            "🚫 Заблокировать карту",
            self.block_card,
            self.red_color
        ).pack(
            pady=10,
            fill="x"
        )

        self.create_button(
            frame,
            "Назад",
            self.dashboard,
            "#475569"
        ).pack(
            pady=20,
            fill="x"
        )


    # ======================================
    # ИЗМЕНЕНИЕ ПАРОЛЯ
    # ======================================

    def change_password(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "🔑 Новый пароль",
            26
        ).pack(pady=25)

        tk.Label(
            frame,
            text="Введите новый пароль",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        password_entry = self.create_entry(
            frame,
            show="*"
        )

        password_entry.pack(
            pady=15,
            ipady=8
        )

        def save_password():

            password = password_entry.get()

            if len(password) < 4:

                messagebox.showwarning(
                    "Ошибка",
                    "Минимум 4 символа!"
                )

                return

            self.users[
                self.current_user
            ]["password"] = password

            messagebox.showinfo(
                "Успешно",
                "Пароль изменён!"
            )

            self.dashboard()

        self.create_button(
            frame,
            "Сохранить пароль",
            save_password
        ).pack(pady=15)

        self.create_button(
            frame,
            "Назад",
            self.settings_screen,
            "#475569"
        ).pack()


    # ======================================
    # БЛОКИРОВКА КАРТЫ
    # ======================================

    def block_card(self):

        answer = messagebox.askyesno(
            "Блокировка",
            "Вы действительно хотите заблокировать карту?"
        )

        if answer:

            self.users[
                self.current_user
            ]["blocked"] = True

            messagebox.showinfo(
                "Карта заблокирована",
                "Карта заблокирована."
            )

            self.logout()


    # ======================================
    # ВЫХОД
    # ======================================

    def logout(self):

        self.current_user = None

        self.start_screen()


# ==========================================
# ЗАПУСК ПРОГРАММЫ
# ==========================================

if __name__ == "__main__":

    root = tk.Tk()

    app = BankApp(root)

    root.mainloop()

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import random


# ==========================================
# 🏦 БАНКОВСКАЯ СИСТЕМА
# Графический интерфейс Tkinter
# ==========================================


class BankApp:

    def __init__(self, root):

        self.root = root

        self.root.title("DANIEL BANK")
        self.root.geometry("900x650")
        self.root.resizable(False, False)

        # Цвета интерфейса
        self.bg_color = "#101827"
        self.card_color = "#1D2A3A"
        self.button_color = "#2563EB"
        self.text_color = "#FFFFFF"
        self.green_color = "#22C55E"
        self.red_color = "#EF4444"

        self.root.configure(
            bg=self.bg_color
        )

        # Данные клиентов
        self.users = {}

        # Текущий пользователь
        self.current_user = None

        # Запуск стартового окна
        self.start_screen()


    # ======================================
    # ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
    # ======================================

    def clear_window(self):

        for widget in self.root.winfo_children():

            widget.destroy()


    def create_button(
        self,
        parent,
        text,
        command,
        color=None
    ):

        if color is None:

            color = self.button_color

        return tk.Button(
            parent,
            text=text,
            command=command,
            bg=color,
            fg="white",
            font=("Arial", 12, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=10
        )


    def create_entry(
        self,
        parent,
        show=None
    ):

        return tk.Entry(
            parent,
            font=("Arial", 13),
            bg="#273449",
            fg="white",
            insertbackground="white",
            relief="flat",
            show=show
        )


    def title_label(
        self,
        parent,
        text,
        size=25
    ):

        return tk.Label(
            parent,
            text=text,
            bg=self.bg_color,
            fg=self.text_color,
            font=("Arial", size, "bold")
        )


    # ======================================
    # СТАРТОВОЕ ОКНО
    # ======================================

    def start_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        tk.Label(
            frame,
            text="🏦",
            font=("Arial", 55),
            bg=self.bg_color,
            fg="white"
        ).pack(pady=10)

        self.title_label(
            frame,
            "DANIEL BANK",
            32
        ).pack(pady=5)

        tk.Label(
            frame,
            text="Ваш учебный цифровой банк",
            bg=self.bg_color,
            fg="#94A3B8",
            font=("Arial", 13)
        ).pack(pady=5)

        self.create_button(
            frame,
            "🔐 Войти в банк",
            self.login_screen
        ).pack(
            pady=15,
            fill="x"
        )

        self.create_button(
            frame,
            "👤 Регистрация",
            self.register_screen
        ).pack(
            pady=5,
            fill="x"
        )

        tk.Label(
            frame,
            text="Учебный проект на Python",
            bg=self.bg_color,
            fg="#64748B",
            font=("Arial", 10)
        ).pack(pady=30)


    # ======================================
    # РЕГИСТРАЦИЯ
    # ======================================

    def register_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "👤 Регистрация",
            26
        ).pack(pady=20)

        tk.Label(
            frame,
            text="Имя пользователя",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        name_entry = self.create_entry(frame)

        name_entry.pack(
            pady=8,
            ipady=8
        )

        tk.Label(
            frame,
            text="Придумайте логин",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        login_entry = self.create_entry(frame)

        login_entry.pack(
            pady=8,
            ipady=8
        )

        tk.Label(
            frame,
            text="Придумайте пароль",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        password_entry = self.create_entry(
            frame,
            show="*"
        )

        password_entry.pack(
            pady=8,
            ipady=8
        )

        def register():

            name = name_entry.get().strip()
            login = login_entry.get().strip()
            password = password_entry.get()

            if not name or not login or not password:

                messagebox.showwarning(
                    "Ошибка",
                    "Заполните все поля!"
                )

                return

            if login in self.users:

                messagebox.showerror(
                    "Ошибка",
                    "Такой логин уже существует!"
                )

                return

            if len(password) < 4:

                messagebox.showwarning(
                    "Пароль",
                    "Пароль должен содержать минимум 4 символа."
                )

                return

            self.users[login] = {

                "name": name,

                "password": password,

                "balance": 1000.0,

                "card": self.generate_card(),

                "pin": str(
                    random.randint(1000, 9999)
                ),

                "history": [

                    "Счёт открыт. Начальный баланс: 1000 сом"

                ],

                "blocked": False

            }

            messagebox.showinfo(
                "Успешно",
                "Регистрация завершена!\n"
                "На счёт начислено 1000 сом."
            )

            self.login_screen()

        self.create_button(
            frame,
            "Зарегистрироваться",
            register
        ).pack(
            pady=15,
            fill="x"
        )

        self.create_button(
            frame,
            "Назад",
            self.start_screen,
            "#475569"
        ).pack(
            fill="x"
        )


    def generate_card(self):

        return " ".join(

            str(
                random.randint(1000, 9999)
            )

            for _ in range(4)

        )


    # ======================================
    # ВХОД
    # ======================================

    def login_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "🔐 Вход в банк",
            27
        ).pack(pady=20)

        tk.Label(
            frame,
            text="Логин",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        login_entry = self.create_entry(frame)

        login_entry.pack(
            pady=8,
            ipady=8
        )

        tk.Label(
            frame,
            text="Пароль",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        password_entry = self.create_entry(
            frame,
            show="*"
        )

        password_entry.pack(
            pady=8,
            ipady=8
        )

        def login():

            login = login_entry.get().strip()
            password = password_entry.get()

            if login not in self.users:

                messagebox.showerror(
                    "Ошибка",
                    "Пользователь не найден!"
                )

                return

            user = self.users[login]

            if user["password"] != password:

                messagebox.showerror(
                    "Ошибка",
                    "Неверный пароль!"
                )

                return

            if user["blocked"]:

                messagebox.showerror(
                    "Карта заблокирована",
                    "Обратитесь в банк."
                )

                return

            self.current_user = login

            self.dashboard()

        self.create_button(
            frame,
            "Войти",
            login
        ).pack(
            pady=15,
            fill="x"
        )

        self.create_button(
            frame,
            "Назад",
            self.start_screen,
            "#475569"
        ).pack(
            fill="x"
        )


    # ======================================
    # ГЛАВНОЕ МЕНЮ
    # ======================================

    def dashboard(self):

        self.clear_window()

        user = self.users[
            self.current_user
        ]

        # Верхняя панель
        top = tk.Frame(
            self.root,
            bg="#172235",
            height=75
        )

        top.pack(
            fill="x"
        )

        tk.Label(
            top,
            text="🏦 DANIEL BANK",
            bg="#172235",
            fg="white",
            font=("Arial", 22, "bold")
        ).pack(
            side="left",
            padx=25,
            pady=20
        )

        tk.Label(
            top,
            text=f"👤 {user['name']}",
            bg="#172235",
            fg="#CBD5E1",
            font=("Arial", 12)
        ).pack(
            side="right",
            padx=25
        )

        # Основная область
        main = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        main.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=25
        )

        tk.Label(
            main,
            text="Главная страница",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 24, "bold")
        ).pack(
            anchor="w"
        )

        # Карточка баланса
        balance_card = tk.Frame(
            main,
            bg=self.card_color,
            height=150
        )

        balance_card.pack(
            fill="x",
            pady=20
        )

        tk.Label(
            balance_card,
            text="Текущий баланс",
            bg=self.card_color,
            fg="#94A3B8",
            font=("Arial", 12)
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 5)
        )

        balance_label = tk.Label(
            balance_card,
            text=f"{user['balance']:,.2f} сом",
            bg=self.card_color,
            fg=self.green_color,
            font=("Arial", 30, "bold")
        )

        balance_label.pack(
            anchor="w",
            padx=25
        )

        # Кнопки меню
        buttons = tk.Frame(
            main,
            bg=self.bg_color
        )

        buttons.pack(
            fill="both",
            expand=True
        )

        menu_items = [

            ("💰 Баланс", self.balance_screen),

            ("➕ Пополнить", self.deposit_screen),

            ("➖ Снять деньги", self.withdraw_screen),

            ("🔄 Перевод", self.transfer_screen),

            ("💳 Моя карта", self.card_screen),

            ("📜 История", self.history_screen),

            ("⚙️ Настройки", self.settings_screen),

            ("🚪 Выйти", self.logout)

        ]

        for index, (text, command) in enumerate(
            menu_items
        ):

            row = index // 2
            col = index % 2

            button = self.create_button(
                buttons,
                text,
                command
            )

            button.grid(
                row=row,
                column=col,
                padx=8,
                pady=8,
                sticky="nsew"
            )

        for i in range(4):

            buttons.rowconfigure(
                i,
                weight=1
            )

        buttons.columnconfigure(
            0,
            weight=1
        )

        buttons.columnconfigure(
            1,
            weight=1
        )


    # ======================================
    # БАЛАНС
    # ======================================

    def balance_screen(self):

        self.clear_window()

        user = self.users[
            self.current_user
        ]

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "💰 Ваш баланс",
            28
        ).pack(pady=25)

        tk.Label(
            frame,
            text=f"{user['balance']:,.2f} сом",
            bg=self.bg_color,
            fg=self.green_color,
            font=("Arial", 38, "bold")
        ).pack(pady=20)

        tk.Label(
            frame,
            text="Доступные средства",
            bg=self.bg_color,
            fg="#94A3B8",
            font=("Arial", 13)
        ).pack()

        self.create_button(
            frame,
            "Назад в меню",
            self.dashboard
        ).pack(
            pady=40
        )


    # ======================================
    # ПОПОЛНЕНИЕ
    # ======================================

    def deposit_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "➕ Пополнение счёта",
            26
        ).pack(pady=25)

        tk.Label(
            frame,
            text="Введите сумму в сомах",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 13)
        ).pack()

        amount_entry = self.create_entry(frame)

        amount_entry.pack(
            pady=15,
            ipady=10
        )

        def deposit():

            try:

                amount = float(
                    amount_entry.get()
                )

                if amount <= 0:

                    raise ValueError

                user = self.users[
                    self.current_user
                ]

                user["balance"] += amount

                user["history"].append(

                    f"Пополнение: +{amount:.2f} сом"

                )

                messagebox.showinfo(
                    "Успешно",
                    f"Пополнено на {amount:.2f} сом"
                )

                self.dashboard()

            except ValueError:

                messagebox.showerror(
                    "Ошибка",
                    "Введите правильную сумму!"
                )

        self.create_button(
            frame,
            "Пополнить",
            deposit
        ).pack(
            pady=15
        )

        self.create_button(
            frame,
            "Назад",
            self.dashboard,
            "#475569"
        ).pack()


    # ======================================
    # СНЯТИЕ
    # ======================================

    def withdraw_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "➖ Снятие денег",
            26
        ).pack(pady=25)

        tk.Label(
            frame,
            text="Введите сумму",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 13)
        ).pack()

        amount_entry = self.create_entry(frame)

        amount_entry.pack(
            pady=15,
            ipady=10
        )

        def withdraw():

            try:

                amount = float(
                    amount_entry.get()
                )

                user = self.users[
                    self.current_user
                ]

                if amount <= 0:

                    raise ValueError

                if amount > user["balance"]:

                    messagebox.showerror(
                        "Ошибка",
                        "Недостаточно средств!"
                    )

                    return

                user["balance"] -= amount

                user["history"].append(

                    f"Снятие: -{amount:.2f} сом"

                )

                messagebox.showinfo(
                    "Успешно",
                    "Деньги сняты!"
                )

                self.dashboard()

            except ValueError:

                messagebox.showerror(
                    "Ошибка",
                    "Введите правильную сумму!"
                )

        self.create_button(
            frame,
            "Снять деньги",
            withdraw
        ).pack(
            pady=15
        )

        self.create_button(
            frame,
            "Назад",
            self.dashboard,
            "#475569"
        ).pack()


    # ======================================
    # ПЕРЕВОД
    # ======================================

    def transfer_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "🔄 Перевод денег",
            26
        ).pack(pady=25)

        tk.Label(
            frame,
            text="Логин получателя",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        recipient_entry = self.create_entry(frame)

        recipient_entry.pack(
            pady=10,
            ipady=8
        )

        tk.Label(
            frame,
            text="Сумма перевода",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        amount_entry = self.create_entry(frame)

        amount_entry.pack(
            pady=10,
            ipady=8
        )

        def transfer():

            recipient = recipient_entry.get().strip()

            try:

                amount = float(
                    amount_entry.get()
                )

                if amount <= 0:

                    raise ValueError

                if recipient not in self.users:

                    messagebox.showerror(
                        "Ошибка",
                        "Получатель не найден!"
                    )

                    return

                if recipient == self.current_user:

                    messagebox.showerror(
                        "Ошибка",
                        "Нельзя переводить самому себе!"
                    )

                    return

                sender = self.users[
                    self.current_user
                ]

                receiver = self.users[
                    recipient
                ]

                if amount > sender["balance"]:

                    messagebox.showerror(
                        "Ошибка",
                        "Недостаточно средств!"
                    )

                    return

                sender["balance"] -= amount

                receiver["balance"] += amount

                sender["history"].append(

                    f"Перевод пользователю {recipient}: "
                    f"-{amount:.2f} сом"

                )

                receiver["history"].append(

                    f"Получен перевод от "
                    f"{self.current_user}: "
                    f"+{amount:.2f} сом"

                )

                messagebox.showinfo(
                    "Успешно",
                    "Перевод выполнен!"
                )

                self.dashboard()

            except ValueError:

                messagebox.showerror(
                    "Ошибка",
                    "Введите правильную сумму!"
                )

        self.create_button(
            frame,
            "Отправить перевод",
            transfer
        ).pack(
            pady=15
        )

        self.create_button(
            frame,
            "Назад",
            self.dashboard,
            "#475569"
        ).pack()


    # ======================================
    # БАНКОВСКАЯ КАРТА
    # ======================================

    def card_screen(self):

        self.clear_window()

        user = self.users[
            self.current_user
        ]

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "💳 Моя банковская карта",
            25
        ).pack(pady=25)

        card = tk.Frame(
            frame,
            bg="#1E40AF",
            width=500,
            height=240
        )

        card.pack(
            pady=15
        )

        card.pack_propagate(False)

        tk.Label(
            card,
            text="DANIEL BANK",
            bg="#1E40AF",
            fg="white",
            font=("Arial", 20, "bold")
        ).pack(
            anchor="w",
            padx=25,
            pady=20
        )

        tk.Label(
            card,
            text=user["card"],
            bg="#1E40AF",
            fg="white",
            font=("Arial", 20)
        ).pack(
            pady=20
        )

        tk.Label(
            card,
            text=user["name"],
            bg="#1E40AF",
            fg="white",
            font=("Arial", 12)
        ).pack(
            anchor="w",
            padx=25
        )

        tk.Label(
            frame,
            text="PIN-код: " + user["pin"],
            bg=self.bg_color,
            fg="#CBD5E1",
            font=("Arial", 13)
        ).pack(pady=10)

        self.create_button(
            frame,
            "Назад",
            self.dashboard
        ).pack(pady=20)


    # ======================================
    # ИСТОРИЯ ОПЕРАЦИЙ
    # ======================================

    def history_screen(self):

        self.clear_window()

        user = self.users[
            self.current_user
        ]

        self.title_label(
            self.root,
            "📜 История операций",
            25
        ).pack(pady=20)

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            fill="both",
            expand=True,
            padx=30
        )

        scrollbar = tk.Scrollbar(frame)

        scrollbar.pack(
            side="right",
            fill="y"
        )

        history_list = tk.Listbox(
            frame,
            bg="#273449",
            fg="white",
            font=("Arial", 12),
            yscrollcommand=scrollbar.set
        )

        history_list.pack(
            fill="both",
            expand=True
        )

        scrollbar.config(
            command=history_list.yview
        )

        for operation in user["history"]:

            history_list.insert(
                tk.END,
                operation
            )

        self.create_button(
            self.root,
            "Назад",
            self.dashboard
        ).pack(pady=15)


    # ======================================
    # НАСТРОЙКИ
    # ======================================

    def settings_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "⚙️ Настройки",
            27
        ).pack(pady=25)

        self.create_button(
            frame,
            "🔑 Изменить пароль",
            self.change_password
        ).pack(
            pady=10,
            fill="x"
        )

        self.create_button(
            frame,
            "🚫 Заблокировать карту",
            self.block_card,
            self.red_color
        ).pack(
            pady=10,
            fill="x"
        )

        self.create_button(
            frame,
            "Назад",
            self.dashboard,
            "#475569"
        ).pack(
            pady=20,
            fill="x"
        )


    # ======================================
    # ИЗМЕНЕНИЕ ПАРОЛЯ
    # ======================================

    def change_password(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "🔑 Новый пароль",
            26
        ).pack(pady=25)

        tk.Label(
            frame,
            text="Введите новый пароль",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        password_entry = self.create_entry(
            frame,
            show="*"
        )

        password_entry.pack(
            pady=15,
            ipady=8
        )

        def save_password():

            password = password_entry.get()

            if len(password) < 4:

                messagebox.showwarning(
                    "Ошибка",
                    "Минимум 4 символа!"
                )

                return

            self.users[
                self.current_user
            ]["password"] = password

            messagebox.showinfo(
                "Успешно",
                "Пароль изменён!"
            )

            self.dashboard()

        self.create_button(
            frame,
            "Сохранить пароль",
            save_password
        ).pack(pady=15)

        self.create_button(
            frame,
            "Назад",
            self.settings_screen,
            "#475569"
        ).pack()


    # ======================================
    # БЛОКИРОВКА КАРТЫ
    # ======================================

    def block_card(self):

        answer = messagebox.askyesno(
            "Блокировка",
            "Вы действительно хотите заблокировать карту?"
        )

        if answer:

            self.users[
                self.current_user
            ]["blocked"] = True

            messagebox.showinfo(
                "Карта заблокирована",
                "Карта заблокирована."
            )

            self.logout()


    # ======================================
    # ВЫХОД
    # ======================================

    def logout(self):

        self.current_user = None

        self.start_screen()


# ==========================================
# ЗАПУСК ПРОГРАММЫ
# ==========================================

if __name__ == "__main__":

    root = tk.Tk()

    app = BankApp(root)

    root.mainloop()

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import random


# ==========================================
# 🏦 БАНКОВСКАЯ СИСТЕМА
# Графический интерфейс Tkinter
# ==========================================


class BankApp:

    def __init__(self, root):

        self.root = root

        self.root.title("DANIEL BANK")
        self.root.geometry("900x650")
        self.root.resizable(False, False)

        # Цвета интерфейса
        self.bg_color = "#101827"
        self.card_color = "#1D2A3A"
        self.button_color = "#2563EB"
        self.text_color = "#FFFFFF"
        self.green_color = "#22C55E"
        self.red_color = "#EF4444"

        self.root.configure(
            bg=self.bg_color
        )

        # Данные клиентов
        self.users = {}

        # Текущий пользователь
        self.current_user = None

        # Запуск стартового окна
        self.start_screen()


    # ======================================
    # ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
    # ======================================

    def clear_window(self):

        for widget in self.root.winfo_children():

            widget.destroy()


    def create_button(
        self,
        parent,
        text,
        command,
        color=None
    ):

        if color is None:

            color = self.button_color

        return tk.Button(
            parent,
            text=text,
            command=command,
            bg=color,
            fg="white",
            font=("Arial", 12, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=10
        )


    def create_entry(
        self,
        parent,
        show=None
    ):

        return tk.Entry(
            parent,
            font=("Arial", 13),
            bg="#273449",
            fg="white",
            insertbackground="white",
            relief="flat",
            show=show
        )


    def title_label(
        self,
        parent,
        text,
        size=25
    ):

        return tk.Label(
            parent,
            text=text,
            bg=self.bg_color,
            fg=self.text_color,
            font=("Arial", size, "bold")
        )


    # ======================================
    # СТАРТОВОЕ ОКНО
    # ======================================

    def start_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        tk.Label(
            frame,
            text="🏦",
            font=("Arial", 55),
            bg=self.bg_color,
            fg="white"
        ).pack(pady=10)

        self.title_label(
            frame,
            "DANIEL BANK",
            32
        ).pack(pady=5)

        tk.Label(
            frame,
            text="Ваш учебный цифровой банк",
            bg=self.bg_color,
            fg="#94A3B8",
            font=("Arial", 13)
        ).pack(pady=5)

        self.create_button(
            frame,
            "🔐 Войти в банк",
            self.login_screen
        ).pack(
            pady=15,
            fill="x"
        )

        self.create_button(
            frame,
            "👤 Регистрация",
            self.register_screen
        ).pack(
            pady=5,
            fill="x"
        )

        tk.Label(
            frame,
            text="Учебный проект на Python",
            bg=self.bg_color,
            fg="#64748B",
            font=("Arial", 10)
        ).pack(pady=30)


    # ======================================
    # РЕГИСТРАЦИЯ
    # ======================================

    def register_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "👤 Регистрация",
            26
        ).pack(pady=20)

        tk.Label(
            frame,
            text="Имя пользователя",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        name_entry = self.create_entry(frame)

        name_entry.pack(
            pady=8,
            ipady=8
        )

        tk.Label(
            frame,
            text="Придумайте логин",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        login_entry = self.create_entry(frame)

        login_entry.pack(
            pady=8,
            ipady=8
        )

        tk.Label(
            frame,
            text="Придумайте пароль",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        password_entry = self.create_entry(
            frame,
            show="*"
        )

        password_entry.pack(
            pady=8,
            ipady=8
        )

        def register():

            name = name_entry.get().strip()
            login = login_entry.get().strip()
            password = password_entry.get()

            if not name or not login or not password:

                messagebox.showwarning(
                    "Ошибка",
                    "Заполните все поля!"
                )

                return

            if login in self.users:

                messagebox.showerror(
                    "Ошибка",
                    "Такой логин уже существует!"
                )

                return

            if len(password) < 4:

                messagebox.showwarning(
                    "Пароль",
                    "Пароль должен содержать минимум 4 символа."
                )

                return

            self.users[login] = {

                "name": name,

                "password": password,

                "balance": 1000.0,

                "card": self.generate_card(),

                "pin": str(
                    random.randint(1000, 9999)
                ),

                "history": [

                    "Счёт открыт. Начальный баланс: 1000 сом"

                ],

                "blocked": False

            }

            messagebox.showinfo(
                "Успешно",
                "Регистрация завершена!\n"
                "На счёт начислено 1000 сом."
            )

            self.login_screen()

        self.create_button(
            frame,
            "Зарегистрироваться",
            register
        ).pack(
            pady=15,
            fill="x"
        )

        self.create_button(
            frame,
            "Назад",
            self.start_screen,
            "#475569"
        ).pack(
            fill="x"
        )


    def generate_card(self):

        return " ".join(

            str(
                random.randint(1000, 9999)
            )

            for _ in range(4)

        )


    # ======================================
    # ВХОД
    # ======================================

    def login_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "🔐 Вход в банк",
            27
        ).pack(pady=20)

        tk.Label(
            frame,
            text="Логин",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        login_entry = self.create_entry(frame)

        login_entry.pack(
            pady=8,
            ipady=8
        )

        tk.Label(
            frame,
            text="Пароль",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        password_entry = self.create_entry(
            frame,
            show="*"
        )

        password_entry.pack(
            pady=8,
            ipady=8
        )

        def login():

            login = login_entry.get().strip()
            password = password_entry.get()

            if login not in self.users:

                messagebox.showerror(
                    "Ошибка",
                    "Пользователь не найден!"
                )

                return

            user = self.users[login]

            if user["password"] != password:

                messagebox.showerror(
                    "Ошибка",
                    "Неверный пароль!"
                )

                return

            if user["blocked"]:

                messagebox.showerror(
                    "Карта заблокирована",
                    "Обратитесь в банк."
                )

                return

            self.current_user = login

            self.dashboard()

        self.create_button(
            frame,
            "Войти",
            login
        ).pack(
            pady=15,
            fill="x"
        )

        self.create_button(
            frame,
            "Назад",
            self.start_screen,
            "#475569"
        ).pack(
            fill="x"
        )


    # ======================================
    # ГЛАВНОЕ МЕНЮ
    # ======================================

    def dashboard(self):

        self.clear_window()

        user = self.users[
            self.current_user
        ]

        # Верхняя панель
        top = tk.Frame(
            self.root,
            bg="#172235",
            height=75
        )

        top.pack(
            fill="x"
        )

        tk.Label(
            top,
            text="🏦 DANIEL BANK",
            bg="#172235",
            fg="white",
            font=("Arial", 22, "bold")
        ).pack(
            side="left",
            padx=25,
            pady=20
        )

        tk.Label(
            top,
            text=f"👤 {user['name']}",
            bg="#172235",
            fg="#CBD5E1",
            font=("Arial", 12)
        ).pack(
            side="right",
            padx=25
        )

        # Основная область
        main = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        main.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=25
        )

        tk.Label(
            main,
            text="Главная страница",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 24, "bold")
        ).pack(
            anchor="w"
        )

        # Карточка баланса
        balance_card = tk.Frame(
            main,
            bg=self.card_color,
            height=150
        )

        balance_card.pack(
            fill="x",
            pady=20
        )

        tk.Label(
            balance_card,
            text="Текущий баланс",
            bg=self.card_color,
            fg="#94A3B8",
            font=("Arial", 12)
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 5)
        )

        balance_label = tk.Label(
            balance_card,
            text=f"{user['balance']:,.2f} сом",
            bg=self.card_color,
            fg=self.green_color,
            font=("Arial", 30, "bold")
        )

        balance_label.pack(
            anchor="w",
            padx=25
        )

        # Кнопки меню
        buttons = tk.Frame(
            main,
            bg=self.bg_color
        )

        buttons.pack(
            fill="both",
            expand=True
        )

        menu_items = [

            ("💰 Баланс", self.balance_screen),

            ("➕ Пополнить", self.deposit_screen),

            ("➖ Снять деньги", self.withdraw_screen),

            ("🔄 Перевод", self.transfer_screen),

            ("💳 Моя карта", self.card_screen),

            ("📜 История", self.history_screen),

            ("⚙️ Настройки", self.settings_screen),

            ("🚪 Выйти", self.logout)

        ]

        for index, (text, command) in enumerate(
            menu_items
        ):

            row = index // 2
            col = index % 2

            button = self.create_button(
                buttons,
                text,
                command
            )

            button.grid(
                row=row,
                column=col,
                padx=8,
                pady=8,
                sticky="nsew"
            )

        for i in range(4):

            buttons.rowconfigure(
                i,
                weight=1
            )

        buttons.columnconfigure(
            0,
            weight=1
        )

        buttons.columnconfigure(
            1,
            weight=1
        )


    # ======================================
    # БАЛАНС
    # ======================================

    def balance_screen(self):

        self.clear_window()

        user = self.users[
            self.current_user
        ]

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "💰 Ваш баланс",
            28
        ).pack(pady=25)

        tk.Label(
            frame,
            text=f"{user['balance']:,.2f} сом",
            bg=self.bg_color,
            fg=self.green_color,
            font=("Arial", 38, "bold")
        ).pack(pady=20)

        tk.Label(
            frame,
            text="Доступные средства",
            bg=self.bg_color,
            fg="#94A3B8",
            font=("Arial", 13)
        ).pack()

        self.create_button(
            frame,
            "Назад в меню",
            self.dashboard
        ).pack(
            pady=40
        )


    # ======================================
    # ПОПОЛНЕНИЕ
    # ======================================

    def deposit_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "➕ Пополнение счёта",
            26
        ).pack(pady=25)

        tk.Label(
            frame,
            text="Введите сумму в сомах",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 13)
        ).pack()

        amount_entry = self.create_entry(frame)

        amount_entry.pack(
            pady=15,
            ipady=10
        )

        def deposit():

            try:

                amount = float(
                    amount_entry.get()
                )

                if amount <= 0:

                    raise ValueError

                user = self.users[
                    self.current_user
                ]

                user["balance"] += amount

                user["history"].append(

                    f"Пополнение: +{amount:.2f} сом"

                )

                messagebox.showinfo(
                    "Успешно",
                    f"Пополнено на {amount:.2f} сом"
                )

                self.dashboard()

            except ValueError:

                messagebox.showerror(
                    "Ошибка",
                    "Введите правильную сумму!"
                )

        self.create_button(
            frame,
            "Пополнить",
            deposit
        ).pack(
            pady=15
        )

        self.create_button(
            frame,
            "Назад",
            self.dashboard,
            "#475569"
        ).pack()


    # ======================================
    # СНЯТИЕ
    # ======================================

    def withdraw_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "➖ Снятие денег",
            26
        ).pack(pady=25)

        tk.Label(
            frame,
            text="Введите сумму",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 13)
        ).pack()

        amount_entry = self.create_entry(frame)

        amount_entry.pack(
            pady=15,
            ipady=10
        )

        def withdraw():

            try:

                amount = float(
                    amount_entry.get()
                )

                user = self.users[
                    self.current_user
                ]

                if amount <= 0:

                    raise ValueError

                if amount > user["balance"]:

                    messagebox.showerror(
                        "Ошибка",
                        "Недостаточно средств!"
                    )

                    return

                user["balance"] -= amount

                user["history"].append(

                    f"Снятие: -{amount:.2f} сом"

                )

                messagebox.showinfo(
                    "Успешно",
                    "Деньги сняты!"
                )

                self.dashboard()

            except ValueError:

                messagebox.showerror(
                    "Ошибка",
                    "Введите правильную сумму!"
                )

        self.create_button(
            frame,
            "Снять деньги",
            withdraw
        ).pack(
            pady=15
        )

        self.create_button(
            frame,
            "Назад",
            self.dashboard,
            "#475569"
        ).pack()


    # ======================================
    # ПЕРЕВОД
    # ======================================

    def transfer_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "🔄 Перевод денег",
            26
        ).pack(pady=25)

        tk.Label(
            frame,
            text="Логин получателя",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        recipient_entry = self.create_entry(frame)

        recipient_entry.pack(
            pady=10,
            ipady=8
        )

        tk.Label(
            frame,
            text="Сумма перевода",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        amount_entry = self.create_entry(frame)

        amount_entry.pack(
            pady=10,
            ipady=8
        )

        def transfer():

            recipient = recipient_entry.get().strip()

            try:

                amount = float(
                    amount_entry.get()
                )

                if amount <= 0:

                    raise ValueError

                if recipient not in self.users:

                    messagebox.showerror(
                        "Ошибка",
                        "Получатель не найден!"
                    )

                    return

                if recipient == self.current_user:

                    messagebox.showerror(
                        "Ошибка",
                        "Нельзя переводить самому себе!"
                    )

                    return

                sender = self.users[
                    self.current_user
                ]

                receiver = self.users[
                    recipient
                ]

                if amount > sender["balance"]:

                    messagebox.showerror(
                        "Ошибка",
                        "Недостаточно средств!"
                    )

                    return

                sender["balance"] -= amount

                receiver["balance"] += amount

                sender["history"].append(

                    f"Перевод пользователю {recipient}: "
                    f"-{amount:.2f} сом"

                )

                receiver["history"].append(

                    f"Получен перевод от "
                    f"{self.current_user}: "
                    f"+{amount:.2f} сом"

                )

                messagebox.showinfo(
                    "Успешно",
                    "Перевод выполнен!"
                )

                self.dashboard()

            except ValueError:

                messagebox.showerror(
                    "Ошибка",
                    "Введите правильную сумму!"
                )

        self.create_button(
            frame,
            "Отправить перевод",
            transfer
        ).pack(
            pady=15
        )

        self.create_button(
            frame,
            "Назад",
            self.dashboard,
            "#475569"
        ).pack()


    # ======================================
    # БАНКОВСКАЯ КАРТА
    # ======================================

    def card_screen(self):

        self.clear_window()

        user = self.users[
            self.current_user
        ]

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "💳 Моя банковская карта",
            25
        ).pack(pady=25)

        card = tk.Frame(
            frame,
            bg="#1E40AF",
            width=500,
            height=240
        )

        card.pack(
            pady=15
        )

        card.pack_propagate(False)

        tk.Label(
            card,
            text="DANIEL BANK",
            bg="#1E40AF",
            fg="white",
            font=("Arial", 20, "bold")
        ).pack(
            anchor="w",
            padx=25,
            pady=20
        )

        tk.Label(
            card,
            text=user["card"],
            bg="#1E40AF",
            fg="white",
            font=("Arial", 20)
        ).pack(
            pady=20
        )

        tk.Label(
            card,
            text=user["name"],
            bg="#1E40AF",
            fg="white",
            font=("Arial", 12)
        ).pack(
            anchor="w",
            padx=25
        )

        tk.Label(
            frame,
            text="PIN-код: " + user["pin"],
            bg=self.bg_color,
            fg="#CBD5E1",
            font=("Arial", 13)
        ).pack(pady=10)

        self.create_button(
            frame,
            "Назад",
            self.dashboard
        ).pack(pady=20)


    # ======================================
    # ИСТОРИЯ ОПЕРАЦИЙ
    # ======================================

    def history_screen(self):

        self.clear_window()

        user = self.users[
            self.current_user
        ]

        self.title_label(
            self.root,
            "📜 История операций",
            25
        ).pack(pady=20)

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            fill="both",
            expand=True,
            padx=30
        )

        scrollbar = tk.Scrollbar(frame)

        scrollbar.pack(
            side="right",
            fill="y"
        )

        history_list = tk.Listbox(
            frame,
            bg="#273449",
            fg="white",
            font=("Arial", 12),
            yscrollcommand=scrollbar.set
        )

        history_list.pack(
            fill="both",
            expand=True
        )

        scrollbar.config(
            command=history_list.yview
        )

        for operation in user["history"]:

            history_list.insert(
                tk.END,
                operation
            )

        self.create_button(
            self.root,
            "Назад",
            self.dashboard
        ).pack(pady=15)


    # ======================================
    # НАСТРОЙКИ
    # ======================================

    def settings_screen(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "⚙️ Настройки",
            27
        ).pack(pady=25)

        self.create_button(
            frame,
            "🔑 Изменить пароль",
            self.change_password
        ).pack(
            pady=10,
            fill="x"
        )

        self.create_button(
            frame,
            "🚫 Заблокировать карту",
            self.block_card,
            self.red_color
        ).pack(
            pady=10,
            fill="x"
        )

        self.create_button(
            frame,
            "Назад",
            self.dashboard,
            "#475569"
        ).pack(
            pady=20,
            fill="x"
        )


    # ======================================
    # ИЗМЕНЕНИЕ ПАРОЛЯ
    # ======================================

    def change_password(self):

        self.clear_window()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            expand=True
        )

        self.title_label(
            frame,
            "🔑 Новый пароль",
            26
        ).pack(pady=25)

        tk.Label(
            frame,
            text="Введите новый пароль",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12)
        ).pack()

        password_entry = self.create_entry(
            frame,
            show="*"
        )

        password_entry.pack(
            pady=15,
            ipady=8
        )

        def save_password():

            password = password_entry.get()

            if len(password) < 4:

                messagebox.showwarning(
                    "Ошибка",
                    "Минимум 4 символа!"
                )

                return

            self.users[
                self.current_user
            ]["password"] = password

            messagebox.showinfo(
                "Успешно",
                "Пароль изменён!"
            )

            self.dashboard()

        self.create_button(
            frame,
            "Сохранить пароль",
            save_password
        ).pack(pady=15)

        self.create_button(
            frame,
            "Назад",
            self.settings_screen,
            "#475569"
        ).pack()


    # ======================================
    # БЛОКИРОВКА КАРТЫ
    # ======================================

    def block_card(self):

        answer = messagebox.askyesno(
            "Блокировка",
            "Вы действительно хотите заблокировать карту?"
        )

        if answer:

            self.users[
                self.current_user
            ]["blocked"] = True

            messagebox.showinfo(
                "Карта заблокирована",
                "Карта заблокирована."
            )

            self.logout()


    # ======================================
    # ВЫХОД
    # ======================================

    def logout(self):

        self.current_user = None

        self.start_screen()


# ==========================================
# ЗАПУСК ПРОГРАММЫ
# ==========================================

if __name__ == "__main__":

    root = tk.Tk()

    app = BankApp(root)

    root.mainloop()