import streamlit as st
import google.generativeai as genai

st.snow()

st.title("🥷🏻AI Sensei: 🤖 Your Personal AI Teaching Master")

f = open(r"C:\Users\Manikanta\Data Science Innomatics\Internship Projects - Tasks\11 Build a Conversational AI Tutor\key.txt")
key = f.read()

genai.configure(api_key=key)

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              system_instruction="You are a helpful AI teaching assistance. You need to answer the question of the user provided in a polite manner, if you don't know the answer then you should say 'I am not able to provide the right now.'")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"]=[]

chat = model.start_chat(history=st.session_state["chat_history"])

for msg in chat.history:
    st.chat_message(msg.role).write(msg.parts[0].text)

user_prompt = st.text_input("Message Sensei... ")

if user_prompt:
    st.chat_message("user").write(user_prompt)
    response = chat.send_message(user_prompt)
    st.chat_message("ai").write(response.text)
    st.session_state["chat_history"]=chat.history