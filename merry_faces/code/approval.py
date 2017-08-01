#!/usr/bin/env python
import rospy
import cv2
import cv_bridge
from sensor_msgs.msg import Image
if __name__ == '__main__':
	rospy.init_node('my_image_display', anonymous=True)
	pub = rospy.Publisher('/robot/xdisplay', Image, latch=True, queue_size=1)
	images = ["approval0001.png","approval0002.png","approval0003.png","approval0004.png","approval0005.png",
	"approval0006.png","approval0007.png","approval0008.png","approval0009.png","approval0010.png",
	"approval0011.png","approval0012.png","approval0013.png","approval0014.png","approval0015.png",
	"approval0016.png","approval0017.png","approval0018.png","approval0019.png","approval0020.png",
	"approval0021.png","approval0022.png","approval0023.png","approval0024.png","approval0025.png",
	"approval0026.png","approval0027.png","approval0028.png","approval0029.png","approval0030.png",
	"approval0031.png","approval0032.png","approval0033.png","approval0034.png","approval0035.png",
	"approval0036.png","approval0037.png","approval0038.png","approval0039.png","approval0040.png",
	"approval0041.png","approval0042.png","approval0043.png","approval0044.png","approval0045.png",
	"approval0046.png","approval0047.png","approval0048.png","approval0049.png","approval0050.png",
	"approval0051.png","approval0052.png","approval0053.png","approval0054.png","approval0055.png"] #e.g: put your list of images here 
	while not rospy.is_shutdown():
		for path in images:
			img = cv2.imread(path)
			msg = cv_bridge.CvBridge().cv2_to_imgmsg(img, encoding="bgr8")
			pub.publish(msg)
			rospy.sleep(0.03)