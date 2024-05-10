from fastapi import FastAPI
from api.recommend import router as recommend_router
from db.database import es_client, close_elasticsearch
from py_eureka_client import eureka_client
from core.config import config

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print(await es_client.info())
    pass

@app.on_event("shutdown")
async def shutdown_event():
    await close_elasticsearch()
    
app.include_router(recommend_router)
