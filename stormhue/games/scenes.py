class Scene(object):
    def __init__(self, name, presences):
        self.name = name
        self.presences = presences
        self.is_active()

    def is_active(self):
        for presence in self.presences:
            if presence.is_present():
                continue
            else:
                return False
        return True

    def event_loop(self):
        pass


class SceneManager(object):
    def __init__(self, scenes=None):
        if not scenes:
            scenes = []

        self.scenes = scenes
        self.active_scene = None

    def add_scene(self, scene):
        self.scenes.append(scene)

    def determine_active_scene(self):
        for scene in self.scenes:
            if scene.is_active():
                self.active_scene = scene
                return self.active_scene


class NotActiveScene(Exception):
    pass
