from fastapi import APIRouter


MAIN_ROUTER = APIRouter()



@MAIN_ROUTER.get('/test')
def test():
    return {'message': 'This is the main router. It looks like it is working.'}
