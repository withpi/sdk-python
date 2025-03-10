# Shared Types

```python
from withpi.types import ScoringSystem, ScoringSystemMetrics, SDKContract, SDKDimension
```

# Contracts

Methods:

- <code title="post /contracts/generate_dimensions">client.contracts.<a href="./src/withpi/resources/contracts/contracts.py">generate_dimensions</a>(\*\*<a href="src/withpi/types/contract_generate_dimensions_params.py">params</a>) -> <a href="./src/withpi/types/shared/sdk_contract.py">SDKContract</a></code>
- <code title="post /contracts/read_from_hf">client.contracts.<a href="./src/withpi/resources/contracts/contracts.py">read_from_hf</a>(\*\*<a href="src/withpi/types/contract_read_from_hf_params.py">params</a>) -> <a href="./src/withpi/types/shared/sdk_contract.py">SDKContract</a></code>
- <code title="post /contracts/score">client.contracts.<a href="./src/withpi/resources/contracts/contracts.py">score</a>(\*\*<a href="src/withpi/types/contract_score_params.py">params</a>) -> <a href="./src/withpi/types/shared/scoring_system_metrics.py">ScoringSystemMetrics</a></code>

## Calibrate

Types:

```python
from withpi.types.contracts import (
    CalibrationStrategy,
    ContractCalibrationStatus,
    SDKLabeledExample,
    SDKPreferenceExample,
    State,
    CalibrateListResponse,
    CalibrateCancelResponse,
    CalibrateStreamMessagesResponse,
)
```

Methods:

- <code title="get /contracts/calibrate/{job_id}">client.contracts.calibrate.<a href="./src/withpi/resources/contracts/calibrate.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/contracts/contract_calibration_status.py">ContractCalibrationStatus</a></code>
- <code title="get /contracts/calibrate">client.contracts.calibrate.<a href="./src/withpi/resources/contracts/calibrate.py">list</a>(\*\*<a href="src/withpi/types/contracts/calibrate_list_params.py">params</a>) -> <a href="./src/withpi/types/contracts/calibrate_list_response.py">CalibrateListResponse</a></code>
- <code title="delete /contracts/calibrate/{job_id}">client.contracts.calibrate.<a href="./src/withpi/resources/contracts/calibrate.py">cancel</a>(job_id) -> str</code>
- <code title="post /contracts/calibrate">client.contracts.calibrate.<a href="./src/withpi/resources/contracts/calibrate.py">start_job</a>(\*\*<a href="src/withpi/types/contracts/calibrate_start_job_params.py">params</a>) -> <a href="./src/withpi/types/contracts/contract_calibration_status.py">ContractCalibrationStatus</a></code>
- <code title="get /contracts/calibrate/{job_id}/messages">client.contracts.calibrate.<a href="./src/withpi/resources/contracts/calibrate.py">stream_messages</a>(job_id) -> str</code>

# Data

## GenerateSyntheticData

Types:

```python
from withpi.types.data import (
    SDKExample,
    SDKExplorationMode,
    SyntheticDataStatus,
    GenerateSyntheticDataListResponse,
    GenerateSyntheticDataCancelResponse,
    GenerateSyntheticDataStreamDataResponse,
    GenerateSyntheticDataStreamMessagesResponse,
)
```

Methods:

- <code title="get /data/generate_synthetic_data/{job_id}">client.data.generate_synthetic_data.<a href="./src/withpi/resources/data/generate_synthetic_data.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/data/synthetic_data_status.py">SyntheticDataStatus</a></code>
- <code title="get /data/generate_synthetic_data">client.data.generate_synthetic_data.<a href="./src/withpi/resources/data/generate_synthetic_data.py">list</a>(\*\*<a href="src/withpi/types/data/generate_synthetic_data_list_params.py">params</a>) -> <a href="./src/withpi/types/data/generate_synthetic_data_list_response.py">GenerateSyntheticDataListResponse</a></code>
- <code title="delete /data/generate_synthetic_data/{job_id}">client.data.generate_synthetic_data.<a href="./src/withpi/resources/data/generate_synthetic_data.py">cancel</a>(job_id) -> str</code>
- <code title="post /data/generate_synthetic_data">client.data.generate_synthetic_data.<a href="./src/withpi/resources/data/generate_synthetic_data.py">start_job</a>(\*\*<a href="src/withpi/types/data/generate_synthetic_data_start_job_params.py">params</a>) -> <a href="./src/withpi/types/data/synthetic_data_status.py">SyntheticDataStatus</a></code>
- <code title="get /data/generate_synthetic_data/{job_id}/data">client.data.generate_synthetic_data.<a href="./src/withpi/resources/data/generate_synthetic_data.py">stream_data</a>(job_id) -> <a href="./src/withpi/types/data/generate_synthetic_data_stream_data_response.py">GenerateSyntheticDataStreamDataResponse</a></code>
- <code title="get /data/generate_synthetic_data/{job_id}/messages">client.data.generate_synthetic_data.<a href="./src/withpi/resources/data/generate_synthetic_data.py">stream_messages</a>(job_id) -> str</code>

