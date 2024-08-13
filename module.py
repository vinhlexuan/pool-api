from fastapi import FastAPI
from services.impl.pool import PoolServiceImpl
from controllers.pool import PoolController

class Module:
    def __init__(self) -> None:
        self.app = FastAPI()
        poolService = PoolServiceImpl()
        poolController = PoolController(poolService)
        self.app.include_router(poolController.router, tags=["pool"], prefix="/pool")