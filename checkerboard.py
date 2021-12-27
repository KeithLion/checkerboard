from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('board.html', row=8, col=8, color1='blue', color2='black')


@app.route('/<int:num>')
def rows(num):
    return render_template('board.html', row=num, col=num)


@app.route('/<int:x>/<int:y>')
def row_col(x, y):
    return render_template('board.html', row=x, col=y)


@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def board_colors(x, y, color1, color2):
    return render_template('board.html', row=x, col=y, color2=color2, color1=color1)


if __name__ == "__main__":
    app.run(debug=True)
