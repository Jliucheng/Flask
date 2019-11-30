from flask import Flask
app = Flask(__name__)
@app.route('/', defaults={'abc': 'jiang'})
@app.route('/<abc>')
def hello(abc):
    text = '<h1 style="text-align:center">Hello Flask!</h1>' \
           '</br>' \
           '<p style="text-align:center">success %s </p>' % abc
    return text


if __name__ == '__main__':
    app.run(debug=True)