## Inputs

Types:

```python
from withpi.types.data import InputClusterResponse
```

Methods:

- <code title="post /data/input/cluster">client.data.inputs.<a href="./src/withpi/resources/data/inputs/inputs.py">cluster</a>(\*\*<a href="src/withpi/types/data/input_cluster_params.py">params</a>) -> <a href="./src/withpi/types/data/input_cluster_response.py">InputClusterResponse</a></code>

### GenerateFromSeeds

Types:

```python
from withpi.types.data.inputs import (
    DataGenerationStatus,
    GenerateFromSeedListResponse,
    GenerateFromSeedCancelResponse,
    GenerateFromSeedStreamDataResponse,
    GenerateFromSeedStreamMessagesResponse,
)
```

Methods:

- <code title="get /data/input/generate_from_seeds/{job_id}">client.data.inputs.generate_from_seeds.<a href="./src/withpi/resources/data/inputs/generate_from_seeds.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/data/inputs/data_generation_status.py">DataGenerationStatus</a></code>
- <code title="get /data/input/generate_from_seeds">client.data.inputs.generate_from_seeds.<a href="./src/withpi/resources/data/inputs/generate_from_seeds.py">list</a>(\*\*<a href="src/withpi/types/data/inputs/generate_from_seed_list_params.py">params</a>) -> <a href="./src/withpi/types/data/inputs/generate_from_seed_list_response.py">GenerateFromSeedListResponse</a></code>
- <code title="delete /data/input/generate_from_seeds/{job_id}">client.data.inputs.generate_from_seeds.<a href="./src/withpi/resources/data/inputs/generate_from_seeds.py">cancel</a>(job_id) -> str</code>
- <code title="post /data/input/generate_from_seeds">client.data.inputs.generate_from_seeds.<a href="./src/withpi/resources/data/inputs/generate_from_seeds.py">start_job</a>(\*\*<a href="src/withpi/types/data/inputs/generate_from_seed_start_job_params.py">params</a>) -> <a href="./src/withpi/types/data/inputs/data_generation_status.py">DataGenerationStatus</a></code>
- <code title="get /data/input/generate_from_seeds/{job_id}/data">client.data.inputs.generate_from_seeds.<a href="./src/withpi/resources/data/inputs/generate_from_seeds.py">stream_data</a>(job_id) -> str</code>
- <code title="get /data/input/generate_from_seeds/{job_id}/messages">client.data.inputs.generate_from_seeds.<a href="./src/withpi/resources/data/inputs/generate_from_seeds.py">stream_messages</a>(job_id) -> str</code>

# Model

## Classifier

Types:

```python
from withpi.types.model import (
    ClassificationStatus,
    TrainedModel,
    ClassifierListResponse,
    ClassifierCancelResponse,
    ClassifierDownloadResponse,
    ClassifierStreamMessagesResponse,
)
```

Methods:

- <code title="get /model/classifier/{job_id}">client.model.classifier.<a href="./src/withpi/resources/model/classifier.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/model/classification_status.py">ClassificationStatus</a></code>
- <code title="get /model/classifier">client.model.classifier.<a href="./src/withpi/resources/model/classifier.py">list</a>(\*\*<a href="src/withpi/types/model/classifier_list_params.py">params</a>) -> <a href="./src/withpi/types/model/classifier_list_response.py">ClassifierListResponse</a></code>
- <code title="delete /model/classifier/{job_id}">client.model.classifier.<a href="./src/withpi/resources/model/classifier.py">cancel</a>(job_id) -> str</code>
- <code title="post /model/classifier/{job_id}/download">client.model.classifier.<a href="./src/withpi/resources/model/classifier.py">download</a>(job_id, \*\*<a href="src/withpi/types/model/classifier_download_params.py">params</a>) -> str</code>
- <code title="post /model/classifier">client.model.classifier.<a href="./src/withpi/resources/model/classifier.py">start_job</a>(\*\*<a href="src/withpi/types/model/classifier_start_job_params.py">params</a>) -> <a href="./src/withpi/types/model/classification_status.py">ClassificationStatus</a></code>
- <code title="get /model/classifier/{job_id}/messages">client.model.classifier.<a href="./src/withpi/resources/model/classifier.py">stream_messages</a>(job_id) -> str</code>

## Rl

### Grpo

Types:

