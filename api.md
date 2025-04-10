# Shared Types

```python
from withpi.types import (
    ClassificationStatus,
    DataGenerationStatus,
    Example,
    ExplorationMode,
    PromptOptimizationStatus,
    QueryFanoutExample,
    ScoringDimension,
    ScoringSpec,
    ScoringSubDimension,
    ScoringSystemMetrics,
    SftStatus,
    SyntheticDataStatus,
    TrainedModel,
)
```

# Data

Types:

```python
from withpi.types import DataClusterInputsResponse
```

Methods:

- <code title="post /data/cluster_inputs">client.data.<a href="./src/withpi/resources/data/data.py">cluster_inputs</a>(\*\*<a href="src/withpi/types/data_cluster_inputs_params.py">params</a>) -> <a href="./src/withpi/types/data_cluster_inputs_response.py">DataClusterInputsResponse</a></code>

## Generate

Types:

```python
from withpi.types.data import (
    GenerateListResponse,
    GenerateCancelResponse,
    GenerateStreamDataResponse,
    GenerateStreamMessagesResponse,
)
```

Methods:

- <code title="get /data/generate/{job_id}">client.data.generate.<a href="./src/withpi/resources/data/generate.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/shared/data_generation_status.py">DataGenerationStatus</a></code>
- <code title="get /data/generate">client.data.generate.<a href="./src/withpi/resources/data/generate.py">list</a>(\*\*<a href="src/withpi/types/data/generate_list_params.py">params</a>) -> <a href="./src/withpi/types/data/generate_list_response.py">GenerateListResponse</a></code>
- <code title="delete /data/generate/{job_id}">client.data.generate.<a href="./src/withpi/resources/data/generate.py">cancel</a>(job_id) -> str</code>
- <code title="post /data/generate">client.data.generate.<a href="./src/withpi/resources/data/generate.py">start_job</a>(\*\*<a href="src/withpi/types/data/generate_start_job_params.py">params</a>) -> <a href="./src/withpi/types/shared/data_generation_status.py">DataGenerationStatus</a></code>
- <code title="get /data/generate/{job_id}/data">client.data.generate.<a href="./src/withpi/resources/data/generate.py">stream_data</a>(job_id) -> str</code>
- <code title="get /data/generate/{job_id}/messages">client.data.generate.<a href="./src/withpi/resources/data/generate.py">stream_messages</a>(job_id) -> str</code>

## GenerateInputResponsePairs

Types:

```python
from withpi.types.data import (
    GenerateInputResponsePairListResponse,
    GenerateInputResponsePairCancelResponse,
    GenerateInputResponsePairStreamDataResponse,
    GenerateInputResponsePairStreamMessagesResponse,
)
```

Methods:

- <code title="get /data/generate_input_response_pairs/{job_id}">client.data.generate_input_response_pairs.<a href="./src/withpi/resources/data/generate_input_response_pairs.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/shared/synthetic_data_status.py">SyntheticDataStatus</a></code>
- <code title="get /data/generate_input_response_pairs">client.data.generate_input_response_pairs.<a href="./src/withpi/resources/data/generate_input_response_pairs.py">list</a>(\*\*<a href="src/withpi/types/data/generate_input_response_pair_list_params.py">params</a>) -> <a href="./src/withpi/types/data/generate_input_response_pair_list_response.py">GenerateInputResponsePairListResponse</a></code>
- <code title="delete /data/generate_input_response_pairs/{job_id}">client.data.generate_input_response_pairs.<a href="./src/withpi/resources/data/generate_input_response_pairs.py">cancel</a>(job_id) -> str</code>
- <code title="post /data/generate_input_response_pairs">client.data.generate_input_response_pairs.<a href="./src/withpi/resources/data/generate_input_response_pairs.py">start_job</a>(\*\*<a href="src/withpi/types/data/generate_input_response_pair_start_job_params.py">params</a>) -> <a href="./src/withpi/types/shared/synthetic_data_status.py">SyntheticDataStatus</a></code>
- <code title="get /data/generate_input_response_pairs/{job_id}/data">client.data.generate_input_response_pairs.<a href="./src/withpi/resources/data/generate_input_response_pairs.py">stream_data</a>(job_id) -> <a href="./src/withpi/types/data/generate_input_response_pair_stream_data_response.py">GenerateInputResponsePairStreamDataResponse</a></code>
- <code title="get /data/generate_input_response_pairs/{job_id}/messages">client.data.generate_input_response_pairs.<a href="./src/withpi/resources/data/generate_input_response_pairs.py">stream_messages</a>(job_id) -> str</code>

