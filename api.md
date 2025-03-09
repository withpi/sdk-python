# Shared Types

```python
from withpi.types import (
    Contract,
    ContractCalibrationStatus,
    DataGenerationStatus,
    Dimension,
    DimensionScoringType,
    Example,
    ExplorationMode,
    LoraConfig,
    PromptOptimizationStatus,
    QueryClassificationResponse,
    QueryFanoutExample,
    RlGrpoStatus,
    SftStatus,
    State,
    SubDimension,
    SyntheticDataStatus,
    TrainedModel,
)
```

# Data

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
    GenerateFromSeedCancelResponse,
    GenerateFromSeedListJobsResponse,
    GenerateFromSeedStreamDataResponse,
    GenerateFromSeedStreamMessagesResponse,
)
```

Methods:

- <code title="get /data/input/generate_from_seeds/{job_id}">client.data.inputs.generate_from_seeds.<a href="./src/withpi/resources/data/inputs/generate_from_seeds.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/shared/data_generation_status.py">DataGenerationStatus</a></code>
- <code title="delete /data/input/generate_from_seeds/{job_id}">client.data.inputs.generate_from_seeds.<a href="./src/withpi/resources/data/inputs/generate_from_seeds.py">cancel</a>(job_id) -> str</code>
- <code title="post /data/input/generate_from_seeds">client.data.inputs.generate_from_seeds.<a href="./src/withpi/resources/data/inputs/generate_from_seeds.py">generate</a>(\*\*<a href="src/withpi/types/data/inputs/generate_from_seed_generate_params.py">params</a>) -> <a href="./src/withpi/types/shared/data_generation_status.py">DataGenerationStatus</a></code>
- <code title="get /data/input/generate_from_seeds">client.data.inputs.generate_from_seeds.<a href="./src/withpi/resources/data/inputs/generate_from_seeds.py">list_jobs</a>(\*\*<a href="src/withpi/types/data/inputs/generate_from_seed_list_jobs_params.py">params</a>) -> <a href="./src/withpi/types/data/inputs/generate_from_seed_list_jobs_response.py">GenerateFromSeedListJobsResponse</a></code>
- <code title="get /data/input/generate_from_seeds/{job_id}/data">client.data.inputs.generate_from_seeds.<a href="./src/withpi/resources/data/inputs/generate_from_seeds.py">stream_data</a>(job_id) -> str</code>
- <code title="get /data/input/generate_from_seeds/{job_id}/messages">client.data.inputs.generate_from_seeds.<a href="./src/withpi/resources/data/inputs/generate_from_seeds.py">stream_messages</a>(job_id) -> str</code>

## GenerateSyntheticData

Types:

```python
from withpi.types.data import (
    GenerateSyntheticDataCancelResponse,
    GenerateSyntheticDataListJobsResponse,
    GenerateSyntheticDataStreamDataResponse,
    GenerateSyntheticDataStreamMessagesResponse,
)
```

Methods:

- <code title="post /data/generate_synthetic_data">client.data.generate_synthetic_data.<a href="./src/withpi/resources/data/generate_synthetic_data.py">create</a>(\*\*<a href="src/withpi/types/data/generate_synthetic_data_create_params.py">params</a>) -> <a href="./src/withpi/types/shared/synthetic_data_status.py">SyntheticDataStatus</a></code>
- <code title="get /data/generate_synthetic_data/{job_id}">client.data.generate_synthetic_data.<a href="./src/withpi/resources/data/generate_synthetic_data.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/shared/synthetic_data_status.py">SyntheticDataStatus</a></code>
- <code title="delete /data/generate_synthetic_data/{job_id}">client.data.generate_synthetic_data.<a href="./src/withpi/resources/data/generate_synthetic_data.py">cancel</a>(job_id) -> str</code>
- <code title="get /data/generate_synthetic_data">client.data.generate_synthetic_data.<a href="./src/withpi/resources/data/generate_synthetic_data.py">list_jobs</a>(\*\*<a href="src/withpi/types/data/generate_synthetic_data_list_jobs_params.py">params</a>) -> <a href="./src/withpi/types/data/generate_synthetic_data_list_jobs_response.py">GenerateSyntheticDataListJobsResponse</a></code>
- <code title="get /data/generate_synthetic_data/{job_id}/data">client.data.generate_synthetic_data.<a href="./src/withpi/resources/data/generate_synthetic_data.py">stream_data</a>(job_id) -> <a href="./src/withpi/types/data/generate_synthetic_data_stream_data_response.py">GenerateSyntheticDataStreamDataResponse</a></code>
- <code title="get /data/generate_synthetic_data/{job_id}/messages">client.data.generate_synthetic_data.<a href="./src/withpi/resources/data/generate_synthetic_data.py">stream_messages</a>(job_id) -> str</code>

# Prompt

Types:

```python
from withpi.types import (
    PromptCancelOptimizationJobResponse,
    PromptListOptimizationJobsResponse,
    PromptStreamMessagesResponse,
)
```

Methods:

- <code title="get /prompt/optimize/{job_id}">client.prompt.<a href="./src/withpi/resources/prompt.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/shared/prompt_optimization_status.py">PromptOptimizationStatus</a></code>
- <code title="delete /prompt/optimize/{job_id}">client.prompt.<a href="./src/withpi/resources/prompt.py">cancel_optimization_job</a>(job_id) -> str</code>
- <code title="get /prompt/optimize">client.prompt.<a href="./src/withpi/resources/prompt.py">list_optimization_jobs</a>(\*\*<a href="src/withpi/types/prompt_list_optimization_jobs_params.py">params</a>) -> <a href="./src/withpi/types/prompt_list_optimization_jobs_response.py">PromptListOptimizationJobsResponse</a></code>
- <code title="post /prompt/optimize">client.prompt.<a href="./src/withpi/resources/prompt.py">optimize</a>(\*\*<a href="src/withpi/types/prompt_optimize_params.py">params</a>) -> <a href="./src/withpi/types/shared/prompt_optimization_status.py">PromptOptimizationStatus</a></code>
- <code title="get /prompt/optimize/{job_id}/messages">client.prompt.<a href="./src/withpi/resources/prompt.py">stream_messages</a>(job_id) -> str</code>

# Model

## Sft

Types:

```python
from withpi.types.model import (
    SftListResponse,
    SftCancelResponse,
    SftDownloadResponse,
    SftStreamMessagesResponse,
)
```

Methods:

- <code title="get /model/sft/{job_id}">client.model.sft.<a href="./src/withpi/resources/model/sft.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/shared/sft_status.py">SftStatus</a></code>
- <code title="get /model/sft">client.model.sft.<a href="./src/withpi/resources/model/sft.py">list</a>(\*\*<a href="src/withpi/types/model/sft_list_params.py">params</a>) -> <a href="./src/withpi/types/model/sft_list_response.py">SftListResponse</a></code>
- <code title="delete /model/sft/{job_id}">client.model.sft.<a href="./src/withpi/resources/model/sft.py">cancel</a>(job_id) -> str</code>
- <code title="post /model/sft/{job_id}/download">client.model.sft.<a href="./src/withpi/resources/model/sft.py">download</a>(job_id, \*\*<a href="src/withpi/types/model/sft_download_params.py">params</a>) -> str</code>
- <code title="post /model/sft/{job_id}/load">client.model.sft.<a href="./src/withpi/resources/model/sft.py">load</a>(job_id) -> <a href="./src/withpi/types/shared/sft_status.py">SftStatus</a></code>
- <code title="post /model/sft">client.model.sft.<a href="./src/withpi/resources/model/sft.py">start_job</a>(\*\*<a href="src/withpi/types/model/sft_start_job_params.py">params</a>) -> <a href="./src/withpi/types/shared/sft_status.py">SftStatus</a></code>
- <code title="get /model/sft/{job_id}/messages">client.model.sft.<a href="./src/withpi/resources/model/sft.py">stream_messages</a>(job_id) -> str</code>

## Rl

### Grpo

Types:

```python
from withpi.types.model.rl import (
    GrpoListResponse,
    GrpoCancelResponse,
    GrpoDownloadResponse,
    GrpoStreamMessagesResponse,
)
```

Methods:

- <code title="get /model/rl/grpo/{job_id}">client.model.rl.grpo.<a href="./src/withpi/resources/model/rl/grpo.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/shared/rl_grpo_status.py">RlGrpoStatus</a></code>
- <code title="get /model/rl/grpo">client.model.rl.grpo.<a href="./src/withpi/resources/model/rl/grpo.py">list</a>(\*\*<a href="src/withpi/types/model/rl/grpo_list_params.py">params</a>) -> <a href="./src/withpi/types/model/rl/grpo_list_response.py">GrpoListResponse</a></code>
- <code title="delete /model/rl/grpo/{job_id}">client.model.rl.grpo.<a href="./src/withpi/resources/model/rl/grpo.py">cancel</a>(job_id) -> str</code>
- <code title="post /model/rl/grpo/{job_id}/download">client.model.rl.grpo.<a href="./src/withpi/resources/model/rl/grpo.py">download</a>(job_id, \*\*<a href="src/withpi/types/model/rl/grpo_download_params.py">params</a>) -> str</code>
- <code title="post /model/rl/grpo/{job_id}/load">client.model.rl.grpo.<a href="./src/withpi/resources/model/rl/grpo.py">load</a>(job_id) -> <a href="./src/withpi/types/shared/rl_grpo_status.py">RlGrpoStatus</a></code>
- <code title="post /model/rl/grpo">client.model.rl.grpo.<a href="./src/withpi/resources/model/rl/grpo.py">start_job</a>(\*\*<a href="src/withpi/types/model/rl/grpo_start_job_params.py">params</a>) -> <a href="./src/withpi/types/shared/rl_grpo_status.py">RlGrpoStatus</a></code>
- <code title="get /model/rl/grpo/{job_id}/messages">client.model.rl.grpo.<a href="./src/withpi/resources/model/rl/grpo.py">stream_messages</a>(job_id) -> str</code>

## Classifier

Types:

```python
from withpi.types.model import (
    ClassifierCreateResponse,
    ClassifierRetrieveResponse,
    ClassifierListResponse,
    ClassifierCancelResponse,
    ClassifierDownloadResponse,
    ClassifierMessagesResponse,
)
```

Methods:

- <code title="post /model/classifier">client.model.classifier.<a href="./src/withpi/resources/model/classifier.py">create</a>(\*\*<a href="src/withpi/types/model/classifier_create_params.py">params</a>) -> <a href="./src/withpi/types/model/classifier_create_response.py">ClassifierCreateResponse</a></code>
- <code title="get /model/classifier/{job_id}">client.model.classifier.<a href="./src/withpi/resources/model/classifier.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/model/classifier_retrieve_response.py">ClassifierRetrieveResponse</a></code>
- <code title="get /model/classifier">client.model.classifier.<a href="./src/withpi/resources/model/classifier.py">list</a>(\*\*<a href="src/withpi/types/model/classifier_list_params.py">params</a>) -> <a href="./src/withpi/types/model/classifier_list_response.py">ClassifierListResponse</a></code>
- <code title="delete /model/classifier/{job_id}">client.model.classifier.<a href="./src/withpi/resources/model/classifier.py">cancel</a>(job_id) -> str</code>
- <code title="post /model/classifier/{job_id}/download">client.model.classifier.<a href="./src/withpi/resources/model/classifier.py">download</a>(job_id, \*\*<a href="src/withpi/types/model/classifier_download_params.py">params</a>) -> str</code>
- <code title="get /model/classifier/{job_id}/messages">client.model.classifier.<a href="./src/withpi/resources/model/classifier.py">messages</a>(job_id) -> str</code>

# Contracts

Types:

```python
from withpi.types import ContractScoreResponse
```

Methods:

- <code title="post /contracts/generate_dimensions">client.contracts.<a href="./src/withpi/resources/contracts/contracts.py">generate_dimensions</a>(\*\*<a href="src/withpi/types/contract_generate_dimensions_params.py">params</a>) -> <a href="./src/withpi/types/shared/contract.py">Contract</a></code>
- <code title="post /contracts/read_from_hf">client.contracts.<a href="./src/withpi/resources/contracts/contracts.py">read_from_hf</a>(\*\*<a href="src/withpi/types/contract_read_from_hf_params.py">params</a>) -> <a href="./src/withpi/types/shared/contract.py">Contract</a></code>
- <code title="post /contracts/score">client.contracts.<a href="./src/withpi/resources/contracts/contracts.py">score</a>(\*\*<a href="src/withpi/types/contract_score_params.py">params</a>) -> <a href="./src/withpi/types/contract_score_response.py">ContractScoreResponse</a></code>

## Calibrate

Types:

```python
from withpi.types.contracts import (
    CalibrateListResponse,
    CalibrateCancelResponse,
    CalibrateStreamMessagesResponse,
)
```

Methods:

- <code title="get /contracts/calibrate/{job_id}">client.contracts.calibrate.<a href="./src/withpi/resources/contracts/calibrate.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/shared/contract_calibration_status.py">ContractCalibrationStatus</a></code>
- <code title="get /contracts/calibrate">client.contracts.calibrate.<a href="./src/withpi/resources/contracts/calibrate.py">list</a>(\*\*<a href="src/withpi/types/contracts/calibrate_list_params.py">params</a>) -> <a href="./src/withpi/types/contracts/calibrate_list_response.py">CalibrateListResponse</a></code>
- <code title="delete /contracts/calibrate/{job_id}">client.contracts.calibrate.<a href="./src/withpi/resources/contracts/calibrate.py">cancel</a>(job_id) -> str</code>
- <code title="post /contracts/calibrate">client.contracts.calibrate.<a href="./src/withpi/resources/contracts/calibrate.py">start_job</a>(\*\*<a href="src/withpi/types/contracts/calibrate_start_job_params.py">params</a>) -> <a href="./src/withpi/types/shared/contract_calibration_status.py">ContractCalibrationStatus</a></code>
- <code title="get /contracts/calibrate/{job_id}/messages">client.contracts.calibrate.<a href="./src/withpi/resources/contracts/calibrate.py">stream_messages</a>(job_id) -> str</code>

# Queries

Types:

```python
from withpi.types import QueryGenerateFanoutsResponse
```

Methods:

- <code title="post /queries/classify">client.queries.<a href="./src/withpi/resources/queries.py">classify</a>(\*\*<a href="src/withpi/types/query_classify_params.py">params</a>) -> <a href="./src/withpi/types/shared/query_classification_response.py">QueryClassificationResponse</a></code>
- <code title="post /queries/generate_fanouts">client.queries.<a href="./src/withpi/resources/queries.py">generate_fanouts</a>(\*\*<a href="src/withpi/types/query_generate_fanouts_params.py">params</a>) -> <a href="./src/withpi/types/query_generate_fanouts_response.py">QueryGenerateFanoutsResponse</a></code>
