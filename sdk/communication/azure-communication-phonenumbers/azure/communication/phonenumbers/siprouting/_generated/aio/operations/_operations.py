# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ...operations._operations import build_sip_routing_get_request, build_sip_routing_update_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class SipRoutingOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.communication.phonenumbers.siprouting.aio.SIPRoutingService`'s
        :attr:`sip_routing` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get(self, **kwargs: Any) -> _models.SipConfiguration:
        """Gets SIP configuration for resource.

        Gets SIP configuration for resource.

        :return: SipConfiguration
        :rtype: ~azure.communication.phonenumbers.siprouting.models.SipConfiguration
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.SipConfiguration] = kwargs.pop("cls", None)

        request = build_sip_routing_get_request(
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CommunicationErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("SipConfiguration", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    @overload
    async def update(
        self,
        body: Optional[_models.SipConfiguration] = None,
        *,
        content_type: str = "application/merge-patch+json",
        **kwargs: Any
    ) -> _models.SipConfiguration:
        """Updates SIP configuration for resource.

        Updates SIP configuration for resource.

        :param body: Sip configuration update object. Default value is None.
        :type body: ~azure.communication.phonenumbers.siprouting.models.SipConfiguration
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: SipConfiguration
        :rtype: ~azure.communication.phonenumbers.siprouting.models.SipConfiguration
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self, body: Optional[IO] = None, *, content_type: str = "application/merge-patch+json", **kwargs: Any
    ) -> _models.SipConfiguration:
        """Updates SIP configuration for resource.

        Updates SIP configuration for resource.

        :param body: Sip configuration update object. Default value is None.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: SipConfiguration
        :rtype: ~azure.communication.phonenumbers.siprouting.models.SipConfiguration
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self, body: Optional[Union[_models.SipConfiguration, IO]] = None, **kwargs: Any
    ) -> _models.SipConfiguration:
        """Updates SIP configuration for resource.

        Updates SIP configuration for resource.

        :param body: Sip configuration update object. Is either a SipConfiguration type or a IO type.
         Default value is None.
        :type body: ~azure.communication.phonenumbers.siprouting.models.SipConfiguration or IO
        :keyword content_type: Body Parameter content-type. Known values are:
         'application/merge-patch+json'. Default value is None.
        :paramtype content_type: str
        :return: SipConfiguration
        :rtype: ~azure.communication.phonenumbers.siprouting.models.SipConfiguration
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.SipConfiguration] = kwargs.pop("cls", None)

        content_type = content_type or "application/merge-patch+json"
        _json = None
        _content = None
        if isinstance(body, (IO, bytes)):
            _content = body
        else:
            if body is not None:
                _json = self._serialize.body(body, "SipConfiguration")
            else:
                _json = None

        request = build_sip_routing_update_request(
            content_type=content_type,
            api_version=self._config.api_version,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CommunicationErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("SipConfiguration", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
