import unittest
from stormhue.games.infobit import InfoBit, CaptureArea
from types import ListType


class TestInfoBit(unittest.TestCase):
    def test_CaptureArea(self):
        ca = CaptureArea(top=1, left=1, width=1, height=1).capture()
        self.assertIsInstance(ca.pixels, ListType)

    def test_CaptureArea_dict_cast(self):
        ca = CaptureArea(top=1, left=1, width=1, height=1)
        self.assertEqual(ca.__dict__(), {"top": 1, "left": 1, "width": 1, "height": 1})

    def test_InfoBit(self):
        infobit = InfoBit(capture_area={})
        self.assertIsInstance(infobit, InfoBit)


if __name__ == '__main__':
    unittest.main()
