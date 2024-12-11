from flask import Flask, render_template

class Game:
    def __init__(self, name, type, platform):
        self.name=name
        self.type=type
        self.platform=platform

app = Flask(__name__)

@app.route("/")
def hello():

    game1 = Game("Mario Wonder", "sidescroller", "Switch")
    game2 = Game("Portal", "Puzzle", "PC")
    games_list = [game1, game2]
    return render_template("list.html", title_var="test", games=games_list)

app.run()