# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1/proto/prediction_service.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.automl_v1.proto import (
    annotation_payload_pb2 as google_dot_cloud_dot_automl__v1_dot_proto_dot_annotation__payload__pb2,
)
from google.cloud.automl_v1.proto import (
    data_items_pb2 as google_dot_cloud_dot_automl__v1_dot_proto_dot_data__items__pb2,
)
from google.cloud.automl_v1.proto import (
    io_pb2 as google_dot_cloud_dot_automl__v1_dot_proto_dot_io__pb2,
)
from google.cloud.automl_v1.proto import (
    operations_pb2 as google_dot_cloud_dot_automl__v1_dot_proto_dot_operations__pb2,
)
from google.longrunning import (
    operations_pb2 as google_dot_longrunning_dot_operations__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1/proto/prediction_service.proto",
    package="google.cloud.automl.v1",
    syntax="proto3",
    serialized_options=_b(
        "\n\032com.google.cloud.automl.v1B\026PredictionServiceProtoP\001Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\252\002\026Google.Cloud.AutoML.V1\312\002\026Google\\Cloud\\AutoMl\\V1\352\002\031Google::Cloud::AutoML::V1"
    ),
    serialized_pb=_b(
        '\n5google/cloud/automl_v1/proto/prediction_service.proto\x12\x16google.cloud.automl.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x19google/api/resource.proto\x1a\x35google/cloud/automl_v1/proto/annotation_payload.proto\x1a-google/cloud/automl_v1/proto/data_items.proto\x1a%google/cloud/automl_v1/proto/io.proto\x1a-google/cloud/automl_v1/proto/operations.proto\x1a#google/longrunning/operations.proto"\xca\x01\n\x0ePredictRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x37\n\x07payload\x18\x02 \x01(\x0b\x32&.google.cloud.automl.v1.ExamplePayload\x12\x42\n\x06params\x18\x03 \x03(\x0b\x32\x32.google.cloud.automl.v1.PredictRequest.ParamsEntry\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\x8b\x02\n\x0fPredictResponse\x12:\n\x07payload\x18\x01 \x03(\x0b\x32).google.cloud.automl.v1.AnnotationPayload\x12\x42\n\x12preprocessed_input\x18\x03 \x01(\x0b\x32&.google.cloud.automl.v1.ExamplePayload\x12G\n\x08metadata\x18\x02 \x03(\x0b\x32\x35.google.cloud.automl.v1.PredictResponse.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xab\x02\n\x13\x42\x61tchPredictRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x45\n\x0cinput_config\x18\x03 \x01(\x0b\x32/.google.cloud.automl.v1.BatchPredictInputConfig\x12G\n\routput_config\x18\x04 \x01(\x0b\x32\x30.google.cloud.automl.v1.BatchPredictOutputConfig\x12G\n\x06params\x18\x05 \x03(\x0b\x32\x37.google.cloud.automl.v1.BatchPredictRequest.ParamsEntry\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\x91\x01\n\x12\x42\x61tchPredictResult\x12J\n\x08metadata\x18\x01 \x03(\x0b\x32\x38.google.cloud.automl.v1.BatchPredictResult.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\x9b\x03\n\x11PredictionService\x12\x99\x01\n\x07Predict\x12&.google.cloud.automl.v1.PredictRequest\x1a\'.google.cloud.automl.v1.PredictResponse"=\x82\xd3\xe4\x93\x02\x37"2/v1/{name=projects/*/locations/*/models/*}:predict:\x01*\x12\x9e\x01\n\x0c\x42\x61tchPredict\x12+.google.cloud.automl.v1.BatchPredictRequest\x1a\x1d.google.longrunning.Operation"B\x82\xd3\xe4\x93\x02<"7/v1/{name=projects/*/locations/*/models/*}:batchPredict:\x01*\x1aI\xca\x41\x15\x61utoml.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\xc2\x01\n\x1a\x63om.google.cloud.automl.v1B\x16PredictionServiceProtoP\x01Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1b\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_api_dot_client__pb2.DESCRIPTOR,
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1_dot_proto_dot_annotation__payload__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1_dot_proto_dot_data__items__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1_dot_proto_dot_io__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1_dot_proto_dot_operations__pb2.DESCRIPTOR,
        google_dot_longrunning_dot_operations__pb2.DESCRIPTOR,
    ],
)


