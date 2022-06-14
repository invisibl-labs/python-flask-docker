from flask import Flask
from multiprocessing import Value

app = Flask(__name__)
counter = Value('i', 0)

@app.route('/')
def hello_geek():
    with counter.get_lock():
        counter.value += 1
        out = counter.value
    return '<h1>Hello from Flask & Docker</h2> ' + str(out)


if __name__ == "__main__":
    app.run(debug=True)