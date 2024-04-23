from fastapi import HTTPException
from app.services.db import gym_db

async def get_all_permissions():
        
        try:
            get_permissions = gym_db.fetch_all(
                sql='SELECT * FROM permissions'
            )
    
            if not get_permissions:
                raise HTTPException(status_code=404, detail='Permissions not found')
            
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=500, 
                detail='Error getting permissions'
            )
        
        return {
            'status': 'success',
            'message': 'Permissions retrieved successfully',
            'data': get_permissions
        }

async def get_permission(perm_id: int):
            
            try:
                get_permission = gym_db.fetch_one(
                    sql='SELECT * FROM permissions WHERE id = %s',
                    params=(perm_id,)
                )
        
                if not get_permission:
                    raise HTTPException(status_code=404, detail='Permission not found')
                
            except Exception as e:
                print(e)
                raise HTTPException(
                    status_code=500, 
                    detail='Error getting permission'
                )
            
            return {
                'status': 'success',
                'message': 'Permission retrieved successfully',
                'data': get_permission
            }