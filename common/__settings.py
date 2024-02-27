import environ
import pathlib


BASE_DIR = pathlib.Path(__file__).parent.parent
env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')





