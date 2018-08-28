from phue import Bridge
from rgbxy import Converter

converter = Converter()


class HueManager(object):
    def __init__(self, station_ip, light_group):
        self.base_station_ip = station_ip
        self.base_station = Bridge(self.base_station_ip)
        self.light_group = light_group
        self._connect()

    def _connect(self):
        self.base_station.connect()
        self._update_info()

    def _update_info(self):
        self.base_station.get_api()

    def set_light(self, enabled):
        self.base_station.set_light(self.light_group, "on", enabled)

    def set_color(self, color_hex, transition_time="200"):
        xy = converter.hex_to_xy(color_hex)
        command = {"xy": [xy[0], xy[1]], "transitiontime": transition_time}
        self.base_station.set_light(self.light_group, command)


class LightGroup(object):
    def __init__(self, lights):
        self.lights = lights

    def __list__(self):
        return self.lights
