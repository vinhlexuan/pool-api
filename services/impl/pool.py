from models.pool import BasePool, PoolQueryReq, PoolQueryRes, PoolUpdateReq, PoolUpdateRes
from services.pool import PoolService
from data import poolData


class PoolServiceImpl(PoolService):
    def update_pool(self, poolUpdateReq: PoolUpdateReq) -> PoolUpdateRes:
        id = poolUpdateReq.poolId
        if id in poolData:
            status = "appended"
            poolData[id].extend(poolUpdateReq.poolValues)
        else:
            status = "inserted"
            poolData[id] = poolUpdateReq.poolValues

        return PoolUpdateRes(
            status=status,
            pool=BasePool(
                poolId=id,
                poolValues=poolData[id]
            )
        ) 
    
    def query_pool(self, poolQueryReq: PoolQueryReq) -> PoolQueryRes:
        id = poolQueryReq.poolId
        values = poolData[id]
        quantile = self._calculate_quantile(values, poolQueryReq.percentile)
        return PoolQueryRes(
            quantile=quantile,
            numOfElements=len(poolData[id])
        )
    
    def _calculate_quantile(self, values: list[int], percentile: float):
        if not values:
            raise Exception()
        size = len(values)
        if size == 1:
            return values[0]
        values.sort()
        idx = (size - 1) * (percentile / 100) + 1
        integer_part = int(idx)
        decimal_part = round(idx - integer_part, 2)
        quantile = values[integer_part - 1] * (1 - decimal_part) + values[integer_part] * decimal_part
        return quantile