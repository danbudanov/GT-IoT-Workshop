# GT-IoT-Workshop

## Edison Setup

#### Connect to Edison through Serial
```
screen /dev/tty.usbserial-A903UL7S 115200
```
* `/dev/tty.usbserial-A903UL7S` will vary per device

#### Add Edison to GTwifi
```
ifconfig -a
ifconfig wlan0 up
configure_edison --wifi
```
* Enter the GTwifi number
* Enter GT username and password

#### Connect to Edison through SSH
```
ifconfig -a
```
* Copy address under wlan0 inet addr
* SSH into `root@` copied address

* Please make sure that the switch is set to 5V instead of 3.3v on the Grove shield!

## Run flask server:
```
export FLASK_APP=hello.py
flask run --host=0.0.0.0
```