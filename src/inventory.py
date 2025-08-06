# src/inventory.py

def calculate_reorder_point(forecast, lead_time, service_level=1.2):
    """Basic reorder point formula: demand * lead time * service buffer."""
    avg_demand = forecast.mean()
    return avg_demand * lead_time * service_level

def calculate_eoq(demand, ordering_cost, holding_cost):
    """Economic Order Quantity (EOQ) formula."""
    import numpy as np
    return np.sqrt((2 * demand * ordering_cost) / holding_cost)
