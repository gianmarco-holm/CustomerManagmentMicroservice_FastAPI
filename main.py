from fastapi import FastAPI, Request
from config.database import Base, engine
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from middlewares.error_handler import ErrorHandler
from routers.clienteRouter import cliente_router

app = FastAPI()
app.title = 'Servicio de Gestión de Clientes'
app.version = '0.0.1'

templates = Jinja2Templates(directory='templates')

app.include_router(cliente_router)
app.add_middleware(ErrorHandler)

Base.metadata.create_all(bind=engine)

@app.get('/', response_class=HTMLResponse, tags=['Home'])
def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})