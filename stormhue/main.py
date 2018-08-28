from stormhue.games.heroesofthestorm import HeroesOfTheStorm
from stormhue.hue.controller import HueManager

# Config values
# TODO: This should be pulled from config.yml
HUE_STATION_IP = "192.168.1.149"
HUE_LIGHTS = ['Door light', 'Desk light']


# Connect to the Base Station
hue_manager = HueManager(station_ip=HUE_STATION_IP, light_group=HUE_LIGHTS)
hots = HeroesOfTheStorm(light_manager=hue_manager).run()
