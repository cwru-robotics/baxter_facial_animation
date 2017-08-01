#!/usr/bin/env python
import rospy
import cv2
import cv_bridge
from sensor_msgs.msg import Image
if __name__ == '__main__':
	rospy.init_node('my_image_display', anonymous=True)
	pub = rospy.Publisher('/robot/xdisplay', Image, latch=True, queue_size=1)
	images = ["disapproval0001.png","disapproval0002.png","disapproval0003.png","disapproval0004.png","disapproval0005.png",
"disapproval0006.png","disapproval0007.png","disapproval0008.png","disapproval0009.png","disapproval0010.png",
"disapproval0011.png","disapproval0012.png","disapproval0013.png","disapproval0014.png","disapproval0015.png",
"disapproval0016.png","disapproval0017.png","disapproval0018.png","disapproval0019.png","disapproval0020.png",
"disapproval0021.png","disapproval0022.png","disapproval0023.png","disapproval0024.png","disapproval0025.png",
"disapproval0026.png","disapproval0027.png","disapproval0028.png","disapproval0029.png","disapproval0030.png",
"disapproval0031.png","disapproval0032.png","disapproval0033.png","disapproval0034.png","disapproval0035.png",
"disapproval0036.png","disapproval0037.png","disapproval0038.png","disapproval0039.png","disapproval0040.png",
"disapproval0041.png","disapproval0042.png","disapproval0043.png","disapproval0044.png","disapproval0045.png",
"disapproval0046.png","disapproval0047.png","disapproval0048.png","disapproval0049.png","disapproval0050.png",
"disapproval0051.png","disapproval0052.png","disapproval0053.png","disapproval0054.png","disapproval0055.png",
"disapproval0056.png","disapproval0057.png","disapproval0058.png","disapproval0059.png","disapproval0060.png",
"disapproval0061.png","disapproval0062.png","disapproval0063.png","disapproval0064.png","disapproval0065.png",] #e.g: put your list of images here 
	while not rospy.is_shutdown():
		for path in images:
			img = cv2.imread(path)
			msg = cv_bridge.CvBridge().cv2_to_imgmsg(img, encoding="bgr8")
			pub.publish(msg)
			rospy.sleep(0.03)
