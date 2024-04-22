from fastapi import HTTPException
from app.services.db import gym_db

async def delete_user(user_id: int):
        
    try:
        get_user = gym_db.fetch_one(
            sql='SELECT * FROM worker_admins WHERE id = %s',
            params=(user_id,)
        )

        if not get_user:
            raise HTTPException(status_code=404, detail='User not found')
        
        delete_user = gym_db.execute(
            sql='DELETE FROM worker_admins WHERE id = %s',
            params=(user_id,)
        )

        
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500, 
            detail='Error deleting user'
        )
    
    return {
        'status': 'success',
        'message': 'User deleted successfully',
        'data': get_user,
        'deleted': delete_user
    }