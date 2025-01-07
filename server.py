import json

from ollama import Message, ChatResponse
from aiohttp import web

from chat import LLMChatResponse
from llm_service import OllamaService
from serversession import ServerSession

# Setup
app = web.Application(middlewares=[])
routes = web.RouteTableDef()
service = OllamaService()


def get_session() -> ServerSession:
    return app["state"]


@routes.get('/')
async def api_main(request):
    return web.Response(text="...")


@routes.post("/messages")
async def api_messages(request: web.Request):
    try:
        data = await request.json()

        raw_model = data["model"]
        raw_message = data["message"]

        llm_message = Message(role="user", content=raw_message)

        get_session().messages.append(llm_message)

        llm_response = await service.send_message(raw_model, llm_message)

        return web.json_response(body=LLMChatResponse(llm_response).to_json())
    except KeyError:
        return web.json_response(status=400, text="Bad Request")
    except json.decoder.JSONDecodeError:
        return web.Response(status=500, text="JSONDecodeError")


if __name__ == "__main__":
    app.add_routes(routes)
    app["state"] = ServerSession()
    web.run_app(app)
