from bottle import route, default_app, Bottle

@route('/hello')
async def hello():
    return "Hello World!"


app = default_app()

'-c ./gunicorn/gunicorn.conf.py'