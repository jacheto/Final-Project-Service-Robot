#ifndef _ROS_roboserv_description_Sensores_h
#define _ROS_roboserv_description_Sensores_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace roboserv_description
{

  class Sensores : public ros::Msg
  {
    public:
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

    Sensores():
      SensorL(0),
      SensorFL(0),
      SensorF(0),
      SensorFR(0),
      SensorR(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        float real;
        uint32_t base;
      } u_SensorL;
      u_SensorL.real = this->SensorL;
      *(outbuffer + offset + 0) = (u_SensorL.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_SensorL.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_SensorL.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_SensorL.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->SensorL);
      union {
        float real;
        uint32_t base;
      } u_SensorFL;
      u_SensorFL.real = this->SensorFL;
      *(outbuffer + offset + 0) = (u_SensorFL.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_SensorFL.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_SensorFL.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_SensorFL.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->SensorFL);
      union {
        float real;
        uint32_t base;
      } u_SensorF;
      u_SensorF.real = this->SensorF;
      *(outbuffer + offset + 0) = (u_SensorF.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_SensorF.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_SensorF.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_SensorF.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->SensorF);
      union {
        float real;
        uint32_t base;
      } u_SensorFR;
      u_SensorFR.real = this->SensorFR;
      *(outbuffer + offset + 0) = (u_SensorFR.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_SensorFR.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_SensorFR.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_SensorFR.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->SensorFR);
      union {
        float real;
        uint32_t base;
      } u_SensorR;
      u_SensorR.real = this->SensorR;
      *(outbuffer + offset + 0) = (u_SensorR.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_SensorR.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_SensorR.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_SensorR.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->SensorR);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        float real;
        uint32_t base;
      } u_SensorL;
      u_SensorL.base = 0;
      u_SensorL.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_SensorL.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_SensorL.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_SensorL.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->SensorL = u_SensorL.real;
      offset += sizeof(this->SensorL);
      union {
        float real;
        uint32_t base;
      } u_SensorFL;
      u_SensorFL.base = 0;
      u_SensorFL.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_SensorFL.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_SensorFL.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_SensorFL.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->SensorFL = u_SensorFL.real;
      offset += sizeof(this->SensorFL);
      union {
        float real;
        uint32_t base;
      } u_SensorF;
      u_SensorF.base = 0;
      u_SensorF.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_SensorF.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_SensorF.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_SensorF.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->SensorF = u_SensorF.real;
      offset += sizeof(this->SensorF);
      union {
        float real;
        uint32_t base;
      } u_SensorFR;
      u_SensorFR.base = 0;
      u_SensorFR.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_SensorFR.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_SensorFR.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_SensorFR.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->SensorFR = u_SensorFR.real;
      offset += sizeof(this->SensorFR);
      union {
        float real;
        uint32_t base;
      } u_SensorR;
      u_SensorR.base = 0;
      u_SensorR.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_SensorR.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_SensorR.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_SensorR.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->SensorR = u_SensorR.real;
      offset += sizeof(this->SensorR);
     return offset;
    }

    const char * getType(){ return "roboserv_description/Sensores"; };
    const char * getMD5(){ return "4e7e993f2ad894e38becbb76ebb5ec09"; };

  };

}
#endif