from flask import Blueprint, request, jsonify
from .models import generate_response

main_routes = Blueprint('main', __name__)

@main_routes.route('/submit-form', methods=['POST'])
def submit_form():
    data = request.json
    # Logic to process form data
    return jsonify({"message": "Form submitted successfully."})

@main_routes.route('/ask-question', methods=['POST'])
def ask_question():
    question = request.json.get("question")
    response = generate_response(question)
    return jsonify({"response": response})
