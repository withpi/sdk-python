# Shared Types

```python
from twopir.types import Contract, Dimension, SubDimension
```

# Data

Types:

```python
from twopir.types import DataGenerationStatus, InputEvaluationMetrics
```

## Inputs

Types:

```python
from twopir.types.data import InputTopicCluster, InputClusterResponse
```

Methods:

- <code title="post /data/input/cluster">client.data.inputs.<a href="./src/twopir/resources/data/inputs/inputs.py">cluster</a>(\*\*<a href="src/twopir/types/data/input_cluster_params.py">params</a>) -> <a href="./src/twopir/types/data/input_cluster_response.py">InputClusterResponse</a></code>
- <code title="post /data/input/evaluate">client.data.inputs.<a href="./src/twopir/resources/data/inputs/inputs.py">evaluate</a>(\*\*<a href="src/twopir/types/data/input_evaluate_params.py">params</a>) -> <a href="./src/twopir/types/input_evaluation_metrics.py">InputEvaluationMetrics</a></code>
- <code title="post /data/input/generate_seeds">client.data.inputs.<a href="./src/twopir/resources/data/inputs/inputs.py">generate_seeds</a>(\*\*<a href="src/twopir/types/data/input_generate_seeds_params.py">params</a>) -> <a href="./src/twopir/types/data_generation_status.py">DataGenerationStatus</a></code>

### GenerateFromSeeds

Types:

```python
from twopir.types.data.inputs import GenerateFromSeedStreamMessagesResponse
```

Methods:

- <code title="get /data/input/generate_from_seeds/{job_id}">client.data.inputs.generate_from_seeds.<a href="./src/twopir/resources/data/inputs/generate_from_seeds.py">retrieve</a>(job_id) -> <a href="./src/twopir/types/data_generation_status.py">DataGenerationStatus</a></code>
- <code title="post /data/input/generate_from_seeds">client.data.inputs.generate_from_seeds.<a href="./src/twopir/resources/data/inputs/generate_from_seeds.py">generate</a>(\*\*<a href="src/twopir/types/data/inputs/generate_from_seed_generate_params.py">params</a>) -> <a href="./src/twopir/types/data_generation_status.py">DataGenerationStatus</a></code>
- <code title="get /data/input/generate_from_seeds/{job_id}/messages">client.data.inputs.generate_from_seeds.<a href="./src/twopir/resources/data/inputs/generate_from_seeds.py">stream_messages</a>(job_id) -> str</code>

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

- <code title="post /contracts/generate_dimensions">client.contracts.<a href="./src/twopir/resources/contracts.py">generate_dimensions</a>(\*\*<a href="src/twopir/types/contract_generate_dimensions_params.py">params</a>) -> <a href="./src/twopir/types/shared/contract.py">Contract</a></code>
- <code title="post /contracts/score">client.contracts.<a href="./src/twopir/resources/contracts.py">score</a>(\*\*<a href="src/twopir/types/contract_score_params.py">params</a>) -> <a href="./src/twopir/types/contracts_score_metrics.py">ContractsScoreMetrics</a></code>

# Feedback

Types:

```python
from twopir.types import FeedbackTopicCluster, FeedbackClusterResponse
```

Methods:

- <code title="post /feedback/cluster">client.feedback.<a href="./src/twopir/resources/feedback.py">cluster</a>(\*\*<a href="src/twopir/types/feedback_cluster_params.py">params</a>) -> <a href="./src/twopir/types/feedback_cluster_response.py">FeedbackClusterResponse</a></code>
