from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
   return render_template("index.html")


@app.route("/programming")
def programming():
   return render_template("programming.html")


@app.route("/extracurriculars")
def extracurriculars():
   return render_template("extracurriculars.html")


@app.route("/social")
def social():
   return render_template("social.html")


@app.route("/contact")
def contact():
   return render_template("contact.html")

if __name__ == "__main__":
   app.run(debug=True)
