import streamlit as st

st.set_page_config(page_title="AslanAI", page_icon=":brain:")


def recommend_strategy(user_input):
    user_input = user_input.lower()  
    
    if "angry" in user_input:
        return "Take deep breaths, and try a calming technique like counting to 10."
    elif "sad" in user_input:
        return "It's okay to feel sad. Try journaling your feelings or talking to someone you trust."
    elif "stressed" in user_input:
        return "Consider a relaxing activity like meditation or going for a walk."
    elif "happy" in user_input:
        return "Keep enjoying the moment! Share your happiness with others."
    else:
        return "It's great that you're sharing your feelings. Remember to reach out to your support system if you need help."


# layout
st.title("Hi, I'm Aslan AI 🤖")
st.write("Share your thoughts or feelings, and I'll provide a helpful coping strategy.")

# Text input
user_input = st.text_area("How are you feeling today?", "")

if user_input:
    st.write(f"You: {user_input}")

    coping_strategy = recommend_strategy(user_input)
    st.write(f"Suggested Coping Strategy: {coping_strategy}")
