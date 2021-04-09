# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event_store.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='event_store.proto',
  package='eventstore',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11\x65vent_store.proto\x12\neventstore\"9\n\x0ePublishRequest\x12\x13\n\x0b\x65vent_topic\x18\x01 \x01(\t\x12\x12\n\nevent_info\x18\x02 \x01(\t\"#\n\x0fPublishResponse\x12\x10\n\x08\x65ntry_id\x18\x01 \x01(\t\";\n\x10SubscribeRequest\x12\x13\n\x0b\x65vent_topic\x18\x01 \x01(\t\x12\x12\n\ngroup_name\x18\x02 \x01(\t\"\\\n\x0cNotification\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\t\x12\x10\n\x08\x65vent_ts\x18\x02 \x01(\x01\x12\x14\n\x0c\x65vent_action\x18\x03 \x01(\t\x12\x12\n\nevent_data\x18\x04 \x01(\t\")\n\x12UnsubscribeRequest\x12\x13\n\x0b\x65vent_topic\x18\x01 \x01(\t\"&\n\x13UnsubscribeResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"!\n\nGetRequest\x12\x13\n\x0b\x65vent_topic\x18\x01 \x01(\t\"\x1d\n\x0bGetResponse\x12\x0e\n\x06\x65vents\x18\x01 \x01(\t2\xa7\x02\n\nEventStore\x12\x44\n\x07publish\x12\x1a.eventstore.PublishRequest\x1a\x1b.eventstore.PublishResponse\"\x00\x12G\n\tsubscribe\x12\x1c.eventstore.SubscribeRequest\x1a\x18.eventstore.Notification\"\x00\x30\x01\x12P\n\x0bunsubscribe\x12\x1e.eventstore.UnsubscribeRequest\x1a\x1f.eventstore.UnsubscribeResponse\"\x00\x12\x38\n\x03get\x12\x16.eventstore.GetRequest\x1a\x17.eventstore.GetResponse\"\x00\x62\x06proto3')
)




_PUBLISHREQUEST = _descriptor.Descriptor(
  name='PublishRequest',
  full_name='eventstore.PublishRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_topic', full_name='eventstore.PublishRequest.event_topic', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_info', full_name='eventstore.PublishRequest.event_info', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=90,
)


_PUBLISHRESPONSE = _descriptor.Descriptor(
  name='PublishResponse',
  full_name='eventstore.PublishResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entry_id', full_name='eventstore.PublishResponse.entry_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=127,
)


_SUBSCRIBEREQUEST = _descriptor.Descriptor(
  name='SubscribeRequest',
  full_name='eventstore.SubscribeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_topic', full_name='eventstore.SubscribeRequest.event_topic', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group_name', full_name='eventstore.SubscribeRequest.group_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=188,
)


_NOTIFICATION = _descriptor.Descriptor(
  name='Notification',
  full_name='eventstore.Notification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_id', full_name='eventstore.Notification.event_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_ts', full_name='eventstore.Notification.event_ts', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_action', full_name='eventstore.Notification.event_action', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_data', full_name='eventstore.Notification.event_data', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=190,
  serialized_end=282,
)


_UNSUBSCRIBEREQUEST = _descriptor.Descriptor(
  name='UnsubscribeRequest',
  full_name='eventstore.UnsubscribeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_topic', full_name='eventstore.UnsubscribeRequest.event_topic', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=284,
  serialized_end=325,
)


_UNSUBSCRIBERESPONSE = _descriptor.Descriptor(
  name='UnsubscribeResponse',
  full_name='eventstore.UnsubscribeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='eventstore.UnsubscribeResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=327,
  serialized_end=365,
)


_GETREQUEST = _descriptor.Descriptor(
  name='GetRequest',
  full_name='eventstore.GetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_topic', full_name='eventstore.GetRequest.event_topic', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=367,
  serialized_end=400,
)


_GETRESPONSE = _descriptor.Descriptor(
  name='GetResponse',
  full_name='eventstore.GetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='events', full_name='eventstore.GetResponse.events', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=402,
  serialized_end=431,
)

