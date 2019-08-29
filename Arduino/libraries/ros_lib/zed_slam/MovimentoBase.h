#ifndef _ROS_zed_slam_MovimentoBase_h
#define _ROS_zed_slam_MovimentoBase_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace zed_slam
{

  class MovimentoBase : public ros::Msg
  {
    public:
      typedef int32_t _VelMotorE_type;
      _VelMotorE_type VelMotorE;
      typedef int32_t _VelMotorD_type;
      _VelMotorD_type VelMotorD;

    MovimentoBase():
      VelMotorE(0),
      VelMotorD(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_VelMotorE;
      u_VelMotorE.real = this->VelMotorE;
      *(outbuffer + offset + 0) = (u_VelMotorE.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_VelMotorE.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_VelMotorE.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_VelMotorE.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->VelMotorE);
      union {
        int32_t real;
        uint32_t base;
      } u_VelMotorD;
      u_VelMotorD.real = this->VelMotorD;
      *(outbuffer + offset + 0) = (u_VelMotorD.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_VelMotorD.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_VelMotorD.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_VelMotorD.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->VelMotorD);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_VelMotorE;
      u_VelMotorE.base = 0;
      u_VelMotorE.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_VelMotorE.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_VelMotorE.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_VelMotorE.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->VelMotorE = u_VelMotorE.real;
      offset += sizeof(this->VelMotorE);
      union {
        int32_t real;
        uint32_t base;
      } u_VelMotorD;
      u_VelMotorD.base = 0;
      u_VelMotorD.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_VelMotorD.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_VelMotorD.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_VelMotorD.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->VelMotorD = u_VelMotorD.real;
      offset += sizeof(this->VelMotorD);
     return offset;
    }

    const char * getType(){ return "zed_slam/MovimentoBase"; };
    const char * getMD5(){ return "93a241cd2b761554dce80f03bc3ad573"; };

  };

}
#endif