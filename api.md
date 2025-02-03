# Shared Types

```python
from withpi.types import Contract, Dimension, SubDimension
```

# Data

Types:

```python
from withpi.types import DataGenerationStatus, InputEvaluationMetrics
```

## Inputs

Types:

```python
from withpi.types.data import InputTopicCluster, InputClusterResponse
```

Methods:

- <code title="post /data/input/cluster">client.data.inputs.<a href="./src/withpi/resources/data/inputs/inputs.py">cluster</a>(\*\*<a href="src/withpi/types/data/input_cluster_params.py">params</a>) -> <a href="./src/withpi/types/data/input_cluster_response.py">InputClusterResponse</a></code>
- <code title="post /data/input/evaluate">client.data.inputs.<a href="./src/withpi/resources/data/inputs/inputs.py">evaluate</a>(\*\*<a href="src/withpi/types/data/input_evaluate_params.py">params</a>) -> <a href="./src/withpi/types/input_evaluation_metrics.py">InputEvaluationMetrics</a></code>
- <code title="post /data/input/generate_seeds">client.data.inputs.<a href="./src/withpi/resources/data/inputs/inputs.py">generate_seeds</a>(\*\*<a href="src/withpi/types/data/input_generate_seeds_params.py">params</a>) -> <a href="./src/withpi/types/data_generation_status.py">DataGenerationStatus</a></code>

### GenerateFromSeeds

Types:

```python
from withpi.types.data.inputs import GenerateFromSeedStreamMessagesResponse
```

Methods:

- <code title="get /data/input/generate_from_seeds/{job_id}">client.data.inputs.generate_from_seeds.<a href="./src/withpi/resources/data/inputs/generate_from_seeds.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/data_generation_status.py">DataGenerationStatus</a></code>
- <code title="post /data/input/generate_from_seeds">client.data.inputs.generate_from_seeds.<a href="./src/withpi/resources/data/inputs/generate_from_seeds.py">generate</a>(\*\*<a href="src/withpi/types/data/inputs/generate_from_seed_generate_params.py">params</a>) -> <a href="./src/withpi/types/data_generation_status.py">DataGenerationStatus</a></code>
- <code title="get /data/input/generate_from_seeds/{job_id}/messages">client.data.inputs.generate_from_seeds.<a href="./src/withpi/resources/data/inputs/generate_from_seeds.py">stream_messages</a>(job_id) -> str</code>

# Prompt

Types:

```python
from withpi.types import PromptOptimizationStatus, PromptStreamMessagesResponse
```

Methods:

- <code title="get /prompt/optimize/{job_id}">client.prompt.<a href="./src/withpi/resources/prompt.py">get_status</a>(job_id) -> <a href="./src/withpi/types/prompt_optimization_status.py">PromptOptimizationStatus</a></code>
- <code title="post /prompt/optimize">client.prompt.<a href="./src/withpi/resources/prompt.py">optimize</a>(\*\*<a href="src/withpi/types/prompt_optimize_params.py">params</a>) -> <a href="./src/withpi/types/prompt_optimization_status.py">PromptOptimizationStatus</a></code>
- <code title="get /prompt/optimize/{job_id}/messages">client.prompt.<a href="./src/withpi/resources/prompt.py">stream_messages</a>(job_id) -> str</code>

# Model

## Sft

Types:

```python
from withpi.types.model import SftStatus, SftStreamMessagesResponse
```

Methods:

- <code title="get /model/sft/{job_id}">client.model.sft.<a href="./src/withpi/resources/model/sft/sft.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/model/sft_status.py">SftStatus</a></code>
- <code title="post /model/sft">client.model.sft.<a href="./src/withpi/resources/model/sft/sft.py">start_job</a>(\*\*<a href="src/withpi/types/model/sft_start_job_params.py">params</a>) -> <a href="./src/withpi/types/model/sft_status.py">SftStatus</a></code>
- <code title="get /model/sft/{job_id}/messages">client.model.sft.<a href="./src/withpi/resources/model/sft/sft.py">stream_messages</a>(job_id) -> str</code>

### Messages

Types:

```python
from withpi.types.model.sft import MessageStreamResponse
```

Methods:

- <code title="get /model/sft/{job_id}/messages">client.model.sft.messages.<a href="./src/withpi/resources/model/sft/messages.py">stream</a>(job_id) -> str</code>

# Contracts

Types:

```python
from withpi.types import ContractsScoreMetrics, ContractWriteToHfResponse
```

Methods:

- <code title="post /contracts/generate_dimensions">client.contracts.<a href="./src/withpi/resources/contracts/contracts.py">generate_dimensions</a>(\*\*<a href="src/withpi/types/contract_generate_dimensions_params.py">params</a>) -> <a href="./src/withpi/types/shared/contract.py">Contract</a></code>
- <code title="post /contracts/read_from_hf">client.contracts.<a href="./src/withpi/resources/contracts/contracts.py">read_from_hf</a>(\*\*<a href="src/withpi/types/contract_read_from_hf_params.py">params</a>) -> <a href="./src/withpi/types/shared/contract.py">Contract</a></code>
- <code title="post /contracts/score">client.contracts.<a href="./src/withpi/resources/contracts/contracts.py">score</a>(\*\*<a href="src/withpi/types/contract_score_params.py">params</a>) -> <a href="./src/withpi/types/contracts_score_metrics.py">ContractsScoreMetrics</a></code>
- <code title="post /contracts/write_to_hf">client.contracts.<a href="./src/withpi/resources/contracts/contracts.py">write_to_hf</a>(\*\*<a href="src/withpi/types/contract_write_to_hf_params.py">params</a>) -> str</code>

## Calibrate

Types:

```python
from withpi.types.contracts import ContractCalibrationStatus, CalibrateStreamMessagesResponse
```

Methods:

- <code title="get /contracts/calibrate/{job_id}">client.contracts.calibrate.<a href="./src/withpi/resources/contracts/calibrate.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/contracts/contract_calibration_status.py">ContractCalibrationStatus</a></code>
- <code title="post /contracts/calibrate">client.contracts.calibrate.<a href="./src/withpi/resources/contracts/calibrate.py">start_job</a>(\*\*<a href="src/withpi/types/contracts/calibrate_start_job_params.py">params</a>) -> <a href="./src/withpi/types/contracts/contract_calibration_status.py">ContractCalibrationStatus</a></code>
- <code title="get /contracts/calibrate/{job_id}/messages">client.contracts.calibrate.<a href="./src/withpi/resources/contracts/calibrate.py">stream_messages</a>(job_id) -> str</code>

# Feedback

Types:

```python
from withpi.types import FeedbackTopicCluster, FeedbackClusterResponse
```

Methods:

- <code title="post /feedback/cluster">client.feedback.<a href="./src/withpi/resources/feedback.py">cluster</a>(\*\*<a href="src/withpi/types/feedback_cluster_params.py">params</a>) -> <a href="./src/withpi/types/feedback_cluster_response.py">FeedbackClusterResponse</a></code>
