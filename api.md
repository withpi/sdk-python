# Shared Types

```python
from twopir.types import Contract, Dimension, SubDimension
```

# Inference

Types:

```python
from twopir.types import InferenceRunResponse
```

Methods:

- <code title="post /inference/run">client.inference.<a href="./src/twopir/resources/inference.py">run</a>(\*\*<a href="src/twopir/types/inference_run_params.py">params</a>) -> <a href="./src/twopir/types/inference_run_response.py">InferenceRunResponse</a></code>

# Data

Types:

```python
from twopir.types import DataGenerationStatus, InputEvaluationMetrics
```

## Inputs

Types:

```python
from twopir.types.data import DataGenerationStatus
```

Methods:

- <code title="post /data/input/evaluate">client.data.inputs.<a href="./src/twopir/resources/data/inputs/inputs.py">evaluate</a>(\*\*<a href="src/twopir/types/data/input_evaluate_params.py">params</a>) -> <a href="./src/twopir/types/input_evaluation_metrics.py">InputEvaluationMetrics</a></code>

### GenerateFromSeeds

Methods:

- <code title="get /data/input/generate_from_seeds/{job_id}">client.data.inputs.generate_from_seeds.<a href="./src/twopir/resources/data/inputs/generate_from_seeds/generate_from_seeds.py">retrieve</a>(job_id) -> <a href="./src/twopir/types/data_generation_status.py">DataGenerationStatus</a></code>

#### Messages

Types:

```python
from twopir.types.data.inputs.generate_from_seeds import MessageListResponse
```

Methods:

- <code title="get /data/input/generate_from_seeds/{job_id}/messages">client.data.inputs.generate_from_seeds.messages.<a href="./src/twopir/resources/data/inputs/generate_from_seeds/messages.py">list</a>(job_id) -> str</code>

# Tune

Types:

```python
from twopir.types import OptimizationStatus
```

## Prompt

Types:

```python
from twopir.types.tune import PromptGetDetailedMessagesResponse
```

Methods:

- <code title="get /tune/prompt/{job_id}/messages">client.tune.prompt.<a href="./src/twopir/resources/tune/prompt.py">get_detailed_messages</a>(job_id) -> str</code>
- <code title="get /tune/prompt/{job_id}">client.tune.prompt.<a href="./src/twopir/resources/tune/prompt.py">get_status</a>(job_id) -> <a href="./src/twopir/types/optimization_status.py">OptimizationStatus</a></code>
- <code title="post /tune/prompt">client.tune.prompt.<a href="./src/twopir/resources/tune/prompt.py">optimize</a>(\*\*<a href="src/twopir/types/tune/prompt_optimize_params.py">params</a>) -> <a href="./src/twopir/types/optimization_status.py">OptimizationStatus</a></code>

# Contracts

Types:

```python
from twopir.types import ContractsScoreMetrics
```

Methods:

- <code title="post /contracts/generate_dimensions">client.contracts.<a href="./src/twopir/resources/contracts/contracts.py">generate_dimensions</a>(\*\*<a href="src/twopir/types/contract_generate_dimensions_params.py">params</a>) -> <a href="./src/twopir/types/shared/contract.py">Contract</a></code>
- <code title="post /contracts/score">client.contracts.<a href="./src/twopir/resources/contracts/contracts.py">score</a>(\*\*<a href="src/twopir/types/contract_score_params.py">params</a>) -> <a href="./src/twopir/types/contracts_score_metrics.py">ContractsScoreMetrics</a></code>
