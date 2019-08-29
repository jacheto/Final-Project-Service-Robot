#ifndef _ROS_SERVICE_save_odometry_db_h
#define _ROS_SERVICE_save_odometry_db_h
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace zed_wrapper
{

static const char SAVE_ODOMETRY_DB[] = "zed_wrapper/save_odometry_db";

  class save_odometry_dbRequest : public ros::Msg
  {
    public:
      typedef const char* _area_path_type;
      _area_path_type area_path;

    save_odometry_dbRequest():
      area_path("")
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      uint32_t length_area_path = strlen(this->area_path);
      varToArr(outbuffer + offset, length_area_path);
      offset += 4;
      memcpy(outbuffer + offset, this->area_path, length_area_path);
      offset += length_area_path;
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      uint32_t length_area_path;
      arrToVar(length_area_path, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_area_path; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_area_path-1]=0;
      this->area_path = (char *)(inbuffer + offset-1);
      offset += length_area_path;
     return offset;
    }

    const char * getType(){ return SAVE_ODOMETRY_DB; };
    const char * getMD5(){ return "3aa42502a35317f413e91f0f35b53028"; };

  };

  class save_odometry_dbResponse : public ros::Msg
  {
    public:
      typedef bool _result_type;
      _result_type result;
      typedef const char* _info_type;
      _info_type info;

    save_odometry_dbResponse():
      result(0),
      info("")
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
      uint32_t length_info = strlen(this->info);
      varToArr(outbuffer + offset, length_info);
      offset += 4;
      memcpy(outbuffer + offset, this->info, length_info);
      offset += length_info;
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
      uint32_t length_info;
      arrToVar(length_info, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_info; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_info-1]=0;
      this->info = (char *)(inbuffer + offset-1);
      offset += length_info;
     return offset;
    }

    const char * getType(){ return SAVE_ODOMETRY_DB; };
    const char * getMD5(){ return "929b8c0d7b68510a3f501a60258c746e"; };

  };

  class save_odometry_db {
    public:
    typedef save_odometry_dbRequest Request;
    typedef save_odometry_dbResponse Response;
  };

}
#endif
