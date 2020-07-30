// Generated by gencpp from file pitakuru/SoundFeedback.msg
// DO NOT EDIT!


#ifndef PITAKURU_MESSAGE_SOUNDFEEDBACK_H
#define PITAKURU_MESSAGE_SOUNDFEEDBACK_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace pitakuru
{
template <class ContainerAllocator>
struct SoundFeedback_
{
  typedef SoundFeedback_<ContainerAllocator> Type;

  SoundFeedback_()
    {
    }
  SoundFeedback_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::pitakuru::SoundFeedback_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pitakuru::SoundFeedback_<ContainerAllocator> const> ConstPtr;

}; // struct SoundFeedback_

typedef ::pitakuru::SoundFeedback_<std::allocator<void> > SoundFeedback;

typedef boost::shared_ptr< ::pitakuru::SoundFeedback > SoundFeedbackPtr;
typedef boost::shared_ptr< ::pitakuru::SoundFeedback const> SoundFeedbackConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pitakuru::SoundFeedback_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pitakuru::SoundFeedback_<ContainerAllocator> >::stream(s, "", v);
return s;
}


} // namespace pitakuru

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::pitakuru::SoundFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pitakuru::SoundFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pitakuru::SoundFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pitakuru::SoundFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pitakuru::SoundFeedback_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pitakuru::SoundFeedback_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pitakuru::SoundFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::pitakuru::SoundFeedback_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::pitakuru::SoundFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pitakuru/SoundFeedback";
  }

  static const char* value(const ::pitakuru::SoundFeedback_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pitakuru::SoundFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
;
  }

  static const char* value(const ::pitakuru::SoundFeedback_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pitakuru::SoundFeedback_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SoundFeedback_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pitakuru::SoundFeedback_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::pitakuru::SoundFeedback_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // PITAKURU_MESSAGE_SOUNDFEEDBACK_H
