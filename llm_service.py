import asyncio

import ollama
from ollama import Message

from llm import run_ollama, list_models, check_model


class OllamaService:
    def __init__(self):
        self.__client = ollama.AsyncClient()

    async def send_message(self, model: str, msg: str | Message):
        if not check_model(model): raise ValueError("Ollama model not found")
        return await self.send_messages(model, [msg])

    async def send_messages(self, model: str, msg: list[str | Message]):
        if not check_model(model): raise ValueError("Ollama model not found")
        return await self.__client.chat(model, messages=msg)


async def _main():
    run_ollama()
    service = OllamaService()
    print(list_models())
    msg = await service.send_message("darkness", Message(role="user", content="hello."))
    print(msg)


if __name__ == "__main__":
    asyncio.run(_main())
