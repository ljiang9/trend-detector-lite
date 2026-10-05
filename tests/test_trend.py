"""trend-detector-lite 单元测试。运行：python3 -m unittest discover -s tests"""
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from trend import moving_average, direction, detect_spikes, analyze  # noqa: E402


class TestTrend(unittest.TestCase):
    def test_ma(self):
        ma = moving_average([1, 2, 3, 4], window=3)
        self.assertEqual(ma[-1], 3.0)

    def test_direction_up(self):
        self.assertEqual(direction([1, 2, 3, 4]), "up")

    def test_direction_down(self):
        self.assertEqual(direction([4, 3, 2, 1]), "down")

    def test_spike(self):
        spikes = detect_spikes([10, 11, 10, 11, 50])
        self.assertIn(4, spikes)

    def test_analyze(self):
        r = analyze([1, 2, 3])
        self.assertEqual(r["direction"], "up")
        self.assertTrue("moving_average" in r)


if __name__ == "__main__":
    unittest.main()
