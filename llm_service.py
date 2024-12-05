import threading
from queue import Queue, Empty

import ollama
from ollama import Message, ChatResponse

from llm import run_ollama, list_models


class OllamaService:
    def __init__(self):
        self.__serve = False
        self.msg_queue_in = Queue()
        self.msg_queue_out = Queue()

    def serve(self, model: str):
        if not self.__serve:
            print("launching ollama model", model)
            threading.Thread(target=chat_instance, args=(model, self.msg_queue_in, self.msg_queue_out)).start()
            self.__serve = True
        else:
            return

    def send_message(self, msg: str | Message):
        if not self.__serve:
            print("chat instance not running")
            return
        self.msg_queue_in.put(msg)

    def send_messages(self, msg: list[str | Message]):
        if not self.__serve:
            print("chat instance not running")
            return
        self.msg_queue_in.put(msg)

    def read_message(self) -> ChatResponse | None:
        try:
            if not self.__serve:
                print("chat instance not running")
                return None
            return self.msg_queue_out.get(timeout=30)
        except Empty:
            return None


def chat_instance(model: str, msg_queue_in: Queue, msg_queue_out: Queue):
    while True:
        try:
            msg = msg_queue_in.get(timeout=30)
            print("OllamaService.chat_instance:", msg)
            if isinstance(msg, str):
                if msg == "${exit}":
                    print("exit called, chat instance killed.")
                    break
            elif isinstance(msg, list):
                try:
                    print("running chat request")
                    response = ollama.chat(model, messages=msg)
                    msg_queue_out.put(response)
                except Exception as e:
                    print("received invalid message:", msg)
                    msg_queue_out.put(Message(role="tool", content="received unknown message: " + str(e)))
            elif isinstance(msg, Message):
                print("running chat request")
                response = ollama.chat(model, messages=[msg])
                msg_queue_out.put(response)
            else:
                print("received unknown message:", msg)
                msg_queue_out.put(Message(role="tool", content="received unknown message: " + msg))
        except Empty:
            continue


if __name__ == "__main__":
    run_ollama()
    service = OllamaService()
    print(list_models())
    # service.serve("mistralistic")
    # service.send_message(Message(role="user", content="hello."))
    # print(service.read_message())
    # service.send_message("${exit}")
