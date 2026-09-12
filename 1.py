from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "my_secret_key"

# Список пользователей
users = {
    "admin": "1234"
}

# Гаджеты магазина
gadgets = [
    {
        "id": 1,
        "name": "iPhone 15",
        "price": 65000,
        "emoji": "📱",
        "description": "Современный смартфон Apple"
    },
    {
        "id": 2,
        "name": "Samsung Galaxy S24",
        "price": 55000,
        "emoji": "📱",
        "description": "Мощный Android смартфон"
    },
    {
        "id": 3,
        "name": "MacBook Air",
        "price": 95000,
        "emoji": "💻",
        "description": "Ноутбук для работы и учёбы"
    },
    {
        "id": 4,
        "name": "AirPods Pro",
        "price": 18000,
        "emoji": "🎧",
        "description": "Беспроводные наушники"
    },
    {
        "id": 5,
        "name": "Apple Watch",
        "price": 30000,
        "emoji": "⌚",
        "description": "Умные часы Apple"
    },
    {
        "id": 6,
        "name": "PlayStation 5",
        "price": 55000,
        "emoji": "🎮",
        "description": "Игровая приставка"
    }
]


# Главная страница
@app.route("/")
def home():
    return render_template(
        "index.html",
        gadgets=gadgets,
        username=session.get("username")
    )


# Страница входа
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:

            session["username"] = username

            return redirect("/")

        return "Неверный логин или пароль!"

    return render_template("login.html")


# Регистрация
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username in users:

            return "Такой пользователь уже существует!"

        users[username] = password

        return redirect("/login")

    return render_template("register.html")


# Выход
@app.route("/logout")
def logout():

    session.pop("username", None)

    return redirect("/")


# Добавление в корзину
@app.route("/add/<int:gadget_id>")
def add_to_cart(gadget_id):

    if "cart" not in session:
        session["cart"] = []

    cart = session["cart"]

    cart.append(gadget_id)

    session["cart"] = cart

    return redirect("/")


# Корзина
@app.route("/cart")
def cart():

    cart_ids = session.get("cart", [])

    selected_gadgets = []

    for gadget in gadgets:

        if gadget["id"] in cart_ids:
            selected_gadgets.append(gadget)

    total = sum(item["price"] for item in selected_gadgets)

    return render_template(
        "cart.html",
        gadgets=selected_gadgets,
        total=total
    )