# Training

## Sft

Types:

```python
from withpi.types.training import (
    SftListResponse,
    SftCancelResponse,
    SftDownloadResponse,
    SftStreamMessagesResponse,
)
```

Methods:

- <code title="get /training/sft/{job_id}">client.training.sft.<a href="./src/withpi/resources/training/sft.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/shared/sft_status.py">SftStatus</a></code>
- <code title="get /training/sft">client.training.sft.<a href="./src/withpi/resources/training/sft.py">list</a>(\*\*<a href="src/withpi/types/training/sft_list_params.py">params</a>) -> <a href="./src/withpi/types/training/sft_list_response.py">SftListResponse</a></code>
- <code title="delete /training/sft/{job_id}">client.training.sft.<a href="./src/withpi/resources/training/sft.py">cancel</a>(job_id) -> str</code>
- <code title="post /training/sft/{job_id}/download">client.training.sft.<a href="./src/withpi/resources/training/sft.py">download</a>(job_id, \*\*<a href="src/withpi/types/training/sft_download_params.py">params</a>) -> str</code>
- <code title="post /training/sft/{job_id}/load">client.training.sft.<a href="./src/withpi/resources/training/sft.py">load</a>(job_id) -> <a href="./src/withpi/types/shared/sft_status.py">SftStatus</a></code>
- <code title="post /training/sft">client.training.sft.<a href="./src/withpi/resources/training/sft.py">start_job</a>(\*\*<a href="src/withpi/types/training/sft_start_job_params.py">params</a>) -> <a href="./src/withpi/types/shared/sft_status.py">SftStatus</a></code>
- <code title="get /training/sft/{job_id}/messages">client.training.sft.<a href="./src/withpi/resources/training/sft.py">stream_messages</a>(job_id) -> str</code>

## Grpo

Types:

```python
from withpi.types.training import (
    GrpoRetrieveResponse,
    GrpoListResponse,
    GrpoCancelResponse,
    GrpoDownloadResponse,
    GrpoLoadResponse,
    GrpoStartJobResponse,
    GrpoStreamMessagesResponse,
)
```

Methods:

- <code title="get /training/grpo/{job_id}">client.training.grpo.<a href="./src/withpi/resources/training/grpo.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/training/grpo_retrieve_response.py">GrpoRetrieveResponse</a></code>
- <code title="get /training/grpo">client.training.grpo.<a href="./src/withpi/resources/training/grpo.py">list</a>(\*\*<a href="src/withpi/types/training/grpo_list_params.py">params</a>) -> <a href="./src/withpi/types/training/grpo_list_response.py">GrpoListResponse</a></code>
- <code title="delete /training/grpo/{job_id}">client.training.grpo.<a href="./src/withpi/resources/training/grpo.py">cancel</a>(job_id) -> str</code>
- <code title="post /training/grpo/{job_id}/download">client.training.grpo.<a href="./src/withpi/resources/training/grpo.py">download</a>(job_id, \*\*<a href="src/withpi/types/training/grpo_download_params.py">params</a>) -> str</code>
- <code title="post /training/grpo/{job_id}/load">client.training.grpo.<a href="./src/withpi/resources/training/grpo.py">load</a>(job_id) -> <a href="./src/withpi/types/training/grpo_load_response.py">GrpoLoadResponse</a></code>
- <code title="post /training/grpo">client.training.grpo.<a href="./src/withpi/resources/training/grpo.py">start_job</a>(\*\*<a href="src/withpi/types/training/grpo_start_job_params.py">params</a>) -> <a href="./src/withpi/types/training/grpo_start_job_response.py">GrpoStartJobResponse</a></code>
- <code title="get /training/grpo/{job_id}/messages">client.training.grpo.<a href="./src/withpi/resources/training/grpo.py">stream_messages</a>(job_id) -> str</code>

