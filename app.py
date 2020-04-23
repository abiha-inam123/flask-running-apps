from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 align="center">Hello World!</h1> <h2 align="center"> This Is Our Operating System Lab Project</h2><h3> Yupiii My app Is Running Lets Party</h3><img src="https://i.pinimg.com/originals/e8/16/b7/e816b79f5eb9717030f89364dd82d70a.gif"></img><h3> Done Running This Application</h3><img src="https://media.giphy.com/media/py2UYwTIX5SXm/giphy.gif"></img><h3> The End ;) </h3><img src="https://i.pinimg.com/originals/e2/bd/7c/e2bd7ce3fc5f2783f1e210b015cc5fb1.gif"></img>'

if __name__ == "__main__":
	app.run(host="0.0.0.0",port=8080)

