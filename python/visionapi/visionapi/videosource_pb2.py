# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: visionapi/videosource.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bvisionapi/videosource.proto\x12\tvisionapi\"n\n\nVideoFrame\x12\x11\n\tsource_id\x18\x01 \x01(\x0c\x12\x18\n\x10timestamp_utc_ms\x18\x02 \x01(\x04\x12\x1f\n\x05shape\x18\x03 \x01(\x0b\x32\x10.visionapi.Shape\x12\x12\n\nframe_data\x18\x04 \x01(\x0c\"8\n\x05Shape\x12\x0e\n\x06height\x18\x01 \x01(\r\x12\r\n\x05width\x18\x02 \x01(\r\x12\x10\n\x08\x63hannels\x18\x03 \x01(\rB\x16\n\x14\x64\x65.starwit.visionapib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'visionapi.videosource_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024de.starwit.visionapi'
  _globals['_VIDEOFRAME']._serialized_start=42
  _globals['_VIDEOFRAME']._serialized_end=152
  _globals['_SHAPE']._serialized_start=154
  _globals['_SHAPE']._serialized_end=210
# @@protoc_insertion_point(module_scope)
