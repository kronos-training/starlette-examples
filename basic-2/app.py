from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route


# 1. Declare a View
async def home():
    return PlainTextResponse('Hello world')

# 2. Put it in a routing table
routes = [
    Route('/', home, name='home'),
]
# 3. Declare the application instance
app = Starlette(routes=routes)
