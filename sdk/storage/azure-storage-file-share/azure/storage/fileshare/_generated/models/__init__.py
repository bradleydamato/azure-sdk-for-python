# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AccessPolicy
    from ._models_py3 import ClearRange
    from ._models_py3 import CopyFileSmbInfo
    from ._models_py3 import CorsRule
    from ._models_py3 import DirectoryItem
    from ._models_py3 import FileHTTPHeaders
    from ._models_py3 import FileItem
    from ._models_py3 import FileProperty
    from ._models_py3 import FileRange
    from ._models_py3 import FilesAndDirectoriesListSegment
    from ._models_py3 import HandleItem
    from ._models_py3 import LeaseAccessConditions
    from ._models_py3 import ListFilesAndDirectoriesSegmentResponse
    from ._models_py3 import ListHandlesResponse
    from ._models_py3 import ListSharesResponse
    from ._models_py3 import Metrics
    from ._models_py3 import RetentionPolicy
    from ._models_py3 import ShareFileRangeList
    from ._models_py3 import ShareItem
    from ._models_py3 import SharePermission
    from ._models_py3 import ShareProperties
    from ._models_py3 import ShareProtocolSettings
    from ._models_py3 import ShareSmbSettings
    from ._models_py3 import ShareStats
    from ._models_py3 import SignedIdentifier
    from ._models_py3 import SmbMultichannel
    from ._models_py3 import SourceModifiedAccessConditions
    from ._models_py3 import StorageError, StorageErrorException
    from ._models_py3 import StorageServiceProperties
except (SyntaxError, ImportError):
    from ._models import AccessPolicy
    from ._models import ClearRange
    from ._models import CopyFileSmbInfo
    from ._models import CorsRule
    from ._models import DirectoryItem
    from ._models import FileHTTPHeaders
    from ._models import FileItem
    from ._models import FileProperty
    from ._models import FileRange
    from ._models import FilesAndDirectoriesListSegment
    from ._models import HandleItem
    from ._models import LeaseAccessConditions
    from ._models import ListFilesAndDirectoriesSegmentResponse
    from ._models import ListHandlesResponse
    from ._models import ListSharesResponse
    from ._models import Metrics
    from ._models import RetentionPolicy
    from ._models import ShareFileRangeList
    from ._models import ShareItem
    from ._models import SharePermission
    from ._models import ShareProperties
    from ._models import ShareProtocolSettings
    from ._models import ShareSmbSettings
    from ._models import ShareStats
    from ._models import SignedIdentifier
    from ._models import SmbMultichannel
    from ._models import SourceModifiedAccessConditions
    from ._models import StorageError, StorageErrorException
    from ._models import StorageServiceProperties
from ._azure_file_storage_enums import (
    CopyStatusType,
    DeleteSnapshotsOptionType,
    FileRangeWriteType,
    LeaseDurationType,
    LeaseStateType,
    LeaseStatusType,
    ListSharesIncludeType,
    PermissionCopyModeType,
    ShareAccessTier,
    StorageErrorCode,
)

__all__ = [
    'AccessPolicy',
    'ClearRange',
    'CopyFileSmbInfo',
    'CorsRule',
    'DirectoryItem',
    'FileHTTPHeaders',
    'FileItem',
    'FileProperty',
    'FileRange',
    'FilesAndDirectoriesListSegment',
    'HandleItem',
    'LeaseAccessConditions',
    'ListFilesAndDirectoriesSegmentResponse',
    'ListHandlesResponse',
    'ListSharesResponse',
    'Metrics',
    'RetentionPolicy',
    'ShareFileRangeList',
    'ShareItem',
    'SharePermission',
    'ShareProperties',
    'ShareProtocolSettings',
    'ShareSmbSettings',
    'ShareStats',
    'SignedIdentifier',
    'SmbMultichannel',
    'SourceModifiedAccessConditions',
    'StorageError', 'StorageErrorException',
    'StorageServiceProperties',
    'StorageErrorCode',
    'LeaseDurationType',
    'LeaseStateType',
    'LeaseStatusType',
    'ShareAccessTier',
    'PermissionCopyModeType',
    'DeleteSnapshotsOptionType',
    'ListSharesIncludeType',
    'CopyStatusType',
    'FileRangeWriteType',
]
