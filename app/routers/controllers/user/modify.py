from fastapi import HTTPException, Depends
from app.models.user import ModifyUser
from app.services.db import gym_db
import bcrypt

async def modify_user(user_id: int | None = None, user: ModifyUser = Depends(ModifyUser.as_form)):
    
    try:
        
        get_user = gym_db.fetch_one(
            sql='SELECT * FROM worker_admins WHERE id = %s',
            params=(user_id,)
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
                bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()) if user.password is not None else get_user['password'],
                user_id,
            )
        )


    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500, 
            detail='Error updating user2'
        )
    
    return {
        'status': 'success',
        'message': 'User updated successfully',
        'data': get_user,
        'new_data': {
            'name': user.name if user.name is not None else '',
            'lastname': user.last_name if user.last_name is not None else '',
            'email': user.email if user.email is not None else ''
        }
    }

async def modify_user_permission(user_id: int, perm_id: int ):
    
        if perm_id not in [1, 2, 3]:
            raise HTTPException(status_code=404, detail='Permission not found')
        get_user = gym_db.fetch_one(
            sql='SELECT * FROM worker_admins WHERE id = %s',
            params=(user_id,)
        )

        if not get_user:
            raise HTTPException(status_code=404, detail='User not found')
        
        if get_user['permission_id'] == perm_id:
            return {
                'status': 'success',
                'message': 'User already has this permission',
                'data': get_user,
                'new_data': {
                    'permission': get_user['permission_id']
                }
            }
        else:
            update_user = gym_db.update(
                table='worker_admins',
                data={
                    'permission_id': perm_id
                },
                where=str(user_id),
            )
            
            permission_name = gym_db.fetch_one(
                sql='SELECT name FROM permissions WHERE id = %s',
                params=(perm_id,)
            )
            get_user_new = gym_db.fetch_one(
                sql='SELECT * FROM worker_admins WHERE id = %s',
                params=(user_id,)
            )
            if not permission_name:
                raise HTTPException(status_code=404, detail='Permission not found')


            return {
                'status': 'success',
                'message': 'User updated successfully',
                'data': get_user_new,
                'new_data': {
                    'permission': permission_name['name']
                }
            }