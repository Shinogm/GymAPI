from fastapi import APIRouter
from app.routers.controllers.client import create, get, modify, delete

router = APIRouter(prefix='/clients', tags=['clients'])

router.post('/create')(create.create_client)
router.get('/get')(get.get_all_clients)
router.put('/modify/{client_id}')(modify.modify_client)
router.delete('/delete/{client_id}')(delete.delete_client)

