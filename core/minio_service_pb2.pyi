from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FileUploadRequest(_message.Message):
    __slots__ = ["file_path", "bucket_name", "object_name"]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    bucket_name: str
    object_name: str
    def __init__(self, file_path: _Optional[str] = ..., bucket_name: _Optional[str] = ..., object_name: _Optional[str] = ...) -> None: ...

class FileUploadResponse(_message.Message):
    __slots__ = ["success", "message"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...

class UploadObjectRequest(_message.Message):
    __slots__ = ["bucket_name", "object_name", "file_content"]
    BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    bucket_name: str
    object_name: str
    file_content: str
    def __init__(self, bucket_name: _Optional[str] = ..., object_name: _Optional[str] = ..., file_content: _Optional[str] = ...) -> None: ...

class UploadObjectResponse(_message.Message):
    __slots__ = ["success", "error_message"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error_message: str
    def __init__(self, success: bool = ..., error_message: _Optional[str] = ...) -> None: ...
