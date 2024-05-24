from ....models.client import Client
from ....services.db import gym_db
from fastapi import Depends, HTTPException

async def create_client(client: Client = Depends(Client.as_form)):
    try:
        create_client = gym_db.execute(
            sql='INSERT INTO clients (name, lastname, email) VALUES (%s, %s, %s)',
            params=(client.name, client.last_name, client.email)
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail='Error creating client'
        )
    
    return {
        'status': 'success',
        'message': 'Client created successfully',
        'client': {
            'id': create_client,
            'name': client.name,
            'last_name': client.last_name,
            'email': client.email
        }
    }