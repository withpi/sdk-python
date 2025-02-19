# Shared Types

```python
from withpi.types import Contract, Dimension, SubDimension
```

# Data

Types:

```python
from withpi.types import DataGenerationStatus
```

## Inputs

Types:

```python
from withpi.types.data import InputTopicCluster, InputClusterResponse
```

Methods:

- <code title="post /data/input/cluster">client.data.inputs.<a href="./src/withpi/resources/data/inputs/inputs.py">cluster</a>(\*\*<a href="src/withpi/types/data/input_cluster_params.py">params</a>) -> <a href="./src/withpi/types/data/input_cluster_response.py">InputClusterResponse</a></code>

### GenerateFromSeeds

Types:

```python
from withpi.types.data.inputs import (
    GenerateFromSeedStreamDataResponse,
    GenerateFromSeedStreamMessagesResponse,
)
```

Methods:

- <code title="get /data/input/generate_from_seeds/{job_id}">client.data.inputs.generate_from_seeds.<a href="./src/withpi/resources/data/inputs/generate_from_seeds.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/data_generation_status.py">DataGenerationStatus</a></code>
- <code title="post /data/input/generate_from_seeds">client.data.inputs.generate_from_seeds.<a href="./src/withpi/resources/data/inputs/generate_from_seeds.py">generate</a>(\*\*<a href="src/withpi/types/data/inputs/generate_from_seed_generate_params.py">params</a>) -> <a href="./src/withpi/types/data_generation_status.py">DataGenerationStatus</a></code>
- <code title="get /data/input/generate_from_seeds/{job_id}/data">client.data.inputs.generate_from_seeds.<a href="./src/withpi/resources/data/inputs/generate_from_seeds.py">stream_data</a>(job_id) -> str</code>
- <code title="get /data/input/generate_from_seeds/{job_id}/messages">client.data.inputs.generate_from_seeds.<a href="./src/withpi/resources/data/inputs/generate_from_seeds.py">stream_messages</a>(job_id) -> str</code>

## GenerateSyntheticData

Types:

```python
from withpi.types.data import (
    GenerateSyntheticDataCreateResponse,
    GenerateSyntheticDataRetrieveResponse,
)
```

Methods:

- <code title="post /data/generate_synthetic_data">client.data.generate_synthetic_data.<a href="./src/withpi/resources/data/generate_synthetic_data/generate_synthetic_data.py">create</a>(\*\*<a href="src/withpi/types/data/generate_synthetic_data_create_params.py">params</a>) -> <a href="./src/withpi/types/data/generate_synthetic_data_create_response.py">GenerateSyntheticDataCreateResponse</a></code>
- <code title="get /data/generate_synthetic_data/{job_id}">client.data.generate_synthetic_data.<a href="./src/withpi/resources/data/generate_synthetic_data/generate_synthetic_data.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/data/generate_synthetic_data_retrieve_response.py">GenerateSyntheticDataRetrieveResponse</a></code>

### Data

Types:

```python
from withpi.types.data.generate_synthetic_data import DataListResponse
```

Methods:

- <code title="get /data/generate_synthetic_data/{job_id}/data">client.data.generate_synthetic_data.data.<a href="./src/withpi/resources/data/generate_synthetic_data/data.py">list</a>(job_id) -> <a href="./src/withpi/types/data/generate_synthetic_data/data_list_response.py">DataListResponse</a></code>

### Messages

Types:

```python
from withpi.types.data.generate_synthetic_data import MessageListResponse
```

Methods:

- <code title="get /data/generate_synthetic_data/{job_id}/messages">client.data.generate_synthetic_data.messages.<a href="./src/withpi/resources/data/generate_synthetic_data/messages.py">list</a>(job_id) -> str</code>

# Prompt

Types:

```python
from withpi.types import PromptOptimizationStatus, PromptStreamMessagesResponse
```

Methods:

- <code title="get /prompt/optimize/{job_id}">client.prompt.<a href="./src/withpi/resources/prompt.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/prompt_optimization_status.py">PromptOptimizationStatus</a></code>
- <code title="post /prompt/optimize">client.prompt.<a href="./src/withpi/resources/prompt.py">optimize</a>(\*\*<a href="src/withpi/types/prompt_optimize_params.py">params</a>) -> <a href="./src/withpi/types/prompt_optimization_status.py">PromptOptimizationStatus</a></code>
- <code title="get /prompt/optimize/{job_id}/messages">client.prompt.<a href="./src/withpi/resources/prompt.py">stream_messages</a>(job_id) -> str</code>

# Model

## Sft

Types:

```python
from withpi.types.model import (
    SftStatus,
    SftCheckResponse,
    SftLoadResponse,
    SftStreamMessagesResponse,
)
```

Methods:

- <code title="get /model/sft/{job_id}">client.model.sft.<a href="./src/withpi/resources/model/sft/sft.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/model/sft_status.py">SftStatus</a></code>
- <code title="get /model/sft/{job_id}/check">client.model.sft.<a href="./src/withpi/resources/model/sft/sft.py">check</a>(job_id) -> <a href="./src/withpi/types/model/sft_check_response.py">SftCheckResponse</a></code>
- <code title="post /model/sft/{job_id}/load">client.model.sft.<a href="./src/withpi/resources/model/sft/sft.py">load</a>(job_id) -> str</code>
- <code title="post /model/sft">client.model.sft.<a href="./src/withpi/resources/model/sft/sft.py">start_job</a>(\*\*<a href="src/withpi/types/model/sft_start_job_params.py">params</a>) -> <a href="./src/withpi/types/model/sft_status.py">SftStatus</a></code>
- <code title="get /model/sft/{job_id}/messages">client.model.sft.<a href="./src/withpi/resources/model/sft/sft.py">stream_messages</a>(job_id) -> str</code>

