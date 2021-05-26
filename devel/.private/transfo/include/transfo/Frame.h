// Generated by gencpp from file transfo/Frame.msg
// DO NOT EDIT!


#ifndef TRANSFO_MESSAGE_FRAME_H
#define TRANSFO_MESSAGE_FRAME_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace transfo
{
template <class ContainerAllocator>
struct Frame_
{
  typedef Frame_<ContainerAllocator> Type;

  Frame_()
    : header()
    , id(0)
    , is_rtr(false)
    , is_extended(false)
    , is_error(false)
    , dlc(0)
    , data()  {
      data.assign(0);
  }
  Frame_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , id(0)
    , is_rtr(false)
    , is_extended(false)
    , is_error(false)
    , dlc(0)
    , data()  {
  (void)_alloc;
      data.assign(0);
  }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef uint32_t _id_type;
  _id_type id;

   typedef uint8_t _is_rtr_type;
  _is_rtr_type is_rtr;

   typedef uint8_t _is_extended_type;
  _is_extended_type is_extended;

   typedef uint8_t _is_error_type;
  _is_error_type is_error;

   typedef uint8_t _dlc_type;
  _dlc_type dlc;

   typedef boost::array<uint8_t, 8>  _data_type;
  _data_type data;





  typedef boost::shared_ptr< ::transfo::Frame_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::transfo::Frame_<ContainerAllocator> const> ConstPtr;

}; // struct Frame_

typedef ::transfo::Frame_<std::allocator<void> > Frame;

typedef boost::shared_ptr< ::transfo::Frame > FramePtr;
typedef boost::shared_ptr< ::transfo::Frame const> FrameConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::transfo::Frame_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::transfo::Frame_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::transfo::Frame_<ContainerAllocator1> & lhs, const ::transfo::Frame_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.id == rhs.id &&
    lhs.is_rtr == rhs.is_rtr &&
    lhs.is_extended == rhs.is_extended &&
    lhs.is_error == rhs.is_error &&
    lhs.dlc == rhs.dlc &&
    lhs.data == rhs.data;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::transfo::Frame_<ContainerAllocator1> & lhs, const ::transfo::Frame_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace transfo

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::transfo::Frame_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::transfo::Frame_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::transfo::Frame_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::transfo::Frame_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::transfo::Frame_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::transfo::Frame_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::transfo::Frame_<ContainerAllocator> >
{
  static const char* value()
  {
    return "64ae5cebf967dc6aae4e78f5683a5b25";
  }

  static const char* value(const ::transfo::Frame_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x64ae5cebf967dc6aULL;
  static const uint64_t static_value2 = 0xae4e78f5683a5b25ULL;
};

template<class ContainerAllocator>
struct DataType< ::transfo::Frame_<ContainerAllocator> >
{
  static const char* value()
  {
    return "transfo/Frame";
  }

  static const char* value(const ::transfo::Frame_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::transfo::Frame_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n"
"uint32 id\n"
"bool is_rtr\n"
"bool is_extended\n"
"bool is_error\n"
"uint8 dlc\n"
"uint8[8] data\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
;
  }

  static const char* value(const ::transfo::Frame_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::transfo::Frame_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.id);
      stream.next(m.is_rtr);
      stream.next(m.is_extended);
      stream.next(m.is_error);
      stream.next(m.dlc);
      stream.next(m.data);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Frame_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::transfo::Frame_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::transfo::Frame_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "id: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.id);
    s << indent << "is_rtr: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.is_rtr);
    s << indent << "is_extended: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.is_extended);
    s << indent << "is_error: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.is_error);
    s << indent << "dlc: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.dlc);
    s << indent << "data[]" << std::endl;
    for (size_t i = 0; i < v.data.size(); ++i)
    {
      s << indent << "  data[" << i << "]: ";
      Printer<uint8_t>::stream(s, indent + "  ", v.data[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // TRANSFO_MESSAGE_FRAME_H
