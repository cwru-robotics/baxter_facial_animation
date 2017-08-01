#!/usr/bin/env python
import rospy
import cv2
import cv_bridge
from sensor_msgs.msg import Image
if __name__ == '__main__':
	rospy.init_node('my_image_display', anonymous=True)
	pub = rospy.Publisher('/robot/xdisplay', Image, latch=True, queue_size=1)
	images = ["laughing0001.png","laughing0002.png","laughing0003.png","laughing0004.png","laughing0005.png",
"laughing0006.png","laughing0007.png","laughing0008.png","laughing0009.png","laughing0010.png",
"laughing0011.png","laughing0012.png","laughing0013.png","laughing0014.png","laughing0015.png",
"laughing0016.png","laughing0017.png","laughing0018.png","laughing0019.png","laughing0020.png",
"laughing0021.png","laughing0022.png","laughing0023.png","laughing0024.png","laughing0025.png",
"laughing0026.png","laughing0027.png","laughing0028.png","laughing0029.png","laughing0030.png",
"laughing0031.png","laughing0032.png","laughing0033.png","laughing0034.png","laughing0035.png",
"laughing0036.png","laughing0037.png","laughing0038.png","laughing0039.png","laughing0040.png",
"laughing0041.png","laughing0042.png","laughing0043.png","laughing0044.png","laughing0045.png",
"laughing0046.png","laughing0047.png","laughing0048.png","laughing0049.png","laughing0050.png",
"laughing0051.png","laughing0052.png","laughing0053.png","laughing0054.png","laughing0055.png",
"laughing0056.png","laughing0057.png","laughing0058.png","laughing0059.png","laughing0060.png",] #e.g: put your list of images here 
	while not rospy.is_shutdown():
		for path in images:
			img = cv2.imread(path)
			msg = cv_bridge.CvBridge().cv2_to_imgmsg(img, encoding="bgr8")
			pub.publish(msg)
			rospy.sleep(0.03)
			#print "what"
