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

    print("Example to execute a node")
    package = 'roslaunch_api_example'
    executable = 'roslaunch_api_example_node'
    node = roslaunch.core.Node(package, executable, output="screen")

    launch = roslaunch.scriptapi.ROSLaunch()
    launch.start()  # Necessary before process is prepared

    process = launch.launch(node)  # Startthe the node

    print("process is alive? : ", process.is_alive())

    time.sleep(10)

    print("Stop node process from script")
    process.stop()
    print("process is alive? : ", process.is_alive())

    # restart of same node
    print("restart")
    process = launch.launch(node)
    print("process is alive? : ", process.is_alive())

    time.sleep(10)

    print("Stop node process from script")
    process.stop()
    launch.stop()
