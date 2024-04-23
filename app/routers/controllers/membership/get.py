from fastapi import HTTPException
from app.services.db import gym_db

async def get_all_clients_memeberships(membership_id: int | None = None):
    try:
        if membership_id == 1:
            clients = gym_db.fetch_all(
                sql='SELECT * FROM is_membership WHERE have_membership_id = %s',
                params=(membership_id,)
            )
            return {
                "message": "All clients with membership_id 1",
                "clients": clients
            }
        if membership_id is None:
            clients = gym_db.fetch_all(
                sql='SELECT * FROM is_membership WHERE have_membership_id = 0'
            )
            return {
                "message": "All clients not memeberships",
                "clients": clients
            }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="error to get clients memberships")
    

async def get_all_client_membership(client_id: int):
    try:
        client_db_with_memebership_all_data = gym_db.fetch_one(
            sql='''
            SELECT clients.id, clients.name, clients.lastname, clients.email, is_membership.have_membership_id, is_membership.expiration_date 
            FROM clients
            INNER JOIN is_membership
            ON clients.id = is_membership.client_id
            WHERE clients.id = %s
            ''',
            params=(client_id,)
        )

        membership_db = gym_db.fetch_one(
            sql='SELECT * FROM is_membership WHERE client_id = %s',
            params=(client_id,)
        )
        if not client_db_with_memebership_all_data:
            raise HTTPException(status_code=404, detail='Client not found')
        
        return {
            "message": "Client with membership",
            "client": client_db_with_memebership_all_data,
            "membership": membership_db
        }

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="error to get client membership")
