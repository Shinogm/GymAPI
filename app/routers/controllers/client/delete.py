from fastapi import HTTPException
from app.services.db import gym_db

async def delete_client(client_id: int | None = None):
    try:
        delete_client = gym_db.execute(
            sql='DELETE FROM clients WHERE id = %s',
            params=(client_id,)
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail='Error deleting client'
        )
    
    return {
        'status': 'success',
        'message': 'Client deleted successfully',
        'data': {
            'id': client_id
        }
    }