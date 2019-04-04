// Generated by gencpp from file industrial_extrinsic_cal/robot_pose_triggerGoal.msg
// DO NOT EDIT!


#ifndef INDUSTRIAL_EXTRINSIC_CAL_MESSAGE_ROBOT_POSE_TRIGGERGOAL_H
#define INDUSTRIAL_EXTRINSIC_CAL_MESSAGE_ROBOT_POSE_TRIGGERGOAL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/Pose.h>

namespace industrial_extrinsic_cal
{
template <class ContainerAllocator>
struct robot_pose_triggerGoal_
{
  typedef robot_pose_triggerGoal_<ContainerAllocator> Type;

  robot_pose_triggerGoal_()
    : pose()  {
    }
  robot_pose_triggerGoal_(const ContainerAllocator& _alloc)
    : pose(_alloc)  {
  (void)_alloc;
    }



   typedef  ::geometry_msgs::Pose_<ContainerAllocator>  _pose_type;
  _pose_type pose;





  typedef boost::shared_ptr< ::industrial_extrinsic_cal::robot_pose_triggerGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::industrial_extrinsic_cal::robot_pose_triggerGoal_<ContainerAllocator> const> ConstPtr;

}; // struct robot_pose_triggerGoal_

typedef ::industrial_extrinsic_cal::robot_pose_triggerGoal_<std::allocator<void> > robot_pose_triggerGoal;

typedef boost::shared_ptr< ::industrial_extrinsic_cal::robot_pose_triggerGoal > robot_pose_triggerGoalPtr;
typedef boost::shared_ptr< ::industrial_extrinsic_cal::robot_pose_triggerGoal const> robot_pose_triggerGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::industrial_extrinsic_cal::robot_pose_triggerGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::industrial_extrinsic_cal::robot_pose_triggerGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace industrial_extrinsic_cal

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/kinetic/share/sensor_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'industrial_extrinsic_cal': ['/home/casch/yumi_depends_ws/devel/share/industrial_extrinsic_cal/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::industrial_extrinsic_cal::robot_pose_triggerGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::industrial_extrinsic_cal::robot_pose_triggerGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::industrial_extrinsic_cal::robot_pose_triggerGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::industrial_extrinsic_cal::robot_pose_triggerGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::industrial_extrinsic_cal::robot_pose_triggerGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::industrial_extrinsic_cal::robot_pose_triggerGoal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::industrial_extrinsic_cal::robot_pose_triggerGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "f192399f711a48924df9a394d37edd67";
  }

  static const char* value(const ::industrial_extrinsic_cal::robot_pose_triggerGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xf192399f711a4892ULL;
  static const uint64_t static_value2 = 0x4df9a394d37edd67ULL;
};

template<class ContainerAllocator>
struct DataType< ::industrial_extrinsic_cal::robot_pose_triggerGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "industrial_extrinsic_cal/robot_pose_triggerGoal";
  }

  static const char* value(const ::industrial_extrinsic_cal::robot_pose_triggerGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::industrial_extrinsic_cal::robot_pose_triggerGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
# Define the goal\n\
geometry_msgs/Pose pose\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Pose\n\
# A representation of pose in free space, composed of position and orientation. \n\
Point position\n\
Quaternion orientation\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Point\n\
# This contains the position of a point in free space\n\
float64 x\n\
float64 y\n\
float64 z\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Quaternion\n\
# This represents an orientation in free space in quaternion form.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
float64 w\n\
";
  }

  static const char* value(const ::industrial_extrinsic_cal::robot_pose_triggerGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::industrial_extrinsic_cal::robot_pose_triggerGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.pose);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct robot_pose_triggerGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::industrial_extrinsic_cal::robot_pose_triggerGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::industrial_extrinsic_cal::robot_pose_triggerGoal_<ContainerAllocator>& v)
  {
    s << indent << "pose: ";
    s << std::endl;
    Printer< ::geometry_msgs::Pose_<ContainerAllocator> >::stream(s, indent + "  ", v.pose);
  }
};

} // namespace message_operations
} // namespace ros

#endif // INDUSTRIAL_EXTRINSIC_CAL_MESSAGE_ROBOT_POSE_TRIGGERGOAL_H