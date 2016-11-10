import pyupm_ttp223 as ttp223
import pyupm_i2clcd as i2clcd

lcd = i2clcd.Jhd1313m1(0, 0x3e, 0x62)
lcd.setCursor(0,0)

lcd.setColor(250, 10, 10)
lcd.write('Hey guys!')
lcd.setCursor(1,2)
lcd.write('Hello again!')
