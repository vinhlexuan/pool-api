from typing import Protocol

from models.pool import PoolQueryReq, PoolQueryRes, PoolUpdateReq, PoolUpdateRes


class PoolService(Protocol):
    def update_pool(poolUpdateReq: PoolUpdateReq) -> PoolUpdateRes:...
    def query_pool(poolQueryReq: PoolQueryReq) -> PoolQueryRes:...