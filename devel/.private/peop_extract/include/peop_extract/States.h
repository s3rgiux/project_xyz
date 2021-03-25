// Generated by gencpp from file peop_extract/States.msg
// DO NOT EDIT!


#ifndef PEOP_EXTRACT_MESSAGE_STATES_H
#define PEOP_EXTRACT_MESSAGE_STATES_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/Twist.h>

namespace peop_extract
{
template <class ContainerAllocator>
struct States_
{
  typedef States_<ContainerAllocator> Type;

  States_()
    : state()
    , state_karugamo()
    , state_collision()
    , state_danger()
    , state_costmap()
    , state_manual()
    , state_scan()
    , trackeds()  {
    }
  States_(const ContainerAllocator& _alloc)
    : state(_alloc)
    , state_karugamo(_alloc)
    , state_collision(_alloc)
    , state_danger(_alloc)
    , state_costmap(_alloc)
    , state_manual(_alloc)
    , state_scan(_alloc)
    , trackeds(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _state_type;
  _state_type state;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _state_karugamo_type;
  _state_karugamo_type state_karugamo;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _state_collision_type;
  _state_collision_type state_collision;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _state_danger_type;
  _state_danger_type state_danger;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _state_costmap_type;
  _state_costmap_type state_costmap;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _state_manual_type;
  _state_manual_type state_manual;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _state_scan_type;
  _state_scan_type state_scan;

   typedef  ::geometry_msgs::Twist_<ContainerAllocator>  _trackeds_type;
  _trackeds_type trackeds;





  typedef boost::shared_ptr< ::peop_extract::States_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::peop_extract::States_<ContainerAllocator> const> ConstPtr;

}; // struct States_

typedef ::peop_extract::States_<std::allocator<void> > States;

typedef boost::shared_ptr< ::peop_extract::States > StatesPtr;
typedef boost::shared_ptr< ::peop_extract::States const> StatesConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::peop_extract::States_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::peop_extract::States_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::peop_extract::States_<ContainerAllocator1> & lhs, const ::peop_extract::States_<ContainerAllocator2> & rhs)
{
  return lhs.state == rhs.state &&
    lhs.state_karugamo == rhs.state_karugamo &&
    lhs.state_collision == rhs.state_collision &&
    lhs.state_danger == rhs.state_danger &&
    lhs.state_costmap == rhs.state_costmap &&
    lhs.state_manual == rhs.state_manual &&
    lhs.state_scan == rhs.state_scan &&
    lhs.trackeds == rhs.trackeds;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::peop_extract::States_<ContainerAllocator1> & lhs, const ::peop_extract::States_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace peop_extract

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::peop_extract::States_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::peop_extract::States_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::peop_extract::States_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::peop_extract::States_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::peop_extract::States_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::peop_extract::States_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::peop_extract::States_<ContainerAllocator> >
{
  static const char* value()
  {
    return "dfd48cf7701c5d144c13acc5c8b54ec0";
  }

  static const char* value(const ::peop_extract::States_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xdfd48cf7701c5d14ULL;
  static const uint64_t static_value2 = 0x4c13acc5c8b54ec0ULL;
};

template<class ContainerAllocator>
struct DataType< ::peop_extract::States_<ContainerAllocator> >
{
  static const char* value()
  {
    return "peop_extract/States";
  }

  static const char* value(const ::peop_extract::States_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::peop_extract::States_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string state\n"
"string state_karugamo\n"
"string state_collision\n"
"string state_danger\n"
"string state_costmap\n"
"string state_manual\n"
"string state_scan\n"
"geometry_msgs/Twist trackeds\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Twist\n"
"# This expresses velocity in free space broken into its linear and angular parts.\n"
"Vector3  linear\n"
"Vector3  angular\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Vector3\n"
"# This represents a vector in free space. \n"
"# It is only meant to represent a direction. Therefore, it does not\n"
"# make sense to apply a translation to it (e.g., when applying a \n"
"# generic rigid transformation to a Vector3, tf2 will only apply the\n"
"# rotation). If you want your data to be translatable too, use the\n"
"# geometry_msgs/Point message instead.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
;
  }

  static const char* value(const ::peop_extract::States_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::peop_extract::States_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.state);
      stream.next(m.state_karugamo);
      stream.next(m.state_collision);
      stream.next(m.state_danger);
      stream.next(m.state_costmap);
      stream.next(m.state_manual);
      stream.next(m.state_scan);
      stream.next(m.trackeds);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct States_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::peop_extract::States_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::peop_extract::States_<ContainerAllocator>& v)
  {
    s << indent << "state: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.state);
    s << indent << "state_karugamo: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.state_karugamo);
    s << indent << "state_collision: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.state_collision);
    s << indent << "state_danger: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.state_danger);
    s << indent << "state_costmap: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.state_costmap);
    s << indent << "state_manual: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.state_manual);
    s << indent << "state_scan: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.state_scan);
    s << indent << "trackeds: ";
    s << std::endl;
    Printer< ::geometry_msgs::Twist_<ContainerAllocator> >::stream(s, indent + "  ", v.trackeds);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PEOP_EXTRACT_MESSAGE_STATES_H
