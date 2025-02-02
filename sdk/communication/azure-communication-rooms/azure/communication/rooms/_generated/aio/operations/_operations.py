# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ...operations._operations import (
    build_rooms_add_participants_request,
    build_rooms_create_room_request,
    build_rooms_delete_room_request,
    build_rooms_get_participants_request,
    build_rooms_get_room_request,
    build_rooms_remove_participants_request,
    build_rooms_update_participants_request,
    build_rooms_update_room_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class RoomsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.communication.rooms.aio.AzureCommunicationRoomsService`'s
        :attr:`rooms` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def create_room(
        self,
        create_room_request: _models.CreateRoomRequest,
        *,
        repeatability_request_id: Optional[str] = None,
        repeatability_first_sent: Optional[datetime.datetime] = None,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.RoomModel:
        """Creates a new room.

        Creates a new room.

        :param create_room_request: The create room request body. Required.
        :type create_room_request: ~azure.communication.rooms.models.CreateRoomRequest
        :keyword repeatability_request_id: If specified, the client directs that the request is
         repeatable; that is, that the client can make the request multiple times with the same
         Repeatability-Request-Id and get back an appropriate response without the server executing the
         request multiple times. The value of the Repeatability-Request-Id is an opaque string
         representing a client-generated, globally unique for all time, identifier for the request. It
         is recommended to use version 4 (random) UUIDs. Default value is None.
        :paramtype repeatability_request_id: str
        :keyword repeatability_first_sent: If Repeatability-Request-ID header is specified, then
         Repeatability-First-Sent header must also be specified. The value should be the date and time
         at which the request was first created, expressed using the IMF-fixdate form of HTTP-date.
         Default value is None.
        :paramtype repeatability_first_sent: ~datetime.datetime
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: RoomModel
        :rtype: ~azure.communication.rooms.models.RoomModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_room(
        self,
        create_room_request: IO,
        *,
        repeatability_request_id: Optional[str] = None,
        repeatability_first_sent: Optional[datetime.datetime] = None,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.RoomModel:
        """Creates a new room.

        Creates a new room.

        :param create_room_request: The create room request body. Required.
        :type create_room_request: IO
        :keyword repeatability_request_id: If specified, the client directs that the request is
         repeatable; that is, that the client can make the request multiple times with the same
         Repeatability-Request-Id and get back an appropriate response without the server executing the
         request multiple times. The value of the Repeatability-Request-Id is an opaque string
         representing a client-generated, globally unique for all time, identifier for the request. It
         is recommended to use version 4 (random) UUIDs. Default value is None.
        :paramtype repeatability_request_id: str
        :keyword repeatability_first_sent: If Repeatability-Request-ID header is specified, then
         Repeatability-First-Sent header must also be specified. The value should be the date and time
         at which the request was first created, expressed using the IMF-fixdate form of HTTP-date.
         Default value is None.
        :paramtype repeatability_first_sent: ~datetime.datetime
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: RoomModel
        :rtype: ~azure.communication.rooms.models.RoomModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_room(
        self,
        create_room_request: Union[_models.CreateRoomRequest, IO],
        *,
        repeatability_request_id: Optional[str] = None,
        repeatability_first_sent: Optional[datetime.datetime] = None,
        **kwargs: Any
    ) -> _models.RoomModel:
        """Creates a new room.

        Creates a new room.

        :param create_room_request: The create room request body. Is either a model type or a IO type.
         Required.
        :type create_room_request: ~azure.communication.rooms.models.CreateRoomRequest or IO
        :keyword repeatability_request_id: If specified, the client directs that the request is
         repeatable; that is, that the client can make the request multiple times with the same
         Repeatability-Request-Id and get back an appropriate response without the server executing the
         request multiple times. The value of the Repeatability-Request-Id is an opaque string
         representing a client-generated, globally unique for all time, identifier for the request. It
         is recommended to use version 4 (random) UUIDs. Default value is None.
        :paramtype repeatability_request_id: str
        :keyword repeatability_first_sent: If Repeatability-Request-ID header is specified, then
         Repeatability-First-Sent header must also be specified. The value should be the date and time
         at which the request was first created, expressed using the IMF-fixdate form of HTTP-date.
         Default value is None.
        :paramtype repeatability_first_sent: ~datetime.datetime
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :return: RoomModel
        :rtype: ~azure.communication.rooms.models.RoomModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.RoomModel]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_room_request, (IO, bytes)):
            _content = create_room_request
        else:
            _json = self._serialize.body(create_room_request, "CreateRoomRequest")

        request = build_rooms_create_room_request(
            repeatability_request_id=repeatability_request_id,
            repeatability_first_sent=repeatability_first_sent,
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
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CommunicationErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("RoomModel", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    @distributed_trace_async
    async def get_room(self, room_id: str, **kwargs: Any) -> _models.RoomModel:
        """Retrieves an existing room by id.

        Retrieves an existing room by id.

        :param room_id: The id of the room requested. Required.
        :type room_id: str
        :return: RoomModel
        :rtype: ~azure.communication.rooms.models.RoomModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[_models.RoomModel]

        request = build_rooms_get_room_request(
            room_id=room_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CommunicationErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("RoomModel", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    @overload
    async def update_room(
        self,
        room_id: str,
        patch_room_request: Optional[_models.UpdateRoomRequest] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.RoomModel:
        """Update a room with given changes.

        Update a room with given changes.

        :param room_id: The id of the room requested. Required.
        :type room_id: str
        :param patch_room_request: The patch room request. Default value is None.
        :type patch_room_request: ~azure.communication.rooms.models.UpdateRoomRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: RoomModel
        :rtype: ~azure.communication.rooms.models.RoomModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update_room(
        self,
        room_id: str,
        patch_room_request: Optional[IO] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.RoomModel:
        """Update a room with given changes.

        Update a room with given changes.

        :param room_id: The id of the room requested. Required.
        :type room_id: str
        :param patch_room_request: The patch room request. Default value is None.
        :type patch_room_request: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Known values are: 'application/json', 'application/merge-patch+json'. Default value is
         "application/json".
        :paramtype content_type: str
        :return: RoomModel
        :rtype: ~azure.communication.rooms.models.RoomModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update_room(
        self, room_id: str, patch_room_request: Optional[Union[_models.UpdateRoomRequest, IO]] = None, **kwargs: Any
    ) -> _models.RoomModel:
        """Update a room with given changes.

        Update a room with given changes.

        :param room_id: The id of the room requested. Required.
        :type room_id: str
        :param patch_room_request: The patch room request. Is either a model type or a IO type. Default
         value is None.
        :type patch_room_request: ~azure.communication.rooms.models.UpdateRoomRequest or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json',
         'application/merge-patch+json'. Default value is None.
        :paramtype content_type: str
        :return: RoomModel
        :rtype: ~azure.communication.rooms.models.RoomModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.RoomModel]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(patch_room_request, (IO, bytes)):
            _content = patch_room_request
        else:
            if patch_room_request is not None:
                _json = self._serialize.body(patch_room_request, "UpdateRoomRequest")
            else:
                _json = None

        request = build_rooms_update_room_request(
            room_id=room_id,
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
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CommunicationErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("RoomModel", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    @distributed_trace_async
    async def delete_room(self, room_id: str, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Delete a room.

        Delete a room.

        :param room_id: The id of the room to be deleted. Required.
        :type room_id: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_rooms_delete_room_request(
            room_id=room_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CommunicationErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def get_participants(self, room_id: str, **kwargs: Any) -> _models.ParticipantsCollection:
        """Get participants in a room.

        Get participants in a room.

        :param room_id: The id of the room to get participants from. Required.
        :type room_id: str
        :return: ParticipantsCollection
        :rtype: ~azure.communication.rooms.models.ParticipantsCollection
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ParticipantsCollection]

        request = build_rooms_get_participants_request(
            room_id=room_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CommunicationErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("ParticipantsCollection", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    @overload
    async def add_participants(
        self,
        room_id: str,
        add_participants_request: _models.AddParticipantsRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ParticipantsCollection:
        """Adds participants to a room. If participants already exist, no change occurs.

        Adds participants to a room. If participants already exist, no change occurs.

        :param room_id: Room id to add participants. Required.
        :type room_id: str
        :param add_participants_request: Participants to be added to the room. Required.
        :type add_participants_request: ~azure.communication.rooms.models.AddParticipantsRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ParticipantsCollection
        :rtype: ~azure.communication.rooms.models.ParticipantsCollection
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def add_participants(
        self, room_id: str, add_participants_request: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ParticipantsCollection:
        """Adds participants to a room. If participants already exist, no change occurs.

        Adds participants to a room. If participants already exist, no change occurs.

        :param room_id: Room id to add participants. Required.
        :type room_id: str
        :param add_participants_request: Participants to be added to the room. Required.
        :type add_participants_request: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ParticipantsCollection
        :rtype: ~azure.communication.rooms.models.ParticipantsCollection
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def add_participants(
        self, room_id: str, add_participants_request: Union[_models.AddParticipantsRequest, IO], **kwargs: Any
    ) -> _models.ParticipantsCollection:
        """Adds participants to a room. If participants already exist, no change occurs.

        Adds participants to a room. If participants already exist, no change occurs.

        :param room_id: Room id to add participants. Required.
        :type room_id: str
        :param add_participants_request: Participants to be added to the room. Is either a model type
         or a IO type. Required.
        :type add_participants_request: ~azure.communication.rooms.models.AddParticipantsRequest or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :return: ParticipantsCollection
        :rtype: ~azure.communication.rooms.models.ParticipantsCollection
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ParticipantsCollection]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(add_participants_request, (IO, bytes)):
            _content = add_participants_request
        else:
            _json = self._serialize.body(add_participants_request, "AddParticipantsRequest")

        request = build_rooms_add_participants_request(
            room_id=room_id,
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
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CommunicationErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("ParticipantsCollection", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    @overload
    async def update_participants(
        self,
        room_id: str,
        update_participants_request: _models.UpdateParticipantsRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ParticipantsCollection:
        """Update participants in a room.

        Update participants in a room.

        :param room_id: The room id. Required.
        :type room_id: str
        :param update_participants_request: Participants in a room to be updated. Required.
        :type update_participants_request: ~azure.communication.rooms.models.UpdateParticipantsRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ParticipantsCollection
        :rtype: ~azure.communication.rooms.models.ParticipantsCollection
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update_participants(
        self, room_id: str, update_participants_request: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ParticipantsCollection:
        """Update participants in a room.

        Update participants in a room.

        :param room_id: The room id. Required.
        :type room_id: str
        :param update_participants_request: Participants in a room to be updated. Required.
        :type update_participants_request: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ParticipantsCollection
        :rtype: ~azure.communication.rooms.models.ParticipantsCollection
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update_participants(
        self, room_id: str, update_participants_request: Union[_models.UpdateParticipantsRequest, IO], **kwargs: Any
    ) -> _models.ParticipantsCollection:
        """Update participants in a room.

        Update participants in a room.

        :param room_id: The room id. Required.
        :type room_id: str
        :param update_participants_request: Participants in a room to be updated. Is either a model
         type or a IO type. Required.
        :type update_participants_request: ~azure.communication.rooms.models.UpdateParticipantsRequest
         or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :return: ParticipantsCollection
        :rtype: ~azure.communication.rooms.models.ParticipantsCollection
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ParticipantsCollection]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(update_participants_request, (IO, bytes)):
            _content = update_participants_request
        else:
            _json = self._serialize.body(update_participants_request, "UpdateParticipantsRequest")

        request = build_rooms_update_participants_request(
            room_id=room_id,
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
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CommunicationErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("ParticipantsCollection", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    @overload
    async def remove_participants(
        self,
        room_id: str,
        remove_participants_request: _models.RemoveParticipantsRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ParticipantsCollection:
        """Remove participants from a room.

        Remove participants from a room.

        :param room_id: Room id to remove the participants from. Required.
        :type room_id: str
        :param remove_participants_request: Participants in a room to be removed. Required.
        :type remove_participants_request: ~azure.communication.rooms.models.RemoveParticipantsRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ParticipantsCollection
        :rtype: ~azure.communication.rooms.models.ParticipantsCollection
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def remove_participants(
        self, room_id: str, remove_participants_request: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ParticipantsCollection:
        """Remove participants from a room.

        Remove participants from a room.

        :param room_id: Room id to remove the participants from. Required.
        :type room_id: str
        :param remove_participants_request: Participants in a room to be removed. Required.
        :type remove_participants_request: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ParticipantsCollection
        :rtype: ~azure.communication.rooms.models.ParticipantsCollection
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def remove_participants(
        self, room_id: str, remove_participants_request: Union[_models.RemoveParticipantsRequest, IO], **kwargs: Any
    ) -> _models.ParticipantsCollection:
        """Remove participants from a room.

        Remove participants from a room.

        :param room_id: Room id to remove the participants from. Required.
        :type room_id: str
        :param remove_participants_request: Participants in a room to be removed. Is either a model
         type or a IO type. Required.
        :type remove_participants_request: ~azure.communication.rooms.models.RemoveParticipantsRequest
         or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :return: ParticipantsCollection
        :rtype: ~azure.communication.rooms.models.ParticipantsCollection
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ParticipantsCollection]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(remove_participants_request, (IO, bytes)):
            _content = remove_participants_request
        else:
            _json = self._serialize.body(remove_participants_request, "RemoveParticipantsRequest")

        request = build_rooms_remove_participants_request(
            room_id=room_id,
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
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CommunicationErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("ParticipantsCollection", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
