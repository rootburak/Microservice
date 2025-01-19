from flask import Flask,render_template
from flask_cors import CORS


app = Flask(__name__,
            template_folder='templates', 
            static_folder='static')
CORS(app)

@app.route("/")
def homePage():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True,host='localhost',port=8001)
