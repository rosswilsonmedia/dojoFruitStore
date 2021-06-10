from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    first_name=request.form['first_name']
    last_name=request.form['last_name']
    form_response=request.form
    fruitCount=int(request.form['strawberry'])+int(request.form['raspberry'])+int(request.form['apple'])
    print(f"Charging {first_name} {last_name} for {fruitCount} fruits")
    return render_template("checkout.html", form_response=form_response)

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)