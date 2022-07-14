# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: simple-storage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='simple-storage.proto',
  package='com.ruckuswireless.scg.protobuf.storage',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x14simple-storage.proto\x12\'com.ruckuswireless.scg.protobuf.storage\x1a google/protobuf/descriptor.proto*m\n\x08\x43\x61tegory\x12\n\n\x06\x43ONFIG\x10\x01\x12\n\n\x06STATUS\x10\x02\x12\n\n\x06\x44\x45VICE\x10\x03\x12\r\n\tSTATISTIC\x10\x04\x12\x08\n\x04\x46ILE\x10\x05\x12\x08\n\x04\x44\x41TA\x10\x06\x12\t\n\x05GROUP\x10\x07\x12\x0f\n\x0bINFORMATION\x10\x08:5\n\rschemaVersion\x12\x1c.google.protobuf.FileOptions\x18\xd0\x86\x03 \x01(\x03:f\n\x08\x63\x61tegory\x12\x1f.google.protobuf.MessageOptions\x18\xd0\x86\x03 \x01(\x0e\x32\x31.com.ruckuswireless.scg.protobuf.storage.Category:1\n\x06\x65ntity\x12\x1f.google.protobuf.MessageOptions\x18\xd1\x86\x03 \x01(\x08:+\n\x02id\x12\x1d.google.protobuf.FieldOptions\x18\xd0\x86\x03 \x01(\x08:0\n\x07version\x12\x1d.google.protobuf.FieldOptions\x18\xd1\x86\x03 \x01(\x08:/\n\x06ingest\x12\x1d.google.protobuf.FieldOptions\x18\xd2\x86\x03 \x01(\t:4\n\x0b\x66ileContent\x12\x1d.google.protobuf.FieldOptions\x18\xd3\x86\x03 \x01(\x08')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])

_CATEGORY = _descriptor.EnumDescriptor(
  name='Category',
  full_name='com.ruckuswireless.scg.protobuf.storage.Category',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONFIG', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICE', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATISTIC', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILE', index=4, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATA', index=5, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GROUP', index=6, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INFORMATION', index=7, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=99,
  serialized_end=208,
)
_sym_db.RegisterEnumDescriptor(_CATEGORY)

Category = enum_type_wrapper.EnumTypeWrapper(_CATEGORY)
CONFIG = 1
STATUS = 2
DEVICE = 3
STATISTIC = 4
FILE = 5
DATA = 6
GROUP = 7
INFORMATION = 8

SCHEMAVERSION_FIELD_NUMBER = 50000
schemaVersion = _descriptor.FieldDescriptor(
  name='schemaVersion', full_name='com.ruckuswireless.scg.protobuf.storage.schemaVersion', index=0,
  number=50000, type=3, cpp_type=2, label=1,
  has_default_value=False, default_value=0,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
CATEGORY_FIELD_NUMBER = 50000
category = _descriptor.FieldDescriptor(
  name='category', full_name='com.ruckuswireless.scg.protobuf.storage.category', index=1,
  number=50000, type=14, cpp_type=8, label=1,
  has_default_value=False, default_value=1,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
ENTITY_FIELD_NUMBER = 50001
entity = _descriptor.FieldDescriptor(
  name='entity', full_name='com.ruckuswireless.scg.protobuf.storage.entity', index=2,
  number=50001, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
ID_FIELD_NUMBER = 50000
id = _descriptor.FieldDescriptor(
  name='id', full_name='com.ruckuswireless.scg.protobuf.storage.id', index=3,
  number=50000, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
VERSION_FIELD_NUMBER = 50001
version = _descriptor.FieldDescriptor(
  name='version', full_name='com.ruckuswireless.scg.protobuf.storage.version', index=4,
  number=50001, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
INGEST_FIELD_NUMBER = 50002
ingest = _descriptor.FieldDescriptor(
  name='ingest', full_name='com.ruckuswireless.scg.protobuf.storage.ingest', index=5,
  number=50002, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=_b("").decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
FILECONTENT_FIELD_NUMBER = 50003
fileContent = _descriptor.FieldDescriptor(
  name='fileContent', full_name='com.ruckuswireless.scg.protobuf.storage.fileContent', index=6,
  number=50003, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)

DESCRIPTOR.enum_types_by_name['Category'] = _CATEGORY
DESCRIPTOR.extensions_by_name['schemaVersion'] = schemaVersion
DESCRIPTOR.extensions_by_name['category'] = category
DESCRIPTOR.extensions_by_name['entity'] = entity
DESCRIPTOR.extensions_by_name['id'] = id
DESCRIPTOR.extensions_by_name['version'] = version
DESCRIPTOR.extensions_by_name['ingest'] = ingest
DESCRIPTOR.extensions_by_name['fileContent'] = fileContent
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(schemaVersion)
category.enum_type = _CATEGORY
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(category)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(entity)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(id)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(version)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(ingest)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(fileContent)

# @@protoc_insertion_point(module_scope)
