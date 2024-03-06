from bottle import route, view
from datetime import datetime

from common import settings_app

@route('/')
@route('/home')
@view(settings_app.path_file_view('index'))
def home():
    return dict(
        layout_path = settings_app.path_file_view('layout.tpl'),
        year=datetime.now().year
    )

@route('/contact')
@view(settings_app.path_file_view('contact'))
def contact():
    """Renders the contact page."""
    return dict(
        layout_path = settings_app.path_file_view('layout.tpl'),
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/about')
@view(settings_app.path_file_view('about'))
def about():
    """Renders the about page."""
    return dict(
        layout_path = settings_app.path_file_view('layout.tpl'),
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )
