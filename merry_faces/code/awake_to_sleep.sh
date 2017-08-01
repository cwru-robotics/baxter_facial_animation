#!/bin/bash
#x=1
cd ..
cd animations
cd idle
rosrun merry_faces idle_temp.py
echo Idled
cd ..
cd sleeping
rosrun merry_faces falling_asleep.py
echo Falling asleep
echo Now sleeping
rosrun merry_faces sleeping.py
done