from fastapi import HTTPException
from app.services.db import gym_db
from datetime import datetime

async def comparar_fechas_y_calcular_dias_restantes(fecha_expiracion: str):
    try:
        # Convertir la cadena de fecha en un objeto datetime
        fecha_proporcionada = datetime.strptime(fecha_expiracion, "%Y-%m-%d")

        # Obtener la fecha y hora actual
        fecha_actual = datetime.now()
        
        # Calcular los días restantes
        dias_restantes = (fecha_proporcionada - fecha_actual).days
        print("Días restantes:", dias_restantes)
        
        
        # Comparar las fechas
        if fecha_proporcionada > fecha_actual:
            return {
                "message": f"Tu membresía expira el {fecha_proporcionada} y faltan {dias_restantes} días."
            }
        elif fecha_proporcionada < fecha_actual:
            dias_caducado = abs(dias_restantes)
            return {
                "message": f"Tu membresía expiró el {fecha_proporcionada} hace {dias_caducado} días."
            }
        else:
            return {
                "message": "Tu membresía caduca hoy."
            }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="error to compare dates")
    
    
async def check_all_membership_is_out():
    try:
        all_clients_data = []  # Lista para almacenar datos de todos los clientes
        all_memberships = gym_db.fetch_all(
            sql='SELECT * FROM is_membership'
        )
        if not all_memberships:
            raise HTTPException(status_code=404, detail='Memberships not found')
        
        for membership in all_memberships:
            client_data = {}
            print(membership['expiration_date'])
            response = await comparar_fechas_y_calcular_dias_restantes(str(membership['expiration_date']))
            client_data['membership'] = membership
            client_data['response'] = response
            # Obtener datos del cliente
            client_db = gym_db.fetch_one(
                sql='SELECT * FROM clients WHERE id = %s',
                params=(membership['client_id'],)
            )
            client_data['client'] = client_db
            all_clients_data.append(client_data)

        return {
            "message": "All memberships",
            "memberships": all_clients_data
        }



    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="error to check all memberships")
    
async def check_all_membership_is_out_code(code: int):
    try:
        # Check all memberships
        all_memberships = gym_db.fetch_all(
            sql='SELECT * FROM is_membership WHERE code_membership = %s',
            params=(code,)
        )
        if not all_memberships:
            raise HTTPException(status_code=404, detail='Memberships not found')
        
        for membership in all_memberships:
            print(membership['expiration_date'])
            response = await comparar_fechas_y_calcular_dias_restantes(str(membership['expiration_date']))
            client_db = gym_db.fetch_one(
                sql='SELECT * FROM clients WHERE id = %s',
                params=(membership['client_id'],)
            )
            
        return {
                "message": "verified membership by codeS",
                "memberships": client_db,
                "response": response
            }
    
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="error to check all memberships")
