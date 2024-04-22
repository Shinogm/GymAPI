from fastapi import HTTPException, Depends
from app.models.user import User
from app.services.db import gym_db
import bcrypt

async def create_user(perm_id: int, user: User = Depends(User.as_form)):
    
    try:
        if perm_id not in [1, 2]:
            raise HTTPException(status_code=400, detail='Invalid permission id')
        user_id = gym_db.insert(
                table='worker_admins',
                data={
                    'name': user.name,
                    'lastname': user.last_name,
                    'password': bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()),
                    'email': user.email,
                    'permission_id': perm_id
                }
            )
        
        user_db = gym_db.fetch_one(
            sql='SELECT * FROM worker_admins WHERE id = %s',
            params=(user_id,)
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail='Error creating user')

    
    return {
        'status': 'success',
        'message': 'User created successfully',
        'data': user_db
    }