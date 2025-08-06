# src/models/ensemble.py

import numpy as np

def ensemble_predictions(*predictions):
    """Average predictions from multiple models."""
    predictions = [np.array(pred) for pred in predictions]
    ensemble = np.mean(predictions, axis=0)
    return ensemble
