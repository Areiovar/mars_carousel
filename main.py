from flask import Flask, render_template

app = Flask (__name__)


@app.route ('/carousel')
def index():
    images = [
        'mars1.jpg',
        'mars2.jpg',
        'mars3.jpg',
    ]

    return render_template ('index.html', images=images)


if __name__ == '__main__':
    app.run ('127.0.0.1', 8080)
