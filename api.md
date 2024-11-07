# Shared Types

```python
from twopir.types import Contract, Dimension, LlmResponse
```

# Inference

Methods:

- <code title="post /inference/run">client.inference.<a href="./src/twopir/resources/inference.py">run</a>(\*\*<a href="src/twopir/types/inference_run_params.py">params</a>) -> <a href="./src/twopir/types/shared/llm_response.py">LlmResponse</a></code>

# Data

Types:

```python
from twopir.types import DataGenerationStatus, InputEvaluationMetrics
```

## Inputs

Methods:

- <code title="post /data/input/evaluate">client.data.inputs.<a href="./src/twopir/resources/data/inputs.py">evaluate</a>(\*\*<a href="src/twopir/types/data/input_evaluate_params.py">params</a>) -> <a href="./src/twopir/types/input_evaluation_metrics.py">InputEvaluationMetrics</a></code>
- <code title="post /data/input/generate">client.data.inputs.<a href="./src/twopir/resources/data/inputs.py">generate</a>(\*\*<a href="src/twopir/types/data/input_generate_params.py">params</a>) -> <a href="./src/twopir/types/data_generation_status.py">DataGenerationStatus</a></code>
- <code title="get /data/input/generate/{job_id}">client.data.inputs.<a href="./src/twopir/resources/data/inputs.py">get</a>(job_id) -> <a href="./src/twopir/types/data_generation_status.py">DataGenerationStatus</a></code>

# Tune

Types:

```python
from twopir.types import OptimizationStatus
```

## Prompt

Methods:

- <code title="get /tune/prompt/{job_id}">client.tune.prompt.<a href="./src/twopir/resources/tune/prompt.py">get</a>(job_id) -> <a href="./src/twopir/types/optimization_status.py">OptimizationStatus</a></code>
- <code title="post /tune/prompt">client.tune.prompt.<a href="./src/twopir/resources/tune/prompt.py">optimize</a>(\*\*<a href="src/twopir/types/tune/prompt_optimize_params.py">params</a>) -> <a href="./src/twopir/types/optimization_status.py">OptimizationStatus</a></code>

# Experiment

Types:

```python
from twopir.types import ExperimentStatus
```

Methods:

- <code title="post /experiments">client.experiment.<a href="./src/twopir/resources/experiment.py">create</a>(\*\*<a href="src/twopir/types/experiment_create_params.py">params</a>) -> <a href="./src/twopir/types/experiment_status.py">ExperimentStatus</a></code>
- <code title="get /experiments/{job_id}">client.experiment.<a href="./src/twopir/resources/experiment.py">get</a>(job_id) -> <a href="./src/twopir/types/experiment_status.py">ExperimentStatus</a></code>

# Contract

Types:

```python
from twopir.types import ContractsScoreMetrics
```

Methods:

- <code title="post /contracts/calibrate">client.contract.<a href="./src/twopir/resources/contract/contract.py">calibrate</a>(\*\*<a href="src/twopir/types/contract_calibrate_params.py">params</a>) -> <a href="./src/twopir/types/shared/contract.py">Contract</a></code>
- <code title="post /contracts/generate_dimensions">client.contract.<a href="./src/twopir/resources/contract/contract.py">generate_dimensions</a>(\*\*<a href="src/twopir/types/contract_generate_dimensions_params.py">params</a>) -> <a href="./src/twopir/types/shared/contract.py">Contract</a></code>
- <code title="post /contracts/score">client.contract.<a href="./src/twopir/resources/contract/contract.py">score</a>(\*\*<a href="src/twopir/types/contract_score_params.py">params</a>) -> <a href="./src/twopir/types/contracts_score_metrics.py">ContractsScoreMetrics</a></code>

## Dimension

Methods:

- <code title="post /contracts/dimensions/generate">client.contract.dimension.<a href="./src/twopir/resources/contract/dimension.py">generate</a>(\*\*<a href="src/twopir/types/contract/dimension_generate_params.py">params</a>) -> <a href="./src/twopir/types/shared/dimension.py">Dimension</a></code>
- <code title="post /contracts/dimensions/score">client.contract.dimension.<a href="./src/twopir/resources/contract/dimension.py">score</a>(\*\*<a href="src/twopir/types/contract/dimension_score_params.py">params</a>) -> <a href="./src/twopir/types/contracts_score_metrics.py">ContractsScoreMetrics</a></code>
