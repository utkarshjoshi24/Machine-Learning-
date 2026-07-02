from flask import Flask,render_template,request, redirect, url_for

app = Flask(__name__)

@app.route("/success/<int:score>")
def success(score):
    res = ""
    if (score>=50):
        res = "PASSED"
    else:
        res = "FAILED"
    
    return render_template("results.html", results=res)

@app.route("/form", methods=["GET", "POST"])
def form():
    total_score = 0
    if request.method == "POST":
        maths = float(request.form["maths"])
        ml = float(request.form["ml"])
        python = float(request.form["python"])
        ds = float(request.form["ds"])
        total_score = (maths + ml + python + ds)/4
    
        return redirect(url_for("success", score = total_score))
    
    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)