```python
from withpi.types.model.rl import (
    LoraConfig,
    RlGrpoStatus,
    TextGenerationBaseModel,
    GrpoListResponse,
    GrpoCancelResponse,
    GrpoDownloadResponse,
    GrpoStreamMessagesResponse,
)
```

Methods:

- <code title="get /model/rl/grpo/{job_id}">client.model.rl.grpo.<a href="./src/withpi/resources/model/rl/grpo.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/model/rl/rl_grpo_status.py">RlGrpoStatus</a></code>
- <code title="get /model/rl/grpo">client.model.rl.grpo.<a href="./src/withpi/resources/model/rl/grpo.py">list</a>(\*\*<a href="src/withpi/types/model/rl/grpo_list_params.py">params</a>) -> <a href="./src/withpi/types/model/rl/grpo_list_response.py">GrpoListResponse</a></code>
- <code title="delete /model/rl/grpo/{job_id}">client.model.rl.grpo.<a href="./src/withpi/resources/model/rl/grpo.py">cancel</a>(job_id) -> str</code>
- <code title="post /model/rl/grpo/{job_id}/download">client.model.rl.grpo.<a href="./src/withpi/resources/model/rl/grpo.py">download</a>(job_id, \*\*<a href="src/withpi/types/model/rl/grpo_download_params.py">params</a>) -> str</code>
- <code title="post /model/rl/grpo/{job_id}/load">client.model.rl.grpo.<a href="./src/withpi/resources/model/rl/grpo.py">load</a>(job_id) -> <a href="./src/withpi/types/model/rl/rl_grpo_status.py">RlGrpoStatus</a></code>
- <code title="post /model/rl/grpo">client.model.rl.grpo.<a href="./src/withpi/resources/model/rl/grpo.py">start_job</a>(\*\*<a href="src/withpi/types/model/rl/grpo_start_job_params.py">params</a>) -> <a href="./src/withpi/types/model/rl/rl_grpo_status.py">RlGrpoStatus</a></code>
- <code title="get /model/rl/grpo/{job_id}/messages">client.model.rl.grpo.<a href="./src/withpi/resources/model/rl/grpo.py">stream_messages</a>(job_id) -> str</code>

## Sft

Types:

```python
from withpi.types.model import (
    SftStatus,
    SftListResponse,
    SftCancelResponse,
    SftDownloadResponse,
    SftStreamMessagesResponse,
)
```

Methods:

- <code title="get /model/sft/{job_id}">client.model.sft.<a href="./src/withpi/resources/model/sft.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/model/sft_status.py">SftStatus</a></code>
- <code title="get /model/sft">client.model.sft.<a href="./src/withpi/resources/model/sft.py">list</a>(\*\*<a href="src/withpi/types/model/sft_list_params.py">params</a>) -> <a href="./src/withpi/types/model/sft_list_response.py">SftListResponse</a></code>
- <code title="delete /model/sft/{job_id}">client.model.sft.<a href="./src/withpi/resources/model/sft.py">cancel</a>(job_id) -> str</code>
- <code title="post /model/sft/{job_id}/download">client.model.sft.<a href="./src/withpi/resources/model/sft.py">download</a>(job_id, \*\*<a href="src/withpi/types/model/sft_download_params.py">params</a>) -> str</code>
- <code title="post /model/sft/{job_id}/load">client.model.sft.<a href="./src/withpi/resources/model/sft.py">load</a>(job_id) -> <a href="./src/withpi/types/model/sft_status.py">SftStatus</a></code>
- <code title="post /model/sft">client.model.sft.<a href="./src/withpi/resources/model/sft.py">start_job</a>(\*\*<a href="src/withpi/types/model/sft_start_job_params.py">params</a>) -> <a href="./src/withpi/types/model/sft_status.py">SftStatus</a></code>
- <code title="get /model/sft/{job_id}/messages">client.model.sft.<a href="./src/withpi/resources/model/sft.py">stream_messages</a>(job_id) -> str</code>

# PiScoringSystem

Methods:

- <code title="post /pi_scoring_system/generate_dimensions">client.pi_scoring_system.<a href="./src/withpi/resources/pi_scoring_system/pi_scoring_system.py">generate_dimensions</a>(\*\*<a href="src/withpi/types/pi_scoring_system_generate_dimensions_params.py">params</a>) -> <a href="./src/withpi/types/shared/scoring_system.py">ScoringSystem</a></code>
- <code title="post /pi_scoring_system/read_from_hf">client.pi_scoring_system.<a href="./src/withpi/resources/pi_scoring_system/pi_scoring_system.py">read_from_hf</a>(\*\*<a href="src/withpi/types/pi_scoring_system_read_from_hf_params.py">params</a>) -> <a href="./src/withpi/types/shared/scoring_system.py">ScoringSystem</a></code>
- <code title="post /pi_scoring_system/score">client.pi_scoring_system.<a href="./src/withpi/resources/pi_scoring_system/pi_scoring_system.py">score</a>(\*\*<a href="src/withpi/types/pi_scoring_system_score_params.py">params</a>) -> <a href="./src/withpi/types/shared/scoring_system_metrics.py">ScoringSystemMetrics</a></code>

