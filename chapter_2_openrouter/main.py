import streamlit as st
import requests

st.set_page_config(page_title="Chat with DeepSeek", layout="centered")
st.title(" Chat with DeepSeek Qwen3 (via OpenRouter)")


API_KEY = "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"


MODEL = "deepseek/deepseek-r1-0528-qwen3-8b:free"

user_input = st.text_input("Ask a question:")

if user_input:
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }

    with st.spinner("Thinking..."):
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload
        )

    if response.status_code == 200:
        message = response.json()["choices"][0]["message"]["content"]
        st.success("✅ Response:")
        st.write(message)
    else:
        st.error(f" Error {response.status_code}")
        st.text(response.text)

st.markdown("""
    <style>
        footer {
            visibility: hidden;
        }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <footer>
        <p>Powered by <a href="https://openrouter.ai" target="_blank">OpenRouter</a></p>
    </footer>
    """, unsafe_allow_html=True)
