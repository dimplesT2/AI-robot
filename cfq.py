import streamlit as st  # 导入Streamlit库

import openai  # 导入OpenAI API库

import openai
import time

openai.api_key = "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"




models = {
    "gpt-3.5-turbo": "gpt-3.5-turbo",
    "gpt-3.5-turbo-0301": "gpt-3.5-turbo-0301",
}


def generate_response(prompt, model):
    # 调用OpenAI API的Completion模块生成回复

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ])

    message = response['choices'][0]['message']['content']
    # message = response.choices[0].text.strip()

    return message


def get_state():
    return {"chat_history": []}


def main():
    st.title("专属AI机器人---for cfq ")
    st.write("输入问题发送 等待回复就行啦！")

    if "state" not in st.session_state:
        st.session_state.state = get_state()

    model = st.selectbox("选择模型", list(models.keys()))

    message = st.text_area("You", height=100, value="", key="input")

    if st.button("Send"):
        chat_history = st.session_state.state["chat_history"]
        chat_history.append("You: " + message)
        response = generate_response("\n".join(chat_history), models[model])
        chat_history.append("ChatGPT: " + response)
        st.session_state.state["chat_history"] = chat_history

    if st.button("Clear chat history"):
        st.session_state.state = get_state()

    for msg in st.session_state.state["chat_history"]:
        st.write(msg)


if __name__ == "__main__":
    main()
