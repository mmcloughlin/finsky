# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app_doc_details.proto

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
  name='app_doc_details.proto',
  package='AppDocDetails',
  syntax='proto2',
  serialized_pb=_b('\n\x15\x61pp_doc_details.proto\x12\rAppDocDetails\"&\n\x10\x44\x65veloperDetails\x12\x12\n\nwebsiteUrl\x18\x01 \x01(\t\")\n\x0e\x43\x65rtificateSet\x12\x17\n\x0f\x63\x65rtificateHash\x18\x01 \x03(\t\"\xe2\x05\n\nAppDetails\x12\x15\n\rdeveloperName\x18\x01 \x01(\t\x12\x1a\n\x12majorVersionNumber\x18\x02 \x01(\x05\x12\x13\n\x0bversionCode\x18\x03 \x01(\x05\x12\x15\n\rversionString\x18\x04 \x01(\t\x12\r\n\x05title\x18\x05 \x01(\t\x12\x13\n\x0b\x61ppCategory\x18\x07 \x03(\t\x12\x15\n\rcontentRating\x18\x08 \x01(\x05\x12\x18\n\x10installationSize\x18\t \x01(\x03\x12\x12\n\npermission\x18\n \x03(\t\x12\x16\n\x0e\x64\x65veloperEmail\x18\x0b \x01(\t\x12\x18\n\x10\x64\x65veloperWebsite\x18\x0c \x01(\t\x12\x14\n\x0cnumDownloads\x18\r \x01(\t\x12\x13\n\x0bpackageName\x18\x0e \x01(\t\x12\x19\n\x11recentChangesHtml\x18\x0f \x01(\t\x12\x12\n\nuploadDate\x18\x10 \x01(\t\x12)\n\x04\x66ile\x18\x11 \x03(\x0b\x32\x1b.AppDocDetails.FileMetadata\x12\x0f\n\x07\x61ppType\x18\x12 \x01(\t\x12\x17\n\x0f\x63\x65rtificateHash\x18\x13 \x03(\t\x12\x17\n\x0fvariesByAccount\x18\x15 \x01(\x08\x12\x35\n\x0e\x63\x65rtificateSet\x18\x16 \x03(\x0b\x32\x1d.AppDocDetails.CertificateSet\x12\x35\n-autoAcquireFreeAppIfHigherVersionAvailableTag\x18\x17 \x03(\t\x12\x13\n\x0b\x64\x65\x63laresIab\x18\x18 \x01(\x08\x12\x0f\n\x07splitId\x18\x19 \x03(\t\x12\x17\n\x0fgamepadRequired\x18\x1a \x01(\x08\x12\x18\n\x10\x65xternallyHosted\x18\x1b \x01(\x08\x12\x1c\n\x14\x65verExternallyHosted\x18\x1c \x01(\x08\x12\x14\n\x0cinstallNotes\x18\x1e \x01(\t\x12\x17\n\x0finstallLocation\x18\x1f \x01(\x05\"T\n\x0c\x46ileMetadata\x12\x10\n\x08\x66ileType\x18\x01 \x01(\x05\x12\x13\n\x0bversionCode\x18\x02 \x01(\x05\x12\x0c\n\x04size\x18\x03 \x01(\x03\x12\x0f\n\x07splitId\x18\x04 \x01(\t\"1\n\x13SubscriptionDetails\x12\x1a\n\x12subscriptionPeriod\x18\x01 \x01(\x05\x42\x31\n com.google.android.finsky.protosB\rAppDocDetails')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DEVELOPERDETAILS = _descriptor.Descriptor(
  name='DeveloperDetails',
  full_name='AppDocDetails.DeveloperDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='websiteUrl', full_name='AppDocDetails.DeveloperDetails.websiteUrl', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=78,
)


_CERTIFICATESET = _descriptor.Descriptor(
  name='CertificateSet',
  full_name='AppDocDetails.CertificateSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='certificateHash', full_name='AppDocDetails.CertificateSet.certificateHash', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=121,
)


