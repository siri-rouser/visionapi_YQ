from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class BoundingBox(_message.Message):
    __slots__ = ["max_x", "max_y", "min_x", "min_y"]
    MAX_X_FIELD_NUMBER: ClassVar[int]
    MAX_Y_FIELD_NUMBER: ClassVar[int]
    MIN_X_FIELD_NUMBER: ClassVar[int]
    MIN_Y_FIELD_NUMBER: ClassVar[int]
    max_x: float
    max_y: float
    min_x: float
    min_y: float
    def __init__(self, min_x: Optional[float] = ..., min_y: Optional[float] = ..., max_x: Optional[float] = ..., max_y: Optional[float] = ...) -> None: ...

class Detection(_message.Message):
    __slots__ = ["bounding_box", "class_id", "confidence", "feature", "geo_coordinate", "object_id"]
    BOUNDING_BOX_FIELD_NUMBER: ClassVar[int]
    CLASS_ID_FIELD_NUMBER: ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: ClassVar[int]
    FEATURE_FIELD_NUMBER: ClassVar[int]
    GEO_COORDINATE_FIELD_NUMBER: ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: ClassVar[int]
    bounding_box: BoundingBox
    class_id: int
    confidence: float
    feature: _containers.RepeatedScalarFieldContainer[float]
    geo_coordinate: GeoCoordinate
    object_id: int
    def __init__(self, bounding_box: Optional[Union[BoundingBox, Mapping]] = ..., confidence: Optional[float] = ..., class_id: Optional[int] = ..., object_id: Optional[int] = ..., geo_coordinate: Optional[Union[GeoCoordinate, Mapping]] = ..., feature: Optional[Iterable[float]] = ...) -> None: ...

class GeoCoordinate(_message.Message):
    __slots__ = ["latitude", "longitude"]
    LATITUDE_FIELD_NUMBER: ClassVar[int]
    LONGITUDE_FIELD_NUMBER: ClassVar[int]
    latitude: float
    longitude: float
    def __init__(self, latitude: Optional[float] = ..., longitude: Optional[float] = ...) -> None: ...

class Metrics(_message.Message):
    __slots__ = ["detection_inference_time_us", "feature_extraction_time_us", "tracking_inference_time_us"]
    DETECTION_INFERENCE_TIME_US_FIELD_NUMBER: ClassVar[int]
    FEATURE_EXTRACTION_TIME_US_FIELD_NUMBER: ClassVar[int]
    TRACKING_INFERENCE_TIME_US_FIELD_NUMBER: ClassVar[int]
    detection_inference_time_us: int
    feature_extraction_time_us: int
    tracking_inference_time_us: int
    def __init__(self, detection_inference_time_us: Optional[int] = ..., tracking_inference_time_us: Optional[int] = ..., feature_extraction_time_us: Optional[int] = ...) -> None: ...

class SaeMessage(_message.Message):
    __slots__ = ["detections", "frame", "metrics", "trajectory"]
    DETECTIONS_FIELD_NUMBER: ClassVar[int]
    FRAME_FIELD_NUMBER: ClassVar[int]
    METRICS_FIELD_NUMBER: ClassVar[int]
    TRAJECTORY_FIELD_NUMBER: ClassVar[int]
    detections: _containers.RepeatedCompositeFieldContainer[Detection]
    frame: VideoFrame
    metrics: Metrics
    trajectory: Trajectory
    def __init__(self, frame: Optional[Union[VideoFrame, Mapping]] = ..., detections: Optional[Iterable[Union[Detection, Mapping]]] = ..., trajectory: Optional[Union[Trajectory, Mapping]] = ..., metrics: Optional[Union[Metrics, Mapping]] = ...) -> None: ...

class Shape(_message.Message):
    __slots__ = ["channels", "height", "width"]
    CHANNELS_FIELD_NUMBER: ClassVar[int]
    HEIGHT_FIELD_NUMBER: ClassVar[int]
    WIDTH_FIELD_NUMBER: ClassVar[int]
    channels: int
    height: int
    width: int
    def __init__(self, height: Optional[int] = ..., width: Optional[int] = ..., channels: Optional[int] = ...) -> None: ...

class Tracklet(_message.Message):
    __slots__ = ["age", "detections_info", "end_time", "entry_zone", "exit_zone", "mean_feature", "start_time", "status"]
    AGE_FIELD_NUMBER: ClassVar[int]
    DETECTIONS_INFO_FIELD_NUMBER: ClassVar[int]
    END_TIME_FIELD_NUMBER: ClassVar[int]
    ENTRY_ZONE_FIELD_NUMBER: ClassVar[int]
    EXIT_ZONE_FIELD_NUMBER: ClassVar[int]
    MEAN_FEATURE_FIELD_NUMBER: ClassVar[int]
    START_TIME_FIELD_NUMBER: ClassVar[int]
    STATUS_FIELD_NUMBER: ClassVar[int]
    age: int
    detections_info: _containers.RepeatedCompositeFieldContainer[Detection]
    end_time: float
    entry_zone: str
    exit_zone: str
    mean_feature: _containers.RepeatedScalarFieldContainer[float]
    start_time: float
    status: str
    def __init__(self, mean_feature: Optional[Iterable[float]] = ..., status: Optional[str] = ..., start_time: Optional[float] = ..., end_time: Optional[float] = ..., entry_zone: Optional[str] = ..., exit_zone: Optional[str] = ..., detections_info: Optional[Iterable[Union[Detection, Mapping]]] = ..., age: Optional[int] = ...) -> None: ...

class TrackletsByCamera(_message.Message):
    __slots__ = ["tracklets"]
    class TrackletsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: Tracklet
        def __init__(self, key: Optional[str] = ..., value: Optional[Union[Tracklet, Mapping]] = ...) -> None: ...
    TRACKLETS_FIELD_NUMBER: ClassVar[int]
    tracklets: _containers.MessageMap[str, Tracklet]
    def __init__(self, tracklets: Optional[Mapping[str, Tracklet]] = ...) -> None: ...

class Trajectory(_message.Message):
    __slots__ = ["cameras"]
    class CamerasEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: TrackletsByCamera
        def __init__(self, key: Optional[str] = ..., value: Optional[Union[TrackletsByCamera, Mapping]] = ...) -> None: ...
    CAMERAS_FIELD_NUMBER: ClassVar[int]
    cameras: _containers.MessageMap[str, TrackletsByCamera]
    def __init__(self, cameras: Optional[Mapping[str, TrackletsByCamera]] = ...) -> None: ...

class VideoFrame(_message.Message):
    __slots__ = ["frame_data", "frame_data_jpeg", "shape", "source_id", "timestamp_utc_ms"]
    FRAME_DATA_FIELD_NUMBER: ClassVar[int]
    FRAME_DATA_JPEG_FIELD_NUMBER: ClassVar[int]
    SHAPE_FIELD_NUMBER: ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: ClassVar[int]
    TIMESTAMP_UTC_MS_FIELD_NUMBER: ClassVar[int]
    frame_data: bytes
    frame_data_jpeg: bytes
    shape: Shape
    source_id: str
    timestamp_utc_ms: int
    def __init__(self, source_id: Optional[str] = ..., timestamp_utc_ms: Optional[int] = ..., shape: Optional[Union[Shape, Mapping]] = ..., frame_data: Optional[bytes] = ..., frame_data_jpeg: Optional[bytes] = ...) -> None: ...
