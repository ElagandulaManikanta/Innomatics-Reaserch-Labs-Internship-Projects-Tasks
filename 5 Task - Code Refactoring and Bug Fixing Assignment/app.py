from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_note = request.form['note']
        notes.append(new_note)
        return redirect(url_for('home'))  
    return render_template('home.html', notes=notes)

if __name__ == '__main__':
    app.run(debug=True)


