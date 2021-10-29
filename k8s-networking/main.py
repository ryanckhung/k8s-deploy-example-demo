from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
	app.run(debug=True, port=5000, host='0.0.0.0')

    # must specify the port and host as above
    # if you just put app.run(debug=True), it will not work when communicate with the host
