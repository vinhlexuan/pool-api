from typing import Protocol

from models.pool import PoolQueryReq, PoolQueryRes, PoolUpdateReq, PoolUpdateRes


class PoolService(Protocol):
    def update_pool(pool_update_req: PoolUpdateReq) -> PoolUpdateRes:...
    def query_pool(pool_query_req: PoolQueryReq) -> PoolQueryRes:...