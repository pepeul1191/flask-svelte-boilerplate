from flask import Flask

app = Flask(__name__, static_folder='static')

@app.route('/hola')
def inicio():
  return '¡Hola, Flask en Ubuntu!'

if __name__ == '__main__':
  app.run(debug=True)
