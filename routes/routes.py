from bottle import route, view, template, response, request, redirect
from datetime import datetime

from peewee import ModelSelect

from common import settings_app, PathView

from datebase_sourse.models import Users, Spases, Token, Groups, Todos
from playhouse.shortcuts import model_to_dict
import json

from security.password import verify_password

from uuid6 import uuid6

from uuid import UUID

import datetime

secret_key = '$6$rounds=656000$8GRboGLT87RU9Kih$E6MuzxgN7RTvPuFaI9vehv5nkFTGBXPS6ah7pZeZdh304ZOTbb0ZD2HpYpFdggeSGLxFVyJOhl4HBw6rn8L3/1'

def set_token_cookie(token: Token) -> None:
    cookie_value = [token.token]
    response.set_cookie("token_auth", cookie_value, secret=secret_key)
    
def get_token_cookie() -> UUID:
    return request.get_cookie("token_auth", secret=secret_key)[0]



# ------------------------------------------------------------------------------------------------

def set_register_cookie(login: str, password: str) -> None:
    cookie_value = [login, password]
    response.set_cookie("register", cookie_value, secret=secret_key)

def get_register_cookie() -> list:
    return request.get_cookie("register", secret=secret_key)

def get_login_cookie() -> str:
    return get_register_cookie()[0]

def get_password_cookie() -> str:
    return get_register_cookie()[1]

# ------------------------------------------------------------------------------------------------

def get_device() -> str:
    return request.headers['Sec-Ch-Ua-Platform']

def get_browser() -> str:
    return request.headers['Sec-Ch-Ua'].split(";")[0]

# ------------------------------------------------------------------------------------------------

def user_auth(login: str, password: str) -> Users:
    user: Users = Users.select().where(Users.login == login).get()
        
    if user is None:
        return None # TODO: return error not ftokenound user
    
    if verify_password(user.password, password):
        return user # TODO: return error not ftokenound user

    return None # TODO: return error not ftokenound user

def create_token(user: Users) -> Token:
    device = get_device()
    browser = get_browser()
    
    return Token.create(user=user, device=device, browser=browser)

def token_lifetime_check(token: Token):
    diff = (token.created_at + token.live) - datetime.datetime.now()
    
    if diff < datetime.timedelta():
        user = user_auth(get_login_cookie(), get_password_cookie())
        
        if user is None: return None # TODO: return error not ftokenound user
        
        token = create_token(user)
        set_token_cookie(token)
        
        return token
    return token

# ------------------------------------------------------------------------------------------------

@route('/')
@route('/home')
def home():
    return template(
        PathView.index,
        dict(
                
        )
    )

@route('/spase')
def spase():
    try:
        token = get_token_cookie()
        
        users_token = Token.select().where(Token.token == token).get()
        
        users_token = token_lifetime_check(users_token)
        
        user: Users = Users.select().where(Users.id == users_token.user).get()
        
        spase = Spases.select(
            Spases.id, Spases.name, Spases.favorite, Spases.img, Spases.created_at, Spases.way
        ).where(Spases.user == user.id).order_by(Spases.created_at)
        
        return json.dumps([model_to_dict(row) for row in spase], default=str, indent=4).replace("\n", '<br>').replace(" ", ' ')
    except Exception as e:
        print(e)
        return str(e)



class GroupView:
    def __init__(self, group: Groups) -> None:
        self.group = group
        
        select = Todos.select().where(Todos.group == group.id).order_by(Todos.id)
        
        self.todos: list[Todos] = [_ for _ in select] if select else []
    
    def __str__(self) -> str:
        return '<p>' +  '<br>'.join(
            [f'id: {self.group.id}', f'name: {self.group.name}', f'created_at: {self.group.created_at}', 'TODO:']
        ) + "<br>" + '<br>'.join(
                               [f'    {todo.selected:<5} {todo.text:^40}' for todo in self.todos]
                            ) + '</p>'




@route('/spase/<uuid_spase>')
def spase(uuid_spase):
    try:
        
        add = request.POST.get('Add')
        print(add)
        
        token = get_token_cookie()
        
        users_token = Token.select().where(Token.token == token).get()
        
        user: Users = Users.select().where(Users.id == users_token.user).get()
        
        ## .where(Spases.way == uuid_spase, Spases.user == user.id)
        
        spases_groups = Groups.select(
            Groups.id, Groups.name, Groups.created_at
        ).join(
            Spases, on=(Groups.spase == Spases.id)
        ).where(
            Spases.user == user.id, Spases.way == uuid_spase,
        ).order_by(
            Groups.created_at
        )
        
        groups_views = [GroupView(group) for group in spases_groups] 
        
        return template(
            PathView.todo,
            dict(
                groups = groups_views
            )
        )
        
    except Exception as e:
        return str(e)

@route('/add_task', method='POST')
def add_task():
    data = request.json
    group_id = data.get('groupId')
    
    print(group_id)
    
    # Ваш код для добавления задачи по group_id
    
    Todos.create(text='New task', group=group_id)

    return 'Task added successfully'  # Можете вернуть любой ответ в зависимости от успешности операции




@route('/test-cookie-set')
def login_auth():
    
    return redirect ("/test-cookie-get")


@route('/test-cookie-get')
def home():
    cookie = request.get_cookie("register", secret=secret_key)
    return f"login={cookie[0]}\npassword={cookie[1]}"



@route('/login')
def login():
    try:    
        login = 'triks'
        password = 'werasqZX123'
        
        user = user_auth(login, password)
        
        if user is not None:
            token = create_token(user)
            set_token_cookie(token)
            set_register_cookie(login, password)
            
        else:
            return 'User not found' # TODO: return error not found user
        
    except Exception as e:
        print(e)

