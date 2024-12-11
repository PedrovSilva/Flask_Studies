from flask import Flask, render_template, request, redirect, session, flash


class Game:
    def __init__(self, name, type, platform):
        self.name=name
        self.type=type
        self.platform=platform

app = Flask(__name__)

app.secret_key = "alura"

game1 = Game("Mario Wonder", "sidescroller", "Switch")
game2 = Game("Portal", "Puzzle", "PC")
games_list = [game1, game2]

@app.route("/create", methods=["POST",])
def create():
    nome = request.form["nome"]
    categoria = request.form["categoria"]
    console = request.form["console"]

    game = Game(nome, categoria, console)

    games_list.append(game)

    return redirect("/")

@app.route("/new")
def new_game():
    if "logged_user" not in session or session["logged_user"] == None:
        return redirect("/login")
    return render_template("new.html", title_var="New Game")
@app.route("/")
def index():


    return render_template("list.html", title_var="Games", games=games_list)


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/autenticar", methods=["POST",])
def autenticar():
    if "cake" == request.form["senha"]:
        session["logged_user"] = request.form["usuario"]
        flash("User logged!")
        return redirect("/")
    else:
        flash("Wrong password!")
        return redirect("/login")

@app.route("/logout")
def logout():
    session["logged_user"] = None
    flash("Logout!")
    return redirect("/")

app.run(debug=True)