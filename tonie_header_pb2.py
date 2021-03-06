# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tonie_header.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tonie_header.proto',
  package='tonie',
  syntax='proto3',
  serialized_pb=_b('\n\x12tonie_header.proto\x12\x05tonie\"q\n\x0bTonieHeader\x12\x10\n\x08\x64\x61taHash\x18\x01 \x01(\x0c\x12\x12\n\ndataLength\x18\x02 \x01(\r\x12\x11\n\ttimestamp\x18\x03 \x01(\r\x12\x18\n\x0c\x63hapterPages\x18\x04 \x03(\rB\x02\x10\x01\x12\x0f\n\x07padding\x18\x05 \x01(\x0c\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TONIEHEADER = _descriptor.Descriptor(
  name='TonieHeader',
  full_name='tonie.TonieHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataHash', full_name='tonie.TonieHeader.dataHash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataLength', full_name='tonie.TonieHeader.dataLength', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='tonie.TonieHeader.timestamp', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chapterPages', full_name='tonie.TonieHeader.chapterPages', index=3,
      number=4, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='padding', full_name='tonie.TonieHeader.padding', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=142,
)

DESCRIPTOR.message_types_by_name['TonieHeader'] = _TONIEHEADER

TonieHeader = _reflection.GeneratedProtocolMessageType('TonieHeader', (_message.Message,), dict(
  DESCRIPTOR = _TONIEHEADER,
  __module__ = 'tonie_header_pb2'
  # @@protoc_insertion_point(class_scope:tonie.TonieHeader)
  ))
_sym_db.RegisterMessage(TonieHeader)


_TONIEHEADER.fields_by_name['chapterPages'].has_options = True
_TONIEHEADER.fields_by_name['chapterPages']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
