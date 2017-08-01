#!/usr/bin/env python
import rospy
import cv2
import cv_bridge
from sensor_msgs.msg import Image
if __name__ == '__main__':
	rospy.init_node('my_image_display', anonymous=True)
	pub = rospy.Publisher('/robot/xdisplay', Image, latch=True, queue_size=1)
	images = ["final-0001.png","final-0002.png","final-0003.png","final-0004.png","final-0005.png",
"final-0006.png","final-0007.png","final-0008.png","final-0009.png","final-0010.png",
"final-0011.png","final-0012.png","final-0013.png","final-0014.png","final-0015.png",
"final-0016.png","final-0017.png","final-0018.png","final-0019.png","final-0020.png",
"final-0021.png","final-0022.png","final-0023.png","final-0024.png","final-0025.png",
"final-0026.png","final-0027.png","final-0028.png","final-0029.png","final-0030.png",
"final-0031.png","final-0032.png","final-0033.png","final-0034.png","final-0035.png",
"final-0036.png","final-0037.png","final-0038.png","final-0039.png","final-0040.png",
"final-0041.png","final-0042.png","final-0043.png","final-0044.png","final-0045.png",
"final-0046.png","final-0047.png","final-0048.png","final-0049.png","final-0050.png",
"final-0051.png","final-0052.png","final-0053.png","final-0054.png","final-0055.png",
"final-0056.png","final-0057.png","final-0058.png","final-0059.png","final-0060.png",
"final-0061.png","final-0062.png","final-0063.png","final-0064.png","final-0065.png",
"final-0066.png","final-0067.png","final-0068.png","final-0069.png","final-0070.png",] #e.g: put your list of images here 
	while not rospy.is_shutdown():
		for path in images:
			img = cv2.imread(path)
			msg = cv_bridge.CvBridge().cv2_to_imgmsg(img, encoding="bgr8")
			pub.publish(msg)
			rospy.sleep(0.03)