_APPDETAILS = _descriptor.Descriptor(
  name='AppDetails',
  full_name='AppDocDetails.AppDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='developerName', full_name='AppDocDetails.AppDetails.developerName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='majorVersionNumber', full_name='AppDocDetails.AppDetails.majorVersionNumber', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='versionCode', full_name='AppDocDetails.AppDetails.versionCode', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='versionString', full_name='AppDocDetails.AppDetails.versionString', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='AppDocDetails.AppDetails.title', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appCategory', full_name='AppDocDetails.AppDetails.appCategory', index=5,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='contentRating', full_name='AppDocDetails.AppDetails.contentRating', index=6,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='installationSize', full_name='AppDocDetails.AppDetails.installationSize', index=7,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='permission', full_name='AppDocDetails.AppDetails.permission', index=8,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='developerEmail', full_name='AppDocDetails.AppDetails.developerEmail', index=9,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='developerWebsite', full_name='AppDocDetails.AppDetails.developerWebsite', index=10,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numDownloads', full_name='AppDocDetails.AppDetails.numDownloads', index=11,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='packageName', full_name='AppDocDetails.AppDetails.packageName', index=12,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recentChangesHtml', full_name='AppDocDetails.AppDetails.recentChangesHtml', index=13,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uploadDate', full_name='AppDocDetails.AppDetails.uploadDate', index=14,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file', full_name='AppDocDetails.AppDetails.file', index=15,
      number=17, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appType', full_name='AppDocDetails.AppDetails.appType', index=16,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='certificateHash', full_name='AppDocDetails.AppDetails.certificateHash', index=17,
      number=19, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variesByAccount', full_name='AppDocDetails.AppDetails.variesByAccount', index=18,
      number=21, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='certificateSet', full_name='AppDocDetails.AppDetails.certificateSet', index=19,
      number=22, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='autoAcquireFreeAppIfHigherVersionAvailableTag', full_name='AppDocDetails.AppDetails.autoAcquireFreeAppIfHigherVersionAvailableTag', index=20,
      number=23, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='declaresIab', full_name='AppDocDetails.AppDetails.declaresIab', index=21,
      number=24, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='splitId', full_name='AppDocDetails.AppDetails.splitId', index=22,
      number=25, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gamepadRequired', full_name='AppDocDetails.AppDetails.gamepadRequired', index=23,
      number=26, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='externallyHosted', full_name='AppDocDetails.AppDetails.externallyHosted', index=24,
      number=27, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='everExternallyHosted', full_name='AppDocDetails.AppDetails.everExternallyHosted', index=25,
      number=28, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='installNotes', full_name='AppDocDetails.AppDetails.installNotes', index=26,
      number=30, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='installLocation', full_name='AppDocDetails.AppDetails.installLocation', index=27,
      number=31, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=862,
)


_FILEMETADATA = _descriptor.Descriptor(
  name='FileMetadata',
  full_name='AppDocDetails.FileMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileType', full_name='AppDocDetails.FileMetadata.fileType', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='versionCode', full_name='AppDocDetails.FileMetadata.versionCode', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='AppDocDetails.FileMetadata.size', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='splitId', full_name='AppDocDetails.FileMetadata.splitId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=864,
  serialized_end=948,
)


_SUBSCRIPTIONDETAILS = _descriptor.Descriptor(
  name='SubscriptionDetails',
  full_name='AppDocDetails.SubscriptionDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='subscriptionPeriod', full_name='AppDocDetails.SubscriptionDetails.subscriptionPeriod', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=950,
  serialized_end=999,
)

_APPDETAILS.fields_by_name['file'].message_type = _FILEMETADATA
_APPDETAILS.fields_by_name['certificateSet'].message_type = _CERTIFICATESET
DESCRIPTOR.message_types_by_name['DeveloperDetails'] = _DEVELOPERDETAILS
DESCRIPTOR.message_types_by_name['CertificateSet'] = _CERTIFICATESET
DESCRIPTOR.message_types_by_name['AppDetails'] = _APPDETAILS
DESCRIPTOR.message_types_by_name['FileMetadata'] = _FILEMETADATA
DESCRIPTOR.message_types_by_name['SubscriptionDetails'] = _SUBSCRIPTIONDETAILS

DeveloperDetails = _reflection.GeneratedProtocolMessageType('DeveloperDetails', (_message.Message,), dict(
  DESCRIPTOR = _DEVELOPERDETAILS,
  __module__ = 'app_doc_details_pb2'
  # @@protoc_insertion_point(class_scope:AppDocDetails.DeveloperDetails)
  ))
_sym_db.RegisterMessage(DeveloperDetails)

CertificateSet = _reflection.GeneratedProtocolMessageType('CertificateSet', (_message.Message,), dict(
  DESCRIPTOR = _CERTIFICATESET,
  __module__ = 'app_doc_details_pb2'
  # @@protoc_insertion_point(class_scope:AppDocDetails.CertificateSet)
  ))
_sym_db.RegisterMessage(CertificateSet)

AppDetails = _reflection.GeneratedProtocolMessageType('AppDetails', (_message.Message,), dict(
  DESCRIPTOR = _APPDETAILS,
  __module__ = 'app_doc_details_pb2'
  # @@protoc_insertion_point(class_scope:AppDocDetails.AppDetails)
  ))
_sym_db.RegisterMessage(AppDetails)

FileMetadata = _reflection.GeneratedProtocolMessageType('FileMetadata', (_message.Message,), dict(
  DESCRIPTOR = _FILEMETADATA,
  __module__ = 'app_doc_details_pb2'
  # @@protoc_insertion_point(class_scope:AppDocDetails.FileMetadata)
  ))
_sym_db.RegisterMessage(FileMetadata)

SubscriptionDetails = _reflection.GeneratedProtocolMessageType('SubscriptionDetails', (_message.Message,), dict(
  DESCRIPTOR = _SUBSCRIPTIONDETAILS,
  __module__ = 'app_doc_details_pb2'
  # @@protoc_insertion_point(class_scope:AppDocDetails.SubscriptionDetails)
  ))
_sym_db.RegisterMessage(SubscriptionDetails)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n com.google.android.finsky.protosB\rAppDocDetails'))
# @@protoc_insertion_point(module_scope)
