#!/bin/bash
#Executes idle_bash.py or wink_bash.py randomly with a higher probability of executing idle than wink.

cd ..
cd animations/random_wink

while :
do
if (( RANDOM %10 )); then rosrun merry_faces idle_once.py && echo idled; else rosrun merry_faces wink_once.py && echo winked; fi
done
