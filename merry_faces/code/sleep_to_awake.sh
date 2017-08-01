#!/bin/bash
#x=1

cd ..
cd animations
cd sleeping
rosrun merry_faces sleeping_temp.py
echo Slept
cd ..
cd waking
rosrun merry_faces waking.py
echo Woke up
cd ..
cd idle
echo Now awake
rosrun merry_faces idle.py

done
