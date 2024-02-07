from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


board_router = APIRouter()

# jinja2 설정
templates = Jinja2Templates(directory='views/templates')
board_router.mount('/static', StaticFiles(directory='views/static'), name='static')


@board_router.get('/list', response_class=HTMLResponse)
def list(req: Request):
    return templates.TemplateResponse('board/list.html', {'request': req})


@board_router.get('/write', response_class=HTMLResponse)
def write(req: Request):
    return templates.TemplateResponse('board/write.html', {'request': req})


@board_router.get('/view', response_class=HTMLResponse)
def view(req: Request):
    return templates.TemplateResponse('board/view.html', {'request': req})

