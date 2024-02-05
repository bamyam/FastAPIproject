from fastapi import APIRouter
from fastapi.responses import HTMLResponse

board_router = APIRouter()

@board_router.get('/list', response_class=HTMLResponse)
def join() :
    return {'msg':'Hello, board list!'}


@board_router.get('/write', response_class=HTMLResponse)
def join() :
    return {'msg':'Hello, board write!'}


@board_router.get('/view', response_class=HTMLResponse)
def join() :
    return {'msg':'Hello, board view!'}