# Запуск сайта
if __name__ == "__main__":

    app.run(debug=True)

    from flask import Flask, render_template, request, redirect, session

    app = Flask(__name__)

    app.secret_key = "my_secret_key"

    # Список пользователей
    users = {
        "admin": "1234"
    }

    # Гаджеты магазина
    gadgets = [
        {
            "id": 1,
            "name": "iPhone 15",
            "price": 65000,
            "emoji": "📱",
            "description": "Современный смартфон Apple"
        },
        {
            "id": 2,
            "name": "Samsung Galaxy S24",
            "price": 55000,
            "emoji": "📱",
            "description": "Мощный Android смартфон"
        },
        {
            "id": 3,
            "name": "MacBook Air",
            "price": 95000,
            "emoji": "💻",
            "description": "Ноутбук для работы и учёбы"
        },
        {
            "id": 4,
            "name": "AirPods Pro",
            "price": 18000,
            "emoji": "🎧",
            "description": "Беспроводные наушники"
        },
        {
            "id": 5,
            "name": "Apple Watch",
            "price": 30000,
            "emoji": "⌚",
            "description": "Умные часы Apple"
        },
        {
            "id": 6,
            "name": "PlayStation 5",
            "price": 55000,
            "emoji": "🎮",
            "description": "Игровая приставка"
        }
    ]


    # Главная страница
    @app.route("/")
    def home():
        return render_template(
            "index.html",
            gadgets=gadgets,
            username=session.get("username")
        )


    # Страница входа
    @app.route("/login", methods=["GET", "POST"])
    def login():

        if request.method == "POST":

            username = request.form["username"]
            password = request.form["password"]

            if username in users and users[username] == password:
                session["username"] = username

                return redirect("/")

            return "Неверный логин или пароль!"

        return render_template("login.html")


    # Регистрация
    @app.route("/register", methods=["GET", "POST"])
    def register():

        if request.method == "POST":

            username = request.form["username"]
            password = request.form["password"]

            if username in users:
                return "Такой пользователь уже существует!"

            users[username] = password

            return redirect("/login")

        return render_template("register.html")


    # Выход
    @app.route("/logout")
    def logout():

        session.pop("username", None)

        return redirect("/")


    # Добавление в корзину
    @app.route("/add/<int:gadget_id>")
    def add_to_cart(gadget_id):

        if "cart" not in session:
            session["cart"] = []

        cart = session["cart"]

        cart.append(gadget_id)

        session["cart"] = cart

        return redirect("/")


    # Корзина
    @app.route("/cart")
    def cart():

        cart_ids = session.get("cart", [])

        selected_gadgets = []

        for gadget in gadgets:

            if gadget["id"] in cart_ids:
                selected_gadgets.append(gadget)

        total = sum(item["price"] for item in selected_gadgets)

        return render_template(
            "cart.html",
            gadgets=selected_gadgets,
            total=total
        )


    # Запуск сайта
    if __name__ == "__main__":
        app.run(debug=True)
        from flask import Flask, render_template, request, redirect, session

        app = Flask(__name__)

        app.secret_key = "my_secret_key"

        # Список пользователей
        users = {
            "admin": "1234"
        }

        # Гаджеты магазина
        gadgets = [
            {
                "id": 1,
                "name": "iPhone 15",
                "price": 65000,
                "emoji": "📱",
                "description": "Современный смартфон Apple"
            },
            {
                "id": 2,
                "name": "Samsung Galaxy S24",
                "price": 55000,
                "emoji": "📱",
                "description": "Мощный Android смартфон"
            },
            {
                "id": 3,
                "name": "MacBook Air",
                "price": 95000,
                "emoji": "💻",
                "description": "Ноутбук для работы и учёбы"
            },
            {
                "id": 4,
                "name": "AirPods Pro",
                "price": 18000,
                "emoji": "🎧",
                "description": "Беспроводные наушники"
            },
            {
                "id": 5,
                "name": "Apple Watch",
                "price": 30000,
                "emoji": "⌚",
                "description": "Умные часы Apple"
            },
            {
                "id": 6,
                "name": "PlayStation 5",
                "price": 55000,
                "emoji": "🎮",
                "description": "Игровая приставка"
            }
        ]


        # Главная страница
        @app.route("/")
        def home():
            return render_template(
                "index.html",
                gadgets=gadgets,
                username=session.get("username")
            )


        # Страница входа
        @app.route("/login", methods=["GET", "POST"])
        def login():

            if request.method == "POST":

                username = request.form["username"]
                password = request.form["password"]

                if username in users and users[username] == password:
                    session["username"] = username

                    return redirect("/")

                return "Неверный логин или пароль!"

            return render_template("login.html")


        # Регистрация
        @app.route("/register", methods=["GET", "POST"])
        def register():

            if request.method == "POST":

                username = request.form["username"]
                password = request.form["password"]

                if username in users:
                    return "Такой пользователь уже существует!"

                users[username] = password

                return redirect("/login")

            return render_template("register.html")


        # Выход
        @app.route("/logout")
        def logout():

            session.pop("username", None)

            return redirect("/")


        # Добавление в корзину
        @app.route("/add/<int:gadget_id>")
        def add_to_cart(gadget_id):

            if "cart" not in session:
                session["cart"] = []

            cart = session["cart"]

            cart.append(gadget_id)

            session["cart"] = cart

            return redirect("/")


        # Корзина
        @app.route("/cart")
        def cart():

            cart_ids = session.get("cart", [])

            selected_gadgets = []

            for gadget in gadgets:

                if gadget["id"] in cart_ids:
                    selected_gadgets.append(gadget)

            total = sum(item["price"] for item in selected_gadgets)

            return render_template(
                "cart.html",
                gadgets=selected_gadgets,
                total=total
            )


        # Запуск сайта
        if __name__ == "__main__":
            app.run(debug=True)
            from flask import Flask, render_template, request, redirect, session

            app = Flask(__name__)

            app.secret_key = "my_secret_key"

            # Список пользователей
            users = {
                "admin": "1234"
            }

            # Гаджеты магазина
            gadgets = [
                {
                    "id": 1,
                    "name": "iPhone 15",
                    "price": 65000,
                    "emoji": "📱",
                    "description": "Современный смартфон Apple"
                },
                {
                    "id": 2,
                    "name": "Samsung Galaxy S24",
                    "price": 55000,
                    "emoji": "📱",
                    "description": "Мощный Android смартфон"
                },
                {
                    "id": 3,
                    "name": "MacBook Air",
                    "price": 95000,
                    "emoji": "💻",
                    "description": "Ноутбук для работы и учёбы"
                },
                {
                    "id": 4,
                    "name": "AirPods Pro",
                    "price": 18000,
                    "emoji": "🎧",
                    "description": "Беспроводные наушники"
                },
                {
                    "id": 5,
                    "name": "Apple Watch",
                    "price": 30000,
                    "emoji": "⌚",
                    "description": "Умные часы Apple"
                },
                {
                    "id": 6,
                    "name": "PlayStation 5",
                    "price": 55000,
                    "emoji": "🎮",
                    "description": "Игровая приставка"
                }
            ]


            # Главная страница
            @app.route("/")
            def home():
                return render_template(
                    "index.html",
                    gadgets=gadgets,
                    username=session.get("username")
                )


            # Страница входа
            @app.route("/login", methods=["GET", "POST"])
            def login():

                if request.method == "POST":

                    username = request.form["username"]
                    password = request.form["password"]

                    if username in users and users[username] == password:
                        session["username"] = username

                        return redirect("/")

                    return "Неверный логин или пароль!"

                return render_template("login.html")


            # Регистрация
            @app.route("/register", methods=["GET", "POST"])
            def register():

                if request.method == "POST":

                    username = request.form["username"]
                    password = request.form["password"]

                    if username in users:
                        return "Такой пользователь уже существует!"

                    users[username] = password

                    return redirect("/login")

                return render_template("register.html")


            # Выход
            @app.route("/logout")
            def logout():

                session.pop("username", None)

                return redirect("/")


            # Добавление в корзину
            @app.route("/add/<int:gadget_id>")
            def add_to_cart(gadget_id):

                if "cart" not in session:
                    session["cart"] = []

                cart = session["cart"]

                cart.append(gadget_id)

                session["cart"] = cart

                return redirect("/")


            # Корзина
            @app.route("/cart")
            def cart():

                cart_ids = session.get("cart", [])

                selected_gadgets = []

                for gadget in gadgets:

                    if gadget["id"] in cart_ids:
                        selected_gadgets.append(gadget)

                total = sum(item["price"] for item in selected_gadgets)

                return render_template(
                    "cart.html",
                    gadgets=selected_gadgets,
                    total=total
                )


            # Запуск сайта
            if __name__ == "__main__":
                app.run(debug=True)
                from flask import Flask, render_template, request, redirect, session

                app = Flask(__name__)

                app.secret_key = "my_secret_key"

                # Список пользователей
                users = {
                    "admin": "1234"
                }

                # Гаджеты магазина
                gadgets = [
                    {
                        "id": 1,
                        "name": "iPhone 15",
                        "price": 65000,
                        "emoji": "📱",
                        "description": "Современный смартфон Apple"
                    },
                    {
                        "id": 2,
                        "name": "Samsung Galaxy S24",
                        "price": 55000,
                        "emoji": "📱",
                        "description": "Мощный Android смартфон"
                    },
                    {
                        "id": 3,
                        "name": "MacBook Air",
                        "price": 95000,
                        "emoji": "💻",
                        "description": "Ноутбук для работы и учёбы"
                    },
                    {
                        "id": 4,
                        "name": "AirPods Pro",
                        "price": 18000,
                        "emoji": "🎧",
                        "description": "Беспроводные наушники"
                    },
                    {
                        "id": 5,
                        "name": "Apple Watch",
                        "price": 30000,
                        "emoji": "⌚",
                        "description": "Умные часы Apple"
                    },
                    {
                        "id": 6,
                        "name": "PlayStation 5",
                        "price": 55000,
                        "emoji": "🎮",
                        "description": "Игровая приставка"
                    }
                ]


                # Главная страница
                @app.route("/")
                def home():
                    return render_template(
                        "index.html",
                        gadgets=gadgets,
                        username=session.get("username")
                    )


                # Страница входа
                @app.route("/login", methods=["GET", "POST"])
                def login():

                    if request.method == "POST":

                        username = request.form["username"]
                        password = request.form["password"]

                        if username in users and users[username] == password:
                            session["username"] = username

                            return redirect("/")

                        return "Неверный логин или пароль!"

                    return render_template("login.html")


                # Регистрация
                @app.route("/register", methods=["GET", "POST"])
                def register():

                    if request.method == "POST":

                        username = request.form["username"]
                        password = request.form["password"]

                        if username in users:
                            return "Такой пользователь уже существует!"

                        users[username] = password

                        return redirect("/login")

                    return render_template("register.html")


                # Выход
                @app.route("/logout")
                def logout():

                    session.pop("username", None)

                    return redirect("/")


                # Добавление в корзину
                @app.route("/add/<int:gadget_id>")
                def add_to_cart(gadget_id):

                    if "cart" not in session:
                        session["cart"] = []

                    cart = session["cart"]

                    cart.append(gadget_id)

                    session["cart"] = cart

                    return redirect("/")


                # Корзина
                @app.route("/cart")
                def cart():

                    cart_ids = session.get("cart", [])

                    selected_gadgets = []

                    for gadget in gadgets:

                        if gadget["id"] in cart_ids:
                            selected_gadgets.append(gadget)

                    total = sum(item["price"] for item in selected_gadgets)

                    return render_template(
                        "cart.html",
                        gadgets=selected_gadgets,
                        total=total
                    )


                # Запуск сайта
                if __name__ == "__main__":
                    app.run(debug=True)
                    from flask import Flask, render_template, request, redirect, session

                    app = Flask(__name__)

                    app.secret_key = "my_secret_key"

                    # Список пользователей
                    users = {
                        "admin": "1234"
                    }

                    # Гаджеты магазина
                    gadgets = [
                        {
                            "id": 1,
                            "name": "iPhone 15",
                            "price": 65000,
                            "emoji": "📱",
                            "description": "Современный смартфон Apple"
                        },
                        {
                            "id": 2,
                            "name": "Samsung Galaxy S24",
                            "price": 55000,
                            "emoji": "📱",
                            "description": "Мощный Android смартфон"
                        },
                        {
                            "id": 3,
                            "name": "MacBook Air",
                            "price": 95000,
                            "emoji": "💻",
                            "description": "Ноутбук для работы и учёбы"
                        },
                        {
                            "id": 4,
                            "name": "AirPods Pro",
                            "price": 18000,
                            "emoji": "🎧",
                            "description": "Беспроводные наушники"
                        },
                        {
                            "id": 5,
                            "name": "Apple Watch",
                            "price": 30000,
                            "emoji": "⌚",
                            "description": "Умные часы Apple"
                        },
                        {
                            "id": 6,
                            "name": "PlayStation 5",
                            "price": 55000,
                            "emoji": "🎮",
                            "description": "Игровая приставка"
                        }
                    ]


                    # Главная страница
                    @app.route("/")
                    def home():
                        return render_template(
                            "index.html",
                            gadgets=gadgets,
                            username=session.get("username")
                        )


                    # Страница входа
                    @app.route("/login", methods=["GET", "POST"])
                    def login():

                        if request.method == "POST":

                            username = request.form["username"]
                            password = request.form["password"]

                            if username in users and users[username] == password:
                                session["username"] = username

                                return redirect("/")

                            return "Неверный логин или пароль!"

                        return render_template("login.html")


                    # Регистрация
                    @app.route("/register", methods=["GET", "POST"])
                    def register():

                        if request.method == "POST":

                            username = request.form["username"]
                            password = request.form["password"]

                            if username in users:
                                return "Такой пользователь уже существует!"

                            users[username] = password

                            return redirect("/login")

                        return render_template("register.html")


                    # Выход
                    @app.route("/logout")
                    def logout():

                        session.pop("username", None)

                        return redirect("/")


                    # Добавление в корзину
                    @app.route("/add/<int:gadget_id>")
                    def add_to_cart(gadget_id):

                        if "cart" not in session:
                            session["cart"] = []

                        cart = session["cart"]

                        cart.append(gadget_id)

                        session["cart"] = cart

                        return redirect("/")


                    # Корзина
                    @app.route("/cart")
                    def cart():

                        cart_ids = session.get("cart", [])

                        selected_gadgets = []

                        for gadget in gadgets:

                            if gadget["id"] in cart_ids:
                                selected_gadgets.append(gadget)

                        total = sum(item["price"] for item in selected_gadgets)

                        return render_template(
                            "cart.html",
                            gadgets=selected_gadgets,
                            total=total
                        )


                    # Запуск сайта
                    if __name__ == "__main__":
                        app.run(debug=True)
                        from flask import Flask, render_template, request, redirect, session

                        app = Flask(__name__)

                        app.secret_key = "my_secret_key"

                        # Список пользователей
                        users = {
                            "admin": "1234"
                        }

                        # Гаджеты магазина
                        gadgets = [
                            {
                                "id": 1,
                                "name": "iPhone 15",
                                "price": 65000,
                                "emoji": "📱",
                                "description": "Современный смартфон Apple"
                            },
                            {
                                "id": 2,
                                "name": "Samsung Galaxy S24",
                                "price": 55000,
                                "emoji": "📱",
                                "description": "Мощный Android смартфон"
                            },
                            {
                                "id": 3,
                                "name": "MacBook Air",
                                "price": 95000,
                                "emoji": "💻",
                                "description": "Ноутбук для работы и учёбы"
                            },
                            {
                                "id": 4,
                                "name": "AirPods Pro",
                                "price": 18000,
                                "emoji": "🎧",
                                "description": "Беспроводные наушники"
                            },
                            {
                                "id": 5,
                                "name": "Apple Watch",
                                "price": 30000,
                                "emoji": "⌚",
                                "description": "Умные часы Apple"
                            },
                            {
                                "id": 6,
                                "name": "PlayStation 5",
                                "price": 55000,
                                "emoji": "🎮",
                                "description": "Игровая приставка"
                            }
                        ]


                        # Главная страница
                        @app.route("/")
                        def home():
                            return render_template(
                                "index.html",
                                gadgets=gadgets,
                                username=session.get("username")
                            )


                        # Страница входа
                        @app.route("/login", methods=["GET", "POST"])
                        def login():

                            if request.method == "POST":

                                username = request.form["username"]
                                password = request.form["password"]

                                if username in users and users[username] == password:
                                    session["username"] = username

                                    return redirect("/")

                                return "Неверный логин или пароль!"

                            return render_template("login.html")


                        # Регистрация
                        @app.route("/register", methods=["GET", "POST"])
                        def register():

                            if request.method == "POST":

                                username = request.form["username"]
                                password = request.form["password"]

                                if username in users:
                                    return "Такой пользователь уже существует!"

                                users[username] = password

                                return redirect("/login")

                            return render_template("register.html")


                        # Выход
                        @app.route("/logout")
                        def logout():

                            session.pop("username", None)

                            return redirect("/")


                        # Добавление в корзину
                        @app.route("/add/<int:gadget_id>")
                        def add_to_cart(gadget_id):

                            if "cart" not in session:
                                session["cart"] = []

                            cart = session["cart"]

                            cart.append(gadget_id)

                            session["cart"] = cart

                            return redirect("/")


                        # Корзина
                        @app.route("/cart")
                        def cart():

                            cart_ids = session.get("cart", [])

                            selected_gadgets = []

                            for gadget in gadgets:

                                if gadget["id"] in cart_ids:
                                    selected_gadgets.append(gadget)

                            total = sum(item["price"] for item in selected_gadgets)

                            return render_template(
                                "cart.html",
                                gadgets=selected_gadgets,
                                total=total
                            )


