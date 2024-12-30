import unittest
import cv2
import numpy as np
from src.color_shape_detection import color_segmentation, contour_detection, draw_contours

class TestColorShapeDetection(unittest.TestCase):

    def setUp(self):
        # Set up any necessary variables or configurations for the tests
        self.test_image_path = "tests/images/test_image.jpg"
        self.test_image = cv2.imread(self.test_image_path)
        self.lower_hsv = (30, 100, 100)
        self.upper_hsv = (90, 255, 255)

    def test_color_segmentation(self):
        # Test the color segmentation function
        mask = color_segmentation(self.test_image, self.lower_hsv, self.upper_hsv)
        self.assertIsNotNone(mask, "Color segmentation failed.")
        self.assertEqual(mask.shape, self.test_image.shape[:2], "Mask has different shape than expected.")

    def test_contour_detection(self):
        # Test the contour detection function
        mask = color_segmentation(self.test_image, self.lower_hsv, self.upper_hsv)
        contours = contour_detection(mask)
        self.assertIsNotNone(contours, "Contour detection failed.")
        self.assertIsInstance(contours, list, "Contours should be a list.")
        for contour in contours:
            self.assertEqual(len(contour), 6, "Detected contour is not a hexagon.")

    def test_draw_contours(self):
        # Test the draw contours function
        mask = color_segmentation(self.test_image, self.lower_hsv, self.upper_hsv)
        contours = contour_detection(mask)
        image_with_contours = draw_contours(self.test_image, contours)
        self.assertIsNotNone(image_with_contours, "Drawing contours failed.")
        self.assertEqual(image_with_contours.shape, self.test_image.shape, "Image with contours has different shape.")

if __name__ == "__main__":
    unittest.main()
