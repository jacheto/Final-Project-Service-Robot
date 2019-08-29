#ifndef _ROS_SERVICE_SalvarMapa_h
#define _ROS_SERVICE_SalvarMapa_h
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace zed_slam
{

static const char SALVARMAPA[] = "zed_slam/SalvarMapa";

  class SalvarMapaRequest : public ros::Msg
  {
    public:
      typedef const char* _path_type;
      _path_type path;

    SalvarMapaRequest():
      path("")
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      uint32_t length_path = strlen(this->path);
      varToArr(outbuffer + offset, length_path);
      offset += 4;
      memcpy(outbuffer + offset, this->path, length_path);
      offset += length_path;
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      uint32_t length_path;
      arrToVar(length_path, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_path; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_path-1]=0;
      this->path = (char *)(inbuffer + offset-1);
      offset += length_path;
     return offset;
    }

    const char * getType(){ return SALVARMAPA; };
    const char * getMD5(){ return "1d00cd540af97efeb6b1589112fab63e"; };

  };

  class SalvarMapaResponse : public ros::Msg
  {
    public:
      typedef bool _result_type;
      _result_type result;

    SalvarMapaResponse():
      result(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        bool real;
        uint8_t base;
      } u_result;
      u_result.real = this->result;
      *(outbuffer + offset + 0) = (u_result.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->result);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        bool real;
        uint8_t base;
      } u_result;
      u_result.base = 0;
      u_result.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->result = u_result.real;
      offset += sizeof(this->result);
     return offset;
    }

    const char * getType(){ return SALVARMAPA; };
    const char * getMD5(){ return "eb13ac1f1354ccecb7941ee8fa2192e8"; };

  };

  class SalvarMapa {
    public:
    typedef SalvarMapaRequest Request;
    typedef SalvarMapaResponse Response;
  };

}
#endif
