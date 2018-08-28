import time
from stormhue.games import Game
from stormhue.games.scenes import Scene, SceneManager, NotActiveScene
from stormhue.games.infobit import CaptureArea, Presence


class HeroesOfTheStorm(Game):
    def __init__(self, light_manager):
        Game.__init__(self, "Heroes of the Storm")
        self.light_manager = light_manager
        self.scene_manager = SceneManager(scenes=[
            DebugScene(light_manager=light_manager),
            LoadingScene(light_manager=light_manager),
            HeroSelectScene(light_manager=light_manager),
            QMPartyScene(light_manager=light_manager),
            BrawlQueueScene(light_manager=light_manager),
            UnrankedQueueScene(light_manager=light_manager),
            RankedQueueScene(light_manager=light_manager),
            CollectionScene(light_manager=light_manager),
            CustomGameScene(light_manager=light_manager),
            LootRoomScene(light_manager=light_manager),
            AIScene(light_manager=light_manager),
            ReplayScene(light_manager=light_manager),
            GameScene(light_manager=light_manager),
        ])
        self.active_scene = None
        self.initialize_lights()

    def determine_active_scene(self):
        self.active_scene = self.scene_manager.determine_active_scene()
        return self.active_scene

    def initialize_lights(self):
        self.light_manager.set_light(True)

    def run(self):
        while True:
            self.determine_active_scene()
            if self.active_scene:
                try:
                    self.active_scene.event_loop()
                except NotActiveScene:
                    pass


