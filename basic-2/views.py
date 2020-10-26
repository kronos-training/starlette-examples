import httpx
from starlette.responses import HTMLResponse, JSONResponse
from starlette.templating import Jinja2Templates
import settings

templates = Jinja2Templates(directory=str(settings.TEMPLATE_DIR))

client = httpx.AsyncClient()


async def home(request):
    template = 'index.html'
    context = {'request': request}
    return templates.TemplateResponse(template, context=context)


async def example_dot_com(request):
    # async with httpx.AsyncClient() as client:
    #     url = 'https://example.org'
    #     response = await client.get(url)
    response = await client.get('https://example.org')

    return HTMLResponse(response.text)


async def search_movies(request):
    q = request.path_params['q']
    # async with httpx.AsyncClient as client:
    #     url = 'https://api.example.io/movies'
    #     params = {'api_key': settings.SOME_API_KEY, 'q': q}
    #     response = await client.get(url, params=params)
    params = {'api_key': settings.SOME_API_KEY, 'q': q}
    response = await client.get('https://api.example.io/movies', params=params)

    return JSONResponse(response.json())