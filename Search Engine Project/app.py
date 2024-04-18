import pandas as pd
from flask import Flask, render_template, request

df = pd.read_csv(r"C:\Users\Manikanta\Data Science Innomatics\Internship Projects - Tasks\Search Engine Project\Dataset\Search-Engine")

# Fill NaN values in 'Movies&WebSeries' column with an empty string
df['Movies&WebSeries'].fillna('', inplace=True)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search_text = request.form.get("search_text")
        if search_text:
            # Filter the DataFrame and handle NaN values in 'Movies&WebSeries' column
            results = df[df['Movies&WebSeries'].str.contains(search_text, case=False, na=False)]['Subtitles'].tolist()
            return render_template("results.html", search_text=search_text, results=results)
        else:
            return render_template("results.html", search_text="Nothing", results=None)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
