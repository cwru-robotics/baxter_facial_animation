#!/usr/bin/env python
import rospy
import cv2
import cv_bridge
from sensor_msgs.msg import Image
if __name__ == '__main__':
	rospy.init_node('my_image_display', anonymous=True)
	pub = rospy.Publisher('/robot/xdisplay', Image, latch=True, queue_size=1)
	images = [
"waking0130.png","waking0131.png","waking0132.png","waking0133.png","waking0134.png",
"waking0135.png","waking0136.png","waking0137.png","waking0138.png","waking0139.png",
"waking0140.png","waking0141.png","waking0142.png", "waking0143.png","waking0144.png",
"waking0145.png","waking0146.png","waking0147.png","waking0148.png","waking0149.png",
"waking0150.png","waking0151.png","waking0152.png","waking0153.png","waking0154.png",
"waking0155.png","waking0156.png","waking0157.png","waking0158.png","waking0159.png",
"waking0160.png","waking0161.png","waking0162.png","waking0163.png","waking0164.png",
"waking0165.png",] #e.g: put your list of images here 
	count=0
	#while not rospy.is_shutdown():
	while(count<1):
		for path in images:
			img = cv2.imread(path)
			msg = cv_bridge.CvBridge().cv2_to_imgmsg(img, encoding="bgr8")
			pub.publish(msg)
			rospy.sleep(0.03)
			count=count+1
