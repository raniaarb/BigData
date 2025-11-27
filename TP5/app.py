import pandas as pd
from flask import Flask

app = Flask(__name__)

# Load Netflix Data
df = pd.read_csv("clean_netflix.csv")

@app.route("/")
def home():
    total_titles = len(df)
    movies = len(df[df['type'] == 'Movie'])
    shows = len(df[df['type'] == 'TV Show'])
    top_genre = df['listed_in'].value_counts().idxmax()

    html = f"""
    <html>
    <head>
        <title>Netflix Dashboard</title>
        <style>
            body {{
                font-family: Arial;
                background-color: #181818;
                color: #fff;
                text-align: center;
                padding-top: 40px;
            }}
            .box {{
                background: #282828;
                padding: 20px;
                margin: 15px auto;
                width: 50%;
                border-radius: 10px;
            }}
        </style>
    </head>
    <body>
        <h1>📺 Netflix Mini Dashboard</h1>

        <div class="box"><h2>Total Titles: {total_titles}</h2></div>
        <div class="box"><h2>Movies: {movies}</h2></div>
        <div class="box"><h2>TV Shows: {shows}</h2></div>
        <div class="box"><h2>Most Popular Genre: {top_genre}</h2></div>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

