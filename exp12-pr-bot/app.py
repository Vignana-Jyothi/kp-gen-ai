from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

def load_pr_content():
    with open('pr_content_generated.json', 'r') as file:
        content = json.load(file)
    return content

def save_feedback(feedback):
    feedback_file = 'pr_content_reviewed.json'
    
    if os.path.exists(feedback_file):
        # Read existing feedback
        try:
            with open(feedback_file, 'r') as file:
                if os.path.getsize(feedback_file) > 0:
                    existing_feedback = json.load(file)
                else:
                    existing_feedback = []
        except json.decoder.JSONDecodeError:
            existing_feedback = []
    else:
        existing_feedback = []

    existing_feedback.append(feedback)

    with open(feedback_file, 'w') as file:
        json.dump(existing_feedback, file, indent=4)

@app.route('/')
def index():
    pr_content = load_pr_content()
    return render_template('index.html', pr_content=pr_content)

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    feedback = {
        'timestamp': request.form['timestamp'],
        'content': request.form['content'],
        'content_rating': int(request.form['content_rating']),
        'content_comment': request.form['content_comment'],
        'structure_rating': int(request.form['structure_rating']),
        'structure_comment': request.form['structure_comment']
    }
    save_feedback(feedback)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
