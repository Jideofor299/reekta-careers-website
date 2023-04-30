from flask import Flask
app = Flask(__name__)
@app.route("/")
def hword():
  return "<p>helllo o World</p>"
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)