import os

import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
MODEL = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")


def ask_llm(message, history):
    if not OPENAI_API_KEY:
        return "Помилка: не задано OPENAI_API_KEY (змінна середовища)."

    client = OpenAI(api_key=OPENAI_API_KEY)

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": message}],
        )
        return response.choices[0].message.content
    except Exception as exc:
        return f"Помилка виклику LLM: {exc}"


demo = gr.ChatInterface(
    fn=ask_llm,
    type="messages",
    title="Мінімальний чат з LLM (OpenAI)",
    examples=["Привіт, яка столиця Парижу?"],
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    #demo.launch(server_name="127.0.0.1", server_port=port)
    demo.launch(server_name="0.0.0.0", server_port=port)