DESCRIPTOR.message_types_by_name['PublishRequest'] = _PUBLISHREQUEST
DESCRIPTOR.message_types_by_name['PublishResponse'] = _PUBLISHRESPONSE
DESCRIPTOR.message_types_by_name['SubscribeRequest'] = _SUBSCRIBEREQUEST
DESCRIPTOR.message_types_by_name['Notification'] = _NOTIFICATION
DESCRIPTOR.message_types_by_name['UnsubscribeRequest'] = _UNSUBSCRIBEREQUEST
DESCRIPTOR.message_types_by_name['UnsubscribeResponse'] = _UNSUBSCRIBERESPONSE
DESCRIPTOR.message_types_by_name['GetRequest'] = _GETREQUEST
DESCRIPTOR.message_types_by_name['GetResponse'] = _GETRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PublishRequest = _reflection.GeneratedProtocolMessageType('PublishRequest', (_message.Message,), dict(
  DESCRIPTOR = _PUBLISHREQUEST,
  __module__ = 'event_store_pb2'
  # @@protoc_insertion_point(class_scope:eventstore.PublishRequest)
  ))
_sym_db.RegisterMessage(PublishRequest)

PublishResponse = _reflection.GeneratedProtocolMessageType('PublishResponse', (_message.Message,), dict(
  DESCRIPTOR = _PUBLISHRESPONSE,
  __module__ = 'event_store_pb2'
  # @@protoc_insertion_point(class_scope:eventstore.PublishResponse)
  ))
_sym_db.RegisterMessage(PublishResponse)

SubscribeRequest = _reflection.GeneratedProtocolMessageType('SubscribeRequest', (_message.Message,), dict(
  DESCRIPTOR = _SUBSCRIBEREQUEST,
  __module__ = 'event_store_pb2'
  # @@protoc_insertion_point(class_scope:eventstore.SubscribeRequest)
  ))
_sym_db.RegisterMessage(SubscribeRequest)

Notification = _reflection.GeneratedProtocolMessageType('Notification', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFICATION,
  __module__ = 'event_store_pb2'
  # @@protoc_insertion_point(class_scope:eventstore.Notification)
  ))
_sym_db.RegisterMessage(Notification)

UnsubscribeRequest = _reflection.GeneratedProtocolMessageType('UnsubscribeRequest', (_message.Message,), dict(
  DESCRIPTOR = _UNSUBSCRIBEREQUEST,
  __module__ = 'event_store_pb2'
  # @@protoc_insertion_point(class_scope:eventstore.UnsubscribeRequest)
  ))
_sym_db.RegisterMessage(UnsubscribeRequest)

UnsubscribeResponse = _reflection.GeneratedProtocolMessageType('UnsubscribeResponse', (_message.Message,), dict(
  DESCRIPTOR = _UNSUBSCRIBERESPONSE,
  __module__ = 'event_store_pb2'
  # @@protoc_insertion_point(class_scope:eventstore.UnsubscribeResponse)
  ))
_sym_db.RegisterMessage(UnsubscribeResponse)

GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETREQUEST,
  __module__ = 'event_store_pb2'
  # @@protoc_insertion_point(class_scope:eventstore.GetRequest)
  ))
_sym_db.RegisterMessage(GetRequest)

GetResponse = _reflection.GeneratedProtocolMessageType('GetResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETRESPONSE,
  __module__ = 'event_store_pb2'
  # @@protoc_insertion_point(class_scope:eventstore.GetResponse)
  ))
_sym_db.RegisterMessage(GetResponse)



_EVENTSTORE = _descriptor.ServiceDescriptor(
  name='EventStore',
  full_name='eventstore.EventStore',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=434,
  serialized_end=729,
  methods=[
  _descriptor.MethodDescriptor(
    name='publish',
    full_name='eventstore.EventStore.publish',
    index=0,
    containing_service=None,
    input_type=_PUBLISHREQUEST,
    output_type=_PUBLISHRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='subscribe',
    full_name='eventstore.EventStore.subscribe',
    index=1,
    containing_service=None,
    input_type=_SUBSCRIBEREQUEST,
    output_type=_NOTIFICATION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='unsubscribe',
    full_name='eventstore.EventStore.unsubscribe',
    index=2,
    containing_service=None,
    input_type=_UNSUBSCRIBEREQUEST,
    output_type=_UNSUBSCRIBERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get',
    full_name='eventstore.EventStore.get',
    index=3,
    containing_service=None,
    input_type=_GETREQUEST,
    output_type=_GETRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_EVENTSTORE)

DESCRIPTOR.services_by_name['EventStore'] = _EVENTSTORE

# @@protoc_insertion_point(module_scope)
