from flask import Flask, render_template, request, jsonify
import json
import os
import openai
from uuid import uuid4
from dotenv import load_dotenv
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load environment variables from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Set the OpenAI API key
openai.api_key = openai_api_key

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

def regenerate_content(feedback):
    prompt = f"Improve the following LinkedIn post based on the feedback provided. Post: {feedback['content']}. Feedback: Content rating: {feedback['content_rating']}, Content comment: {feedback['content_comment']}, Structure rating: {feedback['structure_rating']}, Structure comment: {feedback['structure_comment']}."
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    print ("Regenerating")
    print(messages)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    improved_content = response.choices[0].message['content']
    return improved_content

@app.route('/')
def index():
    pr_content = load_pr_content()
    return render_template('index.html', pr_content=pr_content)

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    feedback = {
        'id': request.form['id'],
        'timestamp': request.form['timestamp'],
        'content': request.form['content'],
        'content_rating': int(request.form['content_rating']),
        'content_comment': request.form['content_comment'],
        'structure_rating': int(request.form['structure_rating']),
        'structure_comment': request.form['structure_comment']
    }
    
    action = request.form['action']
    
    if action == "accept":
        save_feedback(feedback)
        return jsonify(status="success", message="Feedback accepted.")
    elif action == "improve":
        improved_content = regenerate_content(feedback)
        feedback['improved_content'] = improved_content
        save_feedback(feedback)
        return jsonify(status="success", improved_content=improved_content)

if __name__ == '__main__':
    app.run(debug=True)
