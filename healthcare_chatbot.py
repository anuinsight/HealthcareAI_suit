import streamlit as st
from transformers import pipeline

# ------------------------------
# Load QA model
# ------------------------------
@st.cache_resource
def load_model():
    qa_pipeline = pipeline(
        "question-answering",
        model="deepset/bert-base-cased-squad2",  # works well for medical QA
        tokenizer="deepset/bert-base-cased-squad2"
    )
    return qa_pipeline


# ------------------------------
# Generate response
# ------------------------------
def generate_medical_response(user_query):
    # A simple rule-based enhancement for structure
    disease_context = """
    Here is a summary of common diseases, symptoms, and treatments:

    Diabetes:
        - Symptoms: frequent urination, excessive thirst, fatigue, blurred vision
        - Causes: insulin resistance, genetics, obesity
        - Treatments: insulin, exercise, balanced diet

    Heart Disease:
        - Symptoms: chest pain, shortness of breath, fatigue
        - Causes: high blood pressure, smoking, high cholesterol
        - Treatments: medication, surgery, healthy lifestyle

    Fever:
        - Symptoms: high temperature, headache, chills
        - Causes: infection, flu, bacterial illness
        - Treatments: rest, hydration, paracetamol

    COVID-19:
        - Symptoms: cough, fever, loss of taste/smell
        - Causes: coronavirus infection
        - Treatments: rest, fluids, antivirals
    """

    qa = load_model()
    answer = qa(question=user_query, context=disease_context)

    # Structured response
    response = f"""
🩺 **Disease Information**
**Question:** {user_query}

💬 **Answer:** {answer['answer']}

⚕️ **Note:** Always consult a doctor before taking any action.
"""
    return response


# ------------------------------
# Streamlit UI
# ------------------------------
st.title("💬 Healthcare Chatbot")
st.write("Ask me about diseases, symptoms, or treatments (e.g., 'What are the symptoms of diabetes?').")

user_query = st.text_input("Enter your medical question:")

if st.button("Get Answer"):
    if user_query:
        with st.spinner("Analyzing your question..."):
            response = generate_medical_response(user_query)
        st.markdown(response)
    else:
        st.warning("Please enter a question first.")

