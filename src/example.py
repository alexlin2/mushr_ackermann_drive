#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32

# control topics
car_name = "car"
control_steering = rospy.Publisher("/"+ car_name+ "/" + "drive_me_now"+ "/steering",Float32,queue_size=1)
control_speed = rospy.Publisher("/"+ car_name+ "/" + "drive_me_now"+ "/speed",Float32,queue_size=1)

# get gps data


rospy.init_node("test")
while not rospy.is_shutdown():
    rospy.sleep(0.1)
    speed = Float32()
    steering = Float32()
    speed.data = 1.0
    steering.data = 0.0
    control_steering.publish(steering)
    control_speed.publish(speed)