from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

ACTIVE: TrackletStatus
COMPLETED: TrackletStatus
DESCRIPTOR: _descriptor.FileDescriptor
ENTRY: ZoneStatus
EXIT: ZoneStatus
SEARCHING: TrackletStatus
UNDEFINED: ZoneStatus
UNKNOWN: TrackletStatus

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
    __slots__ = ["bounding_box", "class_id", "confidence", "cropped_img_jpeg", "feature", "frame_id", "geo_coordinate", "object_id", "timestamp_utc_ms"]
    BOUNDING_BOX_FIELD_NUMBER: _ClassVar[int]
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    CROPPED_IMG_JPEG_FIELD_NUMBER: _ClassVar[int]
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    FRAME_ID_FIELD_NUMBER: _ClassVar[int]
    GEO_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_UTC_MS_FIELD_NUMBER: _ClassVar[int]
    bounding_box: BoundingBox
    class_id: int
    confidence: float
    cropped_img_jpeg: bytes
    feature: _containers.RepeatedScalarFieldContainer[float]
    frame_id: int
    geo_coordinate: GeoCoordinate
    object_id: int
    timestamp_utc_ms: int
    def __init__(self, bounding_box: _Optional[_Union[BoundingBox, _Mapping]] = ..., confidence: _Optional[float] = ..., class_id: _Optional[int] = ..., object_id: _Optional[int] = ..., geo_coordinate: _Optional[_Union[GeoCoordinate, _Mapping]] = ..., feature: _Optional[_Iterable[float]] = ..., timestamp_utc_ms: _Optional[int] = ..., frame_id: _Optional[int] = ..., cropped_img_jpeg: _Optional[bytes] = ...) -> None: ...

class GeoCoordinate(_message.Message):
    __slots__ = ["latitude", "longitude"]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ...) -> None: ...

class Metrics(_message.Message):
    __slots__ = ["detection_inference_time_us", "feature_extraction_time_us", "merge_inference_time_us", "tracking_inference_time_us"]
    DETECTION_INFERENCE_TIME_US_FIELD_NUMBER: _ClassVar[int]
    FEATURE_EXTRACTION_TIME_US_FIELD_NUMBER: _ClassVar[int]
    MERGE_INFERENCE_TIME_US_FIELD_NUMBER: _ClassVar[int]
    TRACKING_INFERENCE_TIME_US_FIELD_NUMBER: _ClassVar[int]
    detection_inference_time_us: int
    feature_extraction_time_us: int
    merge_inference_time_us: int
    tracking_inference_time_us: int
    def __init__(self, detection_inference_time_us: _Optional[int] = ..., tracking_inference_time_us: _Optional[int] = ..., feature_extraction_time_us: _Optional[int] = ..., merge_inference_time_us: _Optional[int] = ...) -> None: ...

class MotionVector(_message.Message):
    __slots__ = ["x", "y"]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...

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
    __slots__ = ["age", "detections_info", "end_frame", "end_time", "mean_feature", "motion_vector", "start_frame", "start_time", "status", "zone"]
    AGE_FIELD_NUMBER: _ClassVar[int]
    DETECTIONS_INFO_FIELD_NUMBER: _ClassVar[int]
    END_FRAME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    MEAN_FEATURE_FIELD_NUMBER: _ClassVar[int]
    MOTION_VECTOR_FIELD_NUMBER: _ClassVar[int]
    START_FRAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    age: int
    detections_info: _containers.RepeatedCompositeFieldContainer[Detection]
    end_frame: int
    end_time: int
    mean_feature: _containers.RepeatedScalarFieldContainer[float]
    motion_vector: MotionVector
    start_frame: int
    start_time: int
    status: TrackletStatus
    zone: Zone
    def __init__(self, mean_feature: _Optional[_Iterable[float]] = ..., status: _Optional[_Union[TrackletStatus, str]] = ..., start_time: _Optional[int] = ..., start_frame: _Optional[int] = ..., end_frame: _Optional[int] = ..., end_time: _Optional[int] = ..., zone: _Optional[_Union[Zone, _Mapping]] = ..., detections_info: _Optional[_Iterable[_Union[Detection, _Mapping]]] = ..., age: _Optional[int] = ..., motion_vector: _Optional[_Union[MotionVector, _Mapping]] = ...) -> None: ...

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
    __slots__ = ["frame_data", "frame_data_jpeg", "frame_id", "shape", "source_id", "timestamp_utc_ms"]
    FRAME_DATA_FIELD_NUMBER: _ClassVar[int]
    FRAME_DATA_JPEG_FIELD_NUMBER: _ClassVar[int]
    FRAME_ID_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_UTC_MS_FIELD_NUMBER: _ClassVar[int]
    frame_data: bytes
    frame_data_jpeg: bytes
    frame_id: int
    shape: Shape
    source_id: str
    timestamp_utc_ms: int
    def __init__(self, source_id: _Optional[str] = ..., timestamp_utc_ms: _Optional[int] = ..., shape: _Optional[_Union[Shape, _Mapping]] = ..., frame_data: _Optional[bytes] = ..., frame_data_jpeg: _Optional[bytes] = ..., frame_id: _Optional[int] = ...) -> None: ...

class Zone(_message.Message):
    __slots__ = ["entry_zone_id", "entry_zone_type", "exit_zone_id", "exit_zone_type"]
    ENTRY_ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ZONE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXIT_ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    EXIT_ZONE_TYPE_FIELD_NUMBER: _ClassVar[int]
    entry_zone_id: int
    entry_zone_type: ZoneStatus
    exit_zone_id: int
    exit_zone_type: ZoneStatus
    def __init__(self, entry_zone_id: _Optional[int] = ..., exit_zone_id: _Optional[int] = ..., entry_zone_type: _Optional[_Union[ZoneStatus, str]] = ..., exit_zone_type: _Optional[_Union[ZoneStatus, str]] = ...) -> None: ...

class TrackletStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ZoneStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
