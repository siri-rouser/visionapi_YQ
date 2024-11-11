from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BoundingBox(_message.Message):
    __slots__ = ["max_x", "max_y", "min_x", "min_y"]
    MAX_X_FIELD_NUMBER: _ClassVar[int]
    MAX_Y_FIELD_NUMBER: _ClassVar[int]
    MIN_X_FIELD_NUMBER: _ClassVar[int]
    MIN_Y_FIELD_NUMBER: _ClassVar[int]
    max_x: float
    max_y: float
    min_x: float
    min_y: float
    def __init__(self, min_x: _Optional[float] = ..., min_y: _Optional[float] = ..., max_x: _Optional[float] = ..., max_y: _Optional[float] = ...) -> None: ...

class Detection(_message.Message):
    __slots__ = ["bounding_box", "class_id", "confidence", "feature", "geo_coordinate", "object_id"]
    BOUNDING_BOX_FIELD_NUMBER: _ClassVar[int]
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    GEO_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    bounding_box: BoundingBox
    class_id: int
    confidence: float
    feature: _containers.RepeatedScalarFieldContainer[float]
    geo_coordinate: GeoCoordinate
    object_id: int
    def __init__(self, bounding_box: _Optional[_Union[BoundingBox, _Mapping]] = ..., confidence: _Optional[float] = ..., class_id: _Optional[int] = ..., object_id: _Optional[int] = ..., geo_coordinate: _Optional[_Union[GeoCoordinate, _Mapping]] = ..., feature: _Optional[_Iterable[float]] = ...) -> None: ...

class GeoCoordinate(_message.Message):
    __slots__ = ["latitude", "longitude"]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ...) -> None: ...

class Metrics(_message.Message):
    __slots__ = ["detection_inference_time_us", "feature_extraction_time_us", "tracking_inference_time_us"]
    DETECTION_INFERENCE_TIME_US_FIELD_NUMBER: _ClassVar[int]
    FEATURE_EXTRACTION_TIME_US_FIELD_NUMBER: _ClassVar[int]
    TRACKING_INFERENCE_TIME_US_FIELD_NUMBER: _ClassVar[int]
    detection_inference_time_us: int
    feature_extraction_time_us: int
    tracking_inference_time_us: int
    def __init__(self, detection_inference_time_us: _Optional[int] = ..., tracking_inference_time_us: _Optional[int] = ..., feature_extraction_time_us: _Optional[int] = ...) -> None: ...

class SaeMessage(_message.Message):
    __slots__ = ["detections", "frame", "metrics", "trajectory"]
    DETECTIONS_FIELD_NUMBER: _ClassVar[int]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    TRAJECTORY_FIELD_NUMBER: _ClassVar[int]
    detections: _containers.RepeatedCompositeFieldContainer[Detection]
    frame: VideoFrame
    metrics: Metrics
    trajectory: Trajectory
    def __init__(self, frame: _Optional[_Union[VideoFrame, _Mapping]] = ..., detections: _Optional[_Iterable[_Union[Detection, _Mapping]]] = ..., trajectory: _Optional[_Union[Trajectory, _Mapping]] = ..., metrics: _Optional[_Union[Metrics, _Mapping]] = ...) -> None: ...

class Shape(_message.Message):
    __slots__ = ["channels", "height", "width"]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    channels: int
    height: int
    width: int
    def __init__(self, height: _Optional[int] = ..., width: _Optional[int] = ..., channels: _Optional[int] = ...) -> None: ...

class Tracklet(_message.Message):
    __slots__ = ["age", "detections_info", "end_time", "entry_zone", "exit_zone", "mean_feature", "start_time", "status"]
    AGE_FIELD_NUMBER: _ClassVar[int]
    DETECTIONS_INFO_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ZONE_FIELD_NUMBER: _ClassVar[int]
    EXIT_ZONE_FIELD_NUMBER: _ClassVar[int]
    MEAN_FEATURE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    age: int
    detections_info: _containers.RepeatedCompositeFieldContainer[Detection]
    end_time: float
    entry_zone: str
    exit_zone: str
    mean_feature: _containers.RepeatedScalarFieldContainer[float]
    start_time: float
    status: str
    def __init__(self, mean_feature: _Optional[_Iterable[float]] = ..., status: _Optional[str] = ..., start_time: _Optional[float] = ..., end_time: _Optional[float] = ..., entry_zone: _Optional[str] = ..., exit_zone: _Optional[str] = ..., detections_info: _Optional[_Iterable[_Union[Detection, _Mapping]]] = ..., age: _Optional[int] = ...) -> None: ...

class TrackletsByCamera(_message.Message):
    __slots__ = ["tracklets"]
    class TrackletsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Tracklet
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Tracklet, _Mapping]] = ...) -> None: ...
    TRACKLETS_FIELD_NUMBER: _ClassVar[int]
    tracklets: _containers.MessageMap[str, Tracklet]
    def __init__(self, tracklets: _Optional[_Mapping[str, Tracklet]] = ...) -> None: ...

class Trajectory(_message.Message):
    __slots__ = ["cameras"]
    class CamerasEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TrackletsByCamera
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TrackletsByCamera, _Mapping]] = ...) -> None: ...
    CAMERAS_FIELD_NUMBER: _ClassVar[int]
    cameras: _containers.MessageMap[str, TrackletsByCamera]
    def __init__(self, cameras: _Optional[_Mapping[str, TrackletsByCamera]] = ...) -> None: ...

class VideoFrame(_message.Message):
    __slots__ = ["frame_data", "frame_data_jpeg", "shape", "source_id", "timestamp_utc_ms"]
    FRAME_DATA_FIELD_NUMBER: _ClassVar[int]
    FRAME_DATA_JPEG_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_UTC_MS_FIELD_NUMBER: _ClassVar[int]
    frame_data: bytes
    frame_data_jpeg: bytes
    shape: Shape
    source_id: str
    timestamp_utc_ms: int
    def __init__(self, source_id: _Optional[str] = ..., timestamp_utc_ms: _Optional[int] = ..., shape: _Optional[_Union[Shape, _Mapping]] = ..., frame_data: _Optional[bytes] = ..., frame_data_jpeg: _Optional[bytes] = ...) -> None: ...
