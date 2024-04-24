from fastapi import HTTPException
from app.services.db import gym_db

async def delete_membership(client_id: int):
    try:
        get_client = gym_db.fetch_one(
            sql='SELECT * FROM clients WHERE id = %s',
            params=(client_id,)
        )

        if not get_client:
            raise HTTPException(status_code=404, detail='Client not found')
        
        # Check if the client has a membership
        client_membership = gym_db.fetch_one(
            sql='SELECT * FROM is_membership WHERE client_id = %s ',
            params=(client_id,)
        )
        if client_membership is None and client_membership["have_membership_id"] == 0:
            raise HTTPException(status_code=404, detail='Client not have membership')
        
        delete_membership = gym_db.execute(
            sql='DELETE FROM is_membership WHERE client_id = %s',
            params=(client_id,)
        )

        return {
            "message": "The client has been deleted membership",
            "client_id": client_id
        }

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="error to delete client membership")
    

async def quit_temporaly_membership(client_id: int):
    try:
        get_client = gym_db.fetch_one(
            sql='SELECT * FROM clients WHERE id = %s',
            params=(client_id,)
        )

        if not get_client:
            raise HTTPException(status_code=404, detail='Client not found')
        
        # Check if the client has a membership
        client_membership = gym_db.fetch_one(
            sql='SELECT * FROM is_membership WHERE client_id = %s ',
            params=(client_id,)
        )
        if client_membership["have_membership_id"] == 0:
            raise HTTPException(status_code=404, detail='Client not have membership')
        
        delete_membership = gym_db.execute(
            sql='UPDATE is_membership SET have_membership_id = 0 WHERE client_id = %s',
            params=(client_id,)
        )

        return {
            "message": "The client has been deleted membership",
            "client_id": client_id,
            'client': client_membership
        }

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="error to delete client membership"
        )