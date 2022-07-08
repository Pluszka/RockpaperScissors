from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
import datetime as dt
from game import Game
from player import Player

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Stats.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player = db.Column(db.Integer)
    time = db.Column(db.String(5))
    result = db.Column(db.String(10))
    credit = db.Column(db.Integer)
    day = db.Column(db.String)
# db.create_all()

@app.route("/",methods=['GET', 'POST'])
def start():
    if request.method == 'POST':

        if request.form.get('stats_button') == 'Stats':
            today_games = Stats.query.filter_by(day=dt.date.today())
            print(today_games)
            if today_games.count() < 1:
                flash('Play at least once to create stats')
                return render_template('index.html', score=player.credit)
            return render_template('stats.html', games=today_games, name=player.player)

        if request.form.get('credit_button') == 'Add 10 Credit':
            if player.credit == 0:
                player.add()
            else:
                flash('You have more than 0 Credits. You can\'t add more.')
            return render_template('index.html', score=player.credit)

        if request.form.get('rock_button') == 'Rock':
            user = 'rock'
        if request.form.get('paper_button') == 'Paper':
                user = 'paper'
        if request.form.get('scissors_button') == 'Scissors':
                user = 'scissors'

        if player.credit > 3:
            game = Game(user)
            result = game.compare()

            new = Stats(
                player=player.player,
                time=dt.datetime.now().strftime("%H:%M:%S"),
                result=result,
                credit=player.credit,
                day=dt.date.today()
            )
            db.session.add(new)
            db.session.commit()

            player.pay()
            if result == 'win':
                player.win()

            return render_template(f'{result}.html')
        else:
            flash('You can\'t pay for another game')
    return render_template('index.html', score=player.credit)

if __name__ == '__main__':
    player = Player(f'Start{dt.datetime.now()}')
    app.run(debug=True)