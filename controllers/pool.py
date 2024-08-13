from models.pool import PoolQueryReq, PoolQueryRes, PoolUpdateReq, PoolUpdateRes
from services.pool import PoolService
from fastapi import APIRouter

class PoolController:
    def __init__(self, pool_service: PoolService) -> None:
        self.router = APIRouter()
        self.pool_service = pool_service
        self.router.post("/update", response_model=PoolUpdateRes, tags=["pool"])(self.update_pool)
        self.router.post("/query", response_model=PoolQueryRes, tags=["pool"])(self.query_pool)
    
    def update_pool(self, pool_update_req: PoolUpdateReq) -> PoolUpdateRes:
        return self.pool_service.update_pool(pool_update_req)
    
    def query_pool(self, pool_query_req: PoolQueryReq) -> PoolQueryRes:
        return self.pool_service.query_pool(pool_query_req)
