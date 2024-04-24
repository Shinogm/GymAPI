from fastapi import HTTPException
from app.services.db import gym_db
from datetime import datetime, timedelta

async def have_membership(client_id: int, membership_month: int = 30):

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
        if client_membership is None:

            membership_id = 1
            expiration_date = datetime.now() + timedelta(days=membership_month)

            put_membership = gym_db.execute(
                sql='INSERT INTO is_membership (client_id, have_membership_id, expiration_date) VALUES (%s, %s, %s)',
                params=(client_id, membership_id, expiration_date)
            )

            client_db = gym_db.fetch_one(
                sql='SELECT * FROM clients WHERE id = %s',
                params=(client_id,)
            )

            return {
                "message": "The client has a membership now",
                "client_db": client_db,
                "membership_id": f'Tiene membresia',
                "expiration_date": expiration_date
            }

        

        get_client_db = gym_db.fetch_one(
            sql='SELECT * FROM clients WHERE id = %s',
            params=(client_id,)
        )
        return {
                    "message": "The client already has a membership",
                    "client_id": client_id,
                    "client_db": get_client_db

        }




