import streamlit as st
from pyodide.http import pyfetch
import json

st.title("stlite OpenAI API example")

# APIキーを入力する
api_key = st.text_input("API Key", "")

# プロンプトを入力する
prompt = st.text_input("Prompt", "Hello!")

# OpenAI APIを呼び出す
async def call_openai_api(api_key, prompt, model="gpt-3.5-turbo"):
    # APIキーをヘッダに設定する
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key,
    }
    # リクエストボディを設定する
    body = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt,
            },
        ],
    }
    # APIを呼び出す。requests.post()が使えないのでpyfetch()を使う
    API_URL = "https://api.openai.com/v1/chat/completions"
    response = await pyfetch(API_URL, method="POST", headers=headers, body=json.dumps(body))
    response_json = await response.json()
    # レスポンスをパースする
    role = response_json["choices"][0]["message"]["role"]
    message = response_json["choices"][0]["message"]["content"]
    return (role, message)

# APIキーとプロンプトが入力されたらAPIを呼び出す
if api_key and prompt:
    role, message = await call_openai_api(api_key, prompt)
    with st.chat_message(role):
        st.write(message)
