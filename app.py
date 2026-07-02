import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/posts', methods=['GET'])
def get_posts():
    # CSV file se data read karne ke liye
    df = pd.read_csv('forum_posts.csv')
    
    # Data ko JSON standard format mein convert karne ke liye
    posts = df.to_dict(orient='records')
    return jsonify(posts)

if __name__ == '__main__':
    app.run(debug=True)
    
