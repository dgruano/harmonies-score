import unittest
import cv2
import numpy as np
from src.height_estimation import depth_estimation, detect_overlaps, vertical_alignment_check

class TestHeightEstimation(unittest.TestCase):

    def setUp(self):
        # Set up any necessary variables or configurations for the tests
        self.test_image_path = "tests/images/test_image.jpg"
        self.test_image = cv2.imread(self.test_image_path)
        self.contours = [np.array([[0, 0], [1, 0], [1, 1], [0, 1]])]

    def test_depth_estimation(self):
        # Test the depth estimation function
        depth_map = depth_estimation(self.test_image)
        self.assertIsNotNone(depth_map, "Depth estimation failed.")
        self.assertEqual(depth_map.shape, self.test_image.shape[:2], "Depth map has different shape than expected.")

    def test_detect_overlaps(self):
        # Test the detect overlaps function
        heights = detect_overlaps(self.contours)
        self.assertIsNotNone(heights, "Detect overlaps failed.")
        self.assertIsInstance(heights, list, "Heights should be a list.")
        for contour, height in heights:
            self.assertEqual(height, 1, "Default height should be 1.")

    def test_vertical_alignment_check(self):
        # Test the vertical alignment check function
        stacked_pieces = vertical_alignment_check(self.contours)
        self.assertIsNotNone(stacked_pieces, "Vertical alignment check failed.")
        self.assertIsInstance(stacked_pieces, list, "Stacked pieces should be a list.")
        for contour, stacked_count in stacked_pieces:
            self.assertEqual(stacked_count, 1, "Default stacked count should be 1.")

if __name__ == "__main__":
    unittest.main()
