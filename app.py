from flask import Flask, render_template, request

app = Flask(__name__)

# Home
@app.route('/')
def home():
    return render_template('index.html')

# Products
@app.route('/products')
def products():
    return render_template('index.html')

# Contact
@app.route('/contact')
def contact():
    return "<h2>Contact us: jeemano650@email.com</h2>"


# LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email == "admin@gmail.com" and password == "1234":
            return "Login Successful ✅"
        else:
            return "Invalid Email or Password ❌"

    return render_template('login.html')


# SIGNUP
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        return f"User {name} Registered Successfully ✅"

    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)