from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "my_secret_key"

# Список пользователей
users = {
    "admin": "1234"
}

# Гаджеты магазина
gadgets = [
    {
        "id": 1,
        "name": "iPhone 15",
        "price": 65000,
        "emoji": "📱",
        "description": "Современный смартфон Apple"
    },
    {
        "id": 2,
        "name": "Samsung Galaxy S24",
        "price": 55000,
        "emoji": "📱",
        "description": "Мощный Android смартфон"
    },
    {
        "id": 3,
        "name": "MacBook Air",
        "price": 95000,
        "emoji": "💻",
        "description": "Ноутбук для работы и учёбы"
    },
    {
        "id": 4,
        "name": "AirPods Pro",
        "price": 18000,
        "emoji": "🎧",
        "description": "Беспроводные наушники"
    },
    {
        "id": 5,
        "name": "Apple Watch",
        "price": 30000,
        "emoji": "⌚",
        "description": "Умные часы Apple"
    },
    {
        "id": 6,
        "name": "PlayStation 5",
        "price": 55000,
        "emoji": "🎮",
        "description": "Игровая приставка"
    }
]


# Главная страница
@app.route("/")
def home():
    return render_template(
        "index.html",
        gadgets=gadgets,
        username=session.get("username")
    )


# Страница входа
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:

            session["username"] = username

            return redirect("/")

        return "Неверный логин или пароль!"

    return render_template("login.html")


