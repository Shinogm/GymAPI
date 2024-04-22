from fastapi import APIRouter
from app.routers.controllers.membership import membership

router = APIRouter(prefix='/membership', tags=['membership'])

router.post('/membership/update/{client_id}')(membership.have_membership)
router.get('/membership/get/{client_id}')(membership.get_all_clients_memeberships)

