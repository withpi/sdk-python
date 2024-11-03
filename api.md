# Shared Types

```python
from twopir.types import Contract, Dimension, LlmResponse
```

# PromptOptimizationJob

Types:

```python
from twopir.types import PromptOptimizationStatus
```

Methods:

- <code title="get /prompt_optimizers/{optimizer_id}/optimize_job/{job_id}">client.prompt_optimization_job.<a href="./src/twopir/resources/prompt_optimization_job.py">get</a>(job_id, \*, optimizer_id) -> <a href="./src/twopir/types/prompt_optimization_status.py">PromptOptimizationStatus</a></code>
- <code title="post /prompt_optimizers/{optimizer_id}/optimize_job">client.prompt_optimization_job.<a href="./src/twopir/resources/prompt_optimization_job.py">optimize</a>(optimizer_id, \*\*<a href="src/twopir/types/prompt_optimization_job_optimize_params.py">params</a>) -> <a href="./src/twopir/types/prompt_optimization_status.py">PromptOptimizationStatus</a></code>

# Experiment

Types:

```python
from twopir.types import ExperimentStatus
```

Methods:

- <code title="post /experiments/">client.experiment.<a href="./src/twopir/resources/experiment.py">create</a>(\*\*<a href="src/twopir/types/experiment_create_params.py">params</a>) -> <a href="./src/twopir/types/experiment_status.py">ExperimentStatus</a></code>
- <code title="get /experiments/{exp_id}">client.experiment.<a href="./src/twopir/resources/experiment.py">get</a>(exp_id) -> <a href="./src/twopir/types/experiment_status.py">ExperimentStatus</a></code>

# Scorer

Types:

```python
from twopir.types import ResponseMetric
```

Methods:

- <code title="post /scorers/{scorer_id}">client.scorer.<a href="./src/twopir/resources/scorer.py">score</a>(scorer_id, \*\*<a href="src/twopir/types/scorer_score_params.py">params</a>) -> <a href="./src/twopir/types/response_metric.py">ResponseMetric</a></code>
