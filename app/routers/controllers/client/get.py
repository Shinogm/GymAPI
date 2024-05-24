from fastapi import HTTPException
from ....services.db import gym_db

async def get_all_clients(client_id: int | None = None):
    try:
        if client_id:
            get_clients = gym_db.fetch_one(
                sql='SELECT * FROM clients WHERE id = %s',
                params=(client_id,)
            )

            if not get_clients:
                raise HTTPException(status_code=404, detail='Client not found')
            
            return {
                'status': 'success',
                'message': 'Client found',
                'data': get_clients
            }
        else:
            get_clients = gym_db.fetch_all(
                sql='SELECT * FROM clients'
            )
            return {
                'status': 'success',
                'message': 'All clients',
                'data': get_clients
            }
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail='Error getting clients'
        )

async def get_all_clients_with_no_membership():
    try:
        get_clients = gym_db.fetch_all(
            sql='SELECT * FROM clients WHERE id NOT IN (SELECT client_id FROM is_membership)'
        )
        return {
            'status': 'success',
            'message': 'All clients with no membership',
            'data': get_clients
        }
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail='Error getting clients'
        )