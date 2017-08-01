#!/usr/bin/env python
import rospy
import cv2
import cv_bridge
from sensor_msgs.msg import Image
if __name__ == '__main__':
	rospy.init_node('my_image_display', anonymous=True)
	pub = rospy.Publisher('/robot/xdisplay', Image, latch=True, queue_size=1)
	images = ["wink0001.png","wink0002.png","wink0003.png","wink0004.png","wink0005.png",
"wink0006.png","wink0007.png","wink0008.png","wink0009.png","wink0010.png",
"wink0011.png","wink0012.png","wink0013.png","wink0014.png","wink0015.png",
"wink0016.png","wink0017.png","wink0018.png","wink0019.png","wink0020.png",
"wink0021.png","wink0022.png","wink0023.png","wink0024.png","wink0025.png",
"wink0026.png","wink0027.png","wink0028.png","wink0029.png","wink0030.png",
"wink0031.png","wink0032.png","wink0033.png","wink0034.png","wink0035.png",
"wink0036.png","wink0037.png","wink0038.png","wink0039.png","wink0040.png",
"wink0041.png","wink0042.png","wink0043.png","wink0044.png","wink0045.png",
"wink0046.png","wink0047.png","wink0048.png","wink0049.png","wink0050.png",
] #e.g: put your list of images here 
	while not rospy.is_shutdown():
		for path in images:
			img = cv2.imread(path)
			msg = cv_bridge.CvBridge().cv2_to_imgmsg(img, encoding="bgr8")
			pub.publish(msg)
			rospy.sleep(0.03)
			#print "wink"
