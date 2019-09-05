// Generated by gencpp from file zed_wrapper/set_poseRequest.msg
// DO NOT EDIT!


#ifndef ZED_WRAPPER_MESSAGE_SET_POSEREQUEST_H
#define ZED_WRAPPER_MESSAGE_SET_POSEREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace zed_wrapper
{
template <class ContainerAllocator>
struct set_poseRequest_
{
  typedef set_poseRequest_<ContainerAllocator> Type;

  set_poseRequest_()
    : x(0.0)
    , y(0.0)
    , z(0.0)
    , R(0.0)
    , P(0.0)
    , Y(0.0)  {
    }
  set_poseRequest_(const ContainerAllocator& _alloc)
    : x(0.0)
    , y(0.0)
    , z(0.0)
    , R(0.0)
    , P(0.0)
    , Y(0.0)  {
  (void)_alloc;
    }



   typedef float _x_type;
  _x_type x;

   typedef float _y_type;
  _y_type y;

   typedef float _z_type;
  _z_type z;

   typedef float _R_type;
  _R_type R;

   typedef float _P_type;
  _P_type P;

   typedef float _Y_type;
  _Y_type Y;





  typedef boost::shared_ptr< ::zed_wrapper::set_poseRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::zed_wrapper::set_poseRequest_<ContainerAllocator> const> ConstPtr;

}; // struct set_poseRequest_

typedef ::zed_wrapper::set_poseRequest_<std::allocator<void> > set_poseRequest;

typedef boost::shared_ptr< ::zed_wrapper::set_poseRequest > set_poseRequestPtr;
typedef boost::shared_ptr< ::zed_wrapper::set_poseRequest const> set_poseRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::zed_wrapper::set_poseRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::zed_wrapper::set_poseRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace zed_wrapper

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::zed_wrapper::set_poseRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::zed_wrapper::set_poseRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::zed_wrapper::set_poseRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::zed_wrapper::set_poseRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::zed_wrapper::set_poseRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::zed_wrapper::set_poseRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::zed_wrapper::set_poseRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "2d76cb67dcd5839567c5ce0b111a67e4";
  }

  static const char* value(const ::zed_wrapper::set_poseRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x2d76cb67dcd58395ULL;
  static const uint64_t static_value2 = 0x67c5ce0b111a67e4ULL;
};

template<class ContainerAllocator>
struct DataType< ::zed_wrapper::set_poseRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "zed_wrapper/set_poseRequest";
  }

  static const char* value(const ::zed_wrapper::set_poseRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::zed_wrapper::set_poseRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
float32 x\n\
float32 y\n\
float32 z\n\
\n\
float32 R\n\
float32 P\n\
float32 Y\n\
";
  }

  static const char* value(const ::zed_wrapper::set_poseRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::zed_wrapper::set_poseRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x);
      stream.next(m.y);
      stream.next(m.z);
      stream.next(m.R);
      stream.next(m.P);
      stream.next(m.Y);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct set_poseRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::zed_wrapper::set_poseRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::zed_wrapper::set_poseRequest_<ContainerAllocator>& v)
  {
    s << indent << "x: ";
    Printer<float>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<float>::stream(s, indent + "  ", v.y);
    s << indent << "z: ";
    Printer<float>::stream(s, indent + "  ", v.z);
    s << indent << "R: ";
    Printer<float>::stream(s, indent + "  ", v.R);
    s << indent << "P: ";
    Printer<float>::stream(s, indent + "  ", v.P);
    s << indent << "Y: ";
    Printer<float>::stream(s, indent + "  ", v.Y);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ZED_WRAPPER_MESSAGE_SET_POSEREQUEST_H
