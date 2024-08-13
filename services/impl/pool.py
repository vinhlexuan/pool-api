from models.pool import BasePool, PoolQueryReq, PoolQueryRes, PoolUpdateReq, PoolUpdateRes
from services.pool import PoolService
from utils.file_data import load_data, save_data
from utils.lru_cache import LRUCache

class PoolServiceImpl(PoolService):
    def __init__(self) -> None:
        self.cache = LRUCache(3)

    def update_pool(self, pool_update_req: PoolUpdateReq) -> PoolUpdateRes:
        id = pool_update_req.poolId
        pools = load_data()
        if str(id) in pools:
            status = "appended"
            pools[str(id)].extend(pool_update_req.poolValues)
        else:
            status = "inserted"
            pools[str(id)] = pool_update_req.poolValues
        self.cache.put(id, pools[str(id)])
        save_data(pools)
        return PoolUpdateRes(
            status=status,
            pool=BasePool(
                poolId=id,
                poolValues=pools[str(id)]
            )
        ) 
    
    def query_pool(self, pool_query_req: PoolQueryReq) -> PoolQueryRes:
        id = pool_query_req.poolId
        values = self.cache.get(id)
        if not values:
            pools = load_data()
            values = pools[str(id)]
            self.cache.put(id, values)
        quantile = self.calculate_quantile(values, pool_query_req.percentile)
        return PoolQueryRes(
            quantile=quantile,
            numOfElements=len(values)
        )
    
    def calculate_quantile(self, values: list[int], percentile: float) -> float:
        if not values:
            raise ValueError("Values must not be empty!")
        size = len(values)
        if size == 1:
            return values[0]
        values.sort()
        idx = (size - 1) * (percentile / 100) + 1
        integer_part = int(idx)
        decimal_part = idx - integer_part
        quantile = round(values[integer_part - 1] * (1 - decimal_part) + values[integer_part] * decimal_part, 2)
        return quantile