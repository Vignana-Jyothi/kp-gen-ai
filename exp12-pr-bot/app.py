from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

def load_pr_content():
    with open('pr_content_generated.json', 'r') as file:
        content = json.load(file)
    return content

@app.route('/')
def index():
    pr_content = load_pr_content()
    return render_template('index.html', pr_content=pr_content)

if __name__ == '__main__':
    app.run(debug=True)
