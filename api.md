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

- <code title="post /data/generate_examples">client.data.generate_examples.<a href="./src/withpi/resources/data/generate_examples.py">create</a>(\*\*<a href="src/withpi/types/data/generate_example_create_params.py">params</a>) -> <a href="./src/withpi/types/shared/synthetic_data_status.py">SyntheticDataStatus</a></code>
- <code title="get /data/generate_examples/{job_id}">client.data.generate_examples.<a href="./src/withpi/resources/data/generate_examples.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/shared/synthetic_data_status.py">SyntheticDataStatus</a></code>
- <code title="get /data/generate_examples">client.data.generate_examples.<a href="./src/withpi/resources/data/generate_examples.py">list</a>(\*\*<a href="src/withpi/types/data/generate_example_list_params.py">params</a>) -> <a href="./src/withpi/types/data/generate_example_list_response.py">GenerateExampleListResponse</a></code>
- <code title="delete /data/generate_examples/{job_id}">client.data.generate_examples.<a href="./src/withpi/resources/data/generate_examples.py">cancel</a>(job_id) -> str</code>
- <code title="get /data/generate_examples/{job_id}/data">client.data.generate_examples.<a href="./src/withpi/resources/data/generate_examples.py">stream_data</a>(job_id) -> <a href="./src/withpi/types/data/generate_example_stream_data_response.py">GenerateExampleStreamDataResponse</a></code>
- <code title="get /data/generate_examples/{job_id}/messages">client.data.generate_examples.<a href="./src/withpi/resources/data/generate_examples.py">stream_messages</a>(job_id) -> str</code>

# Model

## Classifier

Types:

```python
from withpi.types.model import (
    ClassifierListResponse,
    ClassifierCancelResponse,
    ClassifierDownloadResponse,
    ClassifierStreamMessagesResponse,
)
```

Methods:

- <code title="get /model/classifier/{job_id}">client.model.classifier.<a href="./src/withpi/resources/model/classifier.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/shared/classification_status.py">ClassificationStatus</a></code>
- <code title="get /model/classifier">client.model.classifier.<a href="./src/withpi/resources/model/classifier.py">list</a>(\*\*<a href="src/withpi/types/model/classifier_list_params.py">params</a>) -> <a href="./src/withpi/types/model/classifier_list_response.py">ClassifierListResponse</a></code>
- <code title="delete /model/classifier/{job_id}">client.model.classifier.<a href="./src/withpi/resources/model/classifier.py">cancel</a>(job_id) -> str</code>
- <code title="post /model/classifier/{job_id}/download">client.model.classifier.<a href="./src/withpi/resources/model/classifier.py">download</a>(job_id, \*\*<a href="src/withpi/types/model/classifier_download_params.py">params</a>) -> str</code>
- <code title="post /model/classifier">client.model.classifier.<a href="./src/withpi/resources/model/classifier.py">start_job</a>(\*\*<a href="src/withpi/types/model/classifier_start_job_params.py">params</a>) -> <a href="./src/withpi/types/shared/classification_status.py">ClassificationStatus</a></code>
- <code title="get /model/classifier/{job_id}/messages">client.model.classifier.<a href="./src/withpi/resources/model/classifier.py">stream_messages</a>(job_id) -> str</code>

## Sft

Types:

```python
from withpi.types.model import (
    SftRetrieveResponse,
    SftListResponse,
    SftCancelResponse,
    SftDownloadResponse,
    SftLoadResponse,
    SftStartJobResponse,
    SftStreamMessagesResponse,
)
```

Methods:

- <code title="get /model/sft/{job_id}">client.model.sft.<a href="./src/withpi/resources/model/sft.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/model/sft_retrieve_response.py">SftRetrieveResponse</a></code>
- <code title="get /model/sft">client.model.sft.<a href="./src/withpi/resources/model/sft.py">list</a>(\*\*<a href="src/withpi/types/model/sft_list_params.py">params</a>) -> <a href="./src/withpi/types/model/sft_list_response.py">SftListResponse</a></code>
- <code title="delete /model/sft/{job_id}">client.model.sft.<a href="./src/withpi/resources/model/sft.py">cancel</a>(job_id) -> str</code>
- <code title="post /model/sft/{job_id}/download">client.model.sft.<a href="./src/withpi/resources/model/sft.py">download</a>(job_id, \*\*<a href="src/withpi/types/model/sft_download_params.py">params</a>) -> str</code>
- <code title="post /model/sft/{job_id}/load">client.model.sft.<a href="./src/withpi/resources/model/sft.py">load</a>(job_id) -> <a href="./src/withpi/types/model/sft_load_response.py">SftLoadResponse</a></code>
- <code title="post /model/sft">client.model.sft.<a href="./src/withpi/resources/model/sft.py">start_job</a>(\*\*<a href="src/withpi/types/model/sft_start_job_params.py">params</a>) -> <a href="./src/withpi/types/model/sft_start_job_response.py">SftStartJobResponse</a></code>
- <code title="get /model/sft/{job_id}/messages">client.model.sft.<a href="./src/withpi/resources/model/sft.py">stream_messages</a>(job_id) -> str</code>

## Grpo

Types:

