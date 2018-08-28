from mss import mss, exception
from rgbxy import Converter

converter = Converter()
screen_capture = mss()


class CaptureArea(object):
    def __init__(self, top, left, width, height):
        self.top = top
        self.left = left
        self.width = width
        self.height = height
        self.screen_capture = screen_capture

    def __dict__(self):
        return {"top": self.top, "left": self.left, "width": self.width, "height": self.height}

    def capture(self):
        return self.screen_capture.grab({"top": self.top,
                                         "left": self.left,
                                         "width": self.width,
                                         "height": self.height})


class InfoBit(object):
    def __init__(self, capture_area):
        self.capture_area = capture_area


class Presence(InfoBit):
    def __init__(self, capture_area, color_expectation, tolerance=4):
        InfoBit.__init__(self, capture_area)
        self.color_expectation = color_expectation
        self.tolerance = tolerance

    def is_present(self):
        try:
            for index, value in enumerate(self.capture_area.capture()):
                pixel = value[0]
                pixel_expectation = self.color_expectation[index][0]
                in_r_bounds = pixel_expectation[0] + self.tolerance > pixel[0] > pixel_expectation[0] - self.tolerance
                in_g_bounds = pixel_expectation[1] + self.tolerance > pixel[1] > pixel_expectation[1] - self.tolerance
                in_b_bounds = pixel_expectation[2] + self.tolerance > pixel[2] > pixel_expectation[2] - self.tolerance
                if in_r_bounds and in_g_bounds and in_b_bounds:
                    continue
                else:
                    return False
            return True
        except exception.ScreenShotError:
            return self.is_present()
