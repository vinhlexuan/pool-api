from pydantic import BaseModel

class BasePool(BaseModel):
    poolId: int
    poolValues: list[int]

class PoolUpdateReq(BasePool):
    ...

class PoolQueryReq(BaseModel):
    poolId: int
    percentile: float

class PoolUpdateRes(BaseModel):
    status: str
    pool: BasePool

class PoolQueryRes(BaseModel):
    quantile: float
    numOfElements: int