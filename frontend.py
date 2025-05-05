# Setup UI with streamlit 
import streamlit as st

st.set_page_config(page_title="LangGraph Agent UI",layout="centered")
st.title("AI Chatbot Agents")
st.write("Create and Interact with the AI Agents!")

system_prompt=st.text_area("Define your AI Agent role: ",placeholder="Type your system prompt here ...")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "gemma2-9b-it","llama-3.1-8b-instant"]

selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)

allow_web_search=st.checkbox("Allow Web Search")

user_query=st.text_area("Enter Your Query: ", placeholder="Ask Anything! ")

API_URL="https://chatbot-agent-c0ix.onrender.com"

if st.button("Ask Agent!"):
    if user_query.strip():
        # connect with backend via url
        import requests

        payload={
            "model_name": selected_model,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        response = requests.post(f"{API_URL}/chat", json=payload)

        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response ")
                st.markdown(f"**Final Response:** {response_data}")
