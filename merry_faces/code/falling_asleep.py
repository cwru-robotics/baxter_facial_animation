#!/usr/bin/env python
import rospy
import cv2
import cv_bridge
from sensor_msgs.msg import Image
if __name__ == '__main__':
	rospy.init_node('my_image_display', anonymous=True)
	pub = rospy.Publisher('/robot/xdisplay', Image, latch=True, queue_size=1)
	images = ["sleeping0001.png","sleeping0002.png","sleeping0003.png","sleeping0004.png","sleeping0005.png",
"sleeping0006.png","sleeping0007.png","sleeping0008.png","sleeping0009.png","sleeping0010.png",
"sleeping0011.png","sleeping0012.png","sleeping0013.png","sleeping0014.png","sleeping0015.png",
"sleeping0016.png","sleeping0017.png","sleeping0018.png","sleeping0019.png","sleeping0020.png",
"sleeping0021.png","sleeping0022.png","sleeping0023.png","sleeping0024.png","sleeping0025.png",
"sleeping0026.png","sleeping0027.png","sleeping0028.png","sleeping0029.png","sleeping0030.png",
"sleeping0031.png","sleeping0032.png","sleeping0033.png","sleeping0034.png","sleeping0035.png",
"sleeping0036.png","sleeping0037.png","sleeping0038.png","sleeping0039.png","sleeping0040.png",
"sleeping0041.png","sleeping0042.png","sleeping0043.png","sleeping0044.png","sleeping0045.png",
"sleeping0046.png","sleeping0047.png","sleeping0048.png","sleeping0049.png","sleeping0050.png",
"sleeping0051.png","sleeping0052.png","sleeping0053.png","sleeping0054.png","sleeping0055.png",
"sleeping0056.png","sleeping0057.png","sleeping0058.png","sleeping0059.png","sleeping0060.png",] #e.g: put your list of images here 
	count=0
	#while not rospy.is_shutdown():
	while(count<1):
		for path in images:
			img = cv2.imread(path)
			msg = cv_bridge.CvBridge().cv2_to_imgmsg(img, encoding="bgr8")
			pub.publish(msg)
			rospy.sleep(0.03)
			count=count+1