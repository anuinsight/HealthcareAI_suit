import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Healthcare Assistant", page_icon="💊", layout="wide")

st.title("🏥 Healthcare Assistant Dashboard")

# Define backend FastAPI endpoint
BACKEND_URL = "http://127.0.0.1:8000/ask"

# Tabs
tab1, tab2, tab3 = st.tabs(["💬 Chatbot", "📋 Disease Info", "ℹ️ About"])

# ------------------ TAB 1: Chatbot ------------------
with tab1:
    st.subheader("💬 Ask Medical Questions")
    st.write("You can ask about **symptoms, diseases, and treatments**. The model will analyze and respond with medically relevant info.")

    user_input = st.text_input("Enter your question:")

    if st.button("Get Answer"):
        if user_input.strip() == "":
            st.warning("Please enter a valid medical question.")
        else:
            with st.spinner("Analyzing your question..."):
                try:
                    response = requests.post(BACKEND_URL, json={"question": user_input})
                    if response.status_code == 200:
                        data = response.json()
                        st.success(f"**Answer:** {data['answer']}")
                        st.info(f"**Confidence:** {data['confidence']}")
                        st.caption(data["note"])
                    else:
                        st.error("⚠️ Backend is not responding. Please start FastAPI first.")
                except Exception as e:
                    st.error(f"❌ Connection error: {e}")

# ------------------ TAB 2: Disease Info ------------------
with tab2:
    st.subheader("📋 Common Diseases Information")

    disease_data = {
        "Disease": ["Diabetes", "Heart Disease", "Fever", "COVID-19"],
        "Symptoms": [
            "Frequent urination, thirst, fatigue, blurred vision",
            "Chest pain, breath shortness, fatigue",
            "High temperature, headache, chills",
            "Cough, fever, loss of taste/smell"
        ],
        "Causes": [
            "Insulin resistance, genetics, obesity",
            "High BP, smoking, cholesterol",
            "Viral/bacterial infection",
            "Coronavirus infection"
        ],
        "Treatments": [
            "Insulin, exercise, balanced diet",
            "Medication, surgery, lifestyle changes",
            "Rest, hydration, paracetamol",
            "Rest, fluids, antivirals"
        ]
    }

    df = pd.DataFrame(disease_data)
    st.dataframe(df, use_container_width=True)

# ------------------ TAB 3: About ------------------
with tab3:
    st.subheader("ℹ️ About This Project")
    st.markdown("""
    **Healthcare Assistant** is an end-to-end AI/ML project that:
    - Analyzes patient queries using **BERT Question Answering**
    - Provides information on **diseases, symptoms, and treatments**
    - Demonstrates **AI in healthcare** for clinical decision support

    **Tech Stack:**
    - 🧠 Transformers (BERT)
    - ⚙️ FastAPI (Backend)
    - 💻 Streamlit (Frontend)
    - 🔍 PyTorch, Hugging Face

    **Disclaimer:**  
    This tool is for **educational purposes only**.  
    Always consult a **qualified doctor** before making health decisions.
    """)

    st.markdown("---")
    st.caption("Developed by **Anupriya R** | AI-powered Healthcare Assistant 💊")
