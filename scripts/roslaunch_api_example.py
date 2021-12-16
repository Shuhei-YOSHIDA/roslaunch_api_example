#!/usr/bin/env python3
"""
@file roslaunch_api_example.py
"""

import rospy
import roslaunch
import rospkg
import time

if __name__ == "__main__":
    rospy.init_node('roslaunch_api_example')

    print("Start an example to execute a node")
    package = 'roslaunch_api_example'
    executable = 'roslaunch_api_example_node'
    node = roslaunch.core.Node(package, executable, output="screen")

    launch = roslaunch.scriptapi.ROSLaunch()
    launch.start()  # Necessary before process is prepared

    process = launch.launch(node)  # Start the the node

    print("process is alive? : ", process.is_alive())

    time.sleep(5)

    print("Stop node process from script")
    process.stop()
    print("process is alive? : ", process.is_alive())

    # restart of same node
    print("Respawn the same node")
    process = launch.launch(node)
    print("process is alive? : ", process.is_alive())

    time.sleep(5)

    print("Stop node process from script")
    process.stop()
    launch.stop()
    print("Finished an example to execute a node")

    # Execute a launch file
    print("Start an example to execute a launch file")
    rospack = rospkg.RosPack()
    pkg_path = rospack.get_path("roslaunch_api_example")
    launch_path = pkg_path + '/launch/roslaunch_api_example.launch'

    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    launch = roslaunch.parent.ROSLaunchParent(uuid, [launch_path])

    print("Prepared a launch file")
    launch.start()

    time.sleep(5)

    launch.shutdown()
    print("Stop and re-launch the file")
    launch = roslaunch.parent.ROSLaunchParent(uuid, [launch_path])  # Necessary
    launch.start()

    time.sleep(5)

    launch.shutdown()
    print("Finished example of a launch file ")
