from fastapi import APIRouter
from app.routers.controllers.user import create, get, modify, delete
from app.utils import login

router = APIRouter(prefix='/users', tags=['users'])

router.post('/user/create')(create.create_user)
router.post('/user/login')(login.verify_password)
router.get('/user/get')(get.get_all_users)
router.get('/user/get/{user_id}')(get.get_user)
router.put('/user/modify/{user_id}')(modify.modify_user)
router.put('/user/modify/permission/{user_id}')(modify.modify_user_permission)

router.delete('/user/delete/{user_id}')(delete.delete_user)




