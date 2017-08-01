#!/usr/bin/env python
import rospy
import cv2
import cv_bridge
from sensor_msgs.msg import Image
if __name__ == '__main__':
	rospy.init_node('my_image_display', anonymous=True)
	pub = rospy.Publisher('/robot/xdisplay', Image, latch=True, queue_size=1)
	images = ["happiness0001.png","happiness0002.png","happiness0003.png","happiness0004.png","happiness0005.png",
"happiness0006.png","happiness0007.png","happiness0008.png","happiness0009.png","happiness0010.png",
"happiness0011.png","happiness0012.png","happiness0013.png","happiness0014.png","happiness0015.png",
"happiness0016.png","happiness0017.png","happiness0018.png","happiness0019.png","happiness0020.png",
"happiness0021.png","happiness0022.png","happiness0023.png","happiness0024.png","happiness0025.png",
"happiness0026.png","happiness0027.png","happiness0028.png","happiness0029.png","happiness0030.png",
"happiness0031.png","happiness0032.png","happiness0033.png","happiness0034.png","happiness0035.png",
"happiness0036.png","happiness0037.png","happiness0038.png","happiness0039.png","happiness0040.png",
"happiness0041.png","happiness0042.png","happiness0043.png","happiness0044.png","happiness0045.png",
"happiness0046.png","happiness0047.png","happiness0048.png","happiness0049.png","happiness0050.png",
"happiness0051.png","happiness0052.png","happiness0053.png","happiness0054.png","happiness0055.png",] #e.g: put your list of images here 
	while not rospy.is_shutdown():
		for path in images:
			img = cv2.imread(path)
			msg = cv_bridge.CvBridge().cv2_to_imgmsg(img, encoding="bgr8")
			pub.publish(msg)
			rospy.sleep(0.03)