# Регистрация
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username in users:

            return "Такой пользователь уже существует!"

        users[username] = password

        return redirect("/login")

    return render_template("register.html")


# Выход
@app.route("/logout")
def logout():

    session.pop("username", None)

    return redirect("/")


# Добавление в корзину
@app.route("/add/<int:gadget_id>")
def add_to_cart(gadget_id):

    if "cart" not in session:
        session["cart"] = []

    cart = session["cart"]

    cart.append(gadget_id)

    session["cart"] = cart

    return redirect("/")


# Корзина
@app.route("/cart")
def cart():

    cart_ids = session.get("cart", [])

    selected_gadgets = []

    for gadget in gadgets:

        if gadget["id"] in cart_ids:
            selected_gadgets.append(gadget)

    total = sum(item["price"] for item in selected_gadgets)

    return render_template(
        "cart.html",
        gadgets=selected_gadgets,
        total=total
    )


# Запуск сайта
if __name__ == "__main__":

    app.run(debug=True)from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "my_secret_key"

# Список пользователей
users = {
    "admin": "1234"
}

# Гаджеты магазина
gadgets = [
    {
        "id": 1,
        "name": "iPhone 15",
        "price": 65000,
        "emoji": "📱",
        "description": "Современный смартфон Apple"
    },
    {
        "id": 2,
        "name": "Samsung Galaxy S24",
        "price": 55000,
        "emoji": "📱",
        "description": "Мощный Android смартфон"
    },
    {
        "id": 3,
        "name": "MacBook Air",
        "price": 95000,
        "emoji": "💻",
        "description": "Ноутбук для работы и учёбы"
    },
    {
        "id": 4,
        "name": "AirPods Pro",
        "price": 18000,
        "emoji": "🎧",
        "description": "Беспроводные наушники"
    },
    {
        "id": 5,
        "name": "Apple Watch",
        "price": 30000,
        "emoji": "⌚",
        "description": "Умные часы Apple"
    },
    {
        "id": 6,
        "name": "PlayStation 5",
        "price": 55000,
        "emoji": "🎮",
        "description": "Игровая приставка"
    }
]


