# CMake generated Testfile for 
# Source directory: /home/felipe/roboserv_ws/src/m-explore/map_merge
# Build directory: /home/felipe/roboserv_ws/build/m-explore/map_merge
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_multirobot_map_merge_gtest_test_merging_pipeline "/home/felipe/roboserv_ws/build/catkin_generated/env_cached.sh" "/usr/bin/python" "/opt/ros/kinetic/share/catkin/cmake/test/run_tests.py" "/home/felipe/roboserv_ws/build/test_results/multirobot_map_merge/gtest-test_merging_pipeline.xml" "--return-code" "/home/felipe/roboserv_ws/devel/lib/multirobot_map_merge/test_merging_pipeline --gtest_output=xml:/home/felipe/roboserv_ws/build/test_results/multirobot_map_merge/gtest-test_merging_pipeline.xml")
add_test(_ctest_multirobot_map_merge_roslaunch-check_launch_map_merge.launch "/home/felipe/roboserv_ws/build/catkin_generated/env_cached.sh" "/usr/bin/python" "/opt/ros/kinetic/share/catkin/cmake/test/run_tests.py" "/home/felipe/roboserv_ws/build/test_results/multirobot_map_merge/roslaunch-check_launch_map_merge.launch.xml" "--return-code" "/usr/bin/cmake -E make_directory /home/felipe/roboserv_ws/build/test_results/multirobot_map_merge" "/opt/ros/kinetic/share/roslaunch/cmake/../scripts/roslaunch-check -o '/home/felipe/roboserv_ws/build/test_results/multirobot_map_merge/roslaunch-check_launch_map_merge.launch.xml' '/home/felipe/roboserv_ws/src/m-explore/map_merge/launch/map_merge.launch' ")
add_test(_ctest_multirobot_map_merge_roslaunch-check_launch_experiments "/home/felipe/roboserv_ws/build/catkin_generated/env_cached.sh" "/usr/bin/python" "/opt/ros/kinetic/share/catkin/cmake/test/run_tests.py" "/home/felipe/roboserv_ws/build/test_results/multirobot_map_merge/roslaunch-check_launch_experiments.xml" "--return-code" "/usr/bin/cmake -E make_directory /home/felipe/roboserv_ws/build/test_results/multirobot_map_merge" "/opt/ros/kinetic/share/roslaunch/cmake/../scripts/roslaunch-check -o '/home/felipe/roboserv_ws/build/test_results/multirobot_map_merge/roslaunch-check_launch_experiments.xml' '/home/felipe/roboserv_ws/src/m-explore/map_merge/launch/experiments' ")