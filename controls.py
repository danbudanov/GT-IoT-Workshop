import pyupm_i2clcd as lcd

import time
import pyupm_grove as grove

import pyupm_buzzer as upmBuzzer

# Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS)
myLcd = lcd.Jhd1313m1(1, 0x3E, 0x62)

# Create the temperature sensor object using AIO pin 0
temp = grove.GroveTemp(0)

# Create the button object using GPIO pin 4
button = grove.GroveButton(4)

# Create the light sensor object using AIO pin 1
light = grove.GroveLight(1)

# Create the buzzer object using GPIO pin 3
buzzer = upmBuzzer.Buzzer(6)
chords = [upmBuzzer.DO, upmBuzzer.RE, upmBuzzer.MI, upmBuzzer.FA, 
          upmBuzzer.SOL, upmBuzzer.LA, upmBuzzer.SI, upmBuzzer.DO, 
          upmBuzzer.SI];

def print_lcd(line, string):
    myLcd.setCursor(line, 0)
    # Clear line
    myLcd.write("               ")
    myLcd.write(string)

def read_temp():
    # Read the temperature ten times, printing both the Celsius and
    # equivalent Fahrenheit temperature, waiting one second between readings
    temp_avg = 0
    for i in range(0, 10):
        celsius = temp.value()
        fahrenheit = celsius * 9.0/5.0 + 32.0;
        temp_avg += fahrenheit
        time.sleep(0.02)
    temp_avg /= 10
    return temp_avg

def read_btn():
    return button.value()

def read_light():
    light_avg = 0
    for i in range(0, 10):
        light_avg += light.value()
        time.sleep(0.02)
    light_avg /= 10
    return light_avg

def play_sound(time, sound=0):
    # Play buzzer for time seconds
    buzzer.playSound(chords[sound], 1000000*time)
