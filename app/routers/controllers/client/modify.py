from ....models.client import ModifyClient
from ....services.db import gym_db
from fastapi import Depends, HTTPException

async def modify_client(client_id: int | None = None, client: ModifyClient = Depends(ModifyClient.as_form)):
    try:
        get_clients = gym_db.fetch_one(
            sql='SELECT * FROM clients WHERE id = %s',
            params=(client_id,)
        )

        if not get_clients:
            raise HTTPException(status_code=404, detail='Client not found')
        
        update_client = gym_db.execute(
            sql='UPDATE clients SET name = %s, lastname = %s, email = %s WHERE id = %s',
            params=(
                client.name if client.name is not None else get_clients['name'],
                client.lastname if client.lastname is not None else get_clients['lastname'],
                client.email if client.email is not None else get_clients['email'],
                client_id,
            )
        )

    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail='Error updating client'
        )
    
    return {
        'status': 'success',
        'message': 'Client updated successfully',
        'data': get_clients,
        'new_data': {
            'name': client.name if client.name is not None else '',
            'lastname': client.lastname if client.lastname is not None else '',
            'email': client.email if client.email is not None else ''
        }
    }