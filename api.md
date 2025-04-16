# Shared Types

```python
from withpi.types import (
    DataGenerationStatus,
    Example,
    ExplorationMode,
    QueryClassifierResult,
    QueryFanoutExample,
    Question,
    ScoringDimension,
    ScoringSpec,
    ScoringSpecCalibrationStatus,
    ScoringSubDimension,
    ScoringSystemMetrics,
    SyntheticDataStatus,
)
```

# Data

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

# ScoringSystem

Types:

```python
from withpi.types import (
    ScoringSystemGenerateResponse,
    ScoringSystemImportSpecResponse,
    ScoringSystemUploadToHuggingfaceResponse,
)
```

Methods:

- <code title="post /scoring_system/generate">client.scoring_system.<a href="./src/withpi/resources/scoring_system/scoring_system.py">generate</a>(\*\*<a href="src/withpi/types/scoring_system_generate_params.py">params</a>) -> <a href="./src/withpi/types/scoring_system_generate_response.py">ScoringSystemGenerateResponse</a></code>
- <code title="post /scoring_system/import_spec">client.scoring_system.<a href="./src/withpi/resources/scoring_system/scoring_system.py">import_spec</a>(\*\*<a href="src/withpi/types/scoring_system_import_spec_params.py">params</a>) -> <a href="./src/withpi/types/scoring_system_import_spec_response.py">ScoringSystemImportSpecResponse</a></code>
- <code title="post /scoring_system/score">client.scoring_system.<a href="./src/withpi/resources/scoring_system/scoring_system.py">score</a>(\*\*<a href="src/withpi/types/scoring_system_score_params.py">params</a>) -> <a href="./src/withpi/types/shared/scoring_system_metrics.py">ScoringSystemMetrics</a></code>
- <code title="post /scoring_system/to_huggingface">client.scoring_system.<a href="./src/withpi/resources/scoring_system/scoring_system.py">upload_to_huggingface</a>(\*\*<a href="src/withpi/types/scoring_system_upload_to_huggingface_params.py">params</a>) -> str</code>

## Calibrate

Types:

```python
from withpi.types.scoring_system import (
    CalibrateListResponse,
    CalibrateCancelResponse,
    CalibrateStreamMessagesResponse,
)
```

Methods:

- <code title="get /scoring_system/calibrate/{job_id}">client.scoring_system.calibrate.<a href="./src/withpi/resources/scoring_system/calibrate.py">retrieve</a>(job_id) -> <a href="./src/withpi/types/shared/scoring_spec_calibration_status.py">ScoringSpecCalibrationStatus</a></code>
- <code title="get /scoring_system/calibrate">client.scoring_system.calibrate.<a href="./src/withpi/resources/scoring_system/calibrate.py">list</a>(\*\*<a href="src/withpi/types/scoring_system/calibrate_list_params.py">params</a>) -> <a href="./src/withpi/types/scoring_system/calibrate_list_response.py">CalibrateListResponse</a></code>
- <code title="delete /scoring_system/calibrate/{job_id}">client.scoring_system.calibrate.<a href="./src/withpi/resources/scoring_system/calibrate.py">cancel</a>(job_id) -> str</code>
- <code title="post /scoring_system/calibrate">client.scoring_system.calibrate.<a href="./src/withpi/resources/scoring_system/calibrate.py">start_job</a>(\*\*<a href="src/withpi/types/scoring_system/calibrate_start_job_params.py">params</a>) -> <a href="./src/withpi/types/shared/scoring_spec_calibration_status.py">ScoringSpecCalibrationStatus</a></code>
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

- <code title="post /search/query_classifier/classify">client.search.query_classifier.<a href="./src/withpi/resources/search/query_classifier.py">classify</a>(\*\*<a href="src/withpi/types/search/query_classifier_classify_params.py">params</a>) -> <a href="./src/withpi/types/search/query_classifier_classify_response.py">QueryClassifierClassifyResponse</a></code>