# Главная страница
@app.route("/")
def home():
    return render_template(
        "index.html",
        gadgets=gadgets,
        username=session.get("username")
    )


# Страница входа
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:

            session["username"] = username

            return redirect("/")

        return "Неверный логин или пароль!"

    return render_template("login.html")


# Регистрация
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username in users:

            return "Такой пользователь уже существует!"

        users[username] = password

        return redirect("/login")

    return render_template("register.html")


# Выход
@app.route("/logout")
def logout():

    session.pop("username", None)

    return redirect("/")


# Добавление в корзину
@app.route("/add/<int:gadget_id>")
def add_to_cart(gadget_id):

    if "cart" not in session:
        session["cart"] = []

    cart = session["cart"]

    cart.append(gadget_id)

    session["cart"] = cart

    return redirect("/")


# Корзина
@app.route("/cart")
def cart():

    cart_ids = session.get("cart", [])

    selected_gadgets = []

    for gadget in gadgets:

        if gadget["id"] in cart_ids:
            selected_gadgets.append(gadget)

    total = sum(item["price"] for item in selected_gadgets)

    return render_template(
        "cart.html",
        gadgets=selected_gadgets,
        total=total
    )


# Запуск сайта
if __name__ == "__main__":

    app.run(debug=True)from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "my_secret_key"

