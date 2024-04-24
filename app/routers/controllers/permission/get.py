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
from enum import Enum
class perms(Enum):
      ADMIN = 'admin'
      TRABAJADOR = 'trabajador'
      CLIENTE = 'cliente'

async def get_all_users_where_permission(perm_ENUM: perms):
            perm_id: int = 0
            async def get_users(permission_id: int):

                if permission_id == 1:
                    get_users = gym_db.fetch_all(
                        sql='SELECT * FROM worker_admins where permission_id = 1'
                    )
                if permission_id == 2:
                    get_users = gym_db.fetch_all(
                        sql='SELECT * FROM worker_admins where permission_id = 2'
                    )
                if permission_id == 3:
                     get_users = gym_db.fetch_all(
                        sql='SELECT * FROM clients where permission_id = 3'
                    )
                if permission_id not in [1, 2, 3]:
                    raise HTTPException(status_code=404, detail='Permission not found')
                return get_users
            try:
                if perm_ENUM == perms.ADMIN:
                    user_db = await get_users(
                         permission_id = 1
                    )
                if perm_ENUM == perms.TRABAJADOR:
                    user_db = await get_users(
                         permission_id = 2
                    )
                if perm_ENUM == perms.CLIENTE:
                    user_db = await get_users(
                         permission_id = 3
                    )

                
        
                if not user_db:
                    raise HTTPException(status_code=404, detail='Users not found')
                
            except Exception as e:
                print(e)
                raise HTTPException(
                    status_code=500, 
                    detail='Error getting users'
                )
            
            return {
                'status': 'success',
                'message': 'Users retrieved successfully',
                'data': user_db
            }