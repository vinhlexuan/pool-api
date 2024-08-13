from fastapi import FastAPI
from services.impl.pool import PoolServiceImpl
from controllers.pool import PoolController

class Module:
    def __init__(self) -> None:
        self.app = FastAPI()
        pool_service = PoolServiceImpl()
        pool_controller = PoolController(pool_service)
        self.app.include_router(pool_controller.router, tags=["pool"], prefix="/pool")