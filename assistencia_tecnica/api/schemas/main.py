from fastapi import FastAPI
from .routers import cliente, funcionario, equipamento, ordem_servico, visita_tecnica, conta
from assistencia_tecnica.web import router as web_router

app = FastAPI(title="Assistência Técnica API")

# API routers
app.include_router(cliente.router)
app.include_router(funcionario.router)
app.include_router(equipamento.router)
app.include_router(ordem_servico.router)
app.include_router(visita_tecnica.router)
app.include_router(conta.router)

# UI router
app.include_router(web_router)

@app.get("/")
def home():
    return {"mensagem": "Bem-vindo à API de Assistência Técnica 🚀"}