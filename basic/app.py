from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.responses import PlainTextResponse
from starlette.responses import JSONResponse
# from starlette.staticfiles import StaticFiles
import uvicorn
import asyncio


async def index(request):
    return PlainTextResponse('My index page!')


async def model_status(request):
    return JSONResponse({'status': [1, 0, 2, 3]})


async def model_predict(request):
    prediction_req = request.json()
    # prediction = predict(prediction_req)
    return JSONResponse({'predict': '75%'})


routes = [
    Route('/', index),
    Route('/stats', model_status),
    Route('/predict', model_predict, methods=['POST']),
    # Mount('/media', app=StaticFiles(directory='media'), name='media'),
]

app = Starlette(debug=True, routes=routes)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)