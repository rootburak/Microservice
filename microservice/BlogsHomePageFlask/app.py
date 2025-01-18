from flask import Flask,render_template
from flask_cors import CORS
import os


app = Flask(__name__,
            template_folder=os.path.abspath('../templates'), 
            static_folder=os.path.abspath('../static'))
CORS(app)

@app.route("/")
def homePage():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True,host='localhost',port=8001)
