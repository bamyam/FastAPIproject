from fastapi import APIRouter

member_router = APIRouter()

@member_router.get('/join')
def join() :
    return {'msg':'Hello, Join!'}


@member_router.get('/login')
def join() :
    return {'msg':'Hello, login!'}


@member_router.get('/myinfo')
def join() :
    return {'msg':'Hello, Myinfo!'}

