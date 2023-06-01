// This file is generated by rust-protobuf 3.2.0. Do not edit
// .proto file is parsed by protoc 23.2
// @generated

// https://github.com/rust-lang/rust-clippy/issues/702
#![allow(unknown_lints)]
#![allow(clippy::all)]

#![allow(unused_attributes)]
#![cfg_attr(rustfmt, rustfmt::skip)]

#![allow(box_pointers)]
#![allow(dead_code)]
#![allow(missing_docs)]
#![allow(non_camel_case_types)]
#![allow(non_snake_case)]
#![allow(non_upper_case_globals)]
#![allow(trivial_casts)]
#![allow(unused_results)]
#![allow(unused_mut)]

//! Generated file from `visionapi/videosource.proto`

/// Generated files are compatible only with the same version
/// of protobuf runtime.
const _PROTOBUF_VERSION_CHECK: () = ::protobuf::VERSION_3_2_0;

#[derive(PartialEq,Clone,Default,Debug)]
// @@protoc_insertion_point(message:visionapi.VideoFrame)
pub struct VideoFrame {
    // message fields
    // @@protoc_insertion_point(field:visionapi.VideoFrame.source_id)
    pub source_id: ::std::vec::Vec<u8>,
    // @@protoc_insertion_point(field:visionapi.VideoFrame.timestamp_utc_ms)
    pub timestamp_utc_ms: u64,
    // @@protoc_insertion_point(field:visionapi.VideoFrame.shape)
    pub shape: ::protobuf::MessageField<Shape>,
    // @@protoc_insertion_point(field:visionapi.VideoFrame.frame_data)
    pub frame_data: ::std::vec::Vec<u8>,
    // special fields
    // @@protoc_insertion_point(special_field:visionapi.VideoFrame.special_fields)
    pub special_fields: ::protobuf::SpecialFields,
}

impl<'a> ::std::default::Default for &'a VideoFrame {
    fn default() -> &'a VideoFrame {
        <VideoFrame as ::protobuf::Message>::default_instance()
    }
}

impl VideoFrame {
    pub fn new() -> VideoFrame {
        ::std::default::Default::default()
    }

    fn generated_message_descriptor_data() -> ::protobuf::reflect::GeneratedMessageDescriptorData {
        let mut fields = ::std::vec::Vec::with_capacity(4);
        let mut oneofs = ::std::vec::Vec::with_capacity(0);
        fields.push(::protobuf::reflect::rt::v2::make_simpler_field_accessor::<_, _>(
            "source_id",
            |m: &VideoFrame| { &m.source_id },
            |m: &mut VideoFrame| { &mut m.source_id },
        ));
        fields.push(::protobuf::reflect::rt::v2::make_simpler_field_accessor::<_, _>(
            "timestamp_utc_ms",
            |m: &VideoFrame| { &m.timestamp_utc_ms },
            |m: &mut VideoFrame| { &mut m.timestamp_utc_ms },
        ));
        fields.push(::protobuf::reflect::rt::v2::make_message_field_accessor::<_, Shape>(
            "shape",
            |m: &VideoFrame| { &m.shape },
            |m: &mut VideoFrame| { &mut m.shape },
        ));
        fields.push(::protobuf::reflect::rt::v2::make_simpler_field_accessor::<_, _>(
            "frame_data",
            |m: &VideoFrame| { &m.frame_data },
            |m: &mut VideoFrame| { &mut m.frame_data },
        ));
        ::protobuf::reflect::GeneratedMessageDescriptorData::new_2::<VideoFrame>(
            "VideoFrame",
            fields,
            oneofs,
        )
    }
}

impl ::protobuf::Message for VideoFrame {
    const NAME: &'static str = "VideoFrame";

    fn is_initialized(&self) -> bool {
        true
    }

