// Generated by gencpp from file pitakuru/TriggerAction.msg
// DO NOT EDIT!


#ifndef PITAKURU_MESSAGE_TRIGGERACTION_H
#define PITAKURU_MESSAGE_TRIGGERACTION_H


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
struct TriggerAction_
{
  typedef TriggerAction_<ContainerAllocator> Type;

  TriggerAction_()
    : trigger()  {
    }
  TriggerAction_(const ContainerAllocator& _alloc)
    : trigger(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _trigger_type;
  _trigger_type trigger;



// reducing the odds to have name collisions with Windows.h 
#if defined(_WIN32) && defined(TRIGGER_EMERGENCY_BUTTON_OFF)
  #undef TRIGGER_EMERGENCY_BUTTON_OFF
#endif
#if defined(_WIN32) && defined(TRIGGER_EMERGENCY_BUTTON_ON)
  #undef TRIGGER_EMERGENCY_BUTTON_ON
#endif
#if defined(_WIN32) && defined(TRIGGER_KARUGAMO_BUTTON_ON)
  #undef TRIGGER_KARUGAMO_BUTTON_ON
#endif
#if defined(_WIN32) && defined(TRIGGER_REMOTE_KARUGAMO_BUTTON_ON)
  #undef TRIGGER_REMOTE_KARUGAMO_BUTTON_ON
#endif
#if defined(_WIN32) && defined(TRIGGER_REMOTE_MANUAL_BUTTON_ON)
  #undef TRIGGER_REMOTE_MANUAL_BUTTON_ON
#endif
#if defined(_WIN32) && defined(TRIGGER_REMOTE_IDLE_BUTTON_ON)
  #undef TRIGGER_REMOTE_IDLE_BUTTON_ON
#endif
#if defined(_WIN32) && defined(TRIGGER_IDLE_BUTTON_ON)
  #undef TRIGGER_IDLE_BUTTON_ON
#endif
#if defined(_WIN32) && defined(TRIGGER_DETECT_OBSTACLE)
  #undef TRIGGER_DETECT_OBSTACLE
#endif
#if defined(_WIN32) && defined(TRIGGER_DETECT_DANGER_OBSTACLE)
  #undef TRIGGER_DETECT_DANGER_OBSTACLE
#endif
#if defined(_WIN32) && defined(TRIGGER_COLLISION)
  #undef TRIGGER_COLLISION
#endif
#if defined(_WIN32) && defined(TRIGGER_BREAK_RELEASE_BUTTON_ON)
  #undef TRIGGER_BREAK_RELEASE_BUTTON_ON
#endif
#if defined(_WIN32) && defined(TRIGGER_LONG_LOST)
  #undef TRIGGER_LONG_LOST
#endif


  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  TRIGGER_EMERGENCY_BUTTON_OFF;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  TRIGGER_EMERGENCY_BUTTON_ON;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  TRIGGER_KARUGAMO_BUTTON_ON;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  TRIGGER_REMOTE_KARUGAMO_BUTTON_ON;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  TRIGGER_REMOTE_MANUAL_BUTTON_ON;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  TRIGGER_REMOTE_IDLE_BUTTON_ON;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  TRIGGER_IDLE_BUTTON_ON;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  TRIGGER_DETECT_OBSTACLE;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  TRIGGER_DETECT_DANGER_OBSTACLE;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  TRIGGER_COLLISION;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  TRIGGER_BREAK_RELEASE_BUTTON_ON;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  TRIGGER_LONG_LOST;

  typedef boost::shared_ptr< ::pitakuru::TriggerAction_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pitakuru::TriggerAction_<ContainerAllocator> const> ConstPtr;

}; // struct TriggerAction_

typedef ::pitakuru::TriggerAction_<std::allocator<void> > TriggerAction;

typedef boost::shared_ptr< ::pitakuru::TriggerAction > TriggerActionPtr;
typedef boost::shared_ptr< ::pitakuru::TriggerAction const> TriggerActionConstPtr;

// constants requiring out of line definition

   
   template<typename ContainerAllocator> const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > 
      TriggerAction_<ContainerAllocator>::TRIGGER_EMERGENCY_BUTTON_OFF =
        
          "emergency_button_off"
        
        ;
   

   
   template<typename ContainerAllocator> const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > 
      TriggerAction_<ContainerAllocator>::TRIGGER_EMERGENCY_BUTTON_ON =
        
          "emergency_button_on"
        
        ;
   

   
   template<typename ContainerAllocator> const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > 
      TriggerAction_<ContainerAllocator>::TRIGGER_KARUGAMO_BUTTON_ON =
        
          "karugamo_button_on"
        
        ;
   

   
   template<typename ContainerAllocator> const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > 
      TriggerAction_<ContainerAllocator>::TRIGGER_REMOTE_KARUGAMO_BUTTON_ON =
        
          "remote_karuamo_button_on"
        