# Список пользователей
users = {
    "admin": "1234"
}

# Гаджеты магазина
gadgets = [
    {
        "id": 1,
        "name": "iPhone 15",
        "price": 65000,
        "emoji": "📱",
        "description": "Современный смартфон Apple"
    },
    {
        "id": 2,
        "name": "Samsung Galaxy S24",
        "price": 55000,
        "emoji": "📱",
        "description": "Мощный Android смартфон"
    },
    {
        "id": 3,
        "name": "MacBook Air",
        "price": 95000,
        "emoji": "💻",
        "description": "Ноутбук для работы и учёбы"
    },
    {
        "id": 4,
        "name": "AirPods Pro",
        "price": 18000,
        "emoji": "🎧",
        "description": "Беспроводные наушники"
    },
    {
        "id": 5,
        "name": "Apple Watch",
        "price": 30000,
        "emoji": "⌚",
        "description": "Умные часы Apple"
    },
    {
        "id": 6,
        "name": "PlayStation 5",
        "price": 55000,
        "emoji": "🎮",
        "description": "Игровая приставка"
    }
]


# Главная страница
@app.route("/")
def home():
    return render_template(
        "index.html",
        gadgets=gadgets,
        username=session.get("username")
    )


# Страница входа
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:

            session["username"] = username

            return redirect("/")

        return "Неверный логин или пароль!"

    return render_template("login.html")


# Регистрация
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username in users:

            return "Такой пользователь уже существует!"

        users[username] = password

        return redirect("/login")

    return render_template("register.html")


# Выход
@app.route("/logout")
def logout():

    session.pop("username", None)

    return redirect("/")


# Добавление в корзину
@app.route("/add/<int:gadget_id>")
def add_to_cart(gadget_id):

    if "cart" not in session:
        session["cart"] = []

    cart = session["cart"]

    cart.append(gadget_id)

    session["cart"] = cart

    return redirect("/")


# Корзина
@app.route("/cart")
def cart():

    cart_ids = session.get("cart", [])

    selected_gadgets = []

    for gadget in gadgets:

        if gadget["id"] in cart_ids:
            selected_gadgets.append(gadget)

    total = sum(item["price"] for item in selected_gadgets)

    return render_template(
        "cart.html",
        gadgets=selected_gadgets,
        total=total
    )


# Запуск сайта
if __name__ == "__main__":

    app.run(debug=True)from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "my_secret_key"

# Список пользователей
users = {
    "admin": "1234"
}

# Гаджеты магазина
gadgets = [
    {
        "id": 1,
        "name": "iPhone 15",
        "price": 65000,
        "emoji": "📱",
        "description": "Современный смартфон Apple"
    },
    {
        "id": 2,
        "name": "Samsung Galaxy S24",
        "price": 55000,
        "emoji": "📱",
        "description": "Мощный Android смартфон"
    },
    {
        "id": 3,
        "name": "MacBook Air",
        "price": 95000,
        "emoji": "💻",
        "description": "Ноутбук для работы и учёбы"
    },
    {
        "id": 4,
        "name": "AirPods Pro",
        "price": 18000,
        "emoji": "🎧",
        "description": "Беспроводные наушники"
    },
    {
        "id": 5,
        "name": "Apple Watch",
        "price": 30000,
        "emoji": "⌚",
        "description": "Умные часы Apple"
    },
    {
        "id": 6,
        "name": "PlayStation 5",
        "price": 55000,
        "emoji": "🎮",
        "description": "Игровая приставка"
    }
]


# Главная страница
@app.route("/")
def home():
    return render_template(
        "index.html",
        gadgets=gadgets,
        username=session.get("username")
    )


# Страница входа
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:

            session["username"] = username

            return redirect("/")

        return "Неверный логин или пароль!"

    return render_template("login.html")


# Регистрация
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username in users:

            return "Такой пользователь уже существует!"

        users[username] = password

        return redirect("/login")

    return render_template("register.html")


# Выход
@app.route("/logout")
def logout():

    session.pop("username", None)

    return redirect("/")


# Добавление в корзину
@app.route("/add/<int:gadget_id>")
def add_to_cart(gadget_id):

    if "cart" not in session:
        session["cart"] = []

    cart = session["cart"]

    cart.append(gadget_id)

    session["cart"] = cart

    return redirect("/")


