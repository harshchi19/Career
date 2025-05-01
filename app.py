import streamlit as st
import requests
import json

def main():
    # --- Page Configuration ---
    st.set_page_config(page_title="Career Genius Bot 🎓", page_icon="🤖", layout="centered")

    # --- Gradient Background with CSS ---
    st.markdown("""
        <style>
        body {
            background: linear-gradient(to right, #e0f7fa, #fffde7);
        }
        .stChatMessage {
            background-color: #ffffff;
            padding: 10px 15px;
            border-radius: 12px;
            margin-bottom: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        </style>
    """, unsafe_allow_html=True)

    # --- App Header ---
    st.markdown("<h1 style='text-align: center; color: #4e4376;'>Career Genius Bot 🎓</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Get personalized course and career guidance based on your interests and goals!</p>", unsafe_allow_html=True)
    st.write("")

    # --- Chat history ---
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # --- Display chat history ---
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # --- User Input ---
    user_input = st.chat_input("Ask me about career options, courses, or future scope...")

    if user_input:
        # Display user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # --- API Call to Langbase Agent ---
        url = "https://api.langbase.com/devilhc12347378/career-genius-agent-4c28"
        headers = {
            "Authorization": "Bearer user_3vm9pGck8SmoFzv5RnPifPcMr4ib9FHtrBdt5gnpKEHtx2NxztAuV62qxZghmGkhPMhjxctcppKCThi9piitP4SG",
            "Content-Type": "application/json"
        }
        payload = {"input": user_input}

        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()

            try:
                result = response.json()
                if isinstance(result, dict):
                    bot_reply = result.get("output", "Sorry, I couldn't process that.")
                else:
                    bot_reply = str(result)
            except json.JSONDecodeError:
                bot_reply = response.text

        except Exception as e:
            bot_reply = f"⚠️ Error: {str(e)}"

        # Display bot response
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        with st.chat_message("assistant"):
            st.markdown(bot_reply)

# --- Run the app ---
if __name__ == "__main__":
    main()
