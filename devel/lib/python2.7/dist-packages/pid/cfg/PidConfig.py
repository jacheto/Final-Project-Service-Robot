## *********************************************************
##
## File autogenerated for the pid package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 245, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 290, 'description': 'Kp scale', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'Kp_scale', 'edit_method': "{'enum_description': 'Scale factor for K setting', 'enum': [{'srcline': 7, 'description': 'Scale by 0.1', 'srcfile': '/home/felipe/roboserv_ws/src/pid/cfg/Pid.cfg', 'cconsttype': 'const double', 'value': 0.1, 'ctype': 'double', 'type': 'double', 'name': 'scale_tenth'}, {'srcline': 8, 'description': 'No scaling', 'srcfile': '/home/felipe/roboserv_ws/src/pid/cfg/Pid.cfg', 'cconsttype': 'const double', 'value': 1.0, 'ctype': 'double', 'type': 'double', 'name': 'scale_unity'}, {'srcline': 9, 'description': 'Scale by 10', 'srcfile': '/home/felipe/roboserv_ws/src/pid/cfg/Pid.cfg', 'cconsttype': 'const double', 'value': 10.0, 'ctype': 'double', 'type': 'double', 'name': 'scale_ten'}, {'srcline': 10, 'description': 'Scale by 100', 'srcfile': '/home/felipe/roboserv_ws/src/pid/cfg/Pid.cfg', 'cconsttype': 'const double', 'value': 100.0, 'ctype': 'double', 'type': 'double', 'name': 'scale_hundred'}]}", 'default': 10.0, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 290, 'description': 'Kp', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'Kp', 'edit_method': '', 'default': 0.1, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 290, 'description': 'Ki scale', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'Ki_scale', 'edit_method': "{'enum_description': 'Scale factor for K setting', 'enum': [{'srcline': 7, 'description': 'Scale by 0.1', 'srcfile': '/home/felipe/roboserv_ws/src/pid/cfg/Pid.cfg', 'cconsttype': 'const double', 'value': 0.1, 'ctype': 'double', 'type': 'double', 'name': 'scale_tenth'}, {'srcline': 8, 'description': 'No scaling', 'srcfile': '/home/felipe/roboserv_ws/src/pid/cfg/Pid.cfg', 'cconsttype': 'const double', 'value': 1.0, 'ctype': 'double', 'type': 'double', 'name': 'scale_unity'}, {'srcline': 9, 'description': 'Scale by 10', 'srcfile': '/home/felipe/roboserv_ws/src/pid/cfg/Pid.cfg', 'cconsttype': 'const double', 'value': 10.0, 'ctype': 'double', 'type': 'double', 'name': 'scale_ten'}, {'srcline': 10, 'description': 'Scale by 100', 'srcfile': '/home/felipe/roboserv_ws/src/pid/cfg/Pid.cfg', 'cconsttype': 'const double', 'value': 100.0, 'ctype': 'double', 'type': 'double', 'name': 'scale_hundred'}]}", 'default': 10.0, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 290, 'description': 'Ki', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'Ki', 'edit_method': '', 'default': 0.1, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 290, 'description': 'Kd scale', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'Kd_scale', 'edit_method': "{'enum_description': 'Scale factor for K setting', 'enum': [{'srcline': 7, 'description': 'Scale by 0.1', 'srcfile': '/home/felipe/roboserv_ws/src/pid/cfg/Pid.cfg', 'cconsttype': 'const double', 'value': 0.1, 'ctype': 'double', 'type': 'double', 'name': 'scale_tenth'}, {'srcline': 8, 'description': 'No scaling', 'srcfile': '/home/felipe/roboserv_ws/src/pid/cfg/Pid.cfg', 'cconsttype': 'const double', 'value': 1.0, 'ctype': 'double', 'type': 'double', 'name': 'scale_unity'}, {'srcline': 9, 'description': 'Scale by 10', 'srcfile': '/home/felipe/roboserv_ws/src/pid/cfg/Pid.cfg', 'cconsttype': 'const double', 'value': 10.0, 'ctype': 'double', 'type': 'double', 'name': 'scale_ten'}, {'srcline': 10, 'description': 'Scale by 100', 'srcfile': '/home/felipe/roboserv_ws/src/pid/cfg/Pid.cfg', 'cconsttype': 'const double', 'value': 100.0, 'ctype': 'double', 'type': 'double', 'name': 'scale_hundred'}]}", 'default': 10.0, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 290, 'description': 'Kd', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'Kd', 'edit_method': '', 'default': 0.1, 'level': 0, 'min': -1.0, 'type': 'double'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

Pid_scale_tenth = 0.1
Pid_scale_unity = 1.0
Pid_scale_ten = 10.0
Pid_scale_hundred = 100.0
