from flask import Flask

app = Flask(__name__)

@app.route('/')

def greetings():
    return "<p> Greetings Young Pimp! </p>"

if __name__ == "__main__":
  app.run()
