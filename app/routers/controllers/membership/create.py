from fastapi import HTTPException
from app.services.db import gym_db
from datetime import datetime, timedelta

async def have_membership(client_id: int):
    try:
        # Check if the client has a membership
        client_membership = gym_db.fetch_one(
            sql='SELECT * FROM is_membership WHERE client_id = %s ',
            params=(client_id,)
        )

        if client_membership["have_membership_id"] == 0 or not client_membership:
            membership_id = 1
            expiration_date = datetime.now() + timedelta(days=30)

            put_membership = gym_db.execute(
                sql='INSERT INTO is_membership (client_id, membership_id, expiration_date) VALUES (%s, %s, %s)',
                params=(client_id, membership_id, expiration_date)
            )

            return {
                "message": "The client has a membership now",
                "client_id": client_id,
                "membership_id": membership_id,
                "expiration_date": expiration_date
            }
        else:
            return {
                "message": "The client already has a membership",
                "client_id": client_id,
                "membership_id": client_membership["membership_id"],
                "expiration_date": client_membership["expiration_date"]
            }
    except Exception as e:
        raise HTTPException(status_code=400, detail="error to create membership")




