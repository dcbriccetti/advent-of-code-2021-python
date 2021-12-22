from unittest import TestCase

from day22 import Range3D, Point3D


class TestRange3D(TestCase):
    def test_points_in(self):
        r3d = Range3D(-1, 1, -1, 1, -1, 1)
        points = list(r3d.points_in())
        self.assertEqual(27, len(points))
        self.assertTrue(Point3D(0, 0, 0) in points)
        self.assertTrue(Point3D(-2, 0, 0) not in points)
