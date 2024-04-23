from fastapi import HTTPException
from app.services.db import gym_db
from ..membership.time import check_all_membership_is_out_code

async def get_all_clients_memeberships(membership_code: int):
    try:
        get_member = gym_db.fetch_one(
            sql='SELECT * FROM is_membership WHERE code_membership = %s',
            params=(membership_code,)
        )

        if not get_member:
            raise HTTPException(status_code=404, detail='Client not found')
        
        response = await check_all_membership_is_out_code(membership_code)

        if response is None:
            raise HTTPException(status_code=404, detail='Memberships not found')
        
        get_client_all_data = gym_db.fetch_one(
            sql='SELECT * FROM clients WHERE id = %s',
            params=(get_member['client_id'],)
        )

        return {
            "message": "All clients with membership_id 1",
            "membership": get_member,
            "response": response
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="error to get clients memberships")
