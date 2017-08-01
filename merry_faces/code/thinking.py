#!/usr/bin/env python
import rospy
import cv2
import cv_bridge
from sensor_msgs.msg import Image
if __name__ == '__main__':
	rospy.init_node('my_image_display', anonymous=True)
	pub = rospy.Publisher('/robot/xdisplay', Image, latch=True, queue_size=1)
	images = ["thinking0001.png","thinking0002.png","thinking0003.png","thinking0004.png","thinking0005.png",
"thinking0006.png","thinking0007.png","thinking0008.png","thinking0009.png","thinking0010.png",
"thinking0011.png","thinking0012.png","thinking0013.png","thinking0014.png","thinking0015.png",
"thinking0016.png","thinking0017.png","thinking0018.png","thinking0019.png","thinking0020.png",
"thinking0021.png","thinking0022.png","thinking0023.png","thinking0024.png","thinking0025.png",
"thinking0026.png","thinking0027.png","thinking0028.png","thinking0029.png","thinking0030.png",
"thinking0031.png","thinking0032.png","thinking0033.png","thinking0034.png","thinking0035.png",
"thinking0036.png","thinking0037.png","thinking0038.png","thinking0039.png","thinking0040.png",
"thinking0041.png","thinking0042.png","thinking0043.png","thinking0044.png","thinking0045.png",
"thinking0046.png","thinking0047.png","thinking0048.png","thinking0049.png","thinking0050.png",
"thinking0051.png","thinking0052.png","thinking0053.png","thinking0054.png","thinking0055.png",
"thinking0056.png","thinking0057.png","thinking0058.png","thinking0059.png","thinking0060.png",
"thinking0061.png","thinking0062.png","thinking0063.png","thinking0064.png","thinking0065.png",] #e.g: put your list of images here 
	while not rospy.is_shutdown():
		for path in images:
			img = cv2.imread(path)
			msg = cv_bridge.CvBridge().cv2_to_imgmsg(img, encoding="bgr8")
			pub.publish(msg)
			rospy.sleep(0.03)
