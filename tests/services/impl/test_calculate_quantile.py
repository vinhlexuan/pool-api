import sys
sys.path.append(".")
from services.impl.pool import PoolServiceImpl
import numpy as np

def test_calculate_quantile_success():
    mock_values = [1,2,3,4,5,6,7,8]
    mock_percentile = 50.5
    pool_service = PoolServiceImpl()
    result = pool_service.calculate_quantile(mock_values, mock_percentile)
    expect =  round(np.quantile(mock_values, mock_percentile / 100), 2)
    assert result == expect

def test_calculate_quantile_with_empty_values():
    mock_values = []
    mock_percentile = 50.5
    pool_service = PoolServiceImpl()
    try:
        pool_service.calculate_quantile(mock_values, mock_percentile)
    except ValueError as e:
        assert str(e) == "Values must not be empty!"
    else:
        assert False, "Expected ValueError not raised"
    