# Корзина
@app.route("/cart")
def cart():

    cart_ids = session.get("cart", [])

    selected_gadgets = []

    for gadget in gadgets:

        if gadget["id"] in cart_ids:
            selected_gadgets.append(gadget)

    total = sum(item["price"] for item in selected_gadgets)

    return render_template(
        "cart.html",
        gadgets=selected_gadgets,
        total=total
    )


# Запуск сайта
if __name__ == "__main__":

    app.run(debug=True)from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "my_secret_key"

# Список пользователей
users = {
    "admin": "1234"
}

# Гаджеты магазина
gadgets = [
    {
        "id": 1,
        "name": "iPhone 15",
        "price": 65000,
        "emoji": "📱",
        "description": "Современный смартфон Apple"
    },
    {
        "id": 2,
        "name": "Samsung Galaxy S24",
        "price": 55000,
        "emoji": "📱",
        "description": "Мощный Android смартфон"
    },
    {
        "id": 3,
        "name": "MacBook Air",
        "price": 95000,
        "emoji": "💻",
        "description": "Ноутбук для работы и учёбы"
    },
    {
        "id": 4,
        "name": "AirPods Pro",
        "price": 18000,
        "emoji": "🎧",
        "description": "Беспроводные наушники"
    },
    {
        "id": 5,
        "name": "Apple Watch",
        "price": 30000,
        "emoji": "⌚",
        "description": "Умные часы Apple"
    },
    {
        "id": 6,
        "name": "PlayStation 5",
        "price": 55000,
        "emoji": "🎮",
        "description": "Игровая приставка"
    }
]


# Главная страница
@app.route("/")
def home():
    return render_template(
        "index.html",
        gadgets=gadgets,
        username=session.get("username")
    )


# Страница входа
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:

            session["username"] = username

            return redirect("/")

        return "Неверный логин или пароль!"

    return render_template("login.html")


# Регистрация
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username in users:

            return "Такой пользователь уже существует!"

        users[username] = password

        return redirect("/login")

    return render_template("register.html")


# Выход
@app.route("/logout")
def logout():

    session.pop("username", None)

    return redirect("/")


# Добавление в корзину
@app.route("/add/<int:gadget_id>")
def add_to_cart(gadget_id):

    if "cart" not in session:
        session["cart"] = []

    cart = session["cart"]

    cart.append(gadget_id)

    session["cart"] = cart

    return redirect("/")


# Корзина
@app.route("/cart")
def cart():

    cart_ids = session.get("cart", [])

    selected_gadgets = []

    for gadget in gadgets:

        if gadget["id"] in cart_ids:
            selected_gadgets.append(gadget)

    total = sum(item["price"] for item in selected_gadgets)

    return render_template(
        "cart.html",
        gadgets=selected_gadgets,
        total=total
    )


# Запуск сайта
if __name__ == "__main__":

    app.run(debug=True)from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "my_secret_key"

# Список пользователей
users = {
    "admin": "1234"
}

# Гаджеты магазина
gadgets = [
    {
        "id": 1,
        "name": "iPhone 15",
        "price": 65000,
        "emoji": "📱",
        "description": "Современный смартфон Apple"
    },
    {
        "id": 2,
        "name": "Samsung Galaxy S24",
        "price": 55000,
        "emoji": "📱",
        "description": "Мощный Android смартфон"
    },
    {
        "id": 3,
        "name": "MacBook Air",
        "price": 95000,
        "emoji": "💻",
        "description": "Ноутбук для работы и учёбы"
    },
    {
        "id": 4,
        "name": "AirPods Pro",
        "price": 18000,
        "emoji": "🎧",
        "description": "Беспроводные наушники"
    },
    {
        "id": 5,
        "name": "Apple Watch",
        "price": 30000,
        "emoji": "⌚",
        "description": "Умные часы Apple"
    },
    {
        "id": 6,
        "name": "PlayStation 5",
        "price": 55000,
        "emoji": "🎮",
        "description": "Игровая приставка"
    }
]


# Главная страница
@app.route("/")
def home():
    return render_template(
        "index.html",
        gadgets=gadgets,
        username=session.get("username")
    )


# Страница входа
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:

            session["username"] = username

            return redirect("/")

        return "Неверный логин или пароль!"

    return render_template("login.html")


# Регистрация
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username in users:

            return "Такой пользователь уже существует!"

        users[username] = password

        return redirect("/login")

    return render_template("register.html")


# Выход
@app.route("/logout")
def logout():

    session.pop("username", None)

    return redirect("/")


# Добавление в корзину
@app.route("/add/<int:gadget_id>")
def add_to_cart(gadget_id):

    if "cart" not in session:
        session["cart"] = []

    cart = session["cart"]

    cart.append(gadget_id)

    session["cart"] = cart

    return redirect("/")


# Корзина
@app.route("/cart")
def cart():

    cart_ids = session.get("cart", [])

    selected_gadgets = []

    for gadget in gadgets:

        if gadget["id"] in cart_ids:
            selected_gadgets.append(gadget)

    total = sum(item["price"] for item in selected_gadgets)

    return render_template(
        "cart.html",
        gadgets=selected_gadgets,
        total=total
    )


