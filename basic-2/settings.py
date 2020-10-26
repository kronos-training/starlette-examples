from pathlib import Path
from starlette.config import Config

config = Config('.env')

DEBUG = config('DEBUG', cast=bool, default=False)


BASE_DIR = Path(__file__).parent

TEMPLATE_DIR = BASE_DIR / 'templates'
STATIC_DIR = BASE_DIR / 'static'
SOME_API_KEY = 'wr34875y348'