## Calibrate

Types:

```python
from withpi.types.pi_scoring_system import (
    ScoringSystemCalibrationStatus,
    CalibrateListResponse,
    CalibrateCancelResponse,
    CalibrateStreamMessagesResponse,
)
```

Methods:

- <code title="get /pi_scoring_system/calibrate/{job_id}">client.pi_scoring_system.calibrate.<a href="./src/withpi/resources/pi_scoring_system/calibrate.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/pi_scoring_system/scoring_system_calibration_status.py">ScoringSystemCalibrationStatus</a></code>
- <code title="get /pi_scoring_system/calibrate">client.pi_scoring_system.calibrate.<a href="./src/withpi/resources/pi_scoring_system/calibrate.py">list</a>(\*\*<a href="src/withpi/types/pi_scoring_system/calibrate_list_params.py">params</a>) -> <a href="./src/withpi/types/pi_scoring_system/calibrate_list_response.py">CalibrateListResponse</a></code>
- <code title="delete /pi_scoring_system/calibrate/{job_id}">client.pi_scoring_system.calibrate.<a href="./src/withpi/resources/pi_scoring_system/calibrate.py">cancel</a>(job_id) -> str</code>
- <code title="post /pi_scoring_system/calibrate">client.pi_scoring_system.calibrate.<a href="./src/withpi/resources/pi_scoring_system/calibrate.py">start_job</a>(\*\*<a href="src/withpi/types/pi_scoring_system/calibrate_start_job_params.py">params</a>) -> <a href="./src/withpi/types/pi_scoring_system/scoring_system_calibration_status.py">ScoringSystemCalibrationStatus</a></code>
- <code title="get /pi_scoring_system/calibrate/{job_id}/messages">client.pi_scoring_system.calibrate.<a href="./src/withpi/resources/pi_scoring_system/calibrate.py">stream_messages</a>(job_id) -> str</code>

# Prompt

## Optimize

Types:

```python
from withpi.types.prompt import (
    PromptOptimizationStatus,
    OptimizeListResponse,
    OptimizeCancelResponse,
    OptimizeStreamMessagesResponse,
)
```

Methods:

- <code title="get /prompt/optimize/{job_id}">client.prompt.optimize.<a href="./src/withpi/resources/prompt/optimize.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/prompt/prompt_optimization_status.py">PromptOptimizationStatus</a></code>
- <code title="get /prompt/optimize">client.prompt.optimize.<a href="./src/withpi/resources/prompt/optimize.py">list</a>(\*\*<a href="src/withpi/types/prompt/optimize_list_params.py">params</a>) -> <a href="./src/withpi/types/prompt/optimize_list_response.py">OptimizeListResponse</a></code>
- <code title="delete /prompt/optimize/{job_id}">client.prompt.optimize.<a href="./src/withpi/resources/prompt/optimize.py">cancel</a>(job_id) -> str</code>
- <code title="post /prompt/optimize">client.prompt.optimize.<a href="./src/withpi/resources/prompt/optimize.py">start_job</a>(\*\*<a href="src/withpi/types/prompt/optimize_start_job_params.py">params</a>) -> <a href="./src/withpi/types/prompt/prompt_optimization_status.py">PromptOptimizationStatus</a></code>
- <code title="get /prompt/optimize/{job_id}/messages">client.prompt.optimize.<a href="./src/withpi/resources/prompt/optimize.py">stream_messages</a>(job_id) -> str</code>

# Queries

Types:

```python
from withpi.types import QueryFanoutExample, QueryClassifyResponse, QueryGenerateFanoutsResponse
```

Methods:

- <code title="post /queries/classify">client.queries.<a href="./src/withpi/resources/queries.py">classify</a>(\*\*<a href="src/withpi/types/query_classify_params.py">params</a>) -> <a href="./src/withpi/types/query_classify_response.py">QueryClassifyResponse</a></code>
- <code title="post /queries/generate_fanouts">client.queries.<a href="./src/withpi/resources/queries.py">generate_fanouts</a>(\*\*<a href="src/withpi/types/query_generate_fanouts_params.py">params</a>) -> <a href="./src/withpi/types/query_generate_fanouts_response.py">QueryGenerateFanoutsResponse</a></code>