    fn merge_from(&mut self, is: &mut ::protobuf::CodedInputStream<'_>) -> ::protobuf::Result<()> {
        while let Some(tag) = is.read_raw_tag_or_eof()? {
            match tag {
                10 => {
                    self.source_id = is.read_bytes()?;
                },
                16 => {
                    self.timestamp_utc_ms = is.read_uint64()?;
                },
                26 => {
                    ::protobuf::rt::read_singular_message_into_field(is, &mut self.shape)?;
                },
                34 => {
                    self.frame_data = is.read_bytes()?;
                },
                tag => {
                    ::protobuf::rt::read_unknown_or_skip_group(tag, is, self.special_fields.mut_unknown_fields())?;
                },
            };
        }
        ::std::result::Result::Ok(())
    }

    // Compute sizes of nested messages
    #[allow(unused_variables)]
    fn compute_size(&self) -> u64 {
        let mut my_size = 0;
        if !self.source_id.is_empty() {
            my_size += ::protobuf::rt::bytes_size(1, &self.source_id);
        }
        if self.timestamp_utc_ms != 0 {
            my_size += ::protobuf::rt::uint64_size(2, self.timestamp_utc_ms);
        }
        if let Some(v) = self.shape.as_ref() {
            let len = v.compute_size();
            my_size += 1 + ::protobuf::rt::compute_raw_varint64_size(len) + len;
        }
        if !self.frame_data.is_empty() {
            my_size += ::protobuf::rt::bytes_size(4, &self.frame_data);
        }
        my_size += ::protobuf::rt::unknown_fields_size(self.special_fields.unknown_fields());
        self.special_fields.cached_size().set(my_size as u32);
        my_size
    }

    fn write_to_with_cached_sizes(&self, os: &mut ::protobuf::CodedOutputStream<'_>) -> ::protobuf::Result<()> {
        if !self.source_id.is_empty() {
            os.write_bytes(1, &self.source_id)?;
        }
        if self.timestamp_utc_ms != 0 {
            os.write_uint64(2, self.timestamp_utc_ms)?;
        }
        if let Some(v) = self.shape.as_ref() {
            ::protobuf::rt::write_message_field_with_cached_size(3, v, os)?;
        }
        if !self.frame_data.is_empty() {
            os.write_bytes(4, &self.frame_data)?;
        }
        os.write_unknown_fields(self.special_fields.unknown_fields())?;
        ::std::result::Result::Ok(())
    }

    fn special_fields(&self) -> &::protobuf::SpecialFields {
        &self.special_fields
    }

    fn mut_special_fields(&mut self) -> &mut ::protobuf::SpecialFields {
        &mut self.special_fields
    }

    fn new() -> VideoFrame {
        VideoFrame::new()
    }

    fn clear(&mut self) {
        self.source_id.clear();
        self.timestamp_utc_ms = 0;
        self.shape.clear();
        self.frame_data.clear();
        self.special_fields.clear();
    }

    fn default_instance() -> &'static VideoFrame {
        static instance: VideoFrame = VideoFrame {
            source_id: ::std::vec::Vec::new(),
            timestamp_utc_ms: 0,
            shape: ::protobuf::MessageField::none(),
            frame_data: ::std::vec::Vec::new(),
            special_fields: ::protobuf::SpecialFields::new(),
        };
        &instance
    }
}

impl ::protobuf::MessageFull for VideoFrame {
    fn descriptor() -> ::protobuf::reflect::MessageDescriptor {
        static descriptor: ::protobuf::rt::Lazy<::protobuf::reflect::MessageDescriptor> = ::protobuf::rt::Lazy::new();
        descriptor.get(|| file_descriptor().message_by_package_relative_name("VideoFrame").unwrap()).clone()
    }
}

impl ::std::fmt::Display for VideoFrame {
    fn fmt(&self, f: &mut ::std::fmt::Formatter<'_>) -> ::std::fmt::Result {
        ::protobuf::text_format::fmt(self, f)
    }
}

impl ::protobuf::reflect::ProtobufValue for VideoFrame {
    type RuntimeType = ::protobuf::reflect::rt::RuntimeTypeMessage<Self>;
}

