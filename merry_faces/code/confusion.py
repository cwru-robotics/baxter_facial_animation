#!/usr/bin/env python
import rospy
import cv2
import cv_bridge
from sensor_msgs.msg import Image
if __name__ == '__main__':
	rospy.init_node('my_image_display', anonymous=True)
	pub = rospy.Publisher('/robot/xdisplay', Image, latch=True, queue_size=1)
	images = ["confusion0001.png","confusion0002.png","confusion0003.png","confusion0004.png","confusion0005.png",
"confusion0006.png","confusion0007.png","confusion0008.png","confusion0009.png","confusion0010.png",
"confusion0011.png","confusion0012.png","confusion0013.png","confusion0014.png","confusion0015.png",
"confusion0016.png","confusion0017.png","confusion0018.png","confusion0019.png","confusion0020.png",
"confusion0021.png","confusion0022.png","confusion0023.png","confusion0024.png","confusion0025.png",
"confusion0026.png","confusion0027.png","confusion0028.png","confusion0029.png","confusion0030.png",
"confusion0031.png","confusion0032.png","confusion0033.png","confusion0034.png","confusion0035.png",
"confusion0036.png","confusion0037.png","confusion0038.png","confusion0039.png","confusion0040.png",
"confusion0041.png","confusion0042.png","confusion0043.png","confusion0044.png","confusion0045.png",
"confusion0046.png","confusion0047.png","confusion0048.png","confusion0049.png","confusion0050.png",
"confusion0051.png","confusion0052.png","confusion0053.png","confusion0054.png","confusion0055.png",
"confusion0056.png","confusion0057.png","confusion0058.png","confusion0059.png","confusion0060.png",] #e.g: put your list of images here 
	count=0
	#while (count<5):
	while not rospy.is_shutdown():
		for path in images:
			img = cv2.imread(path)
			msg = cv_bridge.CvBridge().cv2_to_imgmsg(img, encoding="bgr8")
			pub.publish(msg)
			rospy.sleep(0.03)
			#count=count+1
