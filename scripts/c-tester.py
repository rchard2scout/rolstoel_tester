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
            rospy.logdebug("Both frames exist")
            t = self.tf.getLatestCommonTime("/camera_rgb_optical_frame",
                                            "/map")
            rospy.loginfo("t = %s", t)
            pos, quat = self.tf.lookupTransform("/camera_rgb_optical_frame",
                                                "/map", t)
            (roll, pitch, yaw) = tf.transformations.euler_from_quaternion(quat)
#            rospy.logdebug("pos: %s\teuler: %s", pos, eul)
            rospy.loginfo("x: %.5f\ty: %.5f\tz: %.5f", pos[0], pos[1], pos[2])
            rospy.loginfo("r: %.5f\tp: %.5f\ty: %.5f", roll, pitch, yaw)
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