# Prompt

## Optimize

Types:

```python
from withpi.types.prompt import (
    OptimizeListResponse,
    OptimizeCancelResponse,
    OptimizeStreamMessagesResponse,
)
```

Methods:

- <code title="get /prompt/optimize/{job_id}">client.prompt.optimize.<a href="./src/withpi/resources/prompt/optimize.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/shared/prompt_optimization_status.py">PromptOptimizationStatus</a></code>
- <code title="get /prompt/optimize">client.prompt.optimize.<a href="./src/withpi/resources/prompt/optimize.py">list</a>(\*\*<a href="src/withpi/types/prompt/optimize_list_params.py">params</a>) -> <a href="./src/withpi/types/prompt/optimize_list_response.py">OptimizeListResponse</a></code>
- <code title="delete /prompt/optimize/{job_id}">client.prompt.optimize.<a href="./src/withpi/resources/prompt/optimize.py">cancel</a>(job_id) -> str</code>
- <code title="post /prompt/optimize">client.prompt.optimize.<a href="./src/withpi/resources/prompt/optimize.py">start_job</a>(\*\*<a href="src/withpi/types/prompt/optimize_start_job_params.py">params</a>) -> <a href="./src/withpi/types/shared/prompt_optimization_status.py">PromptOptimizationStatus</a></code>
- <code title="get /prompt/optimize/{job_id}/messages">client.prompt.optimize.<a href="./src/withpi/resources/prompt/optimize.py">stream_messages</a>(job_id) -> str</code>

# ScoringSystem

Methods:

- <code title="post /scoring_system/generate">client.scoring_system.<a href="./src/withpi/resources/scoring_system/scoring_system.py">generate</a>(\*\*<a href="src/withpi/types/scoring_system_generate_params.py">params</a>) -> <a href="./src/withpi/types/shared/scoring_spec.py">ScoringSpec</a></code>
- <code title="post /scoring_system/import_spec">client.scoring_system.<a href="./src/withpi/resources/scoring_system/scoring_system.py">import_spec</a>(\*\*<a href="src/withpi/types/scoring_system_import_spec_params.py">params</a>) -> <a href="./src/withpi/types/shared/scoring_spec.py">ScoringSpec</a></code>
- <code title="post /scoring_system/score">client.scoring_system.<a href="./src/withpi/resources/scoring_system/scoring_system.py">score</a>(\*\*<a href="src/withpi/types/scoring_system_score_params.py">params</a>) -> <a href="./src/withpi/types/shared/scoring_system_metrics.py">ScoringSystemMetrics</a></code>

## Calibrate

Types:

```python
from withpi.types.scoring_system import (
    CalibrateRetrieveResponse,
    CalibrateListResponse,
    CalibrateCancelResponse,
    CalibrateStartJobResponse,
    CalibrateStreamMessagesResponse,
)
```

Methods:

