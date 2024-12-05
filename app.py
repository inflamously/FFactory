import gradio as gr
from gradio.components.chatbot import ChatMessage
from ollama import Message

import llm
from llm_service import OllamaService


def chat(message: str, history):
    # Append user message
    history.append({"role": "user", "content": message})
    llm_messages = list(map(lambda msg: Message(role=msg["role"], content=msg["content"]), history))
    llm_service.send_messages(llm_messages)
    res = llm_service.read_message()
    if not res is None:
        if res.message.role == "tool":
            yield ChatMessage(role="assistant", content=message)
        else:
            yield ChatMessage(res.message.role, res.message.content)
    else:
        yield "..."


def run_llm(model):
    llm_service.serve(model)


if __name__ == "__main__":
    llm.run_ollama()
    llm_service = OllamaService()

    with gr.Blocks(fill_height=True) as app:
        with gr.Column() as content:
            with gr.Row() as header:
                with gr.Column() as options:
                    dropdown = gr.Dropdown(choices=list(map(lambda model: model.name, llm.list_models())))
                    gr.Button().click(fn=run_llm, inputs=[dropdown])
            gr.ChatInterface(fn=chat, type="messages", title="FFactory")
    app.launch()
