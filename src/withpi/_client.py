# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import queries
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import WithpiError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.data import data
from .resources.model import model
from .resources.prompt import prompt
from .resources.contracts import contracts
from .resources.scoring_system import scoring_system

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Withpi", "AsyncWithpi", "Client", "AsyncClient"]


class Withpi(SyncAPIClient):
    contracts: contracts.ContractsResource
    data: data.DataResource
    model: model.ModelResource
    prompt: prompt.PromptResource
    queries: queries.QueriesResource
    scoring_system: scoring_system.ScoringSystemResource
    with_raw_response: WithpiWithRawResponse
    with_streaming_response: WithpiWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Withpi client instance.

        This automatically infers the `api_key` argument from the `WITHPI_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("WITHPI_API_KEY")
        if api_key is None:
            raise WithpiError(
                "The api_key client option must be set either by passing api_key to the client or by setting the WITHPI_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("WITHPI_BASE_URL")
        if base_url is None:
            base_url = f"https://api.withpi.ai/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.contracts = contracts.ContractsResource(self)
        self.data = data.DataResource(self)
        self.model = model.ModelResource(self)
        self.prompt = prompt.PromptResource(self)
        self.queries = queries.QueriesResource(self)
        self.scoring_system = scoring_system.ScoringSystemResource(self)
        self.with_raw_response = WithpiWithRawResponse(self)
        self.with_streaming_response = WithpiWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncWithpi(AsyncAPIClient):
    contracts: contracts.AsyncContractsResource
    data: data.AsyncDataResource
    model: model.AsyncModelResource
    prompt: prompt.AsyncPromptResource
    queries: queries.AsyncQueriesResource
    scoring_system: scoring_system.AsyncScoringSystemResource
    with_raw_response: AsyncWithpiWithRawResponse
    with_streaming_response: AsyncWithpiWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncWithpi client instance.

        This automatically infers the `api_key` argument from the `WITHPI_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("WITHPI_API_KEY")
        if api_key is None:
            raise WithpiError(
                "The api_key client option must be set either by passing api_key to the client or by setting the WITHPI_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("WITHPI_BASE_URL")
        if base_url is None:
            base_url = f"https://api.withpi.ai/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.contracts = contracts.AsyncContractsResource(self)
        self.data = data.AsyncDataResource(self)
        self.model = model.AsyncModelResource(self)
        self.prompt = prompt.AsyncPromptResource(self)
        self.queries = queries.AsyncQueriesResource(self)
        self.scoring_system = scoring_system.AsyncScoringSystemResource(self)
        self.with_raw_response = AsyncWithpiWithRawResponse(self)
        self.with_streaming_response = AsyncWithpiWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class WithpiWithRawResponse:
    def __init__(self, client: Withpi) -> None:
        self.contracts = contracts.ContractsResourceWithRawResponse(client.contracts)
        self.data = data.DataResourceWithRawResponse(client.data)
        self.model = model.ModelResourceWithRawResponse(client.model)
        self.prompt = prompt.PromptResourceWithRawResponse(client.prompt)
        self.queries = queries.QueriesResourceWithRawResponse(client.queries)
        self.scoring_system = scoring_system.ScoringSystemResourceWithRawResponse(client.scoring_system)


class AsyncWithpiWithRawResponse:
    def __init__(self, client: AsyncWithpi) -> None:
        self.contracts = contracts.AsyncContractsResourceWithRawResponse(client.contracts)
        self.data = data.AsyncDataResourceWithRawResponse(client.data)
        self.model = model.AsyncModelResourceWithRawResponse(client.model)
        self.prompt = prompt.AsyncPromptResourceWithRawResponse(client.prompt)
        self.queries = queries.AsyncQueriesResourceWithRawResponse(client.queries)
        self.scoring_system = scoring_system.AsyncScoringSystemResourceWithRawResponse(client.scoring_system)


class WithpiWithStreamedResponse:
    def __init__(self, client: Withpi) -> None:
        self.contracts = contracts.ContractsResourceWithStreamingResponse(client.contracts)
        self.data = data.DataResourceWithStreamingResponse(client.data)
        self.model = model.ModelResourceWithStreamingResponse(client.model)
        self.prompt = prompt.PromptResourceWithStreamingResponse(client.prompt)
        self.queries = queries.QueriesResourceWithStreamingResponse(client.queries)
        self.scoring_system = scoring_system.ScoringSystemResourceWithStreamingResponse(client.scoring_system)


class AsyncWithpiWithStreamedResponse:
    def __init__(self, client: AsyncWithpi) -> None:
        self.contracts = contracts.AsyncContractsResourceWithStreamingResponse(client.contracts)
        self.data = data.AsyncDataResourceWithStreamingResponse(client.data)
        self.model = model.AsyncModelResourceWithStreamingResponse(client.model)
        self.prompt = prompt.AsyncPromptResourceWithStreamingResponse(client.prompt)
        self.queries = queries.AsyncQueriesResourceWithStreamingResponse(client.queries)
        self.scoring_system = scoring_system.AsyncScoringSystemResourceWithStreamingResponse(client.scoring_system)


Client = Withpi

AsyncClient = AsyncWithpi
