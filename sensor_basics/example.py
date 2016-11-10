import pyupm_ttp223 as ttp223
import pyupm_i2clcd as i2clcd

lcd = i2clcd.Jhd1313m1(0, 0x3e, 0x62)
touch = ttp223.TTP223(3)

lcd.setCursor(0,0)

lcd.setColor(250, 10, 10)
lcd.write('Hey guys!')
lcd.setCursor(1,2)
lcd.write('Hello again!')

while 1:
    if touch.isPressed():
        led.clear()
        lcd.setCursor(0,0)
        lcd.setColor(250, 0, 0)
        lcd.write('Touch is triggered!')
    else:
        led.clear()
        lcd.setCursor(0,0)
        lcd.setColor(20, 20, 255)
        lcd.write('everything''s calm'.)
