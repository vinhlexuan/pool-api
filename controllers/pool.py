from models.pool import PoolQueryReq, PoolQueryRes, PoolUpdateReq, PoolUpdateRes
from services.pool import PoolService
from fastapi import APIRouter

class PoolController:
    def __init__(self, poolService: PoolService) -> None:
        self.router = APIRouter()
        self.poolService = poolService
        self.router.post("/update", response_model=PoolUpdateRes, tags=["pool"])(self.update_pool)
        self.router.post("/query", response_model=PoolQueryRes, tags=["pool"])(self.query_pool)
    
    def update_pool(self, poolUpdateReq: PoolUpdateReq) -> PoolUpdateRes:
        return self.poolService.update_pool(poolUpdateReq)
    
    def query_pool(self, poolQueryReq: PoolQueryReq) -> PoolQueryRes:
        return self.poolService.query_pool(poolQueryReq)
