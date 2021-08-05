## mushr_ackermann_drive

# This is a package that contains code that interfaces with the vesc in Mushr cars

To start controlling the mushr cars using the provided example.py script, \
you must first launch the system by executing the following command in the \
bash terminal:

`roslaunch mushr_ackermann_drive car.launch car_name:="car"`

Then you can run the control script which will send a speed of 1 m/s \
to the mushr_vehicle being controlled\

`rosrun mushr_ackermann_drive example.py`

