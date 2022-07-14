# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ap_avc_all.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ap_avc_pb2 as ap__avc__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ap_avc_all.proto',
  package='',
  syntax='proto2',
  serialized_options=_b('\n\037com.ruckuswireless.scg.protobuf'),
  serialized_pb=_b('\n\x10\x61p_avc_all.proto\x1a\x0c\x61p_avc.proto\"?\n\nAPAVCStats\x12\x0f\n\x07version\x18\x01 \x02(\r\x12 \n\x0b\x61rc_message\x18\x02 \x03(\x0b\x32\x0b.ArcMessageB!\n\x1f\x63om.ruckuswireless.scg.protobuf')
  ,
  dependencies=[ap__avc__pb2.DESCRIPTOR,])




_APAVCSTATS = _descriptor.Descriptor(
  name='APAVCStats',
  full_name='APAVCStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='APAVCStats.version', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arc_message', full_name='APAVCStats.arc_message', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=97,
)

_APAVCSTATS.fields_by_name['arc_message'].message_type = ap__avc__pb2._ARCMESSAGE
DESCRIPTOR.message_types_by_name['APAVCStats'] = _APAVCSTATS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

APAVCStats = _reflection.GeneratedProtocolMessageType('APAVCStats', (_message.Message,), {
  'DESCRIPTOR' : _APAVCSTATS,
  '__module__' : 'ap_avc_all_pb2'
  # @@protoc_insertion_point(class_scope:APAVCStats)
  })
_sym_db.RegisterMessage(APAVCStats)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)