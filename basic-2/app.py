from starlette.applications import Starlette
from routes import routes
import settings


app = Starlette(debug=settings.DEBUG, routes=routes)
