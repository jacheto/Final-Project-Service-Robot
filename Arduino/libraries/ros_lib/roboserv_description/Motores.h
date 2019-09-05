#ifndef _ROS_roboserv_description_Motores_h
#define _ROS_roboserv_description_Motores_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace roboserv_description
{

  class Motores : public ros::Msg
  {
    public:
      typedef int32_t _MotorL_type;
      _MotorL_type MotorL;
      typedef int32_t _MotorR_type;
      _MotorR_type MotorR;

    Motores():
      MotorL(0),
      MotorR(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_MotorL;
      u_MotorL.real = this->MotorL;
      *(outbuffer + offset + 0) = (u_MotorL.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_MotorL.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_MotorL.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_MotorL.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->MotorL);
      union {
        int32_t real;
        uint32_t base;
      } u_MotorR;
      u_MotorR.real = this->MotorR;
      *(outbuffer + offset + 0) = (u_MotorR.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_MotorR.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_MotorR.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_MotorR.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->MotorR);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_MotorL;
      u_MotorL.base = 0;
      u_MotorL.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_MotorL.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_MotorL.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_MotorL.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->MotorL = u_MotorL.real;
      offset += sizeof(this->MotorL);
      union {
        int32_t real;
        uint32_t base;
      } u_MotorR;
      u_MotorR.base = 0;
      u_MotorR.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_MotorR.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_MotorR.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_MotorR.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->MotorR = u_MotorR.real;
      offset += sizeof(this->MotorR);
     return offset;
    }

    const char * getType(){ return "roboserv_description/Motores"; };
    const char * getMD5(){ return "28ee0bcd94a4539f94474748fbc61333"; };

  };

}
#endif