import json

from ollama import ChatResponse


class LLMChatResponse:
    def __init__(self, response: ChatResponse):
        self.total_duration = round(response.total_duration / 1e+9)
        self.model = response.model
        self.message = response.message

    def to_json(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__,
                          sort_keys=True,
                          indent=4)