```python
from withpi.types.model import (
    GrpoListResponse,
    GrpoCancelResponse,
    GrpoDownloadResponse,
    GrpoLaunchResponse,
    GrpoLoadResponse,
    GrpoMessagesResponse,
    GrpoStatusResponse,
)
```

Methods:

- <code title="get /model/grpo">client.model.grpo.<a href="./src/withpi/resources/model/grpo.py">list</a>(\*\*<a href="src/withpi/types/model/grpo_list_params.py">params</a>) -> <a href="./src/withpi/types/model/grpo_list_response.py">GrpoListResponse</a></code>
- <code title="delete /model/grpo/{job_id}">client.model.grpo.<a href="./src/withpi/resources/model/grpo.py">cancel</a>(job_id) -> str</code>
- <code title="post /model/grpo/{job_id}/download">client.model.grpo.<a href="./src/withpi/resources/model/grpo.py">download</a>(job_id, \*\*<a href="src/withpi/types/model/grpo_download_params.py">params</a>) -> str</code>
- <code title="post /model/grpo">client.model.grpo.<a href="./src/withpi/resources/model/grpo.py">launch</a>(\*\*<a href="src/withpi/types/model/grpo_launch_params.py">params</a>) -> <a href="./src/withpi/types/model/grpo_launch_response.py">GrpoLaunchResponse</a></code>
- <code title="post /model/grpo/{job_id}/load">client.model.grpo.<a href="./src/withpi/resources/model/grpo.py">load</a>(job_id) -> <a href="./src/withpi/types/model/grpo_load_response.py">GrpoLoadResponse</a></code>
- <code title="get /model/grpo/{job_id}/messages">client.model.grpo.<a href="./src/withpi/resources/model/grpo.py">messages</a>(job_id) -> str</code>
- <code title="get /model/grpo/{job_id}">client.model.grpo.<a href="./src/withpi/resources/model/grpo.py">status</a>(job_id) -> <a href="./src/withpi/types/model/grpo_status_response.py">GrpoStatusResponse</a></code>

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

# Queries

Types:

```python
from withpi.types import QueryClassifyResponse, QueryGenerateFanoutsResponse
```

Methods:

- <code title="post /queries/classify">client.queries.<a href="./src/withpi/resources/queries.py">classify</a>(\*\*<a href="src/withpi/types/query_classify_params.py">params</a>) -> <a href="./src/withpi/types/query_classify_response.py">QueryClassifyResponse</a></code>
- <code title="post /queries/generate_fanouts">client.queries.<a href="./src/withpi/resources/queries.py">generate_fanouts</a>(\*\*<a href="src/withpi/types/query_generate_fanouts_params.py">params</a>) -> <a href="./src/withpi/types/query_generate_fanouts_response.py">QueryGenerateFanoutsResponse</a></code>

# Scorer

Types:

```python
from withpi.types import ScorerScoreResponse
```

Methods:

- <code title="post /scorer/generate_dimensions">client.scorer.<a href="./src/withpi/resources/scorer/scorer.py">generate_dimensions</a>(\*\*<a href="src/withpi/types/scorer_generate_dimensions_params.py">params</a>) -> <a href="./src/withpi/types/shared/scorer.py">Scorer</a></code>
- <code title="post /scorer/read_from_hf">client.scorer.<a href="./src/withpi/resources/scorer/scorer.py">read_from_hf</a>(\*\*<a href="src/withpi/types/scorer_read_from_hf_params.py">params</a>) -> <a href="./src/withpi/types/shared/scorer.py">Scorer</a></code>
- <code title="post /scorer/score">client.scorer.<a href="./src/withpi/resources/scorer/scorer.py">score</a>(\*\*<a href="src/withpi/types/scorer_score_params.py">params</a>) -> <a href="./src/withpi/types/scorer_score_response.py">ScorerScoreResponse</a></code>

## Calibrate

Types:

```python
from withpi.types.scorer import (
    CalibrateCreateResponse,
    CalibrateRetrieveResponse,
    CalibrateListResponse,
    CalibrateCancelResponse,
    CalibrateMessagesResponse,
)
```

Methods:

- <code title="post /scorer/calibrate">client.scorer.calibrate.<a href="./src/withpi/resources/scorer/calibrate.py">create</a>(\*\*<a href="src/withpi/types/scorer/calibrate_create_params.py">params</a>) -> <a href="./src/withpi/types/scorer/calibrate_create_response.py">CalibrateCreateResponse</a></code>
- <code title="get /scorer/calibrate/{job_id}">client.scorer.calibrate.<a href="./src/withpi/resources/scorer/calibrate.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/scorer/calibrate_retrieve_response.py">CalibrateRetrieveResponse</a></code>
- <code title="get /scorer/calibrate">client.scorer.calibrate.<a href="./src/withpi/resources/scorer/calibrate.py">list</a>(\*\*<a href="src/withpi/types/scorer/calibrate_list_params.py">params</a>) -> <a href="./src/withpi/types/scorer/calibrate_list_response.py">CalibrateListResponse</a></code>
- <code title="delete /scorer/calibrate/{job_id}">client.scorer.calibrate.<a href="./src/withpi/resources/scorer/calibrate.py">cancel</a>(job_id) -> str</code>
- <code title="get /scorer/calibrate/{job_id}/messages">client.scorer.calibrate.<a href="./src/withpi/resources/scorer/calibrate.py">messages</a>(job_id) -> str</code>
