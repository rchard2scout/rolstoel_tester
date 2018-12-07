#!/usr/bin/env python
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


class middle_value_distance:

    def __init__(self):
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber('/camera/depth/image_raw',
                                          Image,
                                          self.callback)
        rospy.loginfo("Listening to /camera/depth/image_raw")

    def callback(self, data):
        rospy.logdebug(rospy.get_caller_id() +
                       " Received Image with time: %s\nencoding:\n%s",
                       data.header.stamp,
                       data.encoding)
        try:
                cv_image = self.bridge.imgmsg_to_cv2(data, "16UC1")
        except CvBridgeError as e:
                rospy.logerr(e)

        (rows, cols) = cv_image.shape
        rospy.logdebug(rospy.get_caller_id() +
                       " Rows: %d\tCols: %d", rows, cols)

        rospy.loginfo("d: %d", cv_image[rows/2, cols/2])


def main():
    middle_value_distance()
    rospy.init_node('tester', anonymous=True)
    rospy.loginfo("Initialized tester")
    try:
        rospy.spin()
    except KeyboardInterrupt:
        rospy.logerr("Shutting down")
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