class DebugScene(Scene):
    def __init__(self, light_manager):
        Scene.__init__(self,
                       name="PyCharm",
                       presences=[
                           Presence(
                               color_expectation=[((21, 21, 21),), ((21, 21, 21),), ((21, 21, 21),), ((21, 21, 21),),
                                                  ((21, 21, 21),), ((21, 21, 21),), ((21, 21, 21),), ((21, 21, 21),),
                                                  ((21, 21, 21),), ((21, 21, 21),), ((21, 21, 21),), ((21, 21, 21),),
                                                  ((21, 21, 21),), ((21, 21, 21),), ((21, 21, 21),), ((21, 21, 21),),
                                                  ((21, 21, 21),), ((21, 21, 21),), ((21, 21, 21),), ((21, 21, 21),)],
                               capture_area=CaptureArea(
                                   top=164,
                                   left=30,
                                   height=20,
                                   width=1
                               ))
                       ])
        self.light_manager = light_manager

    def event_loop(self):
        while True:
            self.light_manager.set_color("281963", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()
            self.light_manager.set_color("1173df", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()


class LoadingScene(Scene):
    def __init__(self, light_manager):
        Scene.__init__(self,
                       name="Game Loading",
                       presences=[
                           Presence(color_expectation=[((197, 40, 41), (194, 40, 41)), ((194, 40, 41), (194, 40, 41)),
                                                       ((194, 40, 41), (194, 40, 41)), ((194, 40, 41), (194, 40, 41)),
                                                       ((194, 40, 41), (194, 40, 41)), ((194, 41, 44), (194, 41, 44)),
                                                       ((194, 41, 44), (194, 41, 44)), ((194, 41, 44), (194, 41, 44))],
                                    capture_area=CaptureArea(
                                        top=1331,
                                        left=892,
                                        width=2,
                                        height=8,
                                    ))
                       ])
        self.light_manager = light_manager

    def event_loop(self):
        while True:
            self.light_manager.set_color("281963", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()
            self.light_manager.set_color("1173df", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()


class HeroDraft(Scene):
    def __init__(self, light_manager):
        Scene.__init__(self,
                       name="Hero Draft",
                       presences=[
                           Presence(color_expectation=[((197, 40, 41), (194, 40, 41)), ((194, 40, 41), (194, 40, 41)),
                                                       ((194, 40, 41), (194, 40, 41)), ((194, 40, 41), (194, 40, 41)),
                                                       ((194, 40, 41), (194, 40, 41)), ((194, 41, 44), (194, 41, 44)),
                                                       ((194, 41, 44), (194, 41, 44)), ((194, 41, 44), (194, 41, 44))],
                                    capture_area=CaptureArea(
                                        top=1331,
                                        left=892,
                                        width=2,
                                        height=8,
                                    ))
                       ])
        self.light_manager = light_manager

    def event_loop(self):
        while True:
            self.light_manager.set_color("281963", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()
            self.light_manager.set_color("1173df", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()


class GameScene(Scene):
    def __init__(self, light_manager):
        Scene.__init__(self,
                       name="GameActive",
                       presences=[
                           Presence(color_expectation=[((216, 220, 225), (222, 230, 239), (197, 211, 224),
                                                        (184, 201, 215), (186, 202, 217), (189, 204, 220),
                                                        (189, 204, 220), (186, 202, 219), (186, 202, 219),
                                                        (198, 212, 225), (223, 231, 238), (246, 248, 250),
                                                        (238, 239, 239), (120, 124, 124), (42, 44, 43))],
                                    capture_area=CaptureArea(
                                        top=1310,
                                        left=25,
                                        height=1,
                                        width=15
                                    ))
                       ])
        self.light_manager = light_manager
        self.color_steps = ("4ae500", "56d004", "62bb09", "6fa70e", "7b9213", "887e18", "94691d", "a15522", "ad4027", "ba2c2c")
        self.current_color = None

    def event_loop(self):
        while True:
            player_health_hex = self.check_player_health()
            if self.current_color != player_health_hex:
                if not self.is_active():
                    raise NotActiveScene()
                self.current_color = player_health_hex
                self.light_manager.set_color(self.current_color)

            time.sleep(0.1)

    def get_health_percentage(self, pixels):
        current_pixel = 0
        for i in pixels[0]:
            if 117 > i[0] > 76 and 225 > i[1] > 211 and 31 > i[2] > 27:
                current_pixel += 1
                continue
            else:
                break
        total_pixels = len(pixels[0])
        return 100 * float(current_pixel) / float(total_pixels)

    def get_health_hex(self, percentage):
        print "checking percentage: {}".format(percentage)
        if 101 > percentage >= 90:
            return self.color_steps[0]
        elif 90 > percentage >= 80:
            return self.color_steps[1]
        elif 80 > percentage >= 70:
            return self.color_steps[2]
        elif 70 > percentage >= 60:
            return self.color_steps[3]
        elif 60 > percentage >= 50:
            return self.color_steps[4]
        elif 50 > percentage >= 40:
            return self.color_steps[5]
        elif 40 > percentage >= 30:
            return self.color_steps[6]
        elif 30 > percentage >= 20:
            return self.color_steps[7]
        elif 20 > percentage >= 10:
            return self.color_steps[8]
        elif 10 > percentage >= 0:
            return self.color_steps[9]

    def check_player_health(self):
        player_health_pixels = CaptureArea(
            top=1346,
            left=278,
            height=1,
            width=258
        ).capture()
        player_health_percent = self.get_health_percentage(player_health_pixels)
        return self.get_health_hex(player_health_percent)


class ReplayScene(Scene):
    def __init__(self, light_manager):
        Scene.__init__(self,
                       name="Replay Selection",
                       presences=[
                           Presence(color_expectation=[((187, 168, 245), (187, 168, 245), (188, 169, 245),
                                                        (197, 177, 246), (197, 177, 246), (197, 177, 246),
                                                        (197, 177, 246), (202, 182, 246), (205, 185, 246),
                                                        (205, 185, 246), (205, 185, 246), (205, 188, 246),
                                                        (205, 194, 246), (205, 194, 246), (205, 194, 246),
                                                        (205, 194, 246), (211, 197, 246), (213, 198, 246),
                                                        (213, 198, 246), (213, 198, 246), (216, 201, 246),
                                                        (221, 206, 246), (221, 206, 246), (221, 206, 246),
                                                        (221, 206, 246), (221, 210, 246), (221, 210, 246),
                                                        (221, 210, 246), (221, 210, 246), (221, 208, 246),
                                                        (221, 206, 246), (221, 206, 246), (221, 206, 246),
                                                        (220, 206, 246))],
                                    capture_area=CaptureArea(
                                        top=94,
                                        left=674,
                                        height=1,
                                        width=34
                                    ))
                       ])
        self.light_manager = light_manager

    def event_loop(self):
        while True:
            self.light_manager.set_color("281963", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()
            self.light_manager.set_color("1173df", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()


class LootRoomScene(Scene):
    def __init__(self, light_manager):
        Scene.__init__(self,
                       name="Loot Room",
                       presences=[
                           Presence(color_expectation=[((205, 185, 246), (205, 185, 246), (205, 188, 246),
                                                        (205, 194, 246), (205, 194, 246), (205, 194, 246),
                                                        (209, 196, 246), (213, 198, 246), (213, 198, 246),
                                                        (213, 198, 246), (218, 203, 246), (221, 206, 246),
                                                        (221, 206, 246), (221, 206, 246), (221, 209, 246),
                                                        (221, 210, 246), (221, 210, 246), (221, 210, 246),
                                                        (221, 207, 246), (221, 206, 246), (221, 206, 246),
                                                        (221, 206, 246), (214, 203, 246), (213, 202, 246),
                                                        (213, 202, 246), (213, 202, 246), (213, 194, 246),
                                                        (213, 194, 246), (213, 194, 246), (213, 194, 246),
                                                        (205, 185, 246), (205, 185, 246), (205, 185, 246),
                                                        (204, 184, 246))],
                                    capture_area=CaptureArea(
                                        top=94,
                                        left=532,
                                        height=1,
                                        width=34
                                    ))
                       ])
        self.light_manager = light_manager

    def event_loop(self):
        while True:
            self.light_manager.set_color("a0683c", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()
            self.light_manager.set_color("e5da53", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()


class CustomGameScene(Scene):
    def __init__(self, light_manager):
        Scene.__init__(self,
                       name="Custom Game",
                       presences=[
                           Presence(color_expectation=[((55, 38, 97), (55, 38, 97), (55, 38, 97), (55, 38, 97),
                                                        (55, 38, 97), (55, 38, 97), (55, 38, 97), (55, 38, 97),
                                                        (55, 38, 97), (54, 38, 97), (54, 38, 97), (54, 38, 97),
                                                        (54, 38, 97), (54, 38, 97), (54, 38, 97), (54, 38, 97),
                                                        (54, 38, 97), (54, 38, 97), (54, 38, 97), (54, 38, 97),
                                                        (54, 38, 96), (54, 38, 96), (54, 38, 96), (54, 38, 96),
                                                        (54, 38, 96), (54, 38, 96), (54, 38, 96), (54, 38, 96),
                                                        (54, 38, 96), (54, 38, 96), (54, 38, 96), (54, 38, 96),
                                                        (54, 38, 96), (54, 38, 96))],
                                    capture_area=CaptureArea(
                                        top=151,
                                        left=1147,
                                        height=1,
                                        width=34
                                    ),
                                    tolerance=2)
                       ])
        self.light_manager = light_manager

    def event_loop(self):
        while True:
            self.light_manager.set_color("281963", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()
            self.light_manager.set_color("1173df", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()


class CollectionScene(Scene):
    def __init__(self, light_manager):
        Scene.__init__(self,
                       name="Collection",
                       presences=[
                           Presence(color_expectation=[((187, 168, 245), (187, 168, 245), (192, 173, 245),
                                                        (197, 177, 246), (197, 177, 246), (197, 177, 246),
                                                        (197, 177, 246), (197, 177, 246), (203, 183, 246),
                                                        (205, 185, 246), (205, 185, 246), (205, 185, 246),
                                                        (205, 185, 246), (205, 188, 246), (205, 194, 246),
                                                        (205, 194, 246), (205, 194, 246), (205, 194, 246),
                                                        (205, 194, 246), (209, 196, 246), (213, 198, 246),
                                                        (213, 198, 246), (213, 198, 246), (213, 198, 246),
                                                        (213, 198, 246), (219, 204, 246), (221, 206, 246),
                                                        (221, 206, 246), (221, 206, 246), (221, 206, 246),
                                                        (221, 207, 246), (221, 210, 246), (221, 210, 246),
                                                        (221, 210, 246))],
                                    capture_area=CaptureArea(
                                        top=94,
                                        left=319,
                                        height=1,
                                        width=34
                                    ))
                       ])
        self.light_manager = light_manager

    def event_loop(self):
        while True:
            self.light_manager.set_color("281963", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()
            self.light_manager.set_color("1173df", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()


class BrawlQueueScene(Scene):
    def __init__(self, light_manager):
        Scene.__init__(self,
                       name="Brawl - Queue",
                       presences=[
                           Presence(color_expectation=[((162, 139, 235), (162, 139, 235), (170, 148, 236),
                                                        (170, 148, 236), (179, 160, 245), (179, 160, 245),
                                                        (187, 168, 245), (187, 168, 245), (196, 176, 246),
                                                        (197, 177, 246), (204, 184, 246), (205, 186, 246),
                                                        (205, 194, 246), (206, 194, 246), (213, 198, 246),
                                                        (215, 199, 246), (221, 206, 246), (221, 207, 246),
                                                        (221, 210, 246), (221, 209, 246), (221, 206, 246),
                                                        (218, 204, 246), (213, 202, 246), (213, 198, 246),
                                                        (213, 194, 246), (209, 189, 246), (205, 185, 246),
                                                        (200, 180, 246), (196, 176, 246), (191, 171, 245),
                                                        (187, 168, 245), (182, 163, 245), (179, 160, 245),
                                                        (172, 154, 239))],
                                    capture_area=CaptureArea(
                                        top=151,
                                        left=601,
                                        height=1,
                                        width=34
                                    ))
                       ])
        self.light_manager = light_manager

    def event_loop(self):
        while True:
            self.light_manager.set_color("281963", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()
            self.light_manager.set_color("1173df", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()


class RankedQueueScene(Scene):
    def __init__(self, light_manager):
        Scene.__init__(self,
                       name="Ranked Draft - Queue",
                       presences=[
                           Presence(color_expectation=[((107, 77, 186), (108, 78, 188), (118, 87, 193), (118, 87, 193),
                                                        (126, 96, 203), (128, 99, 205), (133, 104, 211),
                                                        (140, 111, 220), (140, 111, 220), (142, 119, 222),
                                                        (142, 119, 222), (151, 129, 232), (151, 129, 232),
                                                        (159, 137, 234), (161, 139, 235), (165, 142, 235),
                                                        (170, 147, 236), (170, 147, 236), (179, 160, 244),
                                                        (179, 160, 244), (187, 168, 245), (187, 168, 245),
                                                        (195, 175, 246), (196, 176, 246), (200, 180, 246),
                                                        (204, 184, 246), (205, 185, 246), (205, 194, 246),
                                                        (205, 194, 246), (213, 198, 246), (213, 198, 246),
                                                        (221, 205, 246), (221, 206, 246), (221, 208, 246))],
                                    capture_area=CaptureArea(
                                        top=151,
                                        left=480,
                                        height=1,
                                        width=34
                                    ))
                       ])
        self.light_manager = light_manager

    def event_loop(self):
        while True:
            self.light_manager.set_color("281963", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()
            self.light_manager.set_color("1173df", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()


class UnrankedQueueScene(Scene):
    def __init__(self, light_manager):
        Scene.__init__(self,
                       name="Unranked - Queue",
                       presences=[
                           Presence(color_expectation=[((131, 102, 209), (139, 109, 218), (140, 111, 220),
                                                        (141, 116, 222), (142, 119, 222), (142, 119, 222),
                                                        (151, 129, 233), (151, 129, 233), (155, 133, 233),
                                                        (161, 139, 235), (161, 139, 235), (170, 147, 236),
                                                        (170, 147, 236), (171, 149, 237), (179, 160, 244),
                                                        (179, 160, 244), (185, 166, 245), (187, 168, 245),
                                                        (187, 168, 245), (196, 176, 246), (196, 176, 246),
                                                        (200, 181, 246), (204, 184, 246), (205, 185, 246),
                                                        (205, 194, 246), (205, 194, 246), (207, 195, 246),
                                                        (213, 198, 246), (213, 198, 246), (220, 205, 246),
                                                        (221, 206, 246), (221, 206, 246), (221, 210, 246),
                                                        (221, 210, 246))],
                                    capture_area=CaptureArea(
                                        top=151,
                                        left=356,
                                        height=1,
                                        width=34
                                    ))
                       ])
        self.light_manager = light_manager

    def event_loop(self):
        while True:
            self.light_manager.set_color("281963", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()
            self.light_manager.set_color("1173df", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()


class UnrankedDraftScene(Scene):
    def __init__(self, light_manager):
        Scene.__init__(self,
                       name="Unranked - Draft",
                       presences=[
                           Presence(color_expectation=[((131, 102, 209), (139, 109, 218), (140, 111, 220),
                                                        (141, 116, 222), (142, 119, 222), (142, 119, 222),
                                                        (151, 129, 233), (151, 129, 233), (155, 133, 233),
                                                        (161, 139, 235), (161, 139, 235), (170, 147, 236),
                                                        (170, 147, 236), (171, 149, 237), (179, 160, 244),
                                                        (179, 160, 244), (185, 166, 245), (187, 168, 245),
                                                        (187, 168, 245), (196, 176, 246), (196, 176, 246),
                                                        (200, 181, 246), (204, 184, 246), (205, 185, 246),
                                                        (205, 194, 246), (205, 194, 246), (207, 195, 246),
                                                        (213, 198, 246), (213, 198, 246), (220, 205, 246),
                                                        (221, 206, 246), (221, 206, 246), (221, 210, 246),
                                                        (221, 210, 246))],
                                    capture_area=CaptureArea(
                                        top=186,
                                        left=5,
                                        height=47,
                                        width=1
                                    ))
                       ])
        self.light_manager = light_manager

    def event_loop(self):
        while True:
            self.light_manager.set_color("281963", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()
            self.light_manager.set_color("1173df", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()


class QMPartyScene(Scene):
    def __init__(self, light_manager):
        Scene.__init__(self,
                       name="Quick Match - Party View",
                       presences=[
                           Presence(color_expectation=[
                               ((8, 5, 19), (6, 4, 16), (15, 13, 30), (47, 43, 88), (47, 43, 88), (47, 43, 88)),
                               ((8, 5, 19), (7, 4, 16), (15, 13, 30), (47, 43, 87), (47, 43, 87), (47, 43, 88)),
                               ((8, 5, 19), (7, 4, 16), (15, 12, 29), (47, 43, 87), (47, 43, 87), (47, 43, 87)),
                               ((8, 5, 19), (7, 4, 17), (8, 6, 19), (14, 12, 29), (15, 12, 29), (15, 13, 30))],
                               capture_area=CaptureArea(
                                   top=1425,
                                   left=1950,
                                   height=4,
                                   width=6
                               ))
                       ])
        self.light_manager = light_manager

    def event_loop(self):
        while True:
            self.light_manager.set_color("281963", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()
            self.light_manager.set_color("1173df", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()


class AIScene(Scene):
    def __init__(self, light_manager):
        Scene.__init__(self,
                       name="AI Match - Party View",
                       presences=[
                           Presence(color_expectation=[((151, 129, 233), (157, 135, 234), (161, 139, 235),
                                                        (161, 139, 235), (170, 147, 236), (170, 147, 236),
                                                        (170, 147, 236), (179, 160, 244), (179, 160, 244),
                                                        (182, 163, 245), (187, 168, 245), (187, 168, 245),
                                                        (195, 175, 246), (196, 176, 246), (196, 176, 246),
                                                        (204, 184, 246), (205, 185, 246), (205, 187, 246),
                                                        (205, 194, 246), (205, 194, 246), (211, 197, 246),
                                                        (213, 198, 246), (213, 198, 246), (221, 206, 246),
                                                        (221, 206, 246), (221, 206, 246), (221, 210, 246),
                                                        (221, 210, 246), (221, 207, 246), (221, 206, 246),
                                                        (221, 206, 246), (213, 202, 246), (213, 202, 246),
                                                        (213, 202, 246))],
                                    capture_area=CaptureArea(
                                        top=151,
                                        left=55,
                                        height=1,
                                        width=34
                                    ),
                                    tolerance=3),
                       ])
        self.light_manager = light_manager

    def event_loop(self):
        while True:
            self.light_manager.set_color("281963", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()
            self.light_manager.set_color("1173df", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()


class HeroSelectScene(Scene):
    def __init__(self, light_manager):
        Scene.__init__(self,
                       name="Hero Selection",
                       presences=[
                           Presence(color_expectation=[((22, 25, 106), (25, 27, 114), (27, 28, 119), (31, 31, 132),
                                                        (35, 36, 149), (37, 40, 158), (38, 43, 163), (39, 45, 169),
                                                        (35, 48, 153), (36, 49, 159), (37, 50, 161), (37, 51, 165),
                                                        (38, 59, 158), (39, 61, 156), (39, 62, 158), (40, 63, 159),
                                                        (40, 60, 155)), (
                                                           (25, 28, 114), (28, 30, 125), (31, 33, 136), (34, 36, 147),
                                                           (38, 41, 161), (39, 45, 170), (41, 50, 179), (41, 51, 180),
                                                           (37, 50, 162), (37, 51, 165), (38, 52, 168), (39, 53, 171),
                                                           (39, 60, 161), (39, 63, 159), (79, 97, 175), (102, 116, 185),
                                                           (101, 114, 183)), (
                                                           (28, 30, 124), (31, 33, 136), (35, 36, 147), (38, 41, 159),
                                                           (39, 45, 169), (41, 48, 178), (43, 52, 187), (43, 51, 186),
                                                           (38, 51, 166), (38, 52, 169), (90, 104, 177),
                                                           (119, 130, 180),
                                                           (148, 160, 199), (155, 168, 206), (201, 207, 224),
                                                           (227, 229, 234), (224, 227, 235)), (
                                                           (25, 32, 127), (28, 35, 136), (30, 38, 146), (32, 43, 148),
                                                           (31, 47, 143), (32, 49, 149), (33, 51, 153), (37, 56, 158),
                                                           (66, 88, 162), (140, 154, 200), (195, 202, 222),
                                                           (209, 215, 226),
                                                           (224, 227, 234), (229, 231, 237), (241, 242, 242),
                                                           (247, 247, 245), (244, 244, 246)), (
                                                           (25, 35, 133), (28, 38, 142), (31, 42, 151), (32, 47, 148),
                                                           (29, 49, 138), (30, 51, 142), (38, 58, 148), (87, 101, 172),
                                                           (184, 194, 216), (214, 222, 231), (232, 236, 241),
                                                           (234, 238, 242), (242, 243, 244), (226, 232, 237),
                                                           (220, 228, 235), (205, 215, 228), (184, 198, 221)), (
                                                           (28, 38, 141), (30, 41, 150), (33, 45, 159), (34, 49, 156),
                                                           (30, 51, 143), (40, 60, 150), (89, 102, 173),
                                                           (181, 186, 214),
                                                           (234, 238, 242), (234, 238, 242), (236, 240, 244),
                                                           (208, 217, 230), (199, 210, 225), (188, 203, 221),
                                                           (184, 200, 220), (162, 184, 210), (147, 170, 204)), (
                                                           (29, 40, 148), (33, 45, 157), (35, 48, 166), (35, 51, 160),
                                                           (31, 53, 146), (64, 82, 163), (176, 181, 211),
                                                           (226, 227, 234),
                                                           (235, 239, 243), (236, 240, 244), (210, 219, 232),
                                                           (187, 200, 221), (172, 190, 215), (169, 188, 213),
                                                           (169, 188, 213), (159, 181, 209), (150, 173, 206)), (
                                                           (29, 44, 152), (32, 48, 164), (34, 51, 160), (37, 56, 147),
                                                           (51, 71, 150), (110, 123, 180), (229, 233, 237),
                                                           (230, 235, 239),
                                                           (227, 234, 240), (213, 224, 237), (188, 204, 226),
                                                           (186, 202, 224), (177, 195, 220), (172, 191, 217),
                                                           (171, 190, 216), (169, 188, 215), (161, 182, 211)), (
                                                           (28, 48, 156), (30, 50, 169), (31, 52, 151), (40, 61, 131),
                                                           (88, 105, 161), (181, 191, 212), (235, 243, 243),
                                                           (233, 242, 243), (211, 223, 235), (189, 207, 230),
                                                           (188, 206, 230), (188, 206, 230), (182, 201, 225),
                                                           (177, 196, 222), (174, 193, 220), (170, 190, 217),
                                                           (166, 187, 215)), (
                                                           (29, 50, 164), (30, 51, 170), (31, 53, 150), (40, 61, 132),
                                                           (111, 127, 174), (235, 243, 243), (236, 244, 244),
                                                           (234, 242, 245), (199, 214, 232), (192, 209, 231),
                                                           (189, 206, 230), (188, 206, 230), (184, 203, 227),
                                                           (181, 200, 225), (177, 196, 222), (174, 193, 220),
                                                           (168, 189, 216)), (
                                                           (30, 51, 173), (31, 52, 168), (32, 54, 147), (48, 68, 138),
                                                           (124, 138, 182), (236, 244, 244), (238, 246, 246),
                                                           (234, 242, 245), (199, 214, 232), (199, 214, 232),
                                                           (192, 209, 231), (189, 207, 230), (188, 206, 230),
                                                           (184, 203, 227), (181, 200, 225), (178, 197, 223),
                                                           (170, 191, 218)), (
                                                           (30, 53, 174), (31, 54, 169), (32, 54, 148), (68, 87, 151),
                                                           (162, 173, 205), (238, 246, 248), (237, 245, 247),
                                                           (229, 239, 244), (200, 215, 232), (200, 215, 232),
                                                           (199, 214, 232), (192, 209, 230), (190, 208, 230),
                                                           (190, 208, 230), (186, 204, 227), (182, 200, 221),
                                                           (160, 177, 200)), (
                                                           (27, 58, 166), (28, 58, 167), (31, 56, 148), (86, 105, 166),
                                                           (193, 204, 226), (238, 246, 254), (234, 243, 252),
                                                           (215, 226, 240), (203, 219, 233), (202, 218, 232),
                                                           (198, 215, 231), (198, 215, 231), (197, 214, 230),
                                                           (197, 214, 230), (197, 214, 230), (164, 179, 189),
                                                           (97, 105, 115)), (
                                                           (26, 59, 175), (28, 59, 167), (31, 57, 149), (94, 112, 172),
                                                           (209, 219, 237), (238, 246, 254), (234, 243, 252),
                                                           (215, 227, 241), (208, 222, 235), (203, 219, 233),
                                                           (203, 219, 233), (203, 219, 233), (198, 215, 231),
                                                           (197, 214, 230), (192, 209, 224), (118, 126, 131),
                                                           (61, 64, 70)),
                                                       ((26, 60, 179), (30, 58, 158), (33, 55, 138), (103, 121, 178),
                                                        (223, 233, 245), (238, 246, 254), (234, 243, 252),
                                                        (215, 227, 241), (208, 222, 235), (208, 222, 235),
                                                        (208, 222, 235), (208, 222, 235), (200, 216, 231),
                                                        (197, 214, 230), (140, 149, 159), (84, 88, 88), (61, 64, 71)), (
                                                           (25, 62, 191), (28, 59, 169), (33, 55, 139), (110, 127, 183),
                                                           (237, 246, 254), (238, 246, 254), (234, 243, 252),
                                                           (216, 227, 241), (213, 226, 238), (213, 226, 238),
                                                           (213, 226, 238), (213, 226, 238), (201, 217, 232),
                                                           (197, 214, 230), (113, 121, 125), (67, 70, 67),
                                                           (55, 66, 93)), (
                                                           (24, 67, 194), (28, 61, 163), (33, 56, 132), (111, 127, 176),
                                                           (238, 243, 247), (238, 243, 247), (238, 242, 247),
                                                           (234, 240, 245), (220, 233, 238), (220, 233, 238),
                                                           (220, 233, 238), (220, 233, 238), (213, 224, 232),
                                                           (211, 221, 230), (117, 120, 128), (66, 65, 73),
                                                           (49, 61, 103)), (
                                                           (25, 67, 188), (28, 62, 162), (33, 56, 132), (111, 126, 175),
                                                           (238, 242, 246), (238, 242, 246), (238, 242, 246),
                                                           (236, 241, 245), (221, 234, 238), (221, 234, 238),
                                                           (221, 234, 238), (221, 234, 238), (215, 225, 232),
                                                           (213, 222, 230), (118, 120, 129), (66, 65, 74),
                                                           (49, 60, 104)), (
                                                           (25, 67, 187), (29, 62, 163), (33, 56, 132), (111, 126, 175),
                                                           (238, 242, 246), (238, 242, 246), (238, 242, 246),
                                                           (236, 241, 245), (221, 234, 238), (221, 234, 238),
                                                           (221, 234, 238), (221, 234, 238), (215, 225, 232),
                                                           (213, 222, 230), (118, 120, 129), (66, 65, 74),
                                                           (49, 60, 104)), (
                                                           (26, 65, 178), (30, 61, 156), (33, 56, 132), (111, 126, 175),
                                                           (225, 230, 233), (176, 182, 182), (113, 117, 116),
                                                           (114, 117, 117), (114, 118, 120), (114, 118, 120),
                                                           (114, 118, 120), (114, 118, 120), (112, 115, 122),
                                                           (112, 114, 123), (82, 82, 91), (66, 65, 74), (49, 60, 104)),
                                                       (
                                                           (29, 57, 157), (31, 57, 147), (33, 56, 137), (86, 102, 153),
                                                           (147, 155, 169), (81, 96, 134), (47, 60, 98), (48, 60, 94),
                                                           (60, 62, 66), (60, 62, 66), (60, 62, 66), (60, 62, 66),
                                                           (60, 62, 72), (60, 62, 74), (60, 62, 74), (60, 62, 74),
                                                           (46, 59, 104)), (
                                                           (28, 51, 154), (31, 54, 146), (33, 56, 140), (52, 71, 136),
                                                           (69, 84, 128), (41, 60, 123), (41, 60, 123), (41, 60, 120),
                                                           (45, 60, 102), (45, 60, 102), (45, 60, 102), (45, 60, 102),
                                                           (49, 61, 96), (51, 61, 94), (51, 61, 94), (51, 61, 94),
                                                           (42, 58, 113)), (
                                                           (26, 50, 159), (29, 52, 151), (31, 55, 144), (36, 57, 133),
                                                           (41, 60, 123), (41, 60, 123), (41, 60, 123), (40, 60, 124),
                                                           (35, 60, 132), (35, 60, 132), (35, 60, 132), (35, 60, 132),
                                                           (39, 62, 128), (41, 62, 127), (41, 62, 127), (41, 62, 127),
                                                           (36, 61, 135))],
                                    capture_area=CaptureArea(
                                        top=314,
                                        left=328,
                                        height=23,
                                        width=17
                                    ))
                       ])
        self.light_manager = light_manager

    def event_loop(self):
        while True:
            self.light_manager.set_color("281963", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()
            self.light_manager.set_color("1173df", transition_time="2000")
            time.sleep(2)
            if not self.is_active():
                raise NotActiveScene()

