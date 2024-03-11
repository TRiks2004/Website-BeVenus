from bottle import route, default_app, Bottle, static_file, run

from common import settings_app

import routes.routes as routes
import os

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=settings_app.path_folder_static)

app = default_app()