        ;
   

   
   template<typename ContainerAllocator> const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > 
      TriggerAction_<ContainerAllocator>::TRIGGER_REMOTE_MANUAL_BUTTON_ON =
        
          "remote_manual_button_on"
        
        ;
   

   
   template<typename ContainerAllocator> const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > 
      TriggerAction_<ContainerAllocator>::TRIGGER_REMOTE_IDLE_BUTTON_ON =
        
          "remote_idle_button_on"
        
        ;
   

   
   template<typename ContainerAllocator> const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > 
      TriggerAction_<ContainerAllocator>::TRIGGER_IDLE_BUTTON_ON =
        
          "idle_button_on"
        
        ;
   

   
   template<typename ContainerAllocator> const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > 
      TriggerAction_<ContainerAllocator>::TRIGGER_DETECT_OBSTACLE =
        
          "detect_obstacle"
        
        ;
   

   
   template<typename ContainerAllocator> const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > 
      TriggerAction_<ContainerAllocator>::TRIGGER_DETECT_DANGER_OBSTACLE =
        
          "detect_danger_obstacle"
        
        ;
   

   
   template<typename ContainerAllocator> const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > 
      TriggerAction_<ContainerAllocator>::TRIGGER_COLLISION =
        
          "collision"
        
        ;
   

   
   template<typename ContainerAllocator> const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > 
      TriggerAction_<ContainerAllocator>::TRIGGER_BREAK_RELEASE_BUTTON_ON =
        
          "break_release_button_on"
        
        ;
   

   
   template<typename ContainerAllocator> const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > 
      TriggerAction_<ContainerAllocator>::TRIGGER_LONG_LOST =
        
          "long_lost"
        
        ;
   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pitakuru::TriggerAction_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pitakuru::TriggerAction_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::pitakuru::TriggerAction_<ContainerAllocator1> & lhs, const ::pitakuru::TriggerAction_<ContainerAllocator2> & rhs)
{
  return lhs.trigger == rhs.trigger;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::pitakuru::TriggerAction_<ContainerAllocator1> & lhs, const ::pitakuru::TriggerAction_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace pitakuru

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::pitakuru::TriggerAction_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pitakuru::TriggerAction_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pitakuru::TriggerAction_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pitakuru::TriggerAction_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pitakuru::TriggerAction_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pitakuru::TriggerAction_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pitakuru::TriggerAction_<ContainerAllocator> >
{
  static const char* value()
  {
    return "529f37831afe7067075cb584db0e391e";
  }

  static const char* value(const ::pitakuru::TriggerAction_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x529f37831afe7067ULL;
  static const uint64_t static_value2 = 0x075cb584db0e391eULL;
};

template<class ContainerAllocator>
struct DataType< ::pitakuru::TriggerAction_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pitakuru/TriggerAction";
  }

  static const char* value(const ::pitakuru::TriggerAction_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pitakuru::TriggerAction_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# 非常停止ボタン解除\n"
"string TRIGGER_EMERGENCY_BUTTON_OFF = emergency_button_off\n"
"# 非常停止ボタン押下\n"
"string TRIGGER_EMERGENCY_BUTTON_ON = emergency_button_on\n"
"# カルガモボタン押下\n"
"string TRIGGER_KARUGAMO_BUTTON_ON = karugamo_button_on\n"
"# リモコン:カルガモボタン押下\n"
"string TRIGGER_REMOTE_KARUGAMO_BUTTON_ON = remote_karuamo_button_on\n"
"# リモコン:マニュアルボタン押下\n"
"string TRIGGER_REMOTE_MANUAL_BUTTON_ON = remote_manual_button_on\n"
"# リモコン:アイドルボタン押下\n"
"string TRIGGER_REMOTE_IDLE_BUTTON_ON = remote_idle_button_on\n"
"# アイドルボタン押下\n"
"string TRIGGER_IDLE_BUTTON_ON = idle_button_on\n"
"# 進行方向 2000 mm 以内に障害物を発見\n"
"string TRIGGER_DETECT_OBSTACLE = detect_obstacle\n"
"# 前方近傍に障害物を発見（LIDAR進行方向 500 mm以内）\n"
"string TRIGGER_DETECT_DANGER_OBSTACLE = detect_danger_obstacle\n"
"# ガードバンパー接触\n"
"string TRIGGER_COLLISION = collision\n"
"# ブレーキ解除ボタン押下\n"
"string TRIGGER_BREAK_RELEASE_BUTTON_ON = break_release_button_on\n"
"# 対象ロストから10秒経過\n"
"string TRIGGER_LONG_LOST = long_lost\n"
"\n"
"string trigger\n"
;
  }

  static const char* value(const ::pitakuru::TriggerAction_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pitakuru::TriggerAction_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.trigger);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct TriggerAction_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pitakuru::TriggerAction_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::pitakuru::TriggerAction_<ContainerAllocator>& v)
  {
    s << indent << "trigger: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.trigger);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PITAKURU_MESSAGE_TRIGGERACTION_H