_PREDICTREQUEST_PARAMSENTRY = _descriptor.Descriptor(
    name="ParamsEntry",
    full_name="google.cloud.automl.v1.PredictRequest.ParamsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.cloud.automl.v1.PredictRequest.ParamsEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.cloud.automl.v1.PredictRequest.ParamsEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=_b("8\001"),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=546,
    serialized_end=591,
)

_PREDICTREQUEST = _descriptor.Descriptor(
    name="PredictRequest",
    full_name="google.cloud.automl.v1.PredictRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.automl.v1.PredictRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="payload",
            full_name="google.cloud.automl.v1.PredictRequest.payload",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="params",
            full_name="google.cloud.automl.v1.PredictRequest.params",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_PREDICTREQUEST_PARAMSENTRY],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=389,
    serialized_end=591,
)


_PREDICTRESPONSE_METADATAENTRY = _descriptor.Descriptor(
    name="MetadataEntry",
    full_name="google.cloud.automl.v1.PredictResponse.MetadataEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.cloud.automl.v1.PredictResponse.MetadataEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.cloud.automl.v1.PredictResponse.MetadataEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=_b("8\001"),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=814,
    serialized_end=861,
)

_PREDICTRESPONSE = _descriptor.Descriptor(
    name="PredictResponse",
    full_name="google.cloud.automl.v1.PredictResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="payload",
            full_name="google.cloud.automl.v1.PredictResponse.payload",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="preprocessed_input",
            full_name="google.cloud.automl.v1.PredictResponse.preprocessed_input",
            index=1,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="metadata",
            full_name="google.cloud.automl.v1.PredictResponse.metadata",
            index=2,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_PREDICTRESPONSE_METADATAENTRY],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=594,
    serialized_end=861,
)


_BATCHPREDICTREQUEST_PARAMSENTRY = _descriptor.Descriptor(
    name="ParamsEntry",
    full_name="google.cloud.automl.v1.BatchPredictRequest.ParamsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.cloud.automl.v1.BatchPredictRequest.ParamsEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.cloud.automl.v1.BatchPredictRequest.ParamsEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=_b("8\001"),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=546,
    serialized_end=591,
)

_BATCHPREDICTREQUEST = _descriptor.Descriptor(
    name="BatchPredictRequest",
    full_name="google.cloud.automl.v1.BatchPredictRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.automl.v1.BatchPredictRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="input_config",
            full_name="google.cloud.automl.v1.BatchPredictRequest.input_config",
            index=1,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="output_config",
            full_name="google.cloud.automl.v1.BatchPredictRequest.output_config",
            index=2,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="params",
            full_name="google.cloud.automl.v1.BatchPredictRequest.params",
            index=3,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_BATCHPREDICTREQUEST_PARAMSENTRY],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=864,
    serialized_end=1163,
)


_BATCHPREDICTRESULT_METADATAENTRY = _descriptor.Descriptor(
    name="MetadataEntry",
    full_name="google.cloud.automl.v1.BatchPredictResult.MetadataEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.cloud.automl.v1.BatchPredictResult.MetadataEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.cloud.automl.v1.BatchPredictResult.MetadataEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=_b("8\001"),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=814,
    serialized_end=861,
)

_BATCHPREDICTRESULT = _descriptor.Descriptor(
    name="BatchPredictResult",
    full_name="google.cloud.automl.v1.BatchPredictResult",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="metadata",
            full_name="google.cloud.automl.v1.BatchPredictResult.metadata",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[_BATCHPREDICTRESULT_METADATAENTRY],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1166,
    serialized_end=1311,
)

