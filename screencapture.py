import time
from mss import mss
from win32gui import GetWindowText, GetForegroundWindow
from phue import Bridge
from rgbxy import Converter
converter = Converter()


lights = ['Door light', 'Desk light']

# Full health to no health
color_steps = ("4ae500", "56d004", "62bb09", "6fa70e", "7b9213", "887e18", "94691d", "a15522", "ad4027", "ba2c2c")

base_station = Bridge('192.168.1.149')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
base_station.connect()
base_station.get_api()
base_station.set_light(lights, 'on', True)
is_light_on = True


def set_light_color(hex):
    print "setting to hex {}".format(hex)
    xy = converter.hex_to_xy(hex)
    command = {"xy": [xy[0], xy[1]], "transitiontime": '200'}
    base_station.set_light(lights, command)


def get_health_hex(percentage):
    print "checking percentage: {}".format(percentage)
    if 101 > percentage >= 90:
        return color_steps[0]
    elif 90 > percentage >= 80:
        return color_steps[1]
    elif 80 > percentage >= 70:
        return color_steps[2]
    elif 70 > percentage >= 60:
        return color_steps[3]
    elif 60 > percentage >= 50:
        return color_steps[4]
    elif 50 > percentage >= 40:
        return color_steps[5]
    elif 40 > percentage >= 30:
        return color_steps[6]
    elif 30 > percentage >= 20:
        return color_steps[7]
    elif 20 > percentage >= 10:
        return color_steps[8]
    elif 10 > percentage >= 0:
        return color_steps[9]


time.sleep(3)


def get_health_percentage(pixels):
    current_pixel = 0
    for i in pixels:
        if 117 > i[0] > 76 and 225 > i[1] > 213 and 31 > i[2] > 27:
            current_pixel += 1
            continue
        else:
            break
    total_pixels = len(pixels)
    return 100 * float(current_pixel) / float(total_pixels)


capture_area = {"top": 1346, "left": 288, "width": 246, "height": 1}


last_hex = "000000"

with mss() as sct:
    while True:
        if GetWindowText(GetForegroundWindow()) == "Heroes of the Storm":
            if not is_light_on:
                base_station.set_light(lights, 'on', True)
                is_light_on = True
            sct_img = sct.grab(capture_area)

            # get health percentage
            character_hp = get_health_percentage(sct_img.pixels[0])
            health_hex = get_health_hex(character_hp)
            if last_hex != health_hex:
                set_light_color(health_hex)
                last_hex = health_hex
        else:
            base_station.set_light(lights, 'on', False)
            is_light_on = False

        time.sleep(0.1)

# Full health
# 77 214 28
# 81 224 30

# Missing health
# 35 34 46
#
