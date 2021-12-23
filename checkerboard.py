from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('board.html', row = 8,col=8)

@app.route('/<int:num>')
def rows(num):
    return render_template('board.html', row=num,col=num)

@app.route('/<int:x>/<int:y>')
def row_col(x,y):
    return render_template('board.html', row = x,col= y)


if __name__ == "__main__":
    app.run(debug=True)
