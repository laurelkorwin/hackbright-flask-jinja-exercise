from random import choice
from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")

@app.route('/game')
def play_game():
    """Ask user if they want to play a game!."""

    player = request.args.get("person")

    return render_template("compliment.html", person=player)

@app.route('/playorquit')
def playorquit():

    player_choice = request.args.get("game")

    if player_choice == "no":
        return render_template("goodbye.html")
    else:
        return render_template("play_game.html")

@app.route('/madlib')
def show_madlib():

    random_person = request.args.get("random_person")
    noun = request.args.get("noun")
    color = request.args.get("color")
    adjective = request.args.get("adjective")



    return render_template("madlibs.html", random_person=random_person,color=color,noun=noun,adjective=adjective)

@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
