#!/usr/bin/env python
import rospy
import tf
from time import sleep


class transform_rotate:

    def __init__(self):
        self.tf = tf.TransformListener()
        rospy.loginfo("Listening to /camera/depth/image_raw")

    def run(self):
        if (self.tf.frameExists("camera_rgb_optical_frame") and
                self.tf.frameExists("map")):
            rospy.loginfo("Both frames exist")
            t = self.tf.getLatestCommonTime("/camera_rgb_optical_frame",
                                            "/map")
            rospy.loginfo("t = %s", t)
            pos, quat = self.tf.lookupTransform("/camera_rgb_optical_frame",
                                                "/map", t)
            rospy.loginfo("pos: %s\tquat: %s", pos, quat)
        else:
            rospy.logerr("One of the frames doesn't exist.")


def main():
    rospy.init_node('tester', anonymous=True)
    rospy.loginfo("Initialized tester")
    tr = transform_rotate()
    while True:
        tr.run()
        sleep(0.05)


if __name__ == '__main__':
    main()
