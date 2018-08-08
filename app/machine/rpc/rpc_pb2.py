# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpc.proto

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
  name='rpc.proto',
  package='rpc',
  syntax='proto3',
  serialized_pb=_b('\n\trpc.proto\x12\x03rpc\"\x17\n\x07\x43ontent\x12\x0c\n\x04text\x18\x01 \x01(\t\"\x16\n\x06Status\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x03\x32\x32\n\x03RPC\x12+\n\x0csendConfFile\x12\x0c.rpc.Content\x1a\x0b.rpc.Status\"\x00\x62\x06proto3')
)




_CONTENT = _descriptor.Descriptor(
  name='Content',
  full_name='rpc.Content',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='rpc.Content.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=18,
  serialized_end=41,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='rpc.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='rpc.Status.code', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=43,
  serialized_end=65,
)

DESCRIPTOR.message_types_by_name['Content'] = _CONTENT
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Content = _reflection.GeneratedProtocolMessageType('Content', (_message.Message,), dict(
  DESCRIPTOR = _CONTENT,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:rpc.Content)
  ))
_sym_db.RegisterMessage(Content)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), dict(
  DESCRIPTOR = _STATUS,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:rpc.Status)
  ))
_sym_db.RegisterMessage(Status)



_RPC = _descriptor.ServiceDescriptor(
  name='RPC',
  full_name='rpc.RPC',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=67,
  serialized_end=117,
  methods=[
  _descriptor.MethodDescriptor(
    name='sendConfFile',
    full_name='rpc.RPC.sendConfFile',
    index=0,
    containing_service=None,
    input_type=_CONTENT,
    output_type=_STATUS,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RPC)

DESCRIPTOR.services_by_name['RPC'] = _RPC

# @@protoc_insertion_point(module_scope)