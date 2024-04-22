from fastapi import APIRouter
from app.routers.controllers.user import create, get, modify, delete
from app.utils import login

router = APIRouter(prefix='/user', tags=['users'])

router.post('/user/login')(login.verify_password)