#[derive(PartialEq,Clone,Default,Debug)]
// @@protoc_insertion_point(message:visionapi.Shape)
pub struct Shape {
    // message fields
    // @@protoc_insertion_point(field:visionapi.Shape.height)
    pub height: u32,
    // @@protoc_insertion_point(field:visionapi.Shape.width)
    pub width: u32,
    // @@protoc_insertion_point(field:visionapi.Shape.channels)
    pub channels: u32,
    // special fields
    // @@protoc_insertion_point(special_field:visionapi.Shape.special_fields)
    pub special_fields: ::protobuf::SpecialFields,
}

impl<'a> ::std::default::Default for &'a Shape {
    fn default() -> &'a Shape {
        <Shape as ::protobuf::Message>::default_instance()
    }
}

impl Shape {
    pub fn new() -> Shape {
        ::std::default::Default::default()
    }

    fn generated_message_descriptor_data() -> ::protobuf::reflect::GeneratedMessageDescriptorData {
        let mut fields = ::std::vec::Vec::with_capacity(3);
        let mut oneofs = ::std::vec::Vec::with_capacity(0);
        fields.push(::protobuf::reflect::rt::v2::make_simpler_field_accessor::<_, _>(
            "height",
            |m: &Shape| { &m.height },
            |m: &mut Shape| { &mut m.height },
        ));
        fields.push(::protobuf::reflect::rt::v2::make_simpler_field_accessor::<_, _>(
            "width",
            |m: &Shape| { &m.width },
            |m: &mut Shape| { &mut m.width },
        ));
        fields.push(::protobuf::reflect::rt::v2::make_simpler_field_accessor::<_, _>(
            "channels",
            |m: &Shape| { &m.channels },
            |m: &mut Shape| { &mut m.channels },
        ));
        ::protobuf::reflect::GeneratedMessageDescriptorData::new_2::<Shape>(
            "Shape",
            fields,
            oneofs,
        )
    }
}

impl ::protobuf::Message for Shape {
    const NAME: &'static str = "Shape";

    fn is_initialized(&self) -> bool {
        true
    }

    fn merge_from(&mut self, is: &mut ::protobuf::CodedInputStream<'_>) -> ::protobuf::Result<()> {
        while let Some(tag) = is.read_raw_tag_or_eof()? {
            match tag {
                8 => {
                    self.height = is.read_uint32()?;
                },
                16 => {
                    self.width = is.read_uint32()?;
                },
                24 => {
                    self.channels = is.read_uint32()?;
                },
                tag => {
                    ::protobuf::rt::read_unknown_or_skip_group(tag, is, self.special_fields.mut_unknown_fields())?;
                },
            };
        }
        ::std::result::Result::Ok(())
    }

    // Compute sizes of nested messages
    #[allow(unused_variables)]
    fn compute_size(&self) -> u64 {
        let mut my_size = 0;
        if self.height != 0 {
            my_size += ::protobuf::rt::uint32_size(1, self.height);
        }
        if self.width != 0 {
            my_size += ::protobuf::rt::uint32_size(2, self.width);
        }
        if self.channels != 0 {
            my_size += ::protobuf::rt::uint32_size(3, self.channels);
        }
        my_size += ::protobuf::rt::unknown_fields_size(self.special_fields.unknown_fields());
        self.special_fields.cached_size().set(my_size as u32);
        my_size
    }

    fn write_to_with_cached_sizes(&self, os: &mut ::protobuf::CodedOutputStream<'_>) -> ::protobuf::Result<()> {
        if self.height != 0 {
            os.write_uint32(1, self.height)?;
        }
        if self.width != 0 {
            os.write_uint32(2, self.width)?;
        }
        if self.channels != 0 {
            os.write_uint32(3, self.channels)?;
        }
        os.write_unknown_fields(self.special_fields.unknown_fields())?;
        ::std::result::Result::Ok(())
    }

    fn special_fields(&self) -> &::protobuf::SpecialFields {
        &self.special_fields
    }

    fn mut_special_fields(&mut self) -> &mut ::protobuf::SpecialFields {
        &mut self.special_fields
    }