- <code title="get /scoring_system/calibrate/{job_id}">client.scoring_system.calibrate.<a href="./src/withpi/resources/scoring_system/calibrate.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/scoring_system/calibrate_retrieve_response.py">CalibrateRetrieveResponse</a></code>
- <code title="get /scoring_system/calibrate">client.scoring_system.calibrate.<a href="./src/withpi/resources/scoring_system/calibrate.py">list</a>(\*\*<a href="src/withpi/types/scoring_system/calibrate_list_params.py">params</a>) -> <a href="./src/withpi/types/scoring_system/calibrate_list_response.py">CalibrateListResponse</a></code>
- <code title="delete /scoring_system/calibrate/{job_id}">client.scoring_system.calibrate.<a href="./src/withpi/resources/scoring_system/calibrate.py">cancel</a>(job_id) -> str</code>
- <code title="post /scoring_system/calibrate">client.scoring_system.calibrate.<a href="./src/withpi/resources/scoring_system/calibrate.py">start_job</a>(\*\*<a href="src/withpi/types/scoring_system/calibrate_start_job_params.py">params</a>) -> <a href="./src/withpi/types/scoring_system/calibrate_start_job_response.py">CalibrateStartJobResponse</a></code>
- <code title="get /scoring_system/calibrate/{job_id}/messages">client.scoring_system.calibrate.<a href="./src/withpi/resources/scoring_system/calibrate.py">stream_messages</a>(job_id) -> str</code>

# Search

## QueryFanout

Types:

```python
from withpi.types.search import QueryFanoutGenerateResponse
```

Methods:

- <code title="post /search/query_fanout/generate">client.search.query_fanout.<a href="./src/withpi/resources/search/query_fanout.py">generate</a>(\*\*<a href="src/withpi/types/search/query_fanout_generate_params.py">params</a>) -> <a href="./src/withpi/types/search/query_fanout_generate_response.py">QueryFanoutGenerateResponse</a></code>

## QueryClassifier

Types:

```python
from withpi.types.search import QueryClassifierClassifyResponse
```

Methods:

- <code title="post /search/query_classifier/classify">client.search.query_classifier.<a href="./src/withpi/resources/search/query_classifier/query_classifier.py">classify</a>(\*\*<a href="src/withpi/types/search/query_classifier_classify_params.py">params</a>) -> <a href="./src/withpi/types/search/query_classifier_classify_response.py">QueryClassifierClassifyResponse</a></code>

### Distill

Types:

```python
from withpi.types.search.query_classifier import (
    DistillListResponse,
    DistillCancelResponse,
    DistillDownloadResponse,
    DistillStreamMessagesResponse,
)
```

Methods:

- <code title="get /search/query_classifier/distill/{job_id}">client.search.query_classifier.distill.<a href="./src/withpi/resources/search/query_classifier/distill.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/shared/classification_status.py">ClassificationStatus</a></code>
- <code title="get /search/query_classifier/distill">client.search.query_classifier.distill.<a href="./src/withpi/resources/search/query_classifier/distill.py">list</a>(\*\*<a href="src/withpi/types/search/query_classifier/distill_list_params.py">params</a>) -> <a href="./src/withpi/types/search/query_classifier/distill_list_response.py">DistillListResponse</a></code>
- <code title="delete /search/query_classifier/distill/{job_id}">client.search.query_classifier.distill.<a href="./src/withpi/resources/search/query_classifier/distill.py">cancel</a>(job_id) -> str</code>
- <code title="post /search/query_classifier/distill/{job_id}/download">client.search.query_classifier.distill.<a href="./src/withpi/resources/search/query_classifier/distill.py">download</a>(job_id, \*\*<a href="src/withpi/types/search/query_classifier/distill_download_params.py">params</a>) -> str</code>
- <code title="post /search/query_classifier/distill">client.search.query_classifier.distill.<a href="./src/withpi/resources/search/query_classifier/distill.py">start_job</a>(\*\*<a href="src/withpi/types/search/query_classifier/distill_start_job_params.py">params</a>) -> <a href="./src/withpi/types/shared/classification_status.py">ClassificationStatus</a></code>
- <code title="get /search/query_classifier/distill/{job_id}/messages">client.search.query_classifier.distill.<a href="./src/withpi/resources/search/query_classifier/distill.py">stream_messages</a>(job_id) -> str</code>
