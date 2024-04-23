from fastapi import APIRouter
from app.routers.controllers.membership import create

router = APIRouter(prefix='/membership', tags=['membership'])

router.post('/membership/update/{client_id}')(create.have_membership)

