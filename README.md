roslaunch_api_example
====

## Usage
Prepare terminals for publish and echo topics.
```
$ roscore
```

```
$ rostopic pub /calling std_msgs/String "data: 'Hello'" -r 1
```

```
$ rostopic echo /chatter
```

Try the python script which utilizes roslaunch API.
```
$ rosrun roslaunch_api_example roslaunch_api_example.py
```
