from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from assistencia_tecnica.api.schemas.routers import interface

# Cria a aplicação FastAPI
app = FastAPI(title="Assistência Técnica")

# Inclui o router de interface (HTML)
app.include_router(interface.router)

# Monta a pasta de arquivos estáticos (CSS, JS, imagens)
app.mount("/static", StaticFiles(directory="assistencia_tecnica/static"), name="static")