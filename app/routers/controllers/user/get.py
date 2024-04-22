from fastapi import HTTPException
from app.services.db import gym_db

async def get_all_users():

    try:
        get_users = gym_db.fetch_all(
            sql=
            '''
            SELECT u.id,
                    u.name,
                    u.lastname,
                    u.email,
                    u.permission_id,
                    p.name as permission_name
            FROM worker_admins u
            JOIN permissions p ON u.permission_id = p.id
            '''
        )

        if not get_users:
            raise HTTPException(status_code=404, detail='Users not found')
        
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500, 
            detail='Error getting users'
        )
    
    return {
        'status': 'success',
        'message': 'Users retrieved successfully',
        'data': get_users
    }


async def get_user(user_id: int):

        try:
            get_user = gym_db.fetch_one(
                sql=
                '''
                SELECT u.id,
                        u.name,
                        u.lastname,
                        u.email,
                        u.permission_id,
                        p.name as permission_name
                FROM worker_admins u
                JOIN permissions p ON u.permission_id = p.id
                WHERE u.id = %s
                ''',
                params=(user_id,)
            )
    
            if not get_user:
                raise HTTPException(status_code=404, detail='User not found')
            
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=500, 
                detail='Error getting user'
            )
        
        return {
            'status': 'success',
            'message': 'User retrieved successfully',
            'data': get_user
        }