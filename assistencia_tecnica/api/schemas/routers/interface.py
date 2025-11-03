from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

# Router para interface web
router = APIRouter(tags=["Interface"])

# Configuração dos templates
templates = Jinja2Templates(directory="assistencia_tecnica/templates")

# Redireciona a raiz para o painel
@router.get("/", include_in_schema=False)
def raiz():
    return RedirectResponse(url="/painel")

# Página inicial do sistema
@router.get("/painel", response_class=HTMLResponse)
def painel(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Página de clientes
@router.get("/clientes/ui", response_class=HTMLResponse)
def clientes_ui(request: Request):
    return templates.TemplateResponse("cliente.html", {"request": request})

# Página de funcionários
@router.get("/funcionarios/ui", response_class=HTMLResponse)
def funcionarios_ui(request: Request):
    return templates.TemplateResponse("funcionario.html", {"request": request})

# Página de equipamentos
@router.get("/equipamentos/ui", response_class=HTMLResponse)
def equipamentos_ui(request: Request):
    return templates.TemplateResponse("equipamento.html", {"request": request})

# Página de ordens de serviço
@router.get("/ordens/ui", response_class=HTMLResponse)
def ordens_ui(request: Request):
    return templates.TemplateResponse("ordem_servico.html", {"request": request})

# Página de visitas técnicas
@router.get("/visitas/ui", response_class=HTMLResponse)
def visitas_ui(request: Request):
    return templates.TemplateResponse("visita_tecnica.html", {"request": request})

# Página de contas
@router.get("/contas/ui", response_class=HTMLResponse)
def contas_ui(request: Request):
    return templates.TemplateResponse("conta.html", {"request": request})
