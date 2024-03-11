from flask import Flask, render_template, request
import re
from validate_email_address import validate_email

app = Flask(__name__)

###########################################################

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    matches = re.findall(regex_pattern, test_string)
    return render_template('results.html', matches=matches)

@app.route('/validate-email', methods=['POST', 'GET'])
def validate_email_address():
    if request.method == 'POST':
        email = request.form['email']
        is_valid = validate_email(email)

        if is_valid:
            return 'Email is valid'
        else:
            return 'Email is not valid'
    else:
        return render_template('validate_email.html')

###########################################################
if __name__ == '__main__':
    app.run(debug=True)