_PREDICTREQUEST_PARAMSENTRY.containing_type = _PREDICTREQUEST
_PREDICTREQUEST.fields_by_name[
    "payload"
].message_type = (
    google_dot_cloud_dot_automl__v1_dot_proto_dot_data__items__pb2._EXAMPLEPAYLOAD
)
_PREDICTREQUEST.fields_by_name["params"].message_type = _PREDICTREQUEST_PARAMSENTRY
_PREDICTRESPONSE_METADATAENTRY.containing_type = _PREDICTRESPONSE
_PREDICTRESPONSE.fields_by_name[
    "payload"
].message_type = (
    google_dot_cloud_dot_automl__v1_dot_proto_dot_annotation__payload__pb2._ANNOTATIONPAYLOAD
)
_PREDICTRESPONSE.fields_by_name[
    "preprocessed_input"
].message_type = (
    google_dot_cloud_dot_automl__v1_dot_proto_dot_data__items__pb2._EXAMPLEPAYLOAD
)
_PREDICTRESPONSE.fields_by_name[
    "metadata"
].message_type = _PREDICTRESPONSE_METADATAENTRY
_BATCHPREDICTREQUEST_PARAMSENTRY.containing_type = _BATCHPREDICTREQUEST
_BATCHPREDICTREQUEST.fields_by_name[
    "input_config"
].message_type = (
    google_dot_cloud_dot_automl__v1_dot_proto_dot_io__pb2._BATCHPREDICTINPUTCONFIG
)
_BATCHPREDICTREQUEST.fields_by_name[
    "output_config"
].message_type = (
    google_dot_cloud_dot_automl__v1_dot_proto_dot_io__pb2._BATCHPREDICTOUTPUTCONFIG
)
_BATCHPREDICTREQUEST.fields_by_name[
    "params"
].message_type = _BATCHPREDICTREQUEST_PARAMSENTRY
_BATCHPREDICTRESULT_METADATAENTRY.containing_type = _BATCHPREDICTRESULT
_BATCHPREDICTRESULT.fields_by_name[
    "metadata"
].message_type = _BATCHPREDICTRESULT_METADATAENTRY
DESCRIPTOR.message_types_by_name["PredictRequest"] = _PREDICTREQUEST
DESCRIPTOR.message_types_by_name["PredictResponse"] = _PREDICTRESPONSE
DESCRIPTOR.message_types_by_name["BatchPredictRequest"] = _BATCHPREDICTREQUEST
DESCRIPTOR.message_types_by_name["BatchPredictResult"] = _BATCHPREDICTRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PredictRequest = _reflection.GeneratedProtocolMessageType(
    "PredictRequest",
    (_message.Message,),
    dict(
        ParamsEntry=_reflection.GeneratedProtocolMessageType(
            "ParamsEntry",
            (_message.Message,),
            dict(
                DESCRIPTOR=_PREDICTREQUEST_PARAMSENTRY,
                __module__="google.cloud.automl_v1.proto.prediction_service_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.PredictRequest.ParamsEntry)
            ),
        ),
        DESCRIPTOR=_PREDICTREQUEST,
        __module__="google.cloud.automl_v1.proto.prediction_service_pb2",
        __doc__="""Request message for
  [PredictionService.Predict][google.cloud.automl.v1.PredictionService.Predict].
  
  
  Attributes:
      name:
          Name of the model requested to serve the prediction.
      payload:
          Required. Payload to perform a prediction on. The payload must
          match the problem type that the model was trained to solve.
      params:
          Additional domain-specific parameters, any string must be up
          to 25000 characters long.  -  For Image Classification:
          ``score_threshold`` - (float) A value from 0.0 to 1.0. When
          the model makes predictions for an image, it will only produce
          results that have at least this confidence score. The default
          is 0.5.  -  For Image Object Detection: ``score_threshold`` -
          (float) When Model    detects objects on the image, it will
          only produce bounding boxes    which have at least this
          confidence score. Value in 0 to 1 range,    default is 0.5.
          ``max_bounding_box_count`` - (int64) No more than    this
          number of bounding boxes will be returned in the response.
          Default is 100, the requested value may be limited by server.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.PredictRequest)
    ),
)
_sym_db.RegisterMessage(PredictRequest)
_sym_db.RegisterMessage(PredictRequest.ParamsEntry)

PredictResponse = _reflection.GeneratedProtocolMessageType(
    "PredictResponse",
    (_message.Message,),
    dict(
        MetadataEntry=_reflection.GeneratedProtocolMessageType(
            "MetadataEntry",
            (_message.Message,),
            dict(
                DESCRIPTOR=_PREDICTRESPONSE_METADATAENTRY,
                __module__="google.cloud.automl_v1.proto.prediction_service_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.PredictResponse.MetadataEntry)
            ),
        ),
        DESCRIPTOR=_PREDICTRESPONSE,
        __module__="google.cloud.automl_v1.proto.prediction_service_pb2",
        __doc__="""Response message for
  [PredictionService.Predict][google.cloud.automl.v1.PredictionService.Predict].
  
  
  Attributes:
      payload:
          Prediction result. Translation and Text Sentiment will return
          precisely one payload.
      preprocessed_input:
          The preprocessed example that AutoML actually makes prediction
          on. Empty if AutoML does not preprocess the input example. \*
          For Text Extraction: If the input is a .pdf file, the OCR'ed
          text will be provided in [document\_text][google.cloud.automl.
          v1.Document.document\_text].  -  For Text Classification: If
          the input is a .pdf file, the OCR'ed    trucated text will be
          provided in    [document\_text][google.cloud.automl.v1.Documen
          t.document\_text].  -  For Text Sentiment: If the input is a
          .pdf file, the OCR'ed trucated    text will be provided in    
          [document\_text][google.cloud.automl.v1.Document.document\_tex
          t].
      metadata:
          Additional domain-specific prediction response metadata.  -
          For Image Object Detection: ``max_bounding_box_count`` -
          (int64) At    most that many bounding boxes per image could
          have been returned.  -  For Text Sentiment:
          ``sentiment_score`` - (float, deprecated) A value    between
          -1 and 1, -1 maps to least positive sentiment, while 1 maps
          to the most positive one and the higher the score, the more
          positive    the sentiment in the document is. Yet these values
          are relative to    the training data, so e.g. if all data was
          positive then -1 will be    also positive (though the least).
          The sentiment\_score shouldn't be    confused with "score" or
          "magnitude" from the previous Natural    Language Sentiment
          Analysis API.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.PredictResponse)
    ),
)
_sym_db.RegisterMessage(PredictResponse)
_sym_db.RegisterMessage(PredictResponse.MetadataEntry)

