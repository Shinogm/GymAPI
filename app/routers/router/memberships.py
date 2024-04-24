from fastapi import APIRouter
from app.routers.controllers.membership import create, time, get, entry, delete

router = APIRouter(prefix='/memberships', tags=['membership'])

router.post('/membership/update/{client_id}')(create.have_membership)
router.get('/membership/check')(time.check_all_membership_is_out)
router.get('/membership/get')(get.get_all_clients_memeberships)
router.get('/membership/get/{client_id}')(get.get_all_client_membership)
router.get('/membership/entry/{membership_code}')(entry.get_all_clients_memeberships)
router.get('/membership/check/{code}')(time.check_all_membership_is_out_code)
#router.put('/membership/quit/{client_id}')(delete.quit_temporaly_membership)
router.delete('/membership/delete/{client_id}')(delete.delete_membership)

