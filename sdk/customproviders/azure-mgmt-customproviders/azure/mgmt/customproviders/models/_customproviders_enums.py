# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class ActionRouting(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The routing types that are supported for action requests.
    """

    PROXY = "Proxy"

class ProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The provisioning state of the resource provider.
    """

    ACCEPTED = "Accepted"
    DELETING = "Deleting"
    RUNNING = "Running"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"

class ResourceTypeRouting(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The routing types that are supported for resource requests.
    """

    PROXY = "Proxy"
    PROXY_CACHE = "Proxy,Cache"

class ValidationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of validation to run against a matching request.
    """

    SWAGGER = "Swagger"
