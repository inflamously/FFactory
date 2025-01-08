from ollama import Message


class ServerSession:
    messages: list[Message]

    def __init__(self):
        self.messages = []
