#!/usr/bin/env python3
import rospy
from ackermann_msgs.msg import AckermannDriveStamped
from std_msgs.msg import Float32
import numpy as np

max_steering = 0.34
max_speed = 2.0

class MushrController():

    def __init__(self, car_name) -> None:
        self.car_name = car_name
        self.rp_ctrls = None
        self.get_ctrls = None
        self.set_up_pub_sub()
        self.steering = 0.0
        self.speed = 0.0 

    def set_up_pub_sub(self):

        self.rp_ctrls = rospy.Publisher(
            "/"
            + self.car_name
            + "/"
            + "mux/ackermann_cmd_mux/input/navigation",
            AckermannDriveStamped,
            queue_size=2,
        )

        self.get_ctrls = rospy.Subscriber(
            "/"
            + self.car_name
            + "/" 
            + "drive_me_now"
            + "/steering",
            Float32,
            callback=self.drive_callback_steering,
            queue_size=1
        )
        self.get_ctrls = rospy.Subscriber(
            "/"
            + self.car_name
            + "/" 
            + "drive_me_now"
            + "/speed",
            Float32,
            callback=self.drive_callback_speed,
            queue_size=1
        )

    def drive_me_now(self, speed: float, steering: float):
        cmd_msg = AckermannDriveStamped()
        cmd_msg.header.stamp = rospy.Time.now()
        cmd_msg.header.frame_id = self.car_name
        cmd_msg.drive.steering_angle = steering * max_steering
        cmd_msg.drive.speed = speed * max_speed
        self.rp_ctrls.publish(cmd_msg)

    def drive_callback_steering(self, msg):
        self.steering = np.clip(msg.data, -1.0, 1.0)
        self.drive_me_now(self.speed, self.steering)

    def drive_callback_speed(self, msg):
        self.speed = np.clip(msg.data, -1.0, 1.0)
        self.drive_me_now(self.speed, self.steering)

if __name__ == "__main__":
    rospy.init_node("drive")
    car_name = rospy.get_param("~car_name")
    controller = MushrController(car_name)
    rospy.spin()
        