BatchPredictRequest = _reflection.GeneratedProtocolMessageType(
    "BatchPredictRequest",
    (_message.Message,),
    dict(
        ParamsEntry=_reflection.GeneratedProtocolMessageType(
            "ParamsEntry",
            (_message.Message,),
            dict(
                DESCRIPTOR=_BATCHPREDICTREQUEST_PARAMSENTRY,
                __module__="google.cloud.automl_v1.proto.prediction_service_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.BatchPredictRequest.ParamsEntry)
            ),
        ),
        DESCRIPTOR=_BATCHPREDICTREQUEST,
        __module__="google.cloud.automl_v1.proto.prediction_service_pb2",
        __doc__="""Request message for
  [PredictionService.BatchPredict][google.cloud.automl.v1.PredictionService.BatchPredict].
  
  
  Attributes:
      name:
          Name of the model requested to serve the batch prediction.
      input_config:
          Required. The input configuration for batch prediction.
      output_config:
          Required. The Configuration specifying where output
          predictions should be written.
      params:
          Additional domain-specific parameters for the predictions, any
          string must be up to 25000 characters long.  -  For Text
          Classification:  ``score_threshold`` - (float) A value from
          0.0 to 1.0. When the model makes predictions for a text
          snippet, it will only produce results that have at least this
          confidence score. The default is 0.5.  -  For Image
          Classification:  ``score_threshold`` - (float) A value from
          0.0 to 1.0. When the model makes predictions for an image, it
          will only produce results that have at least this confidence
          score. The default is 0.5.  -  For Image Object Detection:
          ``score_threshold`` - (float) When Model detects objects on
          the image, it will only produce bounding boxes which have at
          least this confidence score. Value in 0 to 1 range, default is
          0.5. ``max_bounding_box_count`` - (int64) No more than this
          number of bounding boxes will be produced per image. Default
          is 100, the requested value may be limited by server.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.BatchPredictRequest)
    ),
)
_sym_db.RegisterMessage(BatchPredictRequest)
_sym_db.RegisterMessage(BatchPredictRequest.ParamsEntry)

BatchPredictResult = _reflection.GeneratedProtocolMessageType(
    "BatchPredictResult",
    (_message.Message,),
    dict(
        MetadataEntry=_reflection.GeneratedProtocolMessageType(
            "MetadataEntry",
            (_message.Message,),
            dict(
                DESCRIPTOR=_BATCHPREDICTRESULT_METADATAENTRY,
                __module__="google.cloud.automl_v1.proto.prediction_service_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.BatchPredictResult.MetadataEntry)
            ),
        ),
        DESCRIPTOR=_BATCHPREDICTRESULT,
        __module__="google.cloud.automl_v1.proto.prediction_service_pb2",
        __doc__="""Result of the Batch Predict. This message is returned in
  [response][google.longrunning.Operation.response] of the operation
  returned by the
  [PredictionService.BatchPredict][google.cloud.automl.v1.PredictionService.BatchPredict].
  
  
  Attributes:
      metadata:
          Additional domain-specific prediction response metadata.  -
          For Image Object Detection: ``max_bounding_box_count`` -
          (int64) At    most that many bounding boxes per image could
          have been returned.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.BatchPredictResult)
    ),
)
_sym_db.RegisterMessage(BatchPredictResult)
_sym_db.RegisterMessage(BatchPredictResult.MetadataEntry)


DESCRIPTOR._options = None
_PREDICTREQUEST_PARAMSENTRY._options = None
_PREDICTRESPONSE_METADATAENTRY._options = None
_BATCHPREDICTREQUEST_PARAMSENTRY._options = None
_BATCHPREDICTRESULT_METADATAENTRY._options = None

_PREDICTIONSERVICE = _descriptor.ServiceDescriptor(
    name="PredictionService",
    full_name="google.cloud.automl.v1.PredictionService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=_b(
        "\312A\025automl.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform"
    ),
    serialized_start=1314,
    serialized_end=1725,
    methods=[
        _descriptor.MethodDescriptor(
            name="Predict",
            full_name="google.cloud.automl.v1.PredictionService.Predict",
            index=0,
            containing_service=None,
            input_type=_PREDICTREQUEST,
            output_type=_PREDICTRESPONSE,
            serialized_options=_b(
                '\202\323\344\223\0027"2/v1/{name=projects/*/locations/*/models/*}:predict:\001*'
            ),
        ),
        _descriptor.MethodDescriptor(
            name="BatchPredict",
            full_name="google.cloud.automl.v1.PredictionService.BatchPredict",
            index=1,
            containing_service=None,
            input_type=_BATCHPREDICTREQUEST,
            output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
            serialized_options=_b(
                '\202\323\344\223\002<"7/v1/{name=projects/*/locations/*/models/*}:batchPredict:\001*'
            ),
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_PREDICTIONSERVICE)

DESCRIPTOR.services_by_name["PredictionService"] = _PREDICTIONSERVICE

# @@protoc_insertion_point(module_scope)
