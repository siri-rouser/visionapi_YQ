# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/detector.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto import videosource_pb2 as proto_dot_videosource__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14proto/detector.proto\x12\tvisionapi\x1a\x17proto/videosource.proto\"a\n\x0f\x44\x65tectionOutput\x12$\n\x05\x66rame\x18\x01 \x01(\x0b\x32\x15.visionapi.VideoFrame\x12(\n\ndetections\x18\x02 \x03(\x0b\x32\x14.visionapi.Detection\"_\n\tDetection\x12,\n\x0c\x62ounding_box\x18\x01 \x01(\x0b\x32\x16.visionapi.BoundingBox\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12\x10\n\x08\x63lass_id\x18\x03 \x01(\r\"I\n\x0b\x42oundingBox\x12\r\n\x05min_x\x18\x01 \x01(\r\x12\r\n\x05min_y\x18\x02 \x01(\r\x12\r\n\x05max_x\x18\x03 \x01(\r\x12\r\n\x05max_y\x18\x04 \x01(\rb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.detector_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_DETECTIONOUTPUT']._serialized_start=60
  _globals['_DETECTIONOUTPUT']._serialized_end=157
  _globals['_DETECTION']._serialized_start=159
  _globals['_DETECTION']._serialized_end=254
  _globals['_BOUNDINGBOX']._serialized_start=256
  _globals['_BOUNDINGBOX']._serialized_end=329
# @@protoc_insertion_point(module_scope)
