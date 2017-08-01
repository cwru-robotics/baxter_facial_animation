#!/usr/bin/env python
import rospy
import cv2
import cv_bridge
from sensor_msgs.msg import Image
if __name__ == '__main__':
	rospy.init_node('my_image_display', anonymous=True)
	pub = rospy.Publisher('/robot/xdisplay', Image, latch=True, queue_size=1)
	images = [
"sleeping0061.png","sleeping0062.png","sleeping0063.png","sleeping0064.png","sleeping0065.png",
"sleeping0066.png","sleeping0067.png","sleeping0068.png","sleeping0069.png","sleeping0070.png",
"sleeping0071.png","sleeping0072.png","sleeping0073.png", "sleeping0074.png","sleeping0075.png",
"sleeping0076.png","sleeping0077.png","sleeping0078.png","sleeping0079.png","sleeping0080.png",
"sleeping0081.png","sleeping0082.png","sleeping0083.png","sleeping0084.png","sleeping0085.png",
"sleeping0086.png","sleeping0087.png","sleeping0088.png","sleeping0089.png","sleeping0090.png",
"sleeping0091.png","sleeping0092.png","sleeping0093.png","sleeping0094.png","sleeping0095.png",
"sleeping0096.png","sleeping0097.png","sleeping0098.png","sleeping0099.png","sleeping0100.png",
"sleeping0101.png","sleeping0102.png","sleeping0103.png","sleeping0104.png","sleeping0105.png",
"sleeping0106.png","sleeping0107.png","sleeping0108.png","sleeping0109.png","sleeping0110.png",
"sleeping0111.png","sleeping0112.png","sleeping0113.png","sleeping0114.png","sleeping0115.png",
"sleeping0116.png","sleeping0117.png","sleeping0118.png","sleeping0119.png","sleeping0120.png",
"sleeping0121.png","sleeping0122.png","sleeping0123.png","sleeping0124.png","sleeping0125.png",
"sleeping0126.png","sleeping0127.png","sleeping0128.png","sleeping0129.png"] #e.g: put your list of images here 
	while not rospy.is_shutdown():
		for path in images:
			img = cv2.imread(path)
			msg = cv_bridge.CvBridge().cv2_to_imgmsg(img, encoding="bgr8")
			pub.publish(msg)
			rospy.sleep(0.03)
		
