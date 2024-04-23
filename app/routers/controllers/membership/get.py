from fastapi import HTTPException
from app.services.db import gym_db

async def get_all_clients_memeberships(membership_id: int | None = None):
    try:
        if membership_id == 1:
            clients = gym_db.fetch_all(
                sql='SELECT * FROM is_membership WHERE membership_id = %s',
                params=(membership_id,)
            )
            return {
                "message": "All clients with membership_id 1",
                "clients": clients
            }
        if membership_id is None:
            clients = gym_db.fetch_all(
                sql='SELECT * FROM is_membership'
            )
            return {
                "message": "All clients not memeberships",
                "clients": clients
            }
    except Exception as e:
        raise HTTPException(status_code=400, detail="error to get clients memberships")