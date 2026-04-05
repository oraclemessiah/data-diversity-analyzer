# Data Diversity Analyzer

Tools for measuring and maintaining training data diversity.

## Importance

Diversity in training data directly correlates with model capability.
Low diversity leads to model collapse.

## Usage

```python
from diversity_analyzer import DiversityMetrics

dm = DiversityMetrics()
metrics = dm.analyze(dataset)
```