#!/usr/bin/env python
import rospy
import cv2
import cv_bridge
from sensor_msgs.msg import Image
if __name__ == '__main__':
	rospy.init_node('my_image_display', anonymous=True)
	pub = rospy.Publisher('/robot/xdisplay', Image, latch=True, queue_size=1)
	images = ["idle0001.png","idle0002.png","idle0003.png","idle0004.png","idle0005.png",
"idle0006.png","idle0007.png","idle0008.png","idle0009.png","idle0010.png",
"idle0011.png","idle0012.png","idle0012.png","idle0013.png","idle0013.png","idle0014.png","idle0015.png",
"idle0016.png","idle0017.png","idle0018.png","idle0019.png","idle0020.png",
"idle0021.png","idle0022.png","idle0023.png","idle0024.png","idle0025.png",
"idle0026.png","idle0027.png","idle0028.png","idle0029.png","idle0030.png",
"idle0031.png","idle0032.png","idle0033.png","idle0034.png","idle0035.png","idle0035.png",
"idle0036.png","idle0036.png","idle0037.png","idle0038.png","idle0039.png","idle0040.png",
"idle0041.png","idle0042.png","idle0043.png","idle0044.png","idle0045.png",
"idle0046.png","idle0047.png","idle0048.png","idle0049.png","idle0050.png",
"idle0051.png","idle0052.png","idle0052.png","idle0053.png","idle0053.png","idle0054.png","idle0055.png",
"idle0056.png","idle0057.png","idle0058.png","idle0059.png","idle0060.png",
"idle0061.png","idle0062.png","idle0063.png","idle0064.png","idle0065.png",
"idle0066.png","idle0067.png","idle0068.png","idle0069.png","idle0070.png",
"idle0071.png","idle0072.png"] #e.g: put your list of images here 
	while not rospy.is_shutdown():
		for path in images:
			img = cv2.imread(path)
			msg = cv_bridge.CvBridge().cv2_to_imgmsg(img, encoding="bgr8")
			pub.publish(msg)
			rospy.sleep(0.03)
			#print "what"
