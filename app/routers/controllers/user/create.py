from fastapi import HTTPException, Depends
from app.models.user import User
from app.services.db import gym_db
import bcrypt

async def create_user(perm_id: int, user: User = Depends(User.as_form)):
    
    try:
        
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

        if not user_id:
            raise HTTPException(status_code=500, detail='error creating user')

        select_all_user_data = gym_db.execute(
            sql=
            '''
            SELECT worker_admins.id, worker_admins.name, worker_admins.lastname, worker_admins.email, permissions.name as permission
            FROM worker_admins
            JOIN permissions ON worker_admins.permission_id = permissions.id
            WHERE worker_admins.id = %s
            ''',
            params=(user_id)
        )

        if select_all_user_data is not None:
            raise HTTPException(status_code=500, detail='error get user')
        
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500, 
            detail='Error creating user'
        )
    
    return {
        'status': 'success',
        'message': 'User created successfully',
        'data': select_all_user_data
    }