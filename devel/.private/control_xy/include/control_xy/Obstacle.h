// Generated by gencpp from file control_xy/Obstacle.msg
// DO NOT EDIT!


#ifndef CONTROL_XY_MESSAGE_OBSTACLE_H
#define CONTROL_XY_MESSAGE_OBSTACLE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace control_xy
{
template <class ContainerAllocator>
struct Obstacle_
{
  typedef Obstacle_<ContainerAllocator> Type;

  Obstacle_()
    : type(0)
    , angle(0.0)
    , distance(0.0)  {
    }
  Obstacle_(const ContainerAllocator& _alloc)
    : type(0)
    , angle(0.0)
    , distance(0.0)  {
  (void)_alloc;
    }



   typedef uint8_t _type_type;
  _type_type type;

   typedef float _angle_type;
  _angle_type angle;

   typedef float _distance_type;
  _distance_type distance;



// reducing the odds to have name collisions with Windows.h 
#if defined(_WIN32) && defined(TYPE_WARNING)
  #undef TYPE_WARNING
#endif
#if defined(_WIN32) && defined(TYPE_DANGER)
  #undef TYPE_DANGER
#endif

  enum {
    TYPE_WARNING = 0u,
    TYPE_DANGER = 1u,
  };


  typedef boost::shared_ptr< ::control_xy::Obstacle_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::control_xy::Obstacle_<ContainerAllocator> const> ConstPtr;

}; // struct Obstacle_

typedef ::control_xy::Obstacle_<std::allocator<void> > Obstacle;

typedef boost::shared_ptr< ::control_xy::Obstacle > ObstaclePtr;
typedef boost::shared_ptr< ::control_xy::Obstacle const> ObstacleConstPtr;

// constants requiring out of line definition

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::control_xy::Obstacle_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::control_xy::Obstacle_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::control_xy::Obstacle_<ContainerAllocator1> & lhs, const ::control_xy::Obstacle_<ContainerAllocator2> & rhs)
{
  return lhs.type == rhs.type &&
    lhs.angle == rhs.angle &&
    lhs.distance == rhs.distance;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::control_xy::Obstacle_<ContainerAllocator1> & lhs, const ::control_xy::Obstacle_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace control_xy

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::control_xy::Obstacle_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::control_xy::Obstacle_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::control_xy::Obstacle_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::control_xy::Obstacle_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::control_xy::Obstacle_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::control_xy::Obstacle_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::control_xy::Obstacle_<ContainerAllocator> >
{
  static const char* value()
  {
    return "63d99a9ad294899d03af106edf098ef1";
  }

  static const char* value(const ::control_xy::Obstacle_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x63d99a9ad294899dULL;
  static const uint64_t static_value2 = 0x03af106edf098ef1ULL;
};

template<class ContainerAllocator>
struct DataType< ::control_xy::Obstacle_<ContainerAllocator> >
{
  static const char* value()
  {
    return "control_xy/Obstacle";
  }

  static const char* value(const ::control_xy::Obstacle_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::control_xy::Obstacle_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint8 TYPE_WARNING=0\n"
"uint8 TYPE_DANGER=1\n"
"uint8 type\n"
"float32 angle\n"
"float32 distance\n"
;
  }

  static const char* value(const ::control_xy::Obstacle_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::control_xy::Obstacle_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.type);
      stream.next(m.angle);
      stream.next(m.distance);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Obstacle_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::control_xy::Obstacle_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::control_xy::Obstacle_<ContainerAllocator>& v)
  {
    s << indent << "type: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.type);
    s << indent << "angle: ";
    Printer<float>::stream(s, indent + "  ", v.angle);
    s << indent << "distance: ";
    Printer<float>::stream(s, indent + "  ", v.distance);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CONTROL_XY_MESSAGE_OBSTACLE_H
