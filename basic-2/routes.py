from pathlib import Path
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
import views

# static = StaticFiles(directory=str(Path(__file__).parent / 'static'))
static = StaticFiles(directory='static')

routes = [
    Route('/', views.home, name='home'),
    Mount('/static', static, name='static'),
]
