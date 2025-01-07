import json

import aiohttp
from aiohttp import web
from multidict import MultiDictProxy

from llm_service import OllamaService

# Router
routes = web.RouteTableDef()
service = OllamaService()


@routes.get('/')
async def api_main(request):
    return web.Response(text="...")


@routes.post("/messages")
async def api_messages(request: web.Request):
    try:
        data = await request.json()
        model = data["model"]
        message = data["message"]
        result = await service.send_message(model, message)
        return web.json_response({
            "model": model,
            "message": message,
            "result": result
        })
    except KeyError:
        return web.json_response(status=400, text="Bad Request")
    except json.decoder.JSONDecodeError:
        return web.Response(status=500, text="JSONDecodeError")


if __name__ == "__main__":
    app = web.Application(
        middlewares=[]
    )
    app.add_routes(routes)
    web.run_app(app)
