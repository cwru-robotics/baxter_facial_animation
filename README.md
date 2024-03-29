Runs animations on Baxter robot.

Requires a [set up connection with Baxter](http://sdk.rethinkrobotics.com/wiki/Workstation_Setup) with an edited baxter.sh file including baxter_hostname, your_ip, and ros_version.

Connect to Baxter by running `./baxter.sh`. Note: baxter.sh must be moved to the top folder of workspace before it is run.

Move to baxter_facial_animation/merry_faces/code and `chmod +x [animation].py` to make sure all .py files are executable.
Also `source devel/setup.bash` in the top folder of your workspace to make sure merry_faces is a package before running.


Change directory into desired facial expression folder.

Available faces are: approval, confusion, disapproval, happiness, idle, laughing, sleeping, thinking, waking, wink.

Run corresponding python file with ```rosrun merry_faces [animation].py```

Files awake_to_sleep.sh, sleep_to_awake.sh, random_wink.sh can be run directly from the merry_faces/code folder and will play a series of animations.
