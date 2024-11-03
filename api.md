# Shared Types

```python
from twopir.types import Contract, Dimension, LlmResponse
```

# Tune

Types:

```python
from twopir.types import PromptOptimizationStatus
```

# Experiment

Types:

```python
from twopir.types import ExperimentStatus
```

Methods:

- <code title="post /experiments/">client.experiment.<a href="./src/twopir/resources/experiment.py">create</a>(\*\*<a href="src/twopir/types/experiment_create_params.py">params</a>) -> <a href="./src/twopir/types/experiment_status.py">ExperimentStatus</a></code>
- <code title="get /experiments/{exp_id}">client.experiment.<a href="./src/twopir/resources/experiment.py">get</a>(exp_id) -> <a href="./src/twopir/types/experiment_status.py">ExperimentStatus</a></code>

# Contract

Types:

```python
from twopir.types import ResponseMetrics
```