# Запуск сайта
if __name__ == "__main__":

    app.run(debug=True)from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "my_secret_key"

# Список пользователей
users = {
    "admin": "1234"
}

# Гаджеты магазина
gadgets = [
    {
        "id": 1,
        "name": "iPhone 15",
        "price": 65000,
        "emoji": "📱",
        "description": "Современный смартфон Apple"
    },
    {
        "id": 2,
        "name": "Samsung Galaxy S24",
        "price": 55000,
        "emoji": "📱",
        "description": "Мощный Android смартфон"
    },
    {
        "id": 3,
        "name": "MacBook Air",
        "price": 95000,
        "emoji": "💻",
        "description": "Ноутбук для работы и учёбы"
    },
    {
        "id": 4,
        "name": "AirPods Pro",
        "price": 18000,
        "emoji": "🎧",
        "description": "Беспроводные наушники"
    },
    {
        "id": 5,
        "name": "Apple Watch",
        "price": 30000,
        "emoji": "⌚",
        "description": "Умные часы Apple"
    },
    {
        "id": 6,
        "name": "PlayStation 5",
        "price": 55000,
        "emoji": "🎮",
        "description": "Игровая приставка"
    }
]


# Главная страница
@app.route("/")
def home():
    return render_template(
        "index.html",
        gadgets=gadgets,
        username=session.get("username")
    )


# Страница входа
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:

            session["username"] = username

            return redirect("/")

        return "Неверный логин или пароль!"

    return render_template("login.html")


# Регистрация
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username in users:

            return "Такой пользователь уже существует!"

        users[username] = password

        return redirect("/login")

    return render_template("register.html")


# Выход
@app.route("/logout")
def logout():

    session.pop("username", None)

    return redirect("/")


# Добавление в корзину
@app.route("/add/<int:gadget_id>")
def add_to_cart(gadget_id):

    if "cart" not in session:
        session["cart"] = []

    cart = session["cart"]

    cart.append(gadget_id)

    session["cart"] = cart

    return redirect("/")


# Корзина
@app.route("/cart")
def cart():

    cart_ids = session.get("cart", [])

    selected_gadgets = []

    for gadget in gadgets:

        if gadget["id"] in cart_ids:
            selected_gadgets.append(gadget)

    total = sum(item["price"] for item in selected_gadgets)

    return render_template(
        "cart.html",
        gadgets=selected_gadgets,
        total=total
    )


# Запуск сайта
if __name__ == "__main__":

    app.run(debug=True)from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "my_secret_key"

# Список пользователей
users = {
    "admin": "1234"
}

# Гаджеты магазина
gadgets = [
    {
        "id": 1,
        "name": "iPhone 15",
        "price": 65000,
        "emoji": "📱",
        "description": "Современный смартфон Apple"
    },
    {
        "id": 2,
        "name": "Samsung Galaxy S24",
        "price": 55000,
        "emoji": "📱",
        "description": "Мощный Android смартфон"
    },
    {
        "id": 3,
        "name": "MacBook Air",
        "price": 95000,
        "emoji": "💻",
        "description": "Ноутбук для работы и учёбы"
    },
    {
        "id": 4,
        "name": "AirPods Pro",
        "price": 18000,
        "emoji": "🎧",
        "description": "Беспроводные наушники"
    },
    {
        "id": 5,
        "name": "Apple Watch",
        "price": 30000,
        "emoji": "⌚",
        "description": "Умные часы Apple"
    },
    {
        "id": 6,
        "name": "PlayStation 5",
        "price": 55000,
        "emoji": "🎮",
        "description": "Игровая приставка"
    }
]


# Главная страница
@app.route("/")
def home():
    return render_template(
        "index.html",
        gadgets=gadgets,
        username=session.get("username")
    )


# Страница входа
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:

            session["username"] = username

            return redirect("/")

        return "Неверный логин или пароль!"

    return render_template("login.html")


# Регистрация
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username in users:

            return "Такой пользователь уже существует!"

        users[username] = password

        return redirect("/login")

    return render_template("register.html")


# Выход
@app.route("/logout")
def logout():

    session.pop("username", None)

    return redirect("/")


# Добавление в корзину
@app.route("/add/<int:gadget_id>")
def add_to_cart(gadget_id):

    if "cart" not in session:
        session["cart"] = []

    cart = session["cart"]

    cart.append(gadget_id)

    session["cart"] = cart

    return redirect("/")


# Корзина
@app.route("/cart")
def cart():

    cart_ids = session.get("cart", [])

    selected_gadgets = []

    for gadget in gadgets:

        if gadget["id"] in cart_ids:
            selected_gadgets.append(gadget)

    total = sum(item["price"] for item in selected_gadgets)

    return render_template(
        "cart.html",
        gadgets=selected_gadgets,
        total=total
    )


# Запуск сайта
if __name__ == "__main__":

    app.run(debug=True)