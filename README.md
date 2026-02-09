## Tello Documentation

This is a couple of useful scripts for the Tello drone. Specifically meant for users of the Mass Academy drone.

Thanks to Dr. C for buying the drone and hopefully this documentation helps you make the most of it!

### Setup

1. Install all the necessary packages
2. Connect to the drone's wifi network (recommended to only have one device on this at once)
3. (Optional but useful for debugging) Download the [Tello app](https://www.dji.com/downloads/djiapp/tello)

### TelloBoilerplate.py

This is a basic boilerplate for the Tello drone. It includes a lot of useful functions and error handling. It also includes a lot of comments to help you understand what's going on.

### TelloVision.py

This is a basic vision script for the Tello drone. It includes a lot of useful functions and error handling. It also includes a lot of comments to help you understand what's going on.

### Problems 

If the drone is just not listening to your command it might be the battery. The battery seems to last around 20 minutes and needs a few hours to charge.

Any problems with an imu or joystick error code are just random issues. The commands resend to overcome these. Interestingly, the drone gets more of these error when the battery is low.

If you have some random issues with the drone not responding to commands, try manually controlling from the app. After that, return to your autonomous script. It worked for me.

If it talks about imu calibration, run the calibration script in the Tello app. Take the propellers and propeller guards off first. Make sure to take a picture of the propellers configuration before taking them off as the propellers are not symmetrical and their direction matters.