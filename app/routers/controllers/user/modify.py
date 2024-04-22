from fastapi import HTTPException, Depends
from app.models.user import ModifyUser
from app.services.db import gym_db
import bcrypt

async def modify_user(user_id: int | None = None, user: ModifyUser = Depends(ModifyUser.as_form)):
    
    try:
        
        get_user = gym_db.fetch_one(
            sql='SELECT * FROM worker_admins WHERE id = %s',
            params=(user_id)
        )

        if not get_user:
            raise HTTPException(status_code=404, detail='User not found')

        update_user = gym_db.execute(
            sql=
            '''
            UPDATE worker_admins
            SET name = %s, lastname = %s, email = %s, password = %s
            WHERE id = %s
            ''',
            params=(
                user.name if user.name is not None else get_user['name'],
                user.last_name if user.last_name is not None else get_user['lastname'],
                user.email if user.email is not None else get_user['email'],
                bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()),
                user_id
            )
        )

        if not update_user:
            raise HTTPException(status_code=500, detail='Error updating user')
        
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500, 
            detail='Error updating user'
        )
    
    return {
        'status': 'success',
        'message': 'User updated successfully',
        'data': get_user,
        'new_data': {
            'name': user.name if user.name is not None else get_user['name'],
            'lastname': user.last_name if user.last_name is not None else get_user['lastname'],
            'email': user.email if user.email is not None else get_user['email']
        }
    }

async def modify_user_permission(user_id: int | None = None, perm_id: int | None = None):
    
    try:
        
        get_user = gym_db.fetch_one(
            sql='SELECT * FROM worker_admins WHERE id = %s',
            params=(user_id)
        )

        if not get_user:
            raise HTTPException(status_code=404, detail='User not found')
        
        update_user = gym_db.execute(
            sql='UPDATE worker_admins SET permission_id = %s WHERE id = %s',
            params=(perm_id, user_id)
        )

        if not update_user:
            raise HTTPException(status_code=500, detail='Error updating user')
        
        permission_name = gym_db.fetch_one(
            sql='SELECT name FROM permissions WHERE id = %s',
            params=(perm_id)
        )
        
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500, 
            detail='Error updating user'
        )
    
    return {
        'status': 'success',
        'message': 'User updated successfully',
        'data': get_user,
        'new_data': {
            'permission': permission_name['name']
        }
    }