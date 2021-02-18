# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import CheckNameRequest
    from ._models_py3 import CheckNameResult
    from ._models_py3 import DigitalTwinsDescription
    from ._models_py3 import DigitalTwinsDescriptionListResult
    from ._models_py3 import DigitalTwinsEndpointResource
    from ._models_py3 import DigitalTwinsEndpointResourceListResult
    from ._models_py3 import DigitalTwinsEndpointResourceProperties
    from ._models_py3 import DigitalTwinsPatchDescription
    from ._models_py3 import DigitalTwinsResource
    from ._models_py3 import ErrorDefinition
    from ._models_py3 import ErrorResponse
    from ._models_py3 import EventGrid
    from ._models_py3 import EventHub
    from ._models_py3 import ExternalResource
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationListResult
    from ._models_py3 import ServiceBus
except (SyntaxError, ImportError):
    from ._models import CheckNameRequest  # type: ignore
    from ._models import CheckNameResult  # type: ignore
    from ._models import DigitalTwinsDescription  # type: ignore
    from ._models import DigitalTwinsDescriptionListResult  # type: ignore
    from ._models import DigitalTwinsEndpointResource  # type: ignore
    from ._models import DigitalTwinsEndpointResourceListResult  # type: ignore
    from ._models import DigitalTwinsEndpointResourceProperties  # type: ignore
    from ._models import DigitalTwinsPatchDescription  # type: ignore
    from ._models import DigitalTwinsResource  # type: ignore
    from ._models import ErrorDefinition  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import EventGrid  # type: ignore
    from ._models import EventHub  # type: ignore
    from ._models import ExternalResource  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import ServiceBus  # type: ignore

from ._azure_digital_twins_management_client_enums import (
    EndpointProvisioningState,
    EndpointType,
    ProvisioningState,
    Reason,
)

__all__ = [
    'CheckNameRequest',
    'CheckNameResult',
    'DigitalTwinsDescription',
    'DigitalTwinsDescriptionListResult',
    'DigitalTwinsEndpointResource',
    'DigitalTwinsEndpointResourceListResult',
    'DigitalTwinsEndpointResourceProperties',
    'DigitalTwinsPatchDescription',
    'DigitalTwinsResource',
    'ErrorDefinition',
    'ErrorResponse',
    'EventGrid',
    'EventHub',
    'ExternalResource',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'ServiceBus',
    'EndpointProvisioningState',
    'EndpointType',
    'ProvisioningState',
    'Reason',
]
