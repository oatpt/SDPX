from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/getcode")
def get_code():
  return "Hello, world!"

@app.route("/plus/<int:a>/<int:b>")
def plus(a, b):
  return str(a + b)

if __name__ == "__main__":
  app.run(port=5001)