    fn new() -> Shape {
        Shape::new()
    }

    fn clear(&mut self) {
        self.height = 0;
        self.width = 0;
        self.channels = 0;
        self.special_fields.clear();
    }

    fn default_instance() -> &'static Shape {
        static instance: Shape = Shape {
            height: 0,
            width: 0,
            channels: 0,
            special_fields: ::protobuf::SpecialFields::new(),
        };
        &instance
    }
}

impl ::protobuf::MessageFull for Shape {
    fn descriptor() -> ::protobuf::reflect::MessageDescriptor {
        static descriptor: ::protobuf::rt::Lazy<::protobuf::reflect::MessageDescriptor> = ::protobuf::rt::Lazy::new();
        descriptor.get(|| file_descriptor().message_by_package_relative_name("Shape").unwrap()).clone()
    }
}

impl ::std::fmt::Display for Shape {
    fn fmt(&self, f: &mut ::std::fmt::Formatter<'_>) -> ::std::fmt::Result {
        ::protobuf::text_format::fmt(self, f)
    }
}

impl ::protobuf::reflect::ProtobufValue for Shape {
    type RuntimeType = ::protobuf::reflect::rt::RuntimeTypeMessage<Self>;
}

static file_descriptor_proto_data: &'static [u8] = b"\
    \n\x1bvisionapi/videosource.proto\x12\tvisionapi\"\x9a\x01\n\nVideoFrame\
    \x12\x1b\n\tsource_id\x18\x01\x20\x01(\x0cR\x08sourceId\x12(\n\x10timest\
    amp_utc_ms\x18\x02\x20\x01(\x04R\x0etimestampUtcMs\x12&\n\x05shape\x18\
    \x03\x20\x01(\x0b2\x10.visionapi.ShapeR\x05shape\x12\x1d\n\nframe_data\
    \x18\x04\x20\x01(\x0cR\tframeData\"Q\n\x05Shape\x12\x16\n\x06height\x18\
    \x01\x20\x01(\rR\x06height\x12\x14\n\x05width\x18\x02\x20\x01(\rR\x05wid\
    th\x12\x1a\n\x08channels\x18\x03\x20\x01(\rR\x08channelsB\x16\n\x14de.st\
    arwit.visionapib\x06proto3\
";

/// `FileDescriptorProto` object which was a source for this generated file
fn file_descriptor_proto() -> &'static ::protobuf::descriptor::FileDescriptorProto {
    static file_descriptor_proto_lazy: ::protobuf::rt::Lazy<::protobuf::descriptor::FileDescriptorProto> = ::protobuf::rt::Lazy::new();
    file_descriptor_proto_lazy.get(|| {
        ::protobuf::Message::parse_from_bytes(file_descriptor_proto_data).unwrap()
    })
}

/// `FileDescriptor` object which allows dynamic access to files
pub fn file_descriptor() -> &'static ::protobuf::reflect::FileDescriptor {
    static generated_file_descriptor_lazy: ::protobuf::rt::Lazy<::protobuf::reflect::GeneratedFileDescriptor> = ::protobuf::rt::Lazy::new();
    static file_descriptor: ::protobuf::rt::Lazy<::protobuf::reflect::FileDescriptor> = ::protobuf::rt::Lazy::new();
    file_descriptor.get(|| {
        let generated_file_descriptor = generated_file_descriptor_lazy.get(|| {
            let mut deps = ::std::vec::Vec::with_capacity(0);
            let mut messages = ::std::vec::Vec::with_capacity(2);
            messages.push(VideoFrame::generated_message_descriptor_data());
            messages.push(Shape::generated_message_descriptor_data());
            let mut enums = ::std::vec::Vec::with_capacity(0);
            ::protobuf::reflect::GeneratedFileDescriptor::new_generated(
                file_descriptor_proto(),
                deps,
                messages,
                enums,
            )
        });
        ::protobuf::reflect::FileDescriptor::new_generated_2(generated_file_descriptor)
    })
}
