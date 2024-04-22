from fastapi import HTTPException
from app.services.db import gym_db

async def have_membership(client_id: int, have_membership_id: int):
    try:
        get_client = gym_db.fetch_one(
            sql='SELECT * FROM clients WHERE id = %s',
            params=(client_id)
        )

        if not get_client:
            raise HTTPException(status_code=404, detail='Client not found')
        
        if get_client['permission_id'] != 3:
            raise HTTPException(status_code=403, detail='Client does not have permission to update membership')

        if have_membership_id not in (0, 1):
            raise HTTPException(status_code=400, detail='Invalid value for have_membership_id')

        update_membership = gym_db.execute(
            sql='INSERT INTO memberships (client_id, have_membership_id) VALUES (%s, %s)',
            params=(client_id, have_membership_id)
        )

        if not update_membership:
            raise HTTPException(status_code=500, detail='Error updating membership')
        '''
        
        '''
        select_all_client_data = gym_db.execute(
            sql=
            '''
            SELECT clients.id, clients.name, clients.lastname, clients.email, permissions.name as permission
            FROM clients
            JOIN permissions ON clients.permission_id = permissions.id
            WHERE clients.id = %s

            ''',
            params=(client_id)
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500, 
            detail='Error updating membership'
        )
    
    return {
        'status': 'success',
        'message': 'Membership updated successfully',
        'data': select_all_client_data
    }


async def get_all_clients_memeberships():
    try:
        get_clients = gym_db.fetch_all(
            sql=
            '''
            SELECT c.id, c.name, c.lastname, c.email, m.have_membership_id
            FROM clients c
            JOIN memberships m ON c.id = m.client_id
            '''
        )

        if not get_clients:
            raise HTTPException(status_code=404, detail='Clients not found')
        
        if get_clients['permission_id'] != 3:
            raise HTTPException(status_code=403, detail='Client does not have permission to get memberships')
        
        if get_clients['have_membership_id'] != 1:
            raise HTTPException(status_code=400, detail='Invalid value for have_membership_id')
        
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500, 
            detail='Error getting clients'
        )
    
    return {
        'status': 'success',
        'message': 'Clients retrieved successfully',
        'data': get_clients
    }