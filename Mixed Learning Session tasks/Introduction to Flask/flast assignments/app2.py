from flask import Flask, render_template

app = Flask(__name__)

@app.route('/my_profile')
def my_profile():
    return render_template('my_profile.html')

@app.route('/my_print_credit')
def my_print_credit():
    return render_template('my_print_credit.html')

if __name__ == '__main__':
    app.run(debug=True)
