from transformers import pipeline

# Load pre-trained model
question_answering_model = pipeline("question-answering")

def generate_response(question):
    # Use the LLM to generate a response
    context = "Context about U.S. immigration laws and procedures."
    result = question_answering_model(question=question, context=context)
    return result['answer']
