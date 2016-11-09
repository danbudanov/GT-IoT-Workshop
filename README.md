# GT-IoT-Workshop

## Add Edison to GT-Other
```
ifconfig -a
ifconfig wlan0 up
configure_edison --wifi
```
* Enter the GTother number
* Enter GT username and password

```
ifconfig -a
```
* Copy address under wlan0 inet addr
* SSH into `root@` copied address

goto http://edison.local
OR
goto inet addr under wlan0

Please make sure that the switch is set to 5V instead of 3.3v on the Grove shield!

Run flask server:
export FLASK_APP=hello.py
flask run --host=0.0.0.0
