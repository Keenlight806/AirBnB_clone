#!/usr/bin/python3
'''
models/user.py
'''
from models.base_model import BaseModel

class User(BaseModel):
    '''
    The User
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
