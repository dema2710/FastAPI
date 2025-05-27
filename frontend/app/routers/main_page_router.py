from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get('/')
async def index(request: Request):
    context = {"request": request, "data": 123}
    response = templates.TemplateResponse("index.html", context=context)
    return response


@router.get('/login')
@router.post('/login')
async def login(request: Request, user_email: str = Form(''), password: str = Form('')):
    print(request.method, 333333)
    print(f"{user_email}")
    print(f"{password}")
    context = {"request": request}
    response = templates.TemplateResponse("index.html", context=context)
    return response