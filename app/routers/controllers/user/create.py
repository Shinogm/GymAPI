from fastapi import HTTPException, Depends
from app.models.user import User
from app.services.db import gym_db
import bcrypt

from enum import Enum

class PERMISO(Enum):
    ADMIN = 'admin'
    TRABAJADOR = 'trabajador'

async def create_user(perm_ENUM: PERMISO , user: User = Depends(User.as_form)):
    
    try:
        if perm_ENUM.value == 'admin':
            user_id = gym_db.execute(
                sql='INSERT INTO worker_admins (name, lastname, password, email, permission_id) VALUES (%s, %s, %s, %s, %s)',
                params=(user.name, user.last_name, bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()), user.email, 1)
            )
        elif perm_ENUM.value == 'trabajador':
            user_id = gym_db.insert(
                table='worker_admins',
                data={
                    'name': user.name,
                    'lastname': user.last_name,
                    'password': bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()),
                    'email': user.email,
                    'permission_id': 2
                }
            )
        
        user_db = gym_db.fetch_one(
            sql='SELECT * FROM worker_admins WHERE id = %s',
            params=(user_id,)
        )

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail='Error creating user')

    
    return {
        'status': 'success',
        'message': 'User created successfully',
        'data': user_db
    }