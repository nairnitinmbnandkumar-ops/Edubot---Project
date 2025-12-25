import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(page_title="EduBot Live Demo", page_icon="🎓")

# --- Mock Database (RAG Simulation) ---
INSTITUTIONAL_KNOWLEDGE = {
    "tuition": "The deadline for Spring 2026 tuition payment is January 15th, 2026.",
    "exams": "Final exams are scheduled from May 10th to May 20th.",
    "library": "The campus library is open 24/7 during finals week."
}

# --- UI Setup ---
st.title("🎓 EduBot: AI Student Assistant")
st.subheader("Final Project Live Demonstration")
st.info("This demo showcases NLP Intent Recognition and Retrieval-Augmented Generation (RAG).")

# --- Chat Interface ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Ask me about tuition, exams, or library hours..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        with st.spinner("Searching Institutional Database..."):
            time.sleep(1) # Simulate RAG search
            
            query = prompt.lower()
            if "tuition" in query:
                answer = INSTITUTIONAL_KNOWLEDGE["tuition"]
            elif "exam" in query:
                answer = INSTITUTIONAL_KNOWLEDGE["exams"]
            elif "library" in query:
                answer = INSTITUTIONAL_KNOWLEDGE["library"]
            else:
                answer = "I'm sorry, I don't have that specific information in my verified database. Would you like me to connect you to a human advisor?"

        for chunk in answer.split():
            full_response += chunk + " "
            time.sleep(0.05)
            response_placeholder.markdown(full_response + "▌")
        
        response_placeholder.markdown(full_response)
        
    st.session_state.messages.append({"role": "assistant", "content": full_response})
  streamlit
