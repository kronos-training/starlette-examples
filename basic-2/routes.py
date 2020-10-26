from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
import views
import settings

static = StaticFiles(directory=str(settings.STATIC_DIR))

routes = [
    Route('/', views.home, name='home'),
    Route('/movies/{q}', views.search_movies, name='search_movies'),
    Mount('/static', static, name='static'),
]
