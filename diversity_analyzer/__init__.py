"""Data Diversity Analysis"""

import numpy as np

class DiversityMetrics:
    """Calculate diversity metrics for datasets."""
    
    def analyze(self, data: np.ndarray) -> dict:
        unique = len(np.unique(data))
        total = len(data)
        
        return {
            "unique_ratio": unique / total,
            "unique_count": unique,
            "total_samples": total,
            "status": "HEALTHY" if unique/total > 0.1 else "AT_RISK"
        }


__all__ = ["DiversityMetrics"]