### ChatCompletions

Types:

```python
from withpi.types.model.sft import ChatCompletionListResponse
```

Methods:

- <code title="get /model/sft/{job_id}/chat/completions">client.model.sft.chat_completions.<a href="./src/withpi/resources/model/sft/chat_completions.py">list</a>(job_id) -> <a href="./src/withpi/types/model/sft/chat_completion_list_response.py">object</a></code>

### Completions

Types:

```python
from withpi.types.model.sft import CompletionListResponse
```

Methods:

- <code title="get /model/sft/{job_id}/completions">client.model.sft.completions.<a href="./src/withpi/resources/model/sft/completions.py">list</a>(job_id) -> <a href="./src/withpi/types/model/sft/completion_list_response.py">object</a></code>

## Rl

### Grpo

Types:

```python
from withpi.types.model.rl import (
    RlGrpoStatus,
    GrpoCheckResponse,
    GrpoLoadResponse,
    GrpoStreamMessagesResponse,
)
```

Methods:

- <code title="get /model/rl/grpo/{job_id}">client.model.rl.grpo.<a href="./src/withpi/resources/model/rl/grpo/grpo.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/rl_grpo_status.py">RlGrpoStatus</a></code>
- <code title="get /model/rl/grpo/{job_id}/check">client.model.rl.grpo.<a href="./src/withpi/resources/model/rl/grpo/grpo.py">check</a>(job_id) -> <a href="./src/withpi/types/model/rl/grpo_check_response.py">GrpoCheckResponse</a></code>
- <code title="post /model/rl/grpo/{job_id}/load">client.model.rl.grpo.<a href="./src/withpi/resources/model/rl/grpo/grpo.py">load</a>(job_id) -> str</code>
- <code title="post /model/rl/grpo">client.model.rl.grpo.<a href="./src/withpi/resources/model/rl/grpo/grpo.py">start_job</a>(\*\*<a href="src/withpi/types/model/rl/grpo_start_job_params.py">params</a>) -> <a href="./src/withpi/types/rl_grpo_status.py">RlGrpoStatus</a></code>
- <code title="get /model/rl/grpo/{job_id}/messages">client.model.rl.grpo.<a href="./src/withpi/resources/model/rl/grpo/grpo.py">stream_messages</a>(job_id) -> str</code>

#### ChatCompletions

Types:

```python
from withpi.types.model.rl.grpo import ChatCompletionListResponse
```

Methods:

- <code title="get /model/rl/grpo/{job_id}/chat/completions">client.model.rl.grpo.chat_completions.<a href="./src/withpi/resources/model/rl/grpo/chat_completions.py">list</a>(job_id) -> <a href="./src/withpi/types/model/rl/grpo/chat_completion_list_response.py">object</a></code>

#### Completions

Types:

```python
from withpi.types.model.rl.grpo import CompletionListResponse
```

Methods:

- <code title="get /model/rl/grpo/{job_id}/completions">client.model.rl.grpo.completions.<a href="./src/withpi/resources/model/rl/grpo/completions.py">list</a>(job_id) -> <a href="./src/withpi/types/model/rl/grpo/completion_list_response.py">object</a></code>

# Contracts

Types:

```python
from withpi.types import ContractsScoreMetrics
```

Methods:

- <code title="post /contracts/generate_dimensions">client.contracts.<a href="./src/withpi/resources/contracts/contracts.py">generate_dimensions</a>(\*\*<a href="src/withpi/types/contract_generate_dimensions_params.py">params</a>) -> <a href="./src/withpi/types/shared/contract.py">Contract</a></code>
- <code title="post /contracts/read_from_hf">client.contracts.<a href="./src/withpi/resources/contracts/contracts.py">read_from_hf</a>(\*\*<a href="src/withpi/types/contract_read_from_hf_params.py">params</a>) -> <a href="./src/withpi/types/shared/contract.py">Contract</a></code>
- <code title="post /contracts/score">client.contracts.<a href="./src/withpi/resources/contracts/contracts.py">score</a>(\*\*<a href="src/withpi/types/contract_score_params.py">params</a>) -> <a href="./src/withpi/types/contracts_score_metrics.py">ContractsScoreMetrics</a></code>

## Calibrate

Types:

```python
from withpi.types.contracts import ContractCalibrationStatus, CalibrateStreamMessagesResponse
```

Methods:

- <code title="get /contracts/calibrate/{job_id}">client.contracts.calibrate.<a href="./src/withpi/resources/contracts/calibrate.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/contracts/contract_calibration_status.py">ContractCalibrationStatus</a></code>
- <code title="post /contracts/calibrate">client.contracts.calibrate.<a href="./src/withpi/resources/contracts/calibrate.py">start_job</a>(\*\*<a href="src/withpi/types/contracts/calibrate_start_job_params.py">params</a>) -> <a href="./src/withpi/types/contracts/contract_calibration_status.py">ContractCalibrationStatus</a></code>
- <code title="get /contracts/calibrate/{job_id}/messages">client.contracts.calibrate.<a href="./src/withpi/resources/contracts/calibrate.py">stream_messages</a>(job_id) -> str</code>

# Queries

Types:

```python
from withpi.types import QueryGenerateFanoutsResponse
```

Methods:

- <code title="post /queries/generate_fanouts">client.queries.<a href="./src/withpi/resources/queries.py">generate_fanouts</a>(\*\*<a href="src/withpi/types/query_generate_fanouts_params.py">params</a>) -> <a href="./src/withpi/types/query_generate_fanouts_response.py">QueryGenerateFanoutsResponse</a></code>

# ModelRlGrpo

Types:

```python
from withpi.types import RlGrpoStatus
```
