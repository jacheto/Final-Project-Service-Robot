// Generated by gencpp from file roboserv_description/Sensores.msg
// DO NOT EDIT!


#ifndef ROBOSERV_DESCRIPTION_MESSAGE_SENSORES_H
#define ROBOSERV_DESCRIPTION_MESSAGE_SENSORES_H


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
struct Sensores_
{
  typedef Sensores_<ContainerAllocator> Type;

  Sensores_()
    : SensorL(0.0)
    , SensorFL(0.0)
    , SensorF(0.0)
    , SensorFR(0.0)
    , SensorR(0.0)  {
    }
  Sensores_(const ContainerAllocator& _alloc)
    : SensorL(0.0)
    , SensorFL(0.0)
    , SensorF(0.0)
    , SensorFR(0.0)
    , SensorR(0.0)  {
  (void)_alloc;
    }



   typedef float _SensorL_type;
  _SensorL_type SensorL;

   typedef float _SensorFL_type;
  _SensorFL_type SensorFL;

   typedef float _SensorF_type;
  _SensorF_type SensorF;

   typedef float _SensorFR_type;
  _SensorFR_type SensorFR;

   typedef float _SensorR_type;
  _SensorR_type SensorR;





  typedef boost::shared_ptr< ::roboserv_description::Sensores_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::roboserv_description::Sensores_<ContainerAllocator> const> ConstPtr;

}; // struct Sensores_

typedef ::roboserv_description::Sensores_<std::allocator<void> > Sensores;

typedef boost::shared_ptr< ::roboserv_description::Sensores > SensoresPtr;
typedef boost::shared_ptr< ::roboserv_description::Sensores const> SensoresConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::roboserv_description::Sensores_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::roboserv_description::Sensores_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::roboserv_description::Sensores_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::roboserv_description::Sensores_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::roboserv_description::Sensores_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::roboserv_description::Sensores_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::roboserv_description::Sensores_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::roboserv_description::Sensores_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::roboserv_description::Sensores_<ContainerAllocator> >
{
  static const char* value()
  {
    return "4e7e993f2ad894e38becbb76ebb5ec09";
  }

  static const char* value(const ::roboserv_description::Sensores_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x4e7e993f2ad894e3ULL;
  static const uint64_t static_value2 = 0x8becbb76ebb5ec09ULL;
};

template<class ContainerAllocator>
struct DataType< ::roboserv_description::Sensores_<ContainerAllocator> >
{
  static const char* value()
  {
    return "roboserv_description/Sensores";
  }

  static const char* value(const ::roboserv_description::Sensores_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::roboserv_description::Sensores_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 SensorL\n\
float32 SensorFL\n\
float32 SensorF\n\
float32 SensorFR\n\
float32 SensorR\n\
";
  }

  static const char* value(const ::roboserv_description::Sensores_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::roboserv_description::Sensores_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.SensorL);
      stream.next(m.SensorFL);
      stream.next(m.SensorF);
      stream.next(m.SensorFR);
      stream.next(m.SensorR);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Sensores_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::roboserv_description::Sensores_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::roboserv_description::Sensores_<ContainerAllocator>& v)
  {
    s << indent << "SensorL: ";
    Printer<float>::stream(s, indent + "  ", v.SensorL);
    s << indent << "SensorFL: ";
    Printer<float>::stream(s, indent + "  ", v.SensorFL);
    s << indent << "SensorF: ";
    Printer<float>::stream(s, indent + "  ", v.SensorF);
    s << indent << "SensorFR: ";
    Printer<float>::stream(s, indent + "  ", v.SensorFR);
    s << indent << "SensorR: ";
    Printer<float>::stream(s, indent + "  ", v.SensorR);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROBOSERV_DESCRIPTION_MESSAGE_SENSORES_H
