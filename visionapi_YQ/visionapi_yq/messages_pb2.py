# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0emessages.proto\x12\tvisionapi\"\xac\x01\n\nSaeMessage\x12$\n\x05\x66rame\x18\x01 \x01(\x0b\x32\x15.visionapi.VideoFrame\x12(\n\ndetections\x18\x02 \x03(\x0b\x32\x14.visionapi.Detection\x12)\n\ntrajectory\x18\x03 \x01(\x0b\x32\x15.visionapi.Trajectory\x12#\n\x07metrics\x18\x63 \x01(\x0b\x32\x12.visionapi.Metrics\"\x87\x01\n\nVideoFrame\x12\x11\n\tsource_id\x18\x01 \x01(\t\x12\x18\n\x10timestamp_utc_ms\x18\x02 \x01(\x04\x12\x1f\n\x05shape\x18\x03 \x01(\x0b\x32\x10.visionapi.Shape\x12\x12\n\nframe_data\x18\x04 \x01(\x0c\x12\x17\n\x0f\x66rame_data_jpeg\x18\x05 \x01(\x0c\"8\n\x05Shape\x12\x0e\n\x06height\x18\x01 \x01(\r\x12\r\n\x05width\x18\x02 \x01(\r\x12\x10\n\x08\x63hannels\x18\x03 \x01(\r\"\xb5\x01\n\tDetection\x12,\n\x0c\x62ounding_box\x18\x01 \x01(\x0b\x32\x16.visionapi.BoundingBox\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12\x10\n\x08\x63lass_id\x18\x03 \x01(\r\x12\x11\n\tobject_id\x18\x04 \x01(\x05\x12\x30\n\x0egeo_coordinate\x18\x05 \x01(\x0b\x32\x18.visionapi.GeoCoordinate\x12\x0f\n\x07\x66\x65\x61ture\x18\x06 \x03(\x02\"I\n\x0b\x42oundingBox\x12\r\n\x05min_x\x18\x01 \x01(\x02\x12\r\n\x05min_y\x18\x02 \x01(\x02\x12\r\n\x05max_x\x18\x03 \x01(\x02\x12\r\n\x05max_y\x18\x04 \x01(\x02\"4\n\rGeoCoordinate\x12\x10\n\x08latitude\x18\x01 \x01(\x01\x12\x11\n\tlongitude\x18\x02 \x01(\x01\"v\n\x07Metrics\x12#\n\x1b\x64\x65tection_inference_time_us\x18\x01 \x01(\r\x12\"\n\x1atracking_inference_time_us\x18\x02 \x01(\r\x12\"\n\x1a\x66\x65\x61ture_extraction_time_us\x18\x03 \x01(\r\"\x8f\x01\n\nTrajectory\x12\x33\n\x07\x63\x61meras\x18\x01 \x03(\x0b\x32\".visionapi.Trajectory.CamerasEntry\x1aL\n\x0c\x43\x61merasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.visionapi.TrackletsByCamera:\x02\x38\x01\"\x9a\x01\n\x11TrackletsByCamera\x12>\n\ttracklets\x18\x01 \x03(\x0b\x32+.visionapi.TrackletsByCamera.TrackletsEntry\x1a\x45\n\x0eTrackletsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.visionapi.Tracklet:\x02\x38\x01\"\xb9\x01\n\x08Tracklet\x12\x14\n\x0cmean_feature\x18\x03 \x03(\x02\x12\x0e\n\x06status\x18\x04 \x01(\t\x12\x12\n\nstart_time\x18\x05 \x01(\x02\x12\x10\n\x08\x65nd_time\x18\x06 \x01(\x02\x12\x12\n\nentry_zone\x18\x07 \x01(\t\x12\x11\n\texit_zone\x18\x08 \x01(\t\x12-\n\x0f\x64\x65tections_info\x18\t \x03(\x0b\x32\x14.visionapi.Detection\x12\x0b\n\x03\x61ge\x18\n \x01(\rB\x16\n\x14\x64\x65.starwit.visionapib\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messages_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024de.starwit.visionapi'
  _TRAJECTORY_CAMERASENTRY._options = None
  _TRAJECTORY_CAMERASENTRY._serialized_options = b'8\001'
  _TRACKLETSBYCAMERA_TRACKLETSENTRY._options = None
  _TRACKLETSBYCAMERA_TRACKLETSENTRY._serialized_options = b'8\001'
  _SAEMESSAGE._serialized_start=30
  _SAEMESSAGE._serialized_end=202
  _VIDEOFRAME._serialized_start=205
  _VIDEOFRAME._serialized_end=340
  _SHAPE._serialized_start=342
  _SHAPE._serialized_end=398
  _DETECTION._serialized_start=401
  _DETECTION._serialized_end=582
  _BOUNDINGBOX._serialized_start=584
  _BOUNDINGBOX._serialized_end=657
  _GEOCOORDINATE._serialized_start=659
  _GEOCOORDINATE._serialized_end=711
  _METRICS._serialized_start=713
  _METRICS._serialized_end=831
  _TRAJECTORY._serialized_start=834
  _TRAJECTORY._serialized_end=977
  _TRAJECTORY_CAMERASENTRY._serialized_start=901
  _TRAJECTORY_CAMERASENTRY._serialized_end=977
  _TRACKLETSBYCAMERA._serialized_start=980
  _TRACKLETSBYCAMERA._serialized_end=1134
  _TRACKLETSBYCAMERA_TRACKLETSENTRY._serialized_start=1065
  _TRACKLETSBYCAMERA_TRACKLETSENTRY._serialized_end=1134
  _TRACKLET._serialized_start=1137
  _TRACKLET._serialized_end=1322
# @@protoc_insertion_point(module_scope)