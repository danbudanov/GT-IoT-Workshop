# GT-IoT-Workshop

## Add Edison to GT-Other

ifconfig -a
ifconfig wlan0 up

configure_edison --wifi
Enter the GTother number
Enter provided password.

ifconfig -a
copy HWaddr from wlan0
goto [LAWN](auth.lawn.gatech.edu)
Login a different device
Paste HWaddr from wlan0

goto http://edison.local
OR
goto inet addr under wlan0

Please make sure that the switch is set to 5V instead of 3.3v on the Grove shield!

Run flask server:
export FLASK_APP=hello.py
flask run --host=0.0.0.0
