from fastapi import APIRouter

board_router = APIRouter()

@board_router.get('/list')
def join() :
    return {'msg':'Hello, board list!'}


@board_router.get('/write')
def join() :
    return {'msg':'Hello, board write!'}


@board_router.get('/view')
def join() :
    return {'msg':'Hello, board view!'}

