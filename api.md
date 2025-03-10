# Shared Types

```python
from withpi.types import (
    ClassificationStatus,
    DataGenerationStatus,
    ExplorationMode,
    PromptOptimizationStatus,
    QueryFanoutExample,
    Scorer,
    ScorerDimension,
    ScorerSubDimension,
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

## GenerateInputs

Types:

```python
from withpi.types.data import (
    GenerateInputListResponse,
    GenerateInputCancelResponse,
    GenerateInputStreamDataResponse,
    GenerateInputStreamMessagesResponse,
)
```

Methods:

- <code title="get /data/generate_inputs/{job_id}">client.data.generate_inputs.<a href="./src/withpi/resources/data/generate_inputs.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/shared/data_generation_status.py">DataGenerationStatus</a></code>
- <code title="get /data/generate_inputs">client.data.generate_inputs.<a href="./src/withpi/resources/data/generate_inputs.py">list</a>(\*\*<a href="src/withpi/types/data/generate_input_list_params.py">params</a>) -> <a href="./src/withpi/types/data/generate_input_list_response.py">GenerateInputListResponse</a></code>
- <code title="delete /data/generate_inputs/{job_id}">client.data.generate_inputs.<a href="./src/withpi/resources/data/generate_inputs.py">cancel</a>(job_id) -> str</code>
- <code title="post /data/generate_inputs">client.data.generate_inputs.<a href="./src/withpi/resources/data/generate_inputs.py">start_job</a>(\*\*<a href="src/withpi/types/data/generate_input_start_job_params.py">params</a>) -> <a href="./src/withpi/types/shared/data_generation_status.py">DataGenerationStatus</a></code>
- <code title="get /data/generate_inputs/{job_id}/data">client.data.generate_inputs.<a href="./src/withpi/resources/data/generate_inputs.py">stream_data</a>(job_id) -> str</code>
- <code title="get /data/generate_inputs/{job_id}/messages">client.data.generate_inputs.<a href="./src/withpi/resources/data/generate_inputs.py">stream_messages</a>(job_id) -> str</code>

## GenerateExamples

Types:

```python
from withpi.types.data import (
    GenerateExampleListResponse,
    GenerateExampleCancelResponse,
    GenerateExampleStreamDataResponse,
    GenerateExampleStreamMessagesResponse,
)
```

Methods:

- <code title="get /data/generate_examples/{job_id}">client.data.generate_examples.<a href="./src/withpi/resources/data/generate_examples.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/shared/synthetic_data_status.py">SyntheticDataStatus</a></code>
- <code title="get /data/generate_examples">client.data.generate_examples.<a href="./src/withpi/resources/data/generate_examples.py">list</a>(\*\*<a href="src/withpi/types/data/generate_example_list_params.py">params</a>) -> <a href="./src/withpi/types/data/generate_example_list_response.py">GenerateExampleListResponse</a></code>
- <code title="delete /data/generate_examples/{job_id}">client.data.generate_examples.<a href="./src/withpi/resources/data/generate_examples.py">cancel</a>(job_id) -> str</code>
- <code title="post /data/generate_examples">client.data.generate_examples.<a href="./src/withpi/resources/data/generate_examples.py">start_job</a>(\*\*<a href="src/withpi/types/data/generate_example_start_job_params.py">params</a>) -> <a href="./src/withpi/types/shared/synthetic_data_status.py">SyntheticDataStatus</a></code>
- <code title="get /data/generate_examples/{job_id}/data">client.data.generate_examples.<a href="./src/withpi/resources/data/generate_examples.py">stream_data</a>(job_id) -> <a href="./src/withpi/types/data/generate_example_stream_data_response.py">GenerateExampleStreamDataResponse</a></code>
- <code title="get /data/generate_examples/{job_id}/messages">client.data.generate_examples.<a href="./src/withpi/resources/data/generate_examples.py">stream_messages</a>(job_id) -> str</code>

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

# Scorers

Types:

```python
from withpi.types import ScorerScoreResponse
```

Methods:

- <code title="post /scorers/generate_dimensions">client.scorers.<a href="./src/withpi/resources/scorers/scorers.py">generate_dimensions</a>(\*\*<a href="src/withpi/types/scorer_generate_dimensions_params.py">params</a>) -> <a href="./src/withpi/types/shared/scorer.py">Scorer</a></code>
- <code title="post /scorers/read_from_hf">client.scorers.<a href="./src/withpi/resources/scorers/scorers.py">read_from_hf</a>(\*\*<a href="src/withpi/types/scorer_read_from_hf_params.py">params</a>) -> <a href="./src/withpi/types/shared/scorer.py">Scorer</a></code>
- <code title="post /scorers/score">client.scorers.<a href="./src/withpi/resources/scorers/scorers.py">score</a>(\*\*<a href="src/withpi/types/scorer_score_params.py">params</a>) -> <a href="./src/withpi/types/scorer_score_response.py">ScorerScoreResponse</a></code>

## Calibrate

Types:

```python
from withpi.types.scorers import (
    CalibrateCreateResponse,
    CalibrateRetrieveResponse,
    CalibrateListResponse,
    CalibrateCancelResponse,
    CalibrateMessagesResponse,
)
```

Methods:

- <code title="post /scorers/calibrate">client.scorers.calibrate.<a href="./src/withpi/resources/scorers/calibrate.py">create</a>(\*\*<a href="src/withpi/types/scorers/calibrate_create_params.py">params</a>) -> <a href="./src/withpi/types/scorers/calibrate_create_response.py">CalibrateCreateResponse</a></code>
- <code title="get /scorers/calibrate/{job_id}">client.scorers.calibrate.<a href="./src/withpi/resources/scorers/calibrate.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/scorers/calibrate_retrieve_response.py">CalibrateRetrieveResponse</a></code>
- <code title="get /scorers/calibrate">client.scorers.calibrate.<a href="./src/withpi/resources/scorers/calibrate.py">list</a>(\*\*<a href="src/withpi/types/scorers/calibrate_list_params.py">params</a>) -> <a href="./src/withpi/types/scorers/calibrate_list_response.py">CalibrateListResponse</a></code>
- <code title="delete /scorers/calibrate/{job_id}">client.scorers.calibrate.<a href="./src/withpi/resources/scorers/calibrate.py">cancel</a>(job_id) -> str</code>
- <code title="get /scorers/calibrate/{job_id}/messages">client.scorers.calibrate.<a href="./src/withpi/resources/scorers/calibrate.py">messages</a>(job_id) -> str</code>

# Rag

Types:

```python
from withpi.types import RagClassifyQueryResponse, RagGenerateFanoutResponse
```

Methods:

- <code title="post /rag/query_classify">client.rag.<a href="./src/withpi/resources/rag.py">classify_query</a>(\*\*<a href="src/withpi/types/rag_classify_query_params.py">params</a>) -> <a href="./src/withpi/types/rag_classify_query_response.py">RagClassifyQueryResponse</a></code>
- <code title="post /rag/query_fanout">client.rag.<a href="./src/withpi/resources/rag.py">generate_fanout</a>(\*\*<a href="src/withpi/types/rag_generate_fanout_params.py">params</a>) -> <a href="./src/withpi/types/rag_generate_fanout_response.py">RagGenerateFanoutResponse</a></code>

# Training

## Classifier

Types:

```python
from withpi.types.training import (
    ClassifierListResponse,
    ClassifierCancelResponse,
    ClassifierDownloadResponse,
    ClassifierMessagesResponse,
)
```

Methods:

- <code title="post /training/classifier">client.training.classifier.<a href="./src/withpi/resources/training/classifier.py">create</a>(\*\*<a href="src/withpi/types/training/classifier_create_params.py">params</a>) -> <a href="./src/withpi/types/shared/classification_status.py">ClassificationStatus</a></code>
- <code title="get /training/classifier/{job_id}">client.training.classifier.<a href="./src/withpi/resources/training/classifier.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/shared/classification_status.py">ClassificationStatus</a></code>
- <code title="get /training/classifier">client.training.classifier.<a href="./src/withpi/resources/training/classifier.py">list</a>(\*\*<a href="src/withpi/types/training/classifier_list_params.py">params</a>) -> <a href="./src/withpi/types/training/classifier_list_response.py">ClassifierListResponse</a></code>
- <code title="delete /training/classifier/{job_id}">client.training.classifier.<a href="./src/withpi/resources/training/classifier.py">cancel</a>(job_id) -> str</code>
- <code title="post /training/classifier/{job_id}/download">client.training.classifier.<a href="./src/withpi/resources/training/classifier.py">download</a>(job_id, \*\*<a href="src/withpi/types/training/classifier_download_params.py">params</a>) -> str</code>
- <code title="get /training/classifier/{job_id}/messages">client.training.classifier.<a href="./src/withpi/resources/training/classifier.py">messages</a>(job_id) -> str</code>

## Grpo

Types:

```python
from withpi.types.training import (
    GrpoCreateResponse,
    GrpoRetrieveResponse,
    GrpoListResponse,
    GrpoCancelResponse,
    GrpoDownloadResponse,
    GrpoLoadResponse,
    GrpoMessagesResponse,
)
```

Methods:

- <code title="post /training/grpo">client.training.grpo.<a href="./src/withpi/resources/training/grpo.py">create</a>(\*\*<a href="src/withpi/types/training/grpo_create_params.py">params</a>) -> <a href="./src/withpi/types/training/grpo_create_response.py">GrpoCreateResponse</a></code>
- <code title="get /training/grpo/{job_id}">client.training.grpo.<a href="./src/withpi/resources/training/grpo.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/training/grpo_retrieve_response.py">GrpoRetrieveResponse</a></code>
- <code title="get /training/grpo">client.training.grpo.<a href="./src/withpi/resources/training/grpo.py">list</a>(\*\*<a href="src/withpi/types/training/grpo_list_params.py">params</a>) -> <a href="./src/withpi/types/training/grpo_list_response.py">GrpoListResponse</a></code>
- <code title="delete /training/grpo/{job_id}">client.training.grpo.<a href="./src/withpi/resources/training/grpo.py">cancel</a>(job_id) -> str</code>
- <code title="post /training/grpo/{job_id}/download">client.training.grpo.<a href="./src/withpi/resources/training/grpo.py">download</a>(job_id, \*\*<a href="src/withpi/types/training/grpo_download_params.py">params</a>) -> str</code>
- <code title="post /training/grpo/{job_id}/load">client.training.grpo.<a href="./src/withpi/resources/training/grpo.py">load</a>(job_id) -> <a href="./src/withpi/types/training/grpo_load_response.py">GrpoLoadResponse</a></code>
- <code title="get /training/grpo/{job_id}/messages">client.training.grpo.<a href="./src/withpi/resources/training/grpo.py">messages</a>(job_id) -> str</code>

## Sft

Types:

```python
from withpi.types.training import (
    SftCreateResponse,
    SftRetrieveResponse,
    SftListResponse,
    SftCancelResponse,
    SftDownloadResponse,
    SftLoadResponse,
    SftMessagesResponse,
)
```

Methods:

- <code title="post /training/sft">client.training.sft.<a href="./src/withpi/resources/training/sft.py">create</a>(\*\*<a href="src/withpi/types/training/sft_create_params.py">params</a>) -> <a href="./src/withpi/types/training/sft_create_response.py">SftCreateResponse</a></code>
- <code title="get /training/sft/{job_id}">client.training.sft.<a href="./src/withpi/resources/training/sft.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/training/sft_retrieve_response.py">SftRetrieveResponse</a></code>
- <code title="get /training/sft">client.training.sft.<a href="./src/withpi/resources/training/sft.py">list</a>(\*\*<a href="src/withpi/types/training/sft_list_params.py">params</a>) -> <a href="./src/withpi/types/training/sft_list_response.py">SftListResponse</a></code>
- <code title="delete /training/sft/{job_id}">client.training.sft.<a href="./src/withpi/resources/training/sft.py">cancel</a>(job_id) -> str</code>
- <code title="post /training/sft/{job_id}/download">client.training.sft.<a href="./src/withpi/resources/training/sft.py">download</a>(job_id, \*\*<a href="src/withpi/types/training/sft_download_params.py">params</a>) -> str</code>
- <code title="post /training/sft/{job_id}/load">client.training.sft.<a href="./src/withpi/resources/training/sft.py">load</a>(job_id) -> <a href="./src/withpi/types/training/sft_load_response.py">SftLoadResponse</a></code>
- <code title="get /training/sft/{job_id}/messages">client.training.sft.<a href="./src/withpi/resources/training/sft.py">messages</a>(job_id) -> str</code>
