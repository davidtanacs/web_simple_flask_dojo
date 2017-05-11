from flask import Flask

app=Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
@app.route("/request-counter", methods=['GET', 'POST'])
def request_counter():
    




if __name__ == '__main__':
    app.run()
