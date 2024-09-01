from transformers import RagTokenizer, RagRetriever, RagTokenForGeneration

# Initialize the tokenizer, retriever, and model
tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")
retriever = RagRetriever.from_pretrained("facebook/rag-token-nq")
model = RagTokenForGeneration.from_pretrained("facebook/rag-token-nq", retriever=retriever)

def generate_rag_response(question):
    inputs = tokenizer(question, return_tensors="pt")
    output = model.generate(**inputs)
    return tokenizer.batch_decode(output, skip_special_tokens=True)[0]
