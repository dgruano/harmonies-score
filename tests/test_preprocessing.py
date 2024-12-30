import unittest
import cv2
import numpy as np
from src.preprocessing import color_correction, perspective_correction

class TestPreprocessing(unittest.TestCase):

    def setUp(self):
        # Set up any necessary variables or configurations for the tests
        self.test_image_path = "tests/images/test_image.jpg"
        self.test_image = cv2.imread(self.test_image_path)
        self.src_points = np.float32([[0, 0], [1, 0], [0, 1], [1, 1]])
        self.dst_points = np.float32([[0, 0], [1, 0], [0, 1], [1, 1]])

    def test_color_correction(self):
        # Test the color correction function
        corrected_image = color_correction(self.test_image)
        self.assertIsNotNone(corrected_image, "Color correction failed.")
        self.assertEqual(corrected_image.shape, self.test_image.shape, "Color corrected image has different shape.")

    def test_perspective_correction(self):
        # Test the perspective correction function
        corrected_image = perspective_correction(self.test_image, self.src_points, self.dst_points)
        self.assertIsNotNone(corrected_image, "Perspective correction failed.")
        self.assertEqual(corrected_image.shape, self.test_image.shape, "Perspective corrected image has different shape.")

if __name__ == "__main__":
    unittest.main()
