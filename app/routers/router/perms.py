from fastapi import APIRouter
from app.routers.controllers.permission import get

router = APIRouter(prefix='/user', tags=['users'])

router.get('/user/permissions')(get.get_all_permissions)
router.get('/user/permissions/{perm_id}')(get.get_permission)

