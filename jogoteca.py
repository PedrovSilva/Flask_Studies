from flask import Flask, render_template, request

class Game:
    def __init__(self, name, type, platform):
        self.name=name
        self.type=type
        self.platform=platform

app = Flask(__name__)

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

    return render_template("list.html", title_var="Games", games=games_list)

@app.route("/new")
def new_game():
    return render_template("new.html", titulo="New Game")
@app.route("/")
def hello():


    return render_template("list.html", title_var="test", games=games_list)

app.run()