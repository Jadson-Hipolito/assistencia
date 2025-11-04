from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from assistencia_tecnica.api.schemas.routers import interface, cliente, funcionario, equipamento

app = FastAPI(title="Assistência Técnica")

# Inclui os routers
app.include_router(interface.router)
app.include_router(cliente.router)
app.include_router(funcionario.router)
app.include_router(equipamento.router)

# Monta a pasta de arquivos estáticos
app.mount("/static", StaticFiles(directory="assistencia_tecnica/static"), name="static")