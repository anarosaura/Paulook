import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import Union, List
import time


app = FastAPI()


class Posts(BaseModel):
    n_likes: int
    description: str
    user_id: int
    creation_date: Union[datetime, None] = None
    post_id: int
    title_post: str


class Users(BaseModel):
    user_name: str
    user_id: int
    user_age: int
    user_rol: str
    rol_id: int
    career: Union[str, None] = None
    semester: Union[str, None] = None
    friends_list: List[int]


posts_dict = {}
users_dict = {}


@app.put('/posts')
def create_post(post: Posts):
    post = post.dict()
    posts_dict[post['post_id']] = post

    return {'Message': f'Post {post["post_id"]} fue creado correctamente'}

#{
#    n_likes: 500
#    description: 'DS'
#    user_id: 1
#    post_id: 1
#    title_post: 'title'
#}


@app.put('/user')
def create_user(user: Users):
    user = user.dict()
    users_dict[user['user_id']]= user
    return {'description':f'User {user["user_id"]} con rol {user["user_rol"]} fue agregado correctamente.'}

#{
#    "user_name": "Ana",
#    "user_id": 12,
#    "user_age": 20,
#    "user_rol": "Estudiante",
#    "rol_id": 2,
#    "career": "Data Science",
#    "semester": "5to"
#}


@app.post('/users/{user_id}/{friend_id}')
def update_user(user_id: int, friend_id: int):
    user_to_update = users_dict[user_id]
    list_to_update = user_to_update["friends_list"]
    user_to_update.append(friend_id)
    users_dict[user_id]['friends_list'] = list_to_update
    return {'Description': f"Usuario {friend_id}agregado a la lista de amigos de {user_id}"}


@app.get('/users/{user_id}/{friends}')
def get_friends_list(user_id: int):
    friends_lst = users_dict[user_id]["friends_list"]

    return {"User ID": user_id,
            "Friends List": friends_lst}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info", reload=False)
