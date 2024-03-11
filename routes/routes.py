from bottle import route, view, template
from datetime import datetime

from common import settings_app, PathView

@route('/')
@route('/home')
def home():
    return template(
        PathView.index,
        dict(
                
        )
    )

