// Generated by gencpp from file roboserv_description/Motores.msg
// DO NOT EDIT!


#ifndef ROBOSERV_DESCRIPTION_MESSAGE_MOTORES_H
#define ROBOSERV_DESCRIPTION_MESSAGE_MOTORES_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace roboserv_description
{
template <class ContainerAllocator>
struct Motores_
{
  typedef Motores_<ContainerAllocator> Type;

  Motores_()
    : MotorL(0)
    , MotorR(0)  {
    }
  Motores_(const ContainerAllocator& _alloc)
    : MotorL(0)
    , MotorR(0)  {
  (void)_alloc;
    }



   typedef int32_t _MotorL_type;
  _MotorL_type MotorL;

   typedef int32_t _MotorR_type;
  _MotorR_type MotorR;





  typedef boost::shared_ptr< ::roboserv_description::Motores_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::roboserv_description::Motores_<ContainerAllocator> const> ConstPtr;

}; // struct Motores_

typedef ::roboserv_description::Motores_<std::allocator<void> > Motores;

typedef boost::shared_ptr< ::roboserv_description::Motores > MotoresPtr;
typedef boost::shared_ptr< ::roboserv_description::Motores const> MotoresConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::roboserv_description::Motores_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::roboserv_description::Motores_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace roboserv_description

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'roboserv_description': ['/home/felipe/roboserv_ws/src/roboserv_description/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::roboserv_description::Motores_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::roboserv_description::Motores_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::roboserv_description::Motores_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::roboserv_description::Motores_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::roboserv_description::Motores_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::roboserv_description::Motores_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::roboserv_description::Motores_<ContainerAllocator> >
{
  static const char* value()
  {
    return "28ee0bcd94a4539f94474748fbc61333";
  }

  static const char* value(const ::roboserv_description::Motores_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x28ee0bcd94a4539fULL;
  static const uint64_t static_value2 = 0x94474748fbc61333ULL;
};

template<class ContainerAllocator>
struct DataType< ::roboserv_description::Motores_<ContainerAllocator> >
{
  static const char* value()
  {
    return "roboserv_description/Motores";
  }

  static const char* value(const ::roboserv_description::Motores_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::roboserv_description::Motores_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 MotorL\n\
int32 MotorR\n\
";
  }

  static const char* value(const ::roboserv_description::Motores_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::roboserv_description::Motores_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.MotorL);
      stream.next(m.MotorR);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Motores_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::roboserv_description::Motores_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::roboserv_description::Motores_<ContainerAllocator>& v)
  {
    s << indent << "MotorL: ";
    Printer<int32_t>::stream(s, indent + "  ", v.MotorL);
    s << indent << "MotorR: ";
    Printer<int32_t>::stream(s, indent + "  ", v.MotorR);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROBOSERV_DESCRIPTION_MESSAGE_